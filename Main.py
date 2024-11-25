from Rule import Rule
from TuringMachine import TuringMachine

# nastavení počátečního stavu
start_state = 'q_start'

# Zadání pásky k sečtení
tape = "#101#10#110#"       # 1101

# q_start        - spuštění
# q1             - přesun přes 1 číslo
# q2             - přesun přes 2 číslo
# q3             - přesun na konec 3 čísla
# q_go_end       - označené konce pásky písmenem 'k'
# q_to_start     - přechod na začátek pásky
# q4             - pohyb doprava
# q_swap_hash    - vyměna symbolu '#' za '+'
# q_sum          - sčítání
# q_save0        - vybrano číslo 0
# q_save1        - vybráno číslo 1
# q_delete0      - smaže 0
# q_delete1      - smaže 1
# q_replace0     - připočti 0
# q_replace1     - přídání
# q_carry        - přenos bitů

# Mapa stavů do binárních kódů
states = {
    'q_start': '0000',
    'q1': '0001',
    'q2': '0010',
    'q3': '0011',
    'q_go_end': '0100',
    'q_to_start': '0101',
    'q4': '0110',
    'q_swap_hash': '0111',
    'q_sum': '1000',
    'q_save1': '1001',
    'q_save0': '1010',
    'q_replace1': '1011',
    'q_replace0': '1100',
    'q_delete1': '1101',
    'q_delete0': '1110',
    'q_carry': '1111',
    'q_update': '0000'  # Recyklace kódu pro q_update
}

# Mapa symbolů do binárních kódů
symbols = {
    '0': '000',
    '1': '001',
    '#': '010',
    'z': '011',
    '+': '100',
    'c': '101',
    'O': '110',
    'I': '111',
    '_': '000'  # Recyklace prázdného symbolu
}


# Definovat jednotlivé přechodové stavy
# Přidávání pravidel pomocí metody add_rule  ('q_start', '_'): ('q0', '_', 'r'),
rules = Rule(states, symbols)

# Zapíše 'z' na začátek čísel
rules.add_rule('q_start', '1', 'q_start', '1', 'l'),
rules.add_rule('q_start', '#', 'q1', 'z', 'r'),

# Přesun 1 doprava, přes 1 číslo dokud nenajde '#'
rules.add_rule('q1', '0', 'q1', '0', 'r')
rules.add_rule('q1', '1', 'q1', '1', 'r')
rules.add_rule('q1', '#', 'q2', '#', 'r')

# Přesun doprava, přes 2 číslo dokud nenajde '#'
rules.add_rule('q2', '0', 'q2', '0', 'r')
rules.add_rule('q2', '1', 'q2', '1', 'r')
rules.add_rule('q2', '#', 'q3', '#', 'r')

# Přesun doprava, přes 3 číslo dokud nenajde '#'
rules.add_rule('q3', '0', 'q3', '0', 'r')
rules.add_rule('q3', '1', 'q3', '1', 'r')
rules.add_rule('q3', '#', 'q_go_end', '#', 'r')

# Přepíše # na symbol 'k'
rules.add_rule('q_go_end', '#', 'q_to_start', 'k', 'l')

# Přesun na začátek
rules.add_rule('q_to_start', '0', 'q_to_start', '0', 'l')
rules.add_rule('q_to_start', '1', 'q_to_start', '1', 'l')
rules.add_rule('q_to_start', '#', 'q_to_start', '#', 'l')
rules.add_rule('q_to_start', 'z', 'q4', 'z', 'r')

# Přesun doprava, příprava na sčítání
rules.add_rule('q4', '0', 'q4', '0', 'r')
rules.add_rule('q4', '1', 'q4', '1', 'r')
rules.add_rule('q4', '#', 'q_swap_hash', '+', 'r')
rules.add_rule('q4', '_', 'q4', '_', 'r')

# Pravidla pro stav 'q_swap_hash'
rules.add_rule('q_swap_hash', '#', 'q_sum', '#', 'l')
rules.add_rule('q_swap_hash', '1', 'q_swap_hash', '1', 'r')
rules.add_rule('q_swap_hash', '0', 'q_swap_hash', '0', 'r')

# Čtení bitů
rules.add_rule('q_sum', '1', 'q_save1', 'c', 'l')
rules.add_rule('q_sum', '0', 'q_save0', 'c', 'l')
rules.add_rule('q_sum', '+', 'q_update', '_', 'l')

# Práce s bitem 1
rules.add_rule('q_save1', '0', 'q_save1', '0', 'l')
rules.add_rule('q_save1', '1', 'q_save1', '1', 'l')
rules.add_rule('q_save1', '+', 'q_replace1', '+', 'l')

# Práce s bitem 0
rules.add_rule('q_save0', '0', 'q_save0', '0', 'l')
rules.add_rule('q_save0', '1', 'q_save0', '1', 'l')
rules.add_rule('q_save0', '+', 'q_replace0', '+', 'l')

# Připočítání bitu 1
rules.add_rule('q_replace1', '0', 'q_delete1', 'I', 'r')
rules.add_rule('q_replace1', '1', 'q_carry', 'O', 'l')
rules.add_rule('q_replace1', 'O', 'q_replace1', 'O', 'l')
rules.add_rule('q_replace1', 'I', 'q_replace1', 'I', 'l')
rules.add_rule('q_replace1', '_', 'q_replace1', '_', 'l')

# Připočítání bitu 0
rules.add_rule('q_replace0', '0', 'q_delete0', 'O', 'r')
rules.add_rule('q_replace0', '1', 'q_delete0', 'I', 'r')
rules.add_rule('q_replace0', 'O', 'q_replace0', 'O', 'l')
rules.add_rule('q_replace0', 'I', 'q_replace0', 'I', 'l')
rules.add_rule('q_replace0', '_', 'q_replace0', '_', 'l')

# Vymazání dočasného symbolu při práci s 1
rules.add_rule('q_delete1', '0', 'q_delete1', '0', 'r')  # Pokračuje doprava přes 0
rules.add_rule('q_delete1', '1', 'q_delete1', '1', 'r')  # Pokračuje doprava přes 1
rules.add_rule('q_delete1', 'O', 'q_delete1', 'O', 'r')  # Pokračuje doprava přes O
rules.add_rule('q_delete1', 'I', 'q_delete1', 'I', 'r')  # Pokračuje doprava přes I
rules.add_rule('q_delete1', '+', 'q_delete1', '+', 'r')  # Pokračuje doprava přes +
rules.add_rule('q_delete1', '_', 'q_delete1', '_', 'r')  # Pokračuje doprava přes mezeru
rules.add_rule('q_delete1', 'c', 'q_sum', '_', 'l')  # Vymaže c a vrátí se do stavu 'q_sum'

# Vymazání dočasného symbolu při práci s 0
rules.add_rule('q_delete0', '0', 'q_delete0', '0', 'r')  # Pokračuje doprava přes 0
rules.add_rule('q_delete0', '1', 'q_delete0', '1', 'r')  # Pokračuje doprava přes 1
rules.add_rule('q_delete0', 'O', 'q_delete0', 'O', 'r')  # Pokračuje doprava přes O
rules.add_rule('q_delete0', 'I', 'q_delete0', 'I', 'r')  # Pokračuje doprava přes I
rules.add_rule('q_delete0', '+', 'q_delete0', '+', 'r')  # Pokračuje doprava přes +
rules.add_rule('q_delete0', '_', 'q_delete0', '_', 'r')  # Pokračuje doprava přes mezeru
rules.add_rule('q_delete0', 'c', 'q_sum', '_', 'l')   # Vymaže c a vrátí se do stavu 'q_sum'

# Přenos bitu
rules.add_rule('q_carry', '0', 'q_delete1', '1', 'r')    # Přenese 1, pokud narazí na 0
rules.add_rule('q_carry', 'z', 'q_delete1', '1', 'r')    # Přenese 1, pokud narazí na z
rules.add_rule('q_carry', '1', 'q_carry', '0', 'l')  # Přenese 0 a pokračuje vlevo
rules.add_rule('q_carry', ' ', 'q_carry', '_', 'l')  # Pokračuje vlevo, pokud narazí na mezeru
rules.add_rule('q_carry', '+', 'q_carry', '+', 'l')  # Pokračuje vlevo přes +
rules.add_rule('q_carry', 'O', 'q_carry', 'O', 'l')  # Pokračuje vlevo přes O
rules.add_rule('q_carry', 'I', 'q_carry', 'I', 'l')  # Pokračuje vlevo přes I
rules.add_rule('q_carry', 'c', 'q_sum', '_', 'l')     # Vrací se do stavu 'q_sum' po přenosu


rules.add_rule('q_update', '_', 'q_update', '_', 'l')  # Zůstává mezera a pohybuje se doleva
rules.add_rule('q_update', 'I', 'q_update', '1', 'l')  # Přepisuje I na 1 a pohybuje se doleva
rules.add_rule('q_update', 'O', 'q_update', '0', 'l')  # Přepisuje O na 0 a pohybuje se doleva
rules.add_rule('q_update', '1', 'q_update', '1', 'l')  # Zůstává 1 a pohybuje se doleva
rules.add_rule('q_update', '0', 'q_update', '0', 'l')  # Zůstává 0 a pohybuje se doleva
rules.add_rule('q_update', 'z', 'q4', 'z', 'r')        # Zůstává zapsané z a přesune se doprava
rules.add_rule('q_update', '#', 'q_update', '#', '*')  # Přepisuje # na z a přechází doprava


# Získání slovníku pravidel
rule = rules.get_rules()

# Vytisknutí všech pravidel
#rules.print_rules()

# Vytvoření instance Turingova stroje
tm = TuringMachine(rule, tape, start_state)

# Simulace běhu
while tm.step():
    # Vypíše aktuální stav pásky při každém kroku i názvy stavů (q1 z[1]01#10#110)
    # tm.print_tape()

    # Vypíše aktuální stav pásky při každém kroku (jen páska s čísly bez # - > z[1]0110110 )
     tm.print_soft_tape()

# Vytiskně zakódované pravidla Turingova stroje
rules.print_rules_binary()