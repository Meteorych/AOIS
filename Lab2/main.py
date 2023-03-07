import Analyzing


def main():
    # formula = input("Input logic formula:")
    formula = "!((!x1+!x3)*!(!x2*!x3))"
    # formula = "!((x1+x3)*!(x2*x3))"
    Analyzing.first_step(formula)


if __name__ == '__main__':
    main()
