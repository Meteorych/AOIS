import itertools


def first_step(formula):
    list_formula = [char for char in formula]
    for i in range(0, len(list_formula)):
        if list_formula[i] == "!":
            list_formula[i] = " not "
        elif list_formula[i] == "*":
            list_formula[i] = " and "
        elif list_formula[i] == "+":
            list_formula[i] = " or "
    table_of_truth = list(itertools.product(range(2), repeat=3))
    res_value_formulas_table = comparing_table_and_formula(list_formula, table_of_truth)
    print("Table of truth: ")
    [print("".join(str(list(zip(table_of_truth, res_value_formulas_table))[i]))) for i in
     range(len(res_value_formulas_table))]
    preparations_for_operations(res_value_formulas_table, table_of_truth)


def preparations_for_operations(res, table):
    SDNF_numbers, SCNF_numbers, numeric_SDNF, numeric_SCNF, b, index = [], [], "SDNF = (", "SCNF = (", 0, 0
    for i in res:
        index += int(res[b]) * (128 / (pow(2, b)))
        if i == 1:
            SDNF_numbers.append(table[b])
            if numeric_SDNF[-1] == "(":
                numeric_SDNF += f"{b}"
            else:
                numeric_SDNF += f", {b}"
            b += 1
        else:
            SCNF_numbers.append(table[b])
            if numeric_SCNF[-1] == "(":
                numeric_SCNF += f"{b}"
            else:
                numeric_SCNF += f", {b}"
            b += 1
    print("SDNF: " + SDNF_count(SDNF_numbers))
    print("SCNF: " + SCNF_count(SCNF_numbers))
    print("Numeric type: " + numeric_SDNF.lstrip(", ") + ");\t" + numeric_SCNF.lstrip(
        ", ") + ");\n" + f"Index: {int(index)}")


def comparing_table_and_formula(formula, table):
    resulting_table = []
    for i in table:
        formula1 = "".join(formula)
        formula1 = formula1.replace("x1", str(i[0]))
        formula1 = formula1.replace("x2", str(i[1]))
        formula1 = formula1.replace("x3", str(i[2]))
        resulting_table.append(int(eval(formula1)))
    return resulting_table


def SDNF_count(table):
    SDNF_result = ""
    for x1, x2, x3 in table:
        if x1 == 0:
            SDNF_result += "(!x1*"
        else:
            SDNF_result += "(x1*"
        if x2 == 0:
            SDNF_result += "!x2*"
        else:
            SDNF_result += "x2*"
        if x3 == 0:
            SDNF_result += "!x3)+"
        else:
            SDNF_result += "x3)+"
    SDNF_result = SDNF_result[:-1]
    return SDNF_result


def SCNF_count(table):
    SCNF_result = ""
    for x1, x2, x3 in table:
        if x1 == 1:
            SCNF_result += "(!x1+"
        else:
            SCNF_result += "(x1+"
        if x2 == 1:
            SCNF_result += "!x2+"
        else:
            SCNF_result += "x2+"
        if x3 == 1:
            SCNF_result += "!x3)*"
        else:
            SCNF_result += "x3)*"
    SCNF_result = SCNF_result[:-1]
    return SCNF_result
