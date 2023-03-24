from prettytable import PrettyTable
from calculating_method import *


def mccluskey_method(begin_formula):
    glued_formula = []
    for a in begin_formula[:-1]:
        for b in begin_formula[begin_formula.index(a) + 1:]:
            if abs(a.count("!") - b.count("!")) == 1 and step_of_gluing(a, b) is not None:
                glued_formula.append(step_of_gluing(a, b))
            else:
                pass
    table = PrettyTable()
    res = table_doing(begin_formula, glued_formula, table)
    print(f"Glued formula: glued_formula")
    return res

def for_mccluskey_table(begin_formula, glued_formula, table):
    res_elements, res_elements_final, n = [], [],  1
    for full_sub_formula in begin_formula:
        if full_sub_formula.find("*") == -1:
            full_sub_formula = full_sub_formula.split(" + ")
        else:
            full_sub_formula = full_sub_formula.split(" * ")
        for glued_sub_formula in glued_formula:
            if comparing_glued_and_begin_formula(full_sub_formula, glued_sub_formula):
                res_elements.append(1)
            else:
                res_elements.append(0)
        n += 1
        res_elements_final.append(res_elements)
        res_elements = []
    return res_elements_final

def comparing_glued_and_begin_formula(full_sub_formula, glued_sub_formula):
    full_sub_formula = set(full_sub_formula) ^ set(glued_sub_formula)
    if (len(full_sub_formula)) == 1:
        return True
    else:
        return False


def table_doing(begin_formula, glued_formula, table):
    res_elements = for_mccluskey_table(begin_formula, glued_formula, table)
    table.add_column("Implicanta", glued_formula)
    n = 0
    for num, x in enumerate(begin_formula):
        table.add_column(x, res_elements[num])
        n += 1
    print(table)
    return calculating_method(begin_formula)
