Simulátor Turingova stroje

    Tento projekt implementuje simulátor Turingova stroje pro provádění sčítání tří binárních čísel a zakódovaní jednotlivých stavů a symbolů do binární podoby.

Vstupní parametry:

    - start_state: Počáteční stav
    - tape: Vstupní páska

    𝛿 ( 𝑝 , 𝑋 ) = ( 𝑞 , 𝑌 , D ) , kde 5 n-tic je striktně v pořadí p, X, Y, D, q (znak _ představuje prázdný symbol na pásce)
    - state (str): Aktuální stav, např. 'q0'.
    - read_symbol (str): Symbol, který Turingův stroj čte na pásce.
    - new_state (str): Nový stav, do kterého přejde po vykonání tohoto pravidla.
    - write_symbol (str): Symbol, který zapíše na pásku.
    - direction (str): Směr pohybu ('r' nebo 'l').

SW
    Python 3.12

Spuštění projektu
    Main.py: consolový výstup

    vstup:  101_10_110
    výstup: 1101

Architektura projektu
    - Main.py: Spouští skript projektu
    - Rule.py: Správa pravidel pro Turinguv Stroj
    - TuringMachine.py: Implementace Turingova stroje
    - README.md: Dokumentace projektu

Autor: Radovan Němec

Použité zdroje:
    https://turingmachine.io/
    https://www.cs.princeton.edu/courses/archive/fall17/cos126/lectures/CS.15.Turing-2x2.pdf
    https://stackoverflow.com/questions/59045832/turing-machine-for-addition-and-comparison-of-binary-numbers