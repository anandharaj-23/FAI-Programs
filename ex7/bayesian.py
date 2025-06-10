pip install pgmpy


from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define the structure of the Bayesian Network
bn_model = BayesianNetwork([
    ('IQ Level', 'Marks'),        # IQ Level influences Marks
    ('Exam Level', 'Marks'),      # Exam Level influences Marks
    ('IQ Level', 'Aptitude Score'),  # IQ Level influences Aptitude Score
    ('Marks', 'Admission')        # Marks influence Admission
])

# Define the Conditional Probability Tables (CPTs)

# 1. CPT for IQ Level (I)
cpd_iq = TabularCPD(variable='IQ Level', variable_card=2, values=[[0.8], [0.2]])

# 2. CPT for Exam Level (E)
cpd_exam = TabularCPD(variable='Exam Level', variable_card=2, values=[[0.7], [0.3]])

# 3. CPT for Marks (M), which depends on IQ Level (I) and Exam Level (E)
cpd_marks = TabularCPD(
    variable='Marks', variable_card=2,
    values=[[0.6, 0.1, 0.5, 0.8], [0.4, 0.9, 0.5, 0.2]],
    evidence=['IQ Level', 'Exam Level'],
    evidence_card=[2, 2]
)

# 4. CPT for Aptitude Score (S), which depends on IQ Level (I)
cpd_aptitude = TabularCPD(
    variable='Aptitude Score', variable_card=2,
    values=[[0.75, 0.4], [0.25, 0.6]],
    evidence=['IQ Level'],
    evidence_card=[2]
)

# 5. CPT for Admission (A), which depends on Marks (M)
cpd_admission = TabularCPD(
    variable='Admission', variable_card=2,
    values=[[0.6, 0.9], [0.4, 0.1]],
    evidence=['Marks'],
    evidence_card=[2]
)

# Add all the CPDs to the model
bn_model.add_cpds(cpd_iq, cpd_exam, cpd_marks, cpd_aptitude, cpd_admission)

# Verify the model is correctly defined
assert bn_model.check_model()

# Print CPTs for each variable
print("CPT for IQ Level:")
print(cpd_iq)
print("\nCPT for Exam Level:")
print(cpd_exam)
print("\nCPT for Marks:")
print(cpd_marks)
print("\nCPT for Aptitude Score:")
print(cpd_aptitude)
print("\nCPT for Admission:")
print(cpd_admission)

# Perform inference to calculate the joint probability distribution
inference = VariableElimination(bn_model)

# Calculate and print the joint probability distribution for each combination of variables
# For simplicity, we’ll calculate a few queries to illustrate.

# Example: P(Marks=1 | IQ Level=1, Exam Level=0)
result = inference.query(variables=['Marks'], evidence={'IQ Level': 1, 'Exam Level': 0})
print("\nP(Marks=1 | IQ Level=1, Exam Level=0):")
print(result)

# Example: Full joint probability distribution (over all variable states)
# In practice, calculating the full joint can be complex, as it involves all possible states.
# However, we can compute conditional distributions or specific cases as shown above.
