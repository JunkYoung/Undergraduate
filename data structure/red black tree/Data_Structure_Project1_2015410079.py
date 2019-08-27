import sys

PATH_USER = 'c:\\Users\\Ha\\Desktop\\user.txt'
PATH_FRIEND = 'c:\\Users\\Ha\\Desktop\\friend.txt'
PATH_WORD = 'c:\\Users\\Ha\\Desktop\\word.txt'

WHITE = 0
GRAY = 1
BLACK = 2

def main():
    Quit = 0
    vertices = []
    verticesw = []
    top5u = []
    top5w = []
    rb = rbtree()
    rbw = rbtree()
    s = ''
    while Quit == 0:
        print("0. Read data files\n")
        print("1. display statistics\n")
        print("2. Top 5 most tweeted words\n")
        print("3. Top 5 most tweeted users\n")
        print("4. Find users who tweeted a word (e.g., "
              "’연세대’)\n")
        print("5. Find all people who are friends of the above users\n")
        print("6. Delete all mentions of a word\n")
        print("7. Delete all users who mentioned a word\n")
        print("8. Find strongly connected components\n")
        print("9. Find shortest path from a given user\n")
        print("99. Quit\n")
        print("Select Menu:")
        menu = input()
        if menu == '0':
            ReadFile(vertices, verticesw, rb, rbw)
        elif menu == '1':
            Statistic.ANF(vertices)
            Statistic.MinNF(vertices)
            Statistic.MaxNF(vertices)
            Statistic.ATU(vertices)
            Statistic.MinTU(vertices)
            Statistic.MaxTU(vertices)
        elif menu == '2':
            top5w = verticesw
            heap = Heap2(top5w)
            heap.heapsort()
            for i in range(5):
                print(top5w[i].word)
        elif menu == '3':
            top5u = vertices
            heap = Heap()
            heap.A = top5u
            heap.heapsort()
            for i in range(5):
                print(top5u[i].name)
        elif menu == '4':
            print("입력 : ")
            s = input()
            u = rbw.search(s + '\n')
            if u != rbw.nil:
                p = u.firstuser
                while p:
                    u1 = rb.search(p.user)
                    print(u1.name)
                    p = p.next
            else:
                print("그런 단어는 트윗되지 않았습니다.")
        elif menu == '5':
            u = rbw.search(s + '\n')
            p = u.firstuser
            while p:
                u1 = rb.search(p.user)
                print(u1.name + "의 친구들: ")
                p1 = u1.first
                while p1:
                    print(vertices[p1.n].name)
                    p1 = p1.next
                p = p.next
            print('\n')
        elif menu == '6':
            print("삭제할 단어 입력 : ")
            s = input()
            w = rbw.search(s + '\n')
            if w != rbw.nil:
                p = w.firstuser
                while p:
                    rb.search(p.user).wordnum -= 1
                    p = p.next
                rbw.delete_node(w)
                verticesw.remove(w)
                print("삭제되었습니다.\n")
            else:
                print("존재하지 않는 단어입니다.\n")
        elif menu == '7':
            print("이 단어를 트윗한 모든 사람의 데이터가 삭제 됩니다. 입력 : ")
            s = input()
            w = rbw.search(s + '\n')
            if w != rbw.nil:
                u = w.first
                while u:
                    u1 = rb.search(u.user)
                    rb.delete_node(u1)
                    vertices.remove(u1)
                    u = u.next
            else:
                print("존재하지 않는 트윗입니다.\n")
        elif menu == '8':
            DFS = DepthFirstSearch()
            DFS.set_vertices(vertices)
            DFS.scc()
            DFS.print_vertices()
        elif menu == '9':
            print("입력: ")
            u1 = input()
            Dij = Dijkstra()
            w = rb.search(u1+'\n')
            for v in vertices:
                Dij.add_vertex(v)
            Dij.shortestpath(Dij.vertices[w.n])
        elif menu == '99':
            Quit = 1
        else:
            print("Wrong number\n")


def ReadFile(vertices, verticesw, rb, rbw):
    user = open(PATH_USER, 'rt')
    userline = user.readlines()
    friend = open(PATH_FRIEND, 'rt')
    friendline = friend.readlines()
    word = open(PATH_WORD, 'rt')
    wordline = word.readlines()
    n = 0
    for i in range(len(userline)):
        if i%4 == 0:
            v = Vertex(userline[i])
            v.n = n
            v.id = userline[i]
            v.name = userline[i + 2]
            vertices.append(v)
            rb.insert_node(v)
            n += 1
    for i in range(len(friendline)):
        if i%3 == 0:
            v1 = rb.search(friendline[i])
            v2 = rb.search(friendline[i+1])
            v1.add(v2)
            v1.fnum = v1.fnum+1
    n = 0
    for i in range(len(wordline)):
        if i%4 == 0:
            v = rb.search(wordline[i])
            w = Word()
            Word.word = wordline[i+2]
            v.add_word(w)
            v.wordnum = v.wordnum + 1
            w1  = rbw.search(wordline[i+2])
            if w1 == rbw.nil:
                w2 = Vertex(wordline[i+2])
                w2.word = wordline[i+2]
                w2.n = n
                rbw.insert_node(w2)
                verticesw.append(w2)
                u = User()
                u.user = wordline[i]
                w2.add_user(u)
                w2.usernum = w2.usernum + 1
                n += 1
            else:
                u = User()
                u.user = wordline[i]
                w1.add_user(u)
                w1.usernum = w1.usernum + 1

    print("Total users: ", int(len(userline)/4))
    print("Total friendship records: ", int(len(friendline)/3))
    print("Total tweets: ", int(len(wordline)/4))
    print("\n")


class Statistic:
    def ANF(vertices):
        sum = 0
        for v in vertices:
            sum += vertices[v.n].fnum
        print("Average number of friends: ",sum/int(len(vertices)))
    def MinNF(vertices):
        min = 0
        for v in vertices:
            if min > vertices[v.n].fnum:
                min = vertices[v.n].fnum
        print("Minimum friends: " ,min)
    def MaxNF(vertices):
        max = 0
        for v in vertices:
            if max < vertices[v.n].fnum:
                max = vertices[v.n].fnum
        print("Maximum number of friends: ", max)
    def ATU(vertices):
        sum = 0
        for v in vertices:
            sum += vertices[v.n].wordnum
        print("Average tweets per user: ",sum/int(len(vertices)))
    def MinTU(vertices):
        min = 0
        for v in vertices:
            if min > vertices[v.n].wordnum:
                min = vertices[v.n].wordnum
        print("Minimum tweets per user: ", min)

    def MaxTU(vertices):
        max = 0
        for v in vertices:
            if max < vertices[v.n].wordnum:
                max = vertices[v.n].wordnum
        print("Maximum tweets per user: ", max)
        print("\n")


class Adj:
    def __init__(self):
        self.n = 0
        self.next = None

class Word:
    def __init__(self):
        self.word = '(none)'
        self.next = None

class User:
    def __init__(self):
        self.user = '(none)'
        self.next = None

class Weight(Adj):
    def __init__(self, n, w):
        super().__init__()
        self.w = w

class Vertex:
    def __init__(self, key):
        self.color = WHITE
        self.parent = -1
        self.name = '(none)'
        self.n = 0
        self.first = None
        self.id = 0
        self.fnum = 0
        self.f = 0
        self.d2 = 1E01
        self.key = key
        self.red = False
        self.left = None
        self.right = None
        self.p = None
        self.firstword = None
        self.wordnum = 0
        self.firstuser = None
        self.usernum = 0
        self.word = '(none)'
        self.d2 = 1E10
        self.priority = None

    def add(self, v):
        a = Weight(v, v.fnum)
        a.n = v.n
        a.next = self.first
        self.first = a

    def setpriority(self, n):
        self.priority = n

    def decreasekey(self, q):
        prio = self.priority
        ndx = prio.ndx
        q.decreasekey(ndx, self.d2)

    def add_word(self, w):
        a = Word()
        a.word = w.word
        a.next = self.firstword
        self.firstword = a

    def add_user(self, u):
        a = User()
        a.user = u.user
        a.next = self.firstuser
        self.firstuser = a


class Queue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.sz = 0
        self.buf = []

    def create_queue(self, sz):
        self.sz = sz
        self.buf = list(range(sz))

    def enqueue(self, val):
        self.buf[self.rear] = val
        self.rear = (self.rear + 1) % self.sz

    def dequeue(self):
        res = self.buf[self.front]
        self.front = (self.front + 1) % self.sz
        return res

    def is_empty(self):
        return self.front == self.rear


def print_vertex(vertices, n):
    print(vertices[n].name, end=' ')
    print(vertices[n].color, end=' ')
    print(vertices[n].parent, end=' ')
    print(vertices[n].d, end=':')
    p = vertices[n].first
    while p:
        print(vertices[p.n].name, end=' ')
        p = p.next
    print('')


class DepthFirstSearch:
    def __init__(self):
        self.time = 0;
        self.vertices = None

    def set_vertices(self, vertices):
        self.vertices = vertices

    def print_vertices(self):
        for i in range(len(self.vertices)):
            self.print_vertex(i)

    def dfs(self):
        for u in self.vertices:
            u.color = WHITE
            u.parent = -1
        self.time = 0
        for u in self.vertices:
            if u.color == WHITE:
                self.dfs_visit(u)

    def dfs_visit(self, u):
        self.time = self.time + 1
        u.d = self.time
        u.color = GRAY
        v = u.first
        while v:
            if self.vertices[v.n].color == WHITE:
                self.vertices[v.n].parent = u.n
                self.dfs_visit(self.vertices[v.n])
            v = v.next;
        u.color = BLACK
        self.time = self.time + 1
        u.f = self.time

    def print_vertex(self, n):
        print(self.vertices[n].name, end=' ')
        print(self.vertices[n].color, end=' ')
        print(self.vertices[n].parent, end=' ')
        print(self.vertices[n].d, end=' ')
        print(self.vertices[n].f, end=':')
        p = self.vertices[n].first
        while p:
            print(self.vertices[p.n].name, end=' ')
            p = p.next
        print('')

    def print_scc(self, u):
        print(u.name, end=" ")
        vset = self.vertices
        if u.parent >= 0:
            self.print_scc(vset[u.parent])

    def scc_find(self, u):
        u.color = GRAY
        v = u.first
        found = False
        while v:
            if self.vertices[v.n].color == WHITE:
                found = True
                self.vertices[v.n].parent = u.n
                self.scc_find(self.vertices[v.n])
            v = v.next;
        if not found:
            print("SCC:", end=" ")
            self.print_scc(u)
            print("\n")
            u.color = BLACK

    def left(self, n):
        return 2 * n + 1

    def right(self, n):
        return 2 * n + 2

    def heapify(self, A, i, heapsize):
        vset = self.vertices
        l = self.left(i)
        r = self.right(i)
        if l < heapsize and vset[A[l]].f < vset[A[i]].f:
            largest = l
        else:
            largest = i
        if r < heapsize and vset[A[r]].f < vset[A[largest]].f:
            largest = r
        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            self.heapify(A, largest, heapsize)

    def buildheap(self, A):
        for i in range(len(A) // 2 + 1, 0, -1):
            self.heapify(A, i - 1, len(A))

    def heapsort(self, A):
        self.buildheap(A)
        for i in range(len(A), 1, -1):
            A[i - 1], A[0] = A[0], A[i - 1]
            self.heapify(A, 0, i - 1)

    def sort_by_f(self):
        vset = self.vertices
        sorted_indices = list(range(len(vset)))
        self.heapsort(sorted_indices)
        return sorted_indices

    def scc(self):
        self.dfs()
        transpose(self.vertices)
        sorted = self.sort_by_f()
        vset = self.vertices
        for v in vset:
            v.color = WHITE
            v.parent = -1
        for n in sorted:
            if n < 4 and self.vertices[n].color == WHITE:
                self.scc_find(vset[n])


def transpose(vertices):
    vertices2 = []
    for u in vertices:
        v = Vertex(0)
        v.name = u.name
        v.n = u.n
        vertices2.append(v)
    for u in vertices:
        adj_v = vertices[u.n].first
        while adj_v:
            vertices2[adj_v.n].add(vertices2[u.n])
            adj_v = adj_v.next
    return vertices2


class Dijkstra:
    def __init__(self):
        self.vertices = []
        self.q = MinQueue()

    def add_vertex(self, v):
        n = len(self.vertices)
        v1 = v
        v1.n = n
        self.vertices.append(v1)
        return v1

    def get_vertex(self, name):
        for v in self.vertices:
            if v.name == name:
                return v
        return None

    def print_vertex(self, n):
        print(self.vertices[n].name, end=' ')
        print(self.vertices[n].parent, end=' ')
        print(self.vertices[n].d2, end=' ')
        p = self.vertices[n].first
        while p:
            print(p.n.name, end=' ')
            print(p.w, end=' ')
            p = p.next
        print('')

    def print_vertices(self):
        for i in range(len(self.vertices)):
            self.print_vertex(i)

    def relax(self, u):
        vset = self.vertices
        q = self.q
        p = u.first
        v = self.vertices[p.n]
        while p:
            d2 = u.d2 + p.w
            if d2 < v.d2:
                v.d2 = d2
                v.parent = u.n
                print(v)
                v.decreasekey(q)
            p = p.next

    def shortestpath(self,u):
        q = self.q
        vset = self.vertices
        for v in vset:
            n = PrioNode(v.d2, v.n)
            v.setpriority(n)
            q.insert(n)
            self.relax(vset[u.n])


class Heap:
    def __init__(self):
       self.heapsize = 0
       self.A = []
       self.nelem = 0

    def parent(self, n):
        return (n - 1) // 2

    def left(self, n):
        return 2 * n + 1

    def right(self, n):
        return 2 * n + 2

    def exchange(self, i, j):
        A = self.A
        A[i], A[j] = A[j], A[i]

    def heapify(self, i, heapsize):
        A = self.A
        l = self.left(i)
        r = self.right(i)
        if l < heapsize and A[l].wordnum < A[i].wordnum:
            largest = l
        else:
            largest = i
        if r < heapsize and A[r].wordnum < A[largest].wordnum:
            largest = r
        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            self.heapify(largest, heapsize)

    def buildheap(self):
        A = self.A
        for i in range(len(A) // 2 + 1, 0, -1):
            self.heapify(i - 1, len(A))

    def heapsort(self):
        A = self.A
        self.buildheap()
        for i in range(len(A), 1, -1):
            A[i - 1], A[0] = A[0], A[i - 1]
            self.heapify(0, i - 1)

class Heap2:
    def __init__(self, A):
        self.heapsize = 0
        self.A = A

    def parent(self, n):
        return (n - 1) // 2

    def left(self, n):
        return 2 * n + 1

    def right(self, n):
        return 2 * n + 2

    def heapify(self, i, heapsize):
        A = self.A
        l = self.left(i)
        r = self.right(i)
        if l < heapsize and A[l].usernum < A[i].usernum:
            largest = l
        else:
            largest = i
        if r < heapsize and A[r].usernum < A[largest].usernum:
            largest = r
        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            self.heapify(largest, heapsize)

    def buildheap(self):
        A = self.A
        for i in range(len(A) // 2 + 1, 0, -1):
            self.heapify(i - 1, len(A))

    def heapsort(self):
        A = self.A
        self.buildheap()
        for i in range(len(A), 1, -1):
            A[i - 1], A[0] = A[0], A[i - 1]
            self.heapify(0, i - 1)


class PrioNode:
    def __init__(self, key, n):
        self.ndx = 0
        self.n = n
        self.key = key

    def __repr__(self):
        return "(%d:%d,%d)" % (self.ndx, self.n, self.key)


class MaxQueue(Heap):
    def __init__(self):
        super().__init__()

    def compare(self, a, b):
        return a.key > b.key

    def exchange(self, i, j):
        A = self.A
        A[i].ndx = j
        A[j].ndx = i
        super().exchange(i, j)

    def updatekey(self, i):
        parent = lambda x: self.parent(i)
        compare = lambda a, b: self.compare(a, b)
        A = self.A
        while i > 0 and not compare(A[parent(i)], A[i]):
            self.exchange(i, parent(i))
            i = parent(i)

    def increasekey(self, i, key):
        A = self.A
        if key < A[i].key:
            print("Error")
            sys.exit(-1)
        A[i].key = key
        self.updatekey(i)

    def insert(self, n):
        A = self.A
        while (len(A) < self.nelem):
            A.append(None)
        i = self.nelem
        A.append(None)
        self.nelem = self.nelem + 1
        A[i] = n
        A[i].ndx = i
        self.updatekey(i)

    def extract(self):
        elem = self.A[0]
        self.exchange(0, self.nelem - 1)
        self.nelem = self.nelem - 1
        self.heapify(0)
        return elem

    def is_empty(self):
        return self.nelem == 0


class MinQueue(MaxQueue):
    def __init__(self):
        super().__init__()

    def compare(self, a, b):
        return a.key < b.key

    def updatekey(self, i):
        parent = lambda x: self.parent(i)
        A = self.A
        while i > 0 and not self.compare(A[parent(i)], A[i]):
            self.exchange(i, parent(i))
            i = parent(i)

    def decreasekey(self, i, key):
        A = self.A
        if key > A[i].key:
            print("Error")
            sys.exit(-1)
        A[i].key = key
        self.updatekey(i)

    def __repr__(self):
        return "%a %a" % (self.nelem, self.A)


class rbnode(object):
    def __init__(self, key):
        self.key = key
        self.red = False
        self.left = None
        self.right = None
        self.p = None

class rbtree(object):
    def __init__(self, create_node=rbnode):
        self._nil = create_node(key=None)
        self._root = self.nil
        self._create_node = create_node

    root = property(fget=lambda self: self._root, doc="The tree's root node")
    nil = property(fget=lambda self: self._nil, doc="The tree's nil node")

    def search(self, key, x=None):
        if None == x:
            x = self.root
        while x != self.nil and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x


    def minimum(self, x=None):
        if None == x:
            x = self.root
        while x.left != self.nil:
            x = x.left
        return x


    def maximum(self, x=None):
        if None == x:
            x = self.root
        while x.right != self.nil:
            x = x.right
        return x

    def insert_key(self, key):
        self.insert_node(self._create_node(key=key))

    def insert_node(self, z):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == self.nil:
            self._root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.red = True
        self._insert_fixup(z)

    def _insert_fixup(self, z):
        while z.p.red:
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.red:
                    z.p.red = False
                    y.red = False
                    z.p.p.red = True
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self.left_rotate(z)
                    z.p.red = False
                    z.p.p.red = True
                    self.right_rotate(z.p.p)
            else:
                y = z.p.p.left
                if y.red:
                    z.p.red = False
                    y.red = False
                    z.p.p.red = True
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self.right_rotate(z)
                    z.p.red = False
                    z.p.p.red = True
                    self.left_rotate(z.p.p)
        self.root.red = False

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.p = x
        y.p = x.p
        if x.p == self.nil:
            self._root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.nil:
            x.right.p = y
        x.p = y.p
        if y.p == self.nil:
            self._root = x
        elif y == y.p.right:
            y.p.right = x
        else:
            y.p.left = x
        x.right = y
        y.p = x

    def _delete_fixup(self, x):
        while x != self.root and x.red == False:
            if x == x.p.left:
                w = x.p.right
                if w.red == True:
                    w.red = False
                    x.p.red = True
                    self.left_rotate(x.p)
                    w = x.p.right
                if w.left.red == False and w.right.red == False:
                    w.red = True
                    x = x.p
                else:
                    if w.right.red == False:
                        w.left.red = False
                        w.red = True
                        self.right_rotate(w)
                        w= x.p.right
                    w.red = x.p.red
                    x.p.red = False
                    w.right.red = False
                    self.left_rotate(x.p)
                    x = self.root
            else:
                w = x.p.left
                if w.red == True:
                    w.red = False
                    x.p.red = True
                    self.right_rotate(x.p)
                    w = x.p.left
                if w.right.red == False and w.left.red == False:
                    w.red == True
                    x = x.p
                else:
                    if w.left.red == False:
                        w.right.red = False
                        w.red = True
                        self.left_rotate(w)
                        w = x.p.left
                        w.red = x.p.red
                        x.p.red = False
                        w.left.red == False
                        self.right_rotate(x.p)
                        x = self.root
        x.red = False

    def delete_node(self, z):
        if z == self.nil:
            return
        if z.left == self.nil:
            y = z
        else:
            y = z.right
            while y.left != self.nil:
                y = y.left
        if y.left != self.nil:
            x= y.left
        else:
            x = y.right
        x.p = y.p
        if y.p:
           if y == y.p.left:
               y.p.left = x
           else:
                y.p.right = x
        else:
            self.root = x
        if y != z:
            z.key = y.key
        if y.red == False:
            self._delete_fixup(x)



main()