from Rule import Rule
from TuringMachine import TuringMachine

#           AND                     XOR
#       A   B   A + B           A   B   A * B
#       0   0   0               0   0   0
#       0   1   1               0   1   1
#       1   0   1               1   0   1
#       1   1   0               1   1   0


# nastavení počátečního stavu
start_state = 'q_start'

# Zadání pásky k sečtení
tape = "_101_110"
#tape = "_101_10_110"

# Definovat jednotlivé přechodové stavy
# Přidávání pravidel pomocí metody add_rule
rules = Rule()

# První fáze: Zpracování prvních dvou čísel
rules.add_rule('q_start', '_', 'q0', '_', 'r'),

rules.add_rule('q0', '0', 'q0', '0', 'r'),
rules.add_rule('q0', '1', 'q0', '1', 'r'),
rules.add_rule('q0', '_', 'q1', '_', 'r'),

rules.add_rule('q1', '0', 'q1', '0', 'r'),
rules.add_rule('q1', '1', 'q1', '1', 'r'),
rules.add_rule('q1', '_', 'q2', '_', 'l'),

rules.add_rule('q2', '0', 'q2', '1', 'l'),
rules.add_rule('q2', '1', 'q3', '0', 'l'),
rules.add_rule('q2', '_', 'q5', '_', 'r'),

rules.add_rule('q3', '0', 'q3', '0', 'l'),
rules.add_rule('q3', '1', 'q3', '1', 'l'),
rules.add_rule('q3', '_', 'q4', '_', 'l'),

rules.add_rule('q4', '0', 'q0', '1', 'l'),
rules.add_rule('q4', '1', 'q4', '0', 'l'),
rules.add_rule('q4', '_', 'q0', '1', 'r'),

rules.add_rule('q5', '1', 'q5', '_', 'r'),
rules.add_rule('q5', '_', 'halt', '_', '*'),


# Získání slovníku pravidel
rule = rules.get_rules()

# Vytisknutí všech pravidel
#rules.print_rules()

# Vytvoření instance Turingova stroje
tm = TuringMachine(rule, tape, start_state)

# Simulace běhu
while tm.step():
    # Vypíše aktuální stav pásky při každém kroku
    tm.print_tape()