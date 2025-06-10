pip instll pgmpy

from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

bn_model=BayesianNetwork([('i','m'),('e','m'),('i','s'),('m','a')])

cpd_i=TabularCPD(variable='i',variable_card=2,values=[[0.8],[0.2]])
cpd_e=TabularCPD(variable='e',variable_card=2,values=[[0.7],[0.3]])

cpd_m=TabluarCPD(variable='m',varaible_card=2,values=[[0.6, 0.1, 0.5, 0.8], [0.4, 0.9, 0.5, 0.2]],evidence=['i','e'],evidence_card=[2,2])

bn_model.add_cpds(cpd_i,cpd_e,cpd_m)
assert bn_model.check_model()

print(cpd_i)

inference=VariableElimination(bn_model)

result=inference.query(variables=['i','e','m'],joint=true)
print(result)