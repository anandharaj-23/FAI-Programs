# Define CPDs for each variable
P_e = {'difficult': 0.4, 'easy': 0.6}
P_i = {'high': 0.7, 'low': 0.3}
P_m_given_e_i = {
    ('difficult', 'high'): {'high': 0.9, 'low': 0.1},
    ('difficult', 'low'): {'high': 0.4, 'low': 0.6},
    ('easy', 'high'): {'high': 0.6, 'low': 0.4},
    ('easy', 'low'): {'high': 0.1, 'low': 0.9}
}
P_a_given_m = {
    'high': {'yes': 0.8, 'no': 0.2},
    'low': {'yes': 0.5, 'no': 0.5}
}
P_s_given_i = {
    'high': {'good': 0.6, 'poor': 0.4},
    'low': {'good': 0.3, 'poor': 0.7}
}

# Function to print the CPD for Exam Level (e)
def print_cpd_exam_level():
    print("CPD for Exam Level (e):")
    print("+----------------+------+")
    print("| e              | P(e) |")
    print("+----------------+------+")
    for e_state, prob in P_e.items():
        print(f"| {e_state:<14} | {prob:<4} |")
    print("+----------------+------+\n")

# Function to print the CPD for IQ (i)
def print_cpd_iq():
    print("CPD for IQ (i):")
    print("+----------------+------+")
    print("| i              | P(i) |")
    print("+----------------+------+")
    for i_state, prob in P_i.items():
        print(f"| {i_state:<14} | {prob:<4} |")
    print("+----------------+------+\n")

# Function to print the CPD for Marks (m) given Exam Level (e) and IQ (i)
def print_cpd_marks():
    print("CPD for Marks (m):")
    print("+----------------+----------------+----------------+----------------+")
    print("| e              | i              | P(m=high)      | P(m=low)       |")
    print("+----------------+----------------+----------------+----------------+")
    for (e_state, i_state), m_probs in P_m_given_e_i.items():
        print(f"| {e_state:<14} | {i_state:<14} | {m_probs['high']:<14} | {m_probs['low']:<14} |")
    print("+----------------+----------------+----------------+----------------+\n")

# Function to print the CPD for Admission (a) given Marks (m)
def print_cpd_admission():
    print("CPD for Admission (a):")
    print("+----------------+----------------+----------------+")
    print("| m              | P(a=yes)       | P(a=no)        |")
    print("+----------------+----------------+----------------+")
    for m_state, a_probs in P_a_given_m.items():
        print(f"| {m_state:<14} | {a_probs['yes']:<14} | {a_probs['no']:<14} |")
    print("+----------------+----------------+----------------+\n")

# Function to print the CPD for Aptitude Score (s) given IQ (i)
def print_cpd_aptitude_score():
    print("CPD for Aptitude Score (s):")
    print("+----------------+----------------+----------------+")
    print("| i              | P(s=good)      | P(s=poor)      |")
    print("+----------------+----------------+----------------+")
    for i_state, s_probs in P_s_given_i.items():
        print(f"| {i_state:<14} | {s_probs['good']:<14} | {s_probs['poor']:<14} |")
    print("+----------------+----------------+----------------+\n")

# Function to calculate Joint Probability Distribution (JPD)
def calculate_jpd(e_state, i_state, m_state, a_state, s_state):
    P_e_val = P_e[e_state]
    P_i_val = P_i[i_state]
    P_m_val = P_m_given_e_i[(e_state, i_state)][m_state]
    P_a_val = P_a_given_m[m_state][a_state]
    P_s_val = P_s_given_i[i_state][s_state]
    jpd = P_e_val * P_i_val * P_m_val * P_a_val * P_s_val
    return jpd

# Function to calculate and print the Joint Probability Distribution (JPD) table
def print_jpd_table():
    print("Joint Probability Distribution Table:")
    print("+----------------+----------------+----------------+----------------+----------------+----------------+")
    print("| e              | i              | m              | a              | s              | P(e, i, m, a, s) |")
    print("+----------------+----------------+----------------+----------------+----------------+----------------+")
    for e_state in P_e.keys():
        for i_state in P_i.keys():
            for m_state in ['high', 'low']:
                for a_state in ['yes', 'no']:
                    for s_state in ['good', 'poor']:
                        jpd = calculate_jpd(e_state, i_state, m_state, a_state, s_state)
                        print(f"| {e_state:<14} | {i_state:<14} | {m_state:<14} | {a_state:<14} | {s_state:<14} | {jpd:<14.4f} |")
    print("+----------------+----------------+----------------+----------------+----------------+----------------+")

# Function to print the Joint Probability Distribution formula
def print_jpd_formula():
    print("Joint Probability Distribution Formula:")
    print("P(e, i, m, a, s) = P(e) * P(i) * P(m | e, i) * P(a | m) * P(s | i)\n")
    print("Where:")
    print(" P(e): Probability of Exam Level")
    print(" P(i): Probability of IQ")
    print(" P(m | e, i): Probability of Marks given Exam Level and IQ")
    print(" P(a | m): Probability of Admission given Marks")
    print(" P(s | i): Probability of Aptitude Score given IQ\n")

# Function to calculate and print a sample Joint Probability Distribution
def get_input_and_print_probability():
    print("Enter the states for the following variables (leave blank for unknown):")
    e_state = input("Exam Level (e) [difficult/easy]: ").strip().lower() or None
    i_state = input("IQ (i) [high/low]: ").strip().lower() or None
    m_state = input("Marks (m) [high/low]: ").strip().lower() or None
    a_state = input("Admission (a) [yes/no]: ").strip().lower() or None
    s_state = input("Aptitude Score (s) [good/poor]: ").strip().lower() or None
    
    valid_states_e = list(P_e.keys())
    valid_states_i = list(P_i.keys())
    valid_states_m = ['high', 'low']
    valid_states_a = ['yes', 'no']
    valid_states_s = ['good', 'poor']
    
    states_to_check = {
        'e': valid_states_e if e_state is None else [e_state],
        'i': valid_states_i if i_state is None else [i_state],
        'm': valid_states_m if m_state is None else [m_state],
        'a': valid_states_a if a_state is None else [a_state],
        's': valid_states_s if s_state is None else [s_state],
    }
    
    total_jpd = 0
    print("\nCalculating JPD for the following combinations:")
    for e in states_to_check['e']:
        for i in states_to_check['i']:
            for m in states_to_check['m']:
                for a in states_to_check['a']:
                    for s in states_to_check['s']:
                        jpd = calculate_jpd(e, i, m, a, s)
                        total_jpd += jpd
                        print(f"P(e={e}, i={i}, m={m}, a={a}, s={s}) = {jpd:.4f}")
    
    print(f"\nTotal Joint Probability for the given states = {total_jpd:.4f}")

# Call functions to print all CPDs
print_cpd_exam_level()
print_cpd_iq()
print_cpd_marks()
print_cpd_admission()
print_cpd_aptitude_score()

# Print Joint Probability Distribution Formula
print_jpd_formula()

# Print Joint Probability Distribution Table
print_jpd_table()

# Call the function to get input and print the probability
get_input_and_print_probability()