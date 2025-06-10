class Node:
    def __init__(self,name,isMax,value=None):
        self.name=name
        self.isMax=isMax
        self.value=value
        self.children=[]

    def add_child(self,child):
        self.children.append(child)

def minimax(node,depth):
    if not node.children:
        return node.value,[node.name]

    if node.isMax:
        maxi=float('-inf')
        best_path=[]

        for child in node.children:
            value,path=minimax(child,depth+1)

            if value>maxi:
                maxi=value
                best_path=path

            return maxi,[node.name] +best_path

    else:

        mini=float('inf')
        best_path=[]

        for child in node.children:
            value,path=minimax(child,depth+1)

            if value<mini:
                mini=value
                best_path=path

            return mini,[node.name] +best_path


root=Node('A',True)
b=Node('B',False)
c=Node('C',False)

root.add_child(b)
root.add_child(c)

d=Node('D',True)
e=Node('E',True)
f=Node('F',True)
g=Node('G',True)

b.add_child(d)
b.add_child(e)
c.add_child(f)
c.add_child(g)

h=Node('H',False)
i=Node('I',False)
j=Node('J',False)
k=Node('K',False)
l=Node('L',False)
m=Node('M',False)
n=Node('N',False)
o=Node('O',False)

d.add_child(h)
d.add_child(i)
e.add_child(j)
e.add_child(k)
f.add_child(l)
f.add_child(m)
g.add_child(n)
g.add_child(o)

p = Node('p', True, 7)
q = Node('q', True, 9)
r = Node('r', True, 6)
r1 = Node('r1', True,8)
s = Node('s', True, 11)
t = Node('t', True, 12)
t1 = Node('t1', True,10)
t2 = Node('t2', True,6)
u = Node('u', True, 5)
u1 = Node('u1', True,3)
v = Node('v', True, 4)
v1 = Node('v1', True,7)
v2 = Node('v2', True,5)
v3 = Node('v3', True,9)
v4 = Node('v4', True,1)
v5 = Node('v5', True,2)
h.add_child(p)
h.add_child(q)
i.add_child(r)
i.add_child(r1)
j.add_child(s)
j.add_child(t)
k.add_child(t1)
k.add_child(t2)
l.add_child(u)
l.add_child(u1)
m.add_child(v)
m.add_child(v1)
n.add_child(v2)
n.add_child(v3)
o.add_child(v4)
o.add_child(v5)
best_score, best_path = minimax(root, 0)
print("Best score:", best_score)
print("Best path:", best_path)