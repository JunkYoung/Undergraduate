WHITE = 0
GRAY = 1
BLACK = 2


class Adj:
    def __init__(self):
        self.n = 0
        self.next = None


class Vertex:
    def __init__(self):
        self.color = WHITE
        self.parent = -1
        self.name = '(none)'
        self.n = 0
        self.first = None

    def add(self, v):
        a = Adj()
        a.n = v.n
        a.next = self.first
        self.first = a


class BFSVertex(Vertex):
    def __init__(self):
        super().__init__()
        self.d = 1E10  # infty


class DFSVertex(Vertex):
    def __init__(self):
        super().__init__()
        self.d = 0
        self.f = 0


class Queue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.sz = 0
        self.buf = []

    def create_queue(self, sz):
        self.sz = sz
        self.buf = list(range(sz))  # malloc(sizeof(int)*sz)

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

    def transpose(self):
        vertices2 = []
        for u in self.vertices:
            v = DFSVertex()
            v.name = u.name
            v.n = u.n
            vertices2.append(v)
        for u in self.vertices:
            adj_v = self.vertices[u.n].first
            while adj_v:
                vertices2[adj_v.n].add(vertices2[u.n])
                adj_v = adj_v.next
        self.vertices = vertices2


def bfs(vertices, s):
    for u in vertices:
        if u.n != s.n:
            u.color = WHITE
            u.d = 1E10
            u.parent = -1
    s.color = GRAY
    s.d = 0
    s.parent = -1
    q = Queue()
    q.create_queue(len(vertices))
    q.enqueue(s.n)  # enquque node number
    while not q.is_empty():
        u = q.dequeue()  # node number
        adj_v = vertices[u].first
        while adj_v:
            if vertices[adj_v.n].color == WHITE:
                vertices[adj_v.n].color = GRAY  # gray
                vertices[adj_v.n].d = vertices[u].d + 1
                vertices[adj_v.n].parent = u
                q.enqueue(adj_v.n)
            adj_v = adj_v.next
        vertices[u].color = BLACK  # black


def transpose(vertices):
    vertices2 = []
    for u in vertices:
        v = BFSVertex()
        v.name = u.name
        v.n = u.n
        vertices2.append(v)
    for u in vertices:
        adj_v = vertices[u.n].first
        while adj_v:
            vertices2[adj_v.n].add(vertices2[u.n])
            adj_v = adj_v.next
    return vertices2

def test_main():
    r = BFSVertex()
    s = BFSVertex()
    t = BFSVertex()
    u = BFSVertex()
    v = BFSVertex()
    w = BFSVertex()
    x = BFSVertex()
    y = BFSVertex()
    vertices = [r, s, t, u, v, w, x, y]
    r.name = 'r'
    r.n = 0
    s.name = 's'
    s.n = 1
    t.name = 't'
    t.n = 2
    u.name = 'u'
    u.n = 3
    v.name = 'v'
    v.n = 4
    w.name = 'w'
    w.n = 5
    x.name = 'x'
    x.n = 6
    y.name = 'y'
    y.n = 7
    r.add(s)
    r.add(v)
    s.add(r)
    s.add(w)
    t.add(w)
    t.add(x)
    t.add(u)
    u.add(t)
    u.add(x)
    u.add(y)
    v.add(r)
    w.add(s)
    w.add(t)
    w.add(x)
    x.add(w)
    x.add(t)
    x.add(u)
    x.add(y)
    y.add(x)
    y.add(u)
    vertices = transpose(vertices)
    s = vertices[1]
    bfs(vertices, s)
    for i in range(0, len(vertices)):
        print_vertex(vertices, i)

def main():
    r = DFSVertex()
    s = DFSVertex()
    t = DFSVertex()
    u = DFSVertex()
    v = DFSVertex()
    w = DFSVertex()
    x = DFSVertex()
    y = DFSVertex()
    vertices = [r, s, t, u, v, w, x, y]
    r.name = 'r'
    r.n = 0
    s.name = 's'
    s.n = 1
    t.name = 't'
    t.n = 2
    u.name = 'u'
    u.n = 3
    v.name = 'v'
    v.n = 4
    w.name = 'w'
    w.n = 5
    x.name = 'x'
    x.n = 6
    y.name = 'y'
    y.n = 7
    r.add(s)
    r.add(v)
    s.add(r)
    s.add(w)
    t.add(w)
    t.add(x)
    t.add(u)
    u.add(t)
    u.add(x)
    u.add(y)
    v.add(r)
    w.add(s)
    w.add(t)
    w.add(x)
    x.add(w)
    x.add(t)
    x.add(u)
    x.add(y)
    y.add(x)
    y.add(u)

    DFS = DepthFirstSearch()
    DFS.set_vertices(vertices)
    DFS.transpose()
    DFS.dfs()
    for i in range(0, len(vertices)):
        DFS.print_vertex(i)

print("DFS with transpose")
main()
print("")
print("BFS with transpose")
test_main()