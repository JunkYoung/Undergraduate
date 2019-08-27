import numpy as np
import random


def skipgram(currentWord, contextWords, tokens, inputVectors, outputVectors):
    """
    Skip-gram 모델 구현

    Arguments:
    currentWord -- the center word string
    contextWords -- the context words. 2*C개의 string이 들어있는 list
    tokens -- {key : 단어, value : index 숫자} 의 dictionary
    inputVectors -- 모든 "input" word vectors. 2차원의 numpy array이며 token에 해당하는 row로 접근
                    ex) token 253에 대한 word vector : inputVectors[253]
    outputVectors -- 모든 "output" word vectors. inputVectors와 마찬가지로 접근

    Return:
    cost -- Skip-gram의 cost function 값
    grad -- 두 word vector에 대한 gradient
    """

    cost = 0.0
    gradIn = np.zeros(inputVectors.shape)
    gradOut = np.zeros(outputVectors.shape)

    ### YOUR CODE HERE
    
    arr = np.zeros((len(contextWords), np.size(inputVectors.T[0])))
    
    oneHotEncoding = np.zeros((len(contextWords), np.size(inputVectors.T[0])))
    for i in range(len(contextWords)):
        oneHotEncoding[i][tokens[contextWords[i]]] = 1

    x = np.zeros((np.size(oneHotEncoding[0]), 1))
    x[tokens[currentWord]] = 1
    
    h = np.dot(inputVectors.T, x)
    o = np.dot(outputVectors, h)
    o1 = np.exp(o)
    y = o1 / np.sum(o1, axis=0, keepdims=True)
    
    for i in range(len(contextWords)):
        t = oneHotEncoding[i].reshape(5, 1)
        cost += -np.sum(t * np.log(y)) -np.sum((1-t)*np.log(1-y))
    for i in range(len(contextWords)):
        t = oneHotEncoding[i].reshape(5, 1)
        arr[i] = (y - t).T
    gradIn[tokens[currentWord]] = np.dot(outputVectors.T, np.sum(arr, axis=0, keepdims=True).T).T.reshape(3)
    gradOut = np.dot(h, np.sum(arr, axis=0, keepdims=True)).T

    ### END YOUR CODE

    return cost, gradIn, gradOut


def cbow(currentWord, contextWords, tokens, inputVectors, outputVectors):
    """
    CBOW 모델 구현

    Skip-gram 모델과 같은 구성
    """

    cost = 0.0
    gradIn = np.zeros(inputVectors.shape)
    gradOut = np.zeros(outputVectors.shape)

    ### YOUR CODE HERE
    
    arr = np.zeros((len(contextWords), np.size(inputVectors[0])))
    
    oneHotEncoding = np.zeros((len(contextWords), np.size(inputVectors.T[0])))
    for i in range(len(contextWords)):
        oneHotEncoding[i][tokens[contextWords[i]]] = 1

    t = np.zeros((np.size(oneHotEncoding[0]), 1))
    t[tokens[currentWord]] = 1
    
    for i in range(len(contextWords)):
        arr[i] = np.dot(inputVectors.T, oneHotEncoding[i].T).T
    h = np.sum(arr, axis=0, keepdims=True)
    o = np.dot(outputVectors, h.T)
    o1 = np.exp(o)
    y = o1 / np.sum(o1, axis=0, keepdims=True)
    
    cost = -np.sum(t * np.log(y)) -np.sum((1-t)*np.log(1-y))
    for i in range(np.size(inputVectors[0])):
        gradIn[i] = np.dot(outputVectors.T, y - t).reshape(3)
    gradOut = np.dot(h.T, (y - t).T).T
    
    ### END YOUR CODE

    return cost, gradIn, gradOut


##############################################
# 테스트 함수입니다. 절대 수정하지 마세요!!! #
##############################################
def test_word2vec():
    random.seed(31415)
    np.random.seed(9265)
    dummy_vectors = np.random.randn(10,3)
    dummy_tokens = dict([("a",0), ("b",1), ("c",2),("d",3),("e",4)])


    print("=== Results ===")
    print(skipgram("c", ["a", "b", "e", "d", "b", "c"],
        dummy_tokens, dummy_vectors[:5,:], dummy_vectors[5:,:]))
    print(skipgram("c", ["a", "b"],
        dummy_tokens, dummy_vectors[:5,:], dummy_vectors[5:,:]))
    print(cbow("a", ["a", "b", "c", "a"],
        dummy_tokens, dummy_vectors[:5,:], dummy_vectors[5:,:]))
    print(cbow("a", ["a", "b", "a", "c"],
        dummy_tokens, dummy_vectors[:5,:], dummy_vectors[5:,:]))


if __name__ == "__main__":
    test_word2vec()
