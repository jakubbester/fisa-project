from z3 import *

if __name__ == "__main__":
    s = Solver()
    s.from_file("50 USC 1801 (f)-z3.txt")
    print(s.check())
    print(s.model())
