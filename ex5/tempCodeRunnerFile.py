
root = Node('a', True)
b = Node('b', False)
c = Node('c', False)
root.add_child(b)
root.add_child(c)

d = Node('d', True)
e = Node('e', True)
f = Node('f', True)
g = Node('g', True)
b.add_child(d)
b.add_child(e)
c.add_child(f)
c.add_child(g)
h = Node('h', False)
i = Node('i', False)
j = Node('j', False)
k = Node('k', False)
l = Node('l', False)
m = Node('m', False)
n = Node('n', False)
o = Node('o', False)
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
r1 = Node('r1', True)
s = Node('s', True, 11)
t = Node('t', True, 12)
t1 = Node('t1', True)
t2 = Node('t2', True)
u = Node('u', True, 5)
u1 = Node('u1', True)
v = Node('v', True, 4)
v1 = Node('v1', True)
v2 = Node('v2', True)
v3 = Node('v3', True)
v4 = Node('v4', True)
v5 = Node('v5', True)
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
best_score_ab, best_path_ab = minimax_alpha_beta(root, 0, float('-inf'), float('inf'))
print("Best score (with alpha-beta pruning):", best_score_ab)
print("Best path (with alpha-beta pruning):", best_path_ab)