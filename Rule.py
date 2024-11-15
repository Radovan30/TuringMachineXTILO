class Rule:
    def __init__(self):
        self.rules = {}

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

    def print_rules(self):
        # Vytiskne všechna pravidla
        for state, transitions in self.rules.items():
            print(f"Stav {state}:")
            for read_symbol, (new_state, write_symbol, direction) in transitions.items():
                print(
                    f"  Čte '{read_symbol}' -> Přejde do stavu '{new_state}', zapíše '{write_symbol}', směr '{direction}'")