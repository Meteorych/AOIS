from prettytable import PrettyTable
import itertools
from copy import deepcopy


class karno_map:
    def __init__(self, res, values):
        self.res = res
        self.value = values
        self.in_square = False
        self.is_in_4_square = False
        if self.res == 1:
            self.type = "dnf"
        else:
            self.type = "cnf"


def append_value(element):
    element.in_square = True


def table_method(value_table):
    table_of_values = []
    table, y = PrettyTable(), 0
    first_element_values = [0] * 4 + [1] * 4
    table.add_column("x1/x2,x3", [0, 1])
    cycle_iter = itertools.cycle(first_element_values)
    x_table = list(itertools.product(range(2), repeat=2))
    x_table[-1], x_table[-2] = x_table[-2], x_table[-1]
    work_value_table = deepcopy(value_table)
    value_table[2], value_table[6], value_table[3], value_table[7] = value_table[3], value_table[7], work_value_table[
        2], work_value_table[6]
    for x, el in zip(range(8), cycle_iter):
        if x < 4:
            table.add_column(f"{x_table[x]}", [value_table[x], value_table[x + 4]])
        if x == 4:
            y = 0
        karno_map_element = karno_map(int(value_table[x]), [el] + list(x_table[y]))
        y += 1
        table_of_values.append(karno_map_element)
    print(table)
    return making_squares(table_of_values)


def check_values(x, table):
    square = [table[x].value]
    if x != 3:
        if table[x + 1].res == table[x].res:
            square.append(table[x + 1].value)
            table[x + 1].in_square = True
    if table[x + 4].res == table[x].res and table[x + 4].is_in_4_square is False:
        square.append(table[x + 4].value)
        table[x + 4].in_square = True
        if x == 3 and table[x + 1].res == table[x + 4].res:
            square.append(table[x + 1].value)
            table[x + 1].in_square = True
            work_square_3_el = deepcopy(square)
            return [[work_square_3_el[0], work_square_3_el[1]], [work_square_3_el[1], work_square_3_el[2]]], table
    elif x == 0:
        if table[x + 3].res == table[x].res:
            square.append(table[x + 3].value)
            table[x + 3].in_square = True
    if len(square) == 1 and (all(table[x].in_square for x in [x, x+4]) or table[x].is_in_4_square for x in [x, x+4]):
        return None
    if len(square) == 3:
        work_square = deepcopy(square)
        square = [[work_square[0], work_square[1]], [work_square[0], work_square[2]]]
    else:
        square = [deepcopy(square)]
    return square, table


def making_squares(res_value_table):
    array_of_squares_SDNF, array_of_squares_SCNF = [], []
    for x in range(4):
        if check_values(x, res_value_table) is None:
            continue
        if res_value_table[x].type == "dnf":
            if x != 3 and checking_big_squares(x, res_value_table) is not None:
                square, res_value_table = checking_big_squares(x, res_value_table)
                array_of_squares_SDNF.extend(square)
            else:
                square, res_value_table = check_values(x, res_value_table)
                array_of_squares_SDNF.extend(square)
        elif res_value_table[x].type == "cnf":
            if x != 3 and checking_big_squares(x, res_value_table) is not None:
                square, res_value_table = checking_big_squares(x, res_value_table)
                array_of_squares_SCNF.extend(square)
            else:
                square, res_value_table = check_values(x, res_value_table)
                array_of_squares_SCNF.extend(square)
    print(str(array_of_squares_SCNF) + "" + str(array_of_squares_SDNF))
    sdnf_res = minimizing_by_squares(array_of_squares_SDNF, 'sdnf')
    scnf_res = minimizing_by_squares(array_of_squares_SCNF, 'scnf')
    return f"SDNF: {sdnf_res}\nSCNF: {scnf_res}"


def checking_big_squares(x, table):
    indices = [x, x + 1, x + 4, x + 5]
    if table[x].is_in_4_square is True:
        return None
    if all(table[i].res == table[x].res for i in indices):
        square = [table[i].value for i in indices]
        for i in indices[1:]:
            table[i].is_in_4_square = True
        square = [deepcopy(square)]
        return square, table
    elif x == 1:
        indices = [x, x + 3, x + 4, x + 7]
        if all(table[i].res == table[x].res for i in indices):
            square = [table[i].value for i in indices]
            for i in indices[1:]:
                table[i].is_in_4_square = True
            square = [deepcopy(square)]
            return square, table
        else:
            return None
    else:
        return None


def minimizing_by_squares(array_of_squares, type_of_formula):
    res = ""
    for square in array_of_squares:
        res += "("
        for number, tup in enumerate(list(zip(*square))):
            if all(x == 0 for x in tup) and type_of_formula == "sdnf":
                res += f"!x{number + 1}*"
            elif all(x == 1 for x in tup) and type_of_formula == "sdnf":
                res += f"x{number + 1}+"
            if all(x == 0 for x in tup) and type_of_formula == "scnf":
                res += f"x{number + 1}+"
            elif all(x == 1 for x in tup) and type_of_formula == "scnf":
                res += f"!x{number + 1}*"
        res = res.strip("*").strip("+")
        if type_of_formula == "sdnf":
            res += ")+"
        if type_of_formula == "scnf":
            res += ")*"
    res = res.strip("*").strip("+")
    return res
