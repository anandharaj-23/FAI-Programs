class Clause:

    def __init__(self,head,body=[]):
        self.head=head
        self.body=body

class KB:

    def __init__(self,statements=[]):
        self.clauses=[]
        self.atom_to_clauses={}

        for statement in statements:
            self.add_clause(statement)

    def add_clause(self,clause):

        self.clauses.append(clause)

        if clause.head not in self.atom_to_clauses:
            self.atom_to_clauses[clause.head]=[]
        self.atom_to_clauses[clause.head].append(clause)

    def clause_for_atom(self,atom):
        return self.atom_to_clauses.get(atom,[])

def prove(kb,goals,seen=None):

    if seen is None:
        seen=set()

    for atom in goals:
        if atom in seen:
            return False
        seen.add(atom)

        found_proof=False

        for clause in kb.clause_for_atom(atom):
            if not clause.body:
                found_proof=True
                break

            if all(prove(kb,[body_atom],seen) for body_atom in clause.body):
                found_proof=True
                break
        
        if not found_proof :
            return False
    return True


kb=KB([Clause("i_am",["i_think"]),Clause("i_think"),Clause("i_smell",["i_exist"]),Clause("i_exist")])

goals=["i_am","i_smell"]

print(prove(kb,goals))



    
