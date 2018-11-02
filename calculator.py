# S-expressions calculator
# Adan J. Suarez

import sys
from model.compute_expression import Compute_Expression as ce

def main():
    expr = sys.argv[1]
    result = ce(expr).get_value()
    print(result)

if __name__ == "__main__":
    main()
    