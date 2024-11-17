class TuringMachine:
    def __init__(self, rules, tape, start_state):
        self.rules = rules
        self.current_state = start_state
        self.head_position = 0
        self.tape = list(tape) + ['#'] * (100 - len(tape))  # Doplnění pásky prázdnými symboly

        # Vytisknutí počátečního stavu pásky
        # self.print_tape()

    def step(self):
        symbol = self.tape[self.head_position]

        # Zkontrolujeme, zda pravidlo existuje pro aktuální stav a symbol
        if symbol in self.rules[self.current_state]:
            new_state, new_symbol, direction = self.rules[self.current_state][symbol]
            self.tape[self.head_position] = new_symbol  # Zapište symbol na pásku
            self.current_state = new_state  # Nastavte nový stav

            # Pohyb hlavy
            if direction == 'r':
                self.head_position += 1
            elif direction == 'l':
                self.head_position -= 1
            elif direction == '*':
                print("Halt")
                return False
        else:
            print(f"Pravidlo pro stav {self.current_state} a symbol {symbol} nebylo nalezeno.")
            return False
        return True

    def print_tape(self):
        # Získáme symbol pod hlavou a okolní část pásky
        left_part = "".join(self.tape[:self.head_position])
        current_symbol = self.tape[self.head_position]
        right_part = "".join(self.tape[self.head_position + 1:]).rstrip('#')  # Odstranění prázdných symbolů na konci

        # Vytiskneme aktuální stav v požadovaném formátu
        print(f"{self.current_state} {left_part}[{current_symbol}]{right_part}")

    def print_soft_tape(self):
        # Vytvoříme kopii pásky
        tape_copy = self.tape[:]

        # Přidáme symbol pásky s formátováním pro hlavu
        tape_copy[self.head_position] = f"[{self.tape[self.head_position]}]"

        # Připojíme pásku jako text a odstraníme nadbytečné '#'
        formatted_tape = "".join(tape_copy).replace('#', '').strip()

        # Vytiskneme pásku s hlavou
        print(formatted_tape)