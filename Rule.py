class Rule:
    def __init__(self, states, symbols):
        self.rules = {}
        self.states = states
        self.symbols = symbols

    #Přidá nový stav do pravidel, pokud neexistuje
    def add_state(self, state):
        if state not in self.rules:
            self.rules[state] = {}

    def add_rule(self, state, read_symbol, new_state, write_symbol, direction):
        # Přidá stav, pokud ještě neexistuje
        self.add_state(state)
        # Uloží pravidlo pro daný stav a symbol
        self.rules[state][read_symbol] = (new_state, write_symbol, direction)

    # Vrátí všechna pravidla
    def get_rules(self):
        return self.rules

    def print_rules_binary(self):
        # Inicializace prázdného řetězce pro binární výstup
        binary_output = ""

        # Pro každé pravidlo projde všechny přechody
        for state, transitions in self.rules.items():
            for read_symbol, (new_state, write_symbol, direction) in transitions.items():
                # Získání binárních hodnot
                bin_state = self.states.get(state, 'UNKNOWN')
                bin_read_symbol = self.symbols.get(read_symbol, 'UNKNOWN')
                bin_new_state = self.states.get(new_state, 'UNKNOWN')
                bin_write_symbol = self.symbols.get(write_symbol, 'UNKNOWN')
                bin_direction = '0' if direction == 'l' else '1'

                # Přidání binárních hodnot do výstupního řetězce
                binary_output += f"{bin_state}{bin_read_symbol}{bin_new_state}{bin_write_symbol}{bin_direction}"

        # Výpis výsledného binárního řetězce
        print(f"\nZakódovaný Turingov stroje:\n{binary_output}")


    def print_rules(self):
        # Vytiskne všechna pravidla
        for state, transitions in self.rules.items():
            print(f"Stav {state}:")
            for read_symbol, (new_state, write_symbol, direction) in transitions.items():
                print(
                    f"  Čte '{read_symbol}' -> Přejde do stavu '{new_state}', zapíše '{write_symbol}', směr '{direction}'")
