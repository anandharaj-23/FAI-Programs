class Clause(object):
    def __init__(self, head, body=[]):
        self.head = head
        self.body = body

class Askable(object):
    def __init__(self, atom):
        self.atom = atom

class KB:
    def __init__(self, statements=[]):
        self.clauses = []
        self.askables = []
        self.atom_to_clauses = {}

        for statement in statements:
            self.add_clause(statement)

    def add_clause(self, c):
        self.clauses.append(c)
        if c.head not in self.atom_to_clauses:
            self.atom_to_clauses[c.head] = []
        self.atom_to_clauses[c.head].append(c)

    def clauses_for_atom(self, a):
        return self.atom_to_clauses.get(a, [])

def bottom_up_proof(kb):
    known = set()
    new = set()

    while True:
        for clause in kb.clauses:
            if all(body_atom in known for body_atom in clause.body):
                if clause.head not in known:
                    new.add(clause.head)
        if not new:
            break
        known.update(new)
        new.clear()
    return known

def prove(kb, goal):
    if not goal:
        return True
    first, *rest = goal
    for clause in kb.clauses_for_atom(first):
        if prove(kb, clause.body + rest):
            return True
    return False

def add_new_clause(kb, head, body=[]):
    new_clause = Clause(head, body)
    kb.add_clause(new_clause)
    print(f"New clause added: {head} :- {body}")

triv_KB = KB([
    Clause('i_am', ['i_think']),
    Clause('i_think'),
    Clause('i_exist'),
    Clause('i_smell', ['i_exist'])
])

consequence_set = bottom_up_proof(triv_KB)
print("\nBottom-up proof consequence set:\n", consequence_set)

goal = ['i_am']
is_provable = prove(triv_KB, goal)
print("\nTop-down proof for goal 'i_am':", is_provable)

goal = ['i_smell']
is_provable = prove(triv_KB, goal)
print("\nTop-down proof for goal 'i_smell':", is_provable)

add_new_clause(triv_KB, 'i_see', ['i_exist'])

goal = ['i_see']
is_provable = prove(triv_KB, goal)
print("\nTop-down proof for goal 'i_see' after adding new clause:", is_provable)

updated_consequence_set = bottom_up_proof(triv_KB)
print("\nUpdated bottom-up proof consequence set:", updated_consequence_set)

goal = ['i_fly']
is_provable = prove(triv_KB, goal)
print("\nTop-down proof for goal 'i_fly':", is_provable)
