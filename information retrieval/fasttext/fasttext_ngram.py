import csv
import numpy as np
import tensorflow as tf
import collections
from nltk.corpus import stopwords
from tensorflow.python.framework import ops

ops.reset_default_graph()

# 파라미터 정의, 배치 사이즈나 에폭 등은 워드 임베딩 학습이나 분류학습에 똑같이 적용
class Config:
    mode = 'monogram'
    #mode = 'bigram'
    hash = False
    batch_size = 500
    voca_size = 50000
    epoch = 10000
    learn_rate = 0.001
    embed_size = 100
    window_size = 5
    print_loss_every = 1000;
    num_sampled = int(batch_size/2)
    max_words = 200

# 데이터 로딩, 정규화, 해싱, n_gram, 인덱싱, 배치데이터 생성
class Data:
    def __init__(self):
        print("Data processing")
        
        self.texts_train = []
        self.target_train = []
        self.text_data_train = []

        self.texts_test = []
        self.target_test = []
        self.texts_data_test = []
        
        self.texts_train, self.target_train = self.load_data('train')
        self.texts_train = self.normalize_text(self.texts_train)
        self.text_data_train = self.preprocess(self.texts_train)
        
        self.texts_test, self.target_test = self.load_data('test')
        self.texst_test = self.normalize_text(self.texts_test)
        self.text_data_test = self.preprocess(self.texts_test)
    
    def load_data(self, s):
        print("    loading data")
        f = open(s+'.csv', 'r', encoding='utf-8')
        reader = csv.reader(f)
        pos = []
        neg = []
        texts = []
        target = []
        for line in reader:
            if line[0] == '1':
                neg.append(line[1])
            else:
                pos.append(line[1])
        texts = pos+neg
        target = [1]*len(pos) + [0]*len(neg)
        f.close()

        return (texts, target)

    def normalize_text(self, texts):
        print("    normalizing text")
        stops = stopwords.words('english')
        texts = [x.lower() for x in texts]
        texts = [' '.join([word for word in x.split() if word not in (stops)]) for x in texts]
        texts = [' '.join(x.split()) for x in texts]
        
        return texts

    # 인덱싱(n gram 생성 및 해싱 포함) : 단어를 숫자로 치환하고 문장을 숫자의 모음으로 치환하여 반환
    def preprocess(self, texts):
        print("    preprocessing")
        word_dict = {}
        text_data = []
        split_texts = [t.split() for t in texts]
        words = [x for sublist in split_texts for x in sublist]
        if Config.mode == 'bigram':
            for w in range(len(words)-1):
                words[w] = words[w] + '_' + words[w+1]
        if Config.hash == True:
            words = self.hash_words(words)
            for t in texts:
                sentence_data = []
                for word in t.split():
                    if word in words:
                        word_ix = words.index(word)
                    else:
                        word_ix = 0
                    sentence_data.append(word_ix)
                text_data.append(sentence_data)

            return text_data
        
        else:
            count = []
            count.extend(collections.Counter(words).most_common(Config.voca_size-1))
            for word, word_count in count:
                word_dict[word] = len(word_dict)
            for t in texts:
                sentence_data = []
                for word in t.split():
                    if word in word_dict:
                        word_ix = word_dict[word]
                    else:
                        word_ix = 0
                    sentence_data.append(word_ix)
                text_data.append(sentence_data)

            return text_data

    def hash_words(self, words, seed=0):
        hash_words = []
        for word in words:
            FNV_prime = 16777619
            offset_basis = 2166136261
            hash_word = offset_basis + seed
            for char in word:
                hash_word = hash_word ^ ord(char)
                hash_word = hash_word * FNV_prime
            if hash_word not in hash_words:
                hash_words.append(hash_word)
                
        return hash_words

    #배치 데이터 생성
    def generate_batch_data(self, text_data):
        batch_data = []
        label_data = []
        while len(batch_data) < Config.batch_size:
            rand_text_ix = int(np.random.choice(len(text_data), size = 1))
            rand_text = text_data[rand_text_ix]
            window_sequences = [rand_text[max((ix-Config.window_size),0):(ix+Config.window_size+1)] for ix, x in enumerate(rand_text)]
            label_indices = [ix if ix<Config.window_size else Config.window_size for ix,x in enumerate(window_sequences)]
            batch_and_labels = [(x[:y] + x[(y+1):], x[y]) for x,y in zip(window_sequences, label_indices)]
            batch_and_labels = [(x,y) for x,y in batch_and_labels if len(x)==2*Config.window_size]
            batch = []
            labels = []
            for x,y in batch_and_labels:
                batch.append(x)
                labels.append(y)
            batch_data.extend(batch[:Config.batch_size])
            label_data.extend(labels[:Config.batch_size])
        batch_data = batch_data[:Config.batch_size]
        label_data = label_data[:Config.batch_size]
        batch_data = np.array(batch_data)
        label_data = np.array(label_data)

        return (batch_data, np.array([label_data]).T)
        

#word embedding training
class CBOW:
    def __init__(self, data):
        print("CBOW training")

        self.data = data
        self.sess = tf.Session()
        self.create_model()
        self.start_train()

    def create_model(self):
        print("    creating model")
        self.embeddings = tf.Variable(tf.random_uniform([Config.voca_size, Config.embed_size], -1.0, 1.0))
        self.nce_weights = tf.Variable(tf.truncated_normal([Config.voca_size, Config.embed_size], stddev=1.0 / np.sqrt(Config.embed_size)))
        self.nce_biases = tf.Variable(tf.zeros(Config.voca_size))
        self.x_inputs = tf.placeholder(tf.int32, shape=[Config.batch_size, 2*Config.window_size])
        self.y_target = tf.placeholder(tf.int32, shape=[Config.batch_size, 1])
        self.embed = tf.zeros([Config.batch_size, Config.embed_size])
        for element in range(2*Config.window_size):
            self.embed += tf.nn.embedding_lookup(self.embeddings, self.x_inputs[:, element])
        self.loss = tf.reduce_mean(tf.nn.nce_loss(self.nce_weights, self.nce_biases, self.y_target, self.embed, Config.num_sampled, Config.voca_size))
        self.optimizer = tf.train.GradientDescentOptimizer(learning_rate=Config.learn_rate).minimize(self.loss)
        init = tf.global_variables_initializer()
        self.sess.run(init)

    def start_train(self):
        print("    start training")
        for i in range(Config.epoch):
            batch_inputs, batch_labels = self.data.generate_batch_data(self.data.text_data_test)
            feed_dict = {self.x_inputs : batch_inputs, self.y_target : batch_labels}
            self.sess.run(self.optimizer, feed_dict=feed_dict)
            if (i+1) % Config.print_loss_every == 0:
                loss_val =  self.sess.run(self.loss, feed_dict=feed_dict)
                print('        epoch {} loss {}'.format(i+1, loss_val))


#로지스틱 분석으로 예측
class Prediction:
    def __init__(self, data, cbow):
        self.data = data
        self.cbow = cbow

        #맥스 워드 만큼 패딩 or 자르기
        self.text_data_train = np.array([x[0:Config.max_words] for x in [y+[0]*Config.max_words for y in self.data.text_data_train]])
        self.text_data_test = np.array([x[0:Config.max_words] for x in [y+[0]*Config.max_words for y in self.data.text_data_test]])
        self.data.target_train = np.array(self.data.target_train)
        self.data.target_test = np.array(self.data.target_test)

        print("Prediction")
        self.sess = tf.Session()
        self.creating_model()
        self.start_predict()
        
    def creating_model(self):
        print("    creating_model")
        self.x_inputs = tf.placeholder(tf.int32, shape=[None, Config.max_words])
        self.y_target = tf.placeholder(tf.int32, shape=[None, 1])
        embed = tf.zeros([Config.batch_size, Config.embed_size])
        for element in range(Config.max_words):
            embed += tf.nn.embedding_lookup(self.cbow.embeddings, self.x_inputs[:, element])
        A = tf.Variable(tf.random_normal(shape=[Config.embed_size, 1]))
        b = tf.Variable(tf.random_normal(shape=[1,1]))
        embed_avg = tf.reduce_mean(embed, 0)
        model_output = tf.add(tf.matmul(tf.expand_dims(embed_avg, 0) , A), b)
        
        #소프트맥스 오류나서 시그모이드 이용
        self.loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(labels=tf.cast(self.y_target, tf.float32), logits=model_output))
        prediction = tf.round(tf.sigmoid(model_output))
        predictions_correct = tf.cast(tf.equal(prediction, tf.cast(self.y_target, tf.float32)), tf.float32)
        self.accuracy = tf.reduce_mean(predictions_correct)
        opt = tf.train.GradientDescentOptimizer(learning_rate=Config.learn_rate)
        self.train_step = opt.minimize(self.loss)
        init = tf.global_variables_initializer()
        self.sess.run(init)

    def start_predict(self):
        print("    strat_predict")
        for i in range(Config.epoch):
            rand_index_train = np.random.choice(self.text_data_train.shape[0], size=Config.batch_size)
            rand_x_train = self.text_data_train[rand_index_train]
            rand_y_train = np.transpose([self.data.target_train[rand_index_train]])
            self.sess.run(self.train_step, feed_dict={self.x_inputs: rand_x_train, self.y_target: rand_y_train})
            if (i+1)%1000==0:
                rand_index_test = np.random.choice(self.text_data_test.shape[0], size=Config.batch_size)
                rand_x_test = self.text_data_test[rand_index_test]
                rand_y_test = np.transpose([self.data.target_test[rand_index_test]])
                train_loss_temp = self.sess.run(self.loss, feed_dict={self.x_inputs: rand_x_train, self.y_target: rand_y_train})
                test_loss_temp = self.sess.run(self.loss, feed_dict={self.x_inputs:  rand_x_test, self.y_target: rand_y_test})
                train_acc_temp = self.sess.run(self.accuracy, feed_dict={self.x_inputs: rand_x_train, self.y_target: rand_y_train})
                test_acc_temp = self.sess.run(self.accuracy, feed_dict={self.x_inputs: rand_x_test, self.y_target: rand_y_test})
                print('        epoch {} train loss {} test loss {} train accuracy {} test accuracy {}'.format(i+1, train_loss_temp, test_loss_temp, train_acc_temp, test_acc_temp))
            

if __name__ == '__main__':
    data = Data()
    cbow = CBOW(data)
    Prediction(data, cbow)
