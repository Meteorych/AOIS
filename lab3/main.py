import sdnf_scnf
import minimization

TESTS = ['!((!x1+!x3)*(!x2*!x3))',
        '!(x1+x2)*!(!x2+!x3)',
        '!((!x1+x3)*!(x2*!x3))',
        "!((!x2+x3)*!(x1*!x3))"
]
def main():
    formula = "!((!x2+x3)*!(x1*!x3))"
    table_truth, res_table = sdnf_scnf.first_step(formula)


if __name__ == "__main__":
    main()
