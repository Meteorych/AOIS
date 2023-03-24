from copy import deepcopy

class element_of_formula_SDNF:
    def __init__(self, name):
        self.name = name
        if self.name[0] == "!":
            self.value = "0"
            self.using_value = "1"
        else:
            self.value = "1"
            self.using_value = "1"

class element_of_formula_SCNF:
    def __init__(self, name):
        self.name = name
        if self.name[0] == "!":
            self.value = "1"
            self.using_value = "0"
        else:
            self.value = "0"
            self.using_value = "0"

def calculating_method(begin_formula):
    glued_formula = gluing_formula(begin_formula)
    if begin_formula[0].find("*") != -1:
        return checking_of_extras_SDNF(glued_formula)
    else:
        return checking_of_extras_SCNF(glued_formula)


def gluing_formula(begin_formula):
    changed, glued_formula = [], []
    for a in begin_formula[:-1]:
        for b in begin_formula[begin_formula.index(a) + 1:]:
            if abs(a.count("!") - b.count("!")) == 1 and step_of_gluing(a, b) is not None:
                glued_formula.append(step_of_gluing(a, b))
            else:
                pass
    return glued_formula


def checking_of_extras_SDNF(formula):
    res_formula = deepcopy(formula)
    for number, constituenta in enumerate(formula):
        elements = []
        for element in constituenta:
            element = element_of_formula_SDNF(element)
            elements.append(element)
        remain_formula = formula[:number] + formula[(number + 1):]
        remain_elements_summ = create_remain_elements_summ_SDNF(remain_formula, elements)
        if remain_summ_SDNF(remain_elements_summ):
            res_formula.remove(constituenta)
    if all(x[0] == formula[0][0] or x[1] == formula[0][0] for x in formula):
        if not all(x[0] == formula[0][0] or x[1] == formula[0][0] for x in res_formula):
            res_formula.append(formula[0][0])
    if all(x[0] == formula[0][1] or x[1] == formula[0][1] for x in formula):
        if not all(x[0] == formula[0][1] or x[1] == formula[0][1] for x in res_formula):
            res_formula.append(formula[0][1])
    res_formula_as_strings = [str(element) for element in res_formula]
    res_formula = " \\/ ".join(res_formula_as_strings)
    return res_formula

# Give values for remain_formula
def create_remain_elements_summ_SDNF(remain_formula, elements):
    remain_elements_summ, final_remain_elements_summ, value_of_remains = [], [], 0
    for remain_constituenta in remain_formula:
        remain_elements_summ = []
        for remain_element in remain_constituenta:
            for x in elements:
                if remain_element == x.name:
                    value_of_remains = x.using_value
                    break
                elif remain_element == ("!" + x.name):
                    value_of_remains = str(int(x.using_value) - 1)
                    break
                elif remain_element == x.name[1:]:
                    value_of_remains = x.value
                    break
                else:
                    value_of_remains = remain_element
            remain_elements_summ.append(value_of_remains)
        final_remain_elements_summ.append(remain_elements_summ)
    return final_remain_elements_summ


# Function for summarizing expressions of sdnf, that doesn't take main role in minimizing actions
def remain_summ_SDNF(remain_elements_summ):
    res_element, res_elements, literals = 0, 0, []
    for constituenta in remain_elements_summ:
        for element in constituenta:
            if element == '1' and (res_element == 1 or res_element == 0):
                res_element = 1
            if element != '1' and element != '0':
                res_element = element
            elif element == '0':
                res_element = 0
                break
        if res_element != 0 and res_element != 1:
            literals.append(res_element)
        else:
            res_elements += res_element
    if res_elements == 0 and len(literals) == 0:
        return False
    if len(literals) > 0:
        if all(x[0] == literals[0][0] for x in literals):
            return False
    return True


def step_of_gluing(element_1, element_2):
    if element_1.find("+") != -1:
        element_1, element_2 = element_1.split(" + "), element_2.split(" + ")
    else:
        element_1, element_2 = element_1.split(" * "), element_2.split(" * ")
    changed_elements = list(set(element_1) ^ set(element_2))
    if len(changed_elements) != 2:
        return None
    if changed_elements[0] in element_1:
        element_1.remove(changed_elements[0])
    else:
        element_1.remove(changed_elements[1])
    return element_1


def checking_of_extras_SCNF(formula):
    res_formula = formula[:]
    for number, constituenta in enumerate(formula):
        elements = []
        for element in constituenta:
            element = element_of_formula_SCNF(element)
            elements.append(element)
        remain_formula = formula[:number] + formula[(number + 1):]
        remain_elements_summ = create_remain_elements_summ_SCNF(remain_formula, elements)
        if remain_summ_SCNF(remain_elements_summ):
            res_formula.remove(constituenta)
    res_formula = uno_elements_SCNF(res_formula, formula)
    res_formula_as_strings = [str(element) for element in res_formula]
    res_formula = " /\\ ".join(res_formula_as_strings)
    return res_formula

def uno_elements_SCNF(res_formula, formula):
    for x in res_formula:
        formula.remove(x)
    if all(x[0] == formula[0][0] or x[1] == formula[0][0] for x in formula):
        try:
            res_formula.append(formula[0][0])
        except IndexError:
            pass
    if all(x[0] == formula[0][1] or x[1] == formula[0][1] for x in formula):
        try:
            res_formula.append(formula[0][1])
        except IndexError:
            pass
    return res_formula


def create_remain_elements_summ_SCNF(remain_formula, elements):
    remain_elements_summ, final_remain_elements_summ, value_of_remains = [], [], 0
    for remain_constituenta in remain_formula:
        remain_elements_summ = []
        for remain_element in remain_constituenta:
            for x in elements:
                if remain_element == x.name:
                    value_of_remains = x.using_value
                    break
                elif remain_element == ("!" + x.name):
                    value_of_remains = str(int(x.using_value) + 1)
                    break
                elif remain_element == x.name[1:]:
                    value_of_remains = x.value
                    break
                else:
                    value_of_remains = remain_element
            remain_elements_summ.append(value_of_remains)
        final_remain_elements_summ.append(remain_elements_summ)
    return final_remain_elements_summ


def remain_summ_SCNF(remain_elements_summ):
    res_element, res_elements, literals = 0, 1, []
    for constituenta in remain_elements_summ:
        for element in constituenta:
            if element == "1":
                res_element = 1
                break
            elif element != "1" and element != "0":
                res_element = element
            elif element == "0" and res_element == "0":
                res_element = 0
        if res_element != 0 and res_element != 1:
            literals.append(res_element)
        else:
            res_elements *= res_element
    if res_elements == 1 and len(literals) == 0:
        return False
    if len(literals) > 0:
        if all(x[0] == literals[0][0] for x in literals):
            return False
    return True
