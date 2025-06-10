class Clause:
    def __init__(self,head,body=[]):
        self.head=head
        self.body=body
    
class KB:

    def __init__(self,statements=[]):
        self.clauses=[]
        self.atom_to_clause={}

        for statement in statements:
            self.add_clause(statement)

    def add_clause(self,clause):
        self.clauses.append(clause)

        if clause.head not in self.atom_to_clause:
            self.atom_to_clause[clause.head]=[]

        self.atom_to_clause[clause.head].append(clause)

    def clauses_for_atom(self,atom):
        return self.atom_to_clause(atom,[])

def bottom(kb):

    known_facts=set()
    new_facts=set()
    for clause in kb.clauses:
        if not clause.body:
            known_facts.add(clause.head)
            new_facts.add(clause.head)

    print("Initial Known Facts:", known_facts)

    while new_facts:

        current_facts=new_facts.copy()

        new_facts=set()

        for clause in kb.clauses:
            if clause.head not in known_facts:
                if all(atom in known_facts  for atom in clause.body):
                    known_facts.add(clause.head)
                    new_facts.add(clause.head)
    print("Updated Known Facts:", known_facts) 
    return known_facts

triv_KB = KB([
    Clause('i_am', ['i_think']),
    Clause('i_think'),
    Clause('i_smell', ['i_exist']),
    Clause('i_exist')
])

# Run the bottom-up proof procedure
result = bottom(triv_KB)

# Output the result
print("Inferred Facts using BOTTOM-UP APPROACH:")
print(result)


