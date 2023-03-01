def comparing_length(num1, num2):  # Comparing length of binary codes
    max_length = max(len(num1), len(num2))
    if num1[0] and num2[0] == "0":
        num1 = num1.zfill(max_length)
        num2 = num2.zfill(max_length)
    if num1[0] == "1":
        num1 = num1.rjust(max_length, "1")
    if num2[0] == "1":
        num2 = num2.rjust(max_length, "1")
    return num1, num2


def dec_to_bin_straight(num):  # Прямой код
    binary = ""
    tick_of_actions, clone_of_num, tick_of_bits = 0, num, 0
    result = ""
    if abs(num) < 100:
        bit_size = 8
    else:
        bit_size = 16
    if num < 0:
        clone_of_num = -num
    if num == 0:
        binary = str(0)
    while clone_of_num >= 1:
        zero_or_unit = str(int(clone_of_num % 2))
        binary = binary + zero_or_unit
        tick_of_bits += 1
        clone_of_num /= 2
        tick_of_actions = tick_of_actions + 1
        result = binary[::-1]
    if tick_of_bits < bit_size:
        result = result.zfill(bit_size)
    if num < 0:
        result = str(1) + result[1:]
    else:
        result = str(0) + result[1:]
    return result


def subtraction(num1, num2):
    max_len = max(len(num1), len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)
    result = ''
    sign_of_result = 0
    for i in range(max_len - 1, - 1, - 1):
        num = int(num1[i]) - int(num2[i]) - sign_of_result
        if num % 2 == 1:
            result = '1' + result
        else:
            result = '0' + result
        if num < 0:
            sign_of_result = 1
        else:
            sign_of_result = 0
    if sign_of_result != 0:
        result = '01' + result
    if int(result) == 0:
        result = 0
    return result


def dec_to_bin_add(num):  # Дополненный код
    if num < 0:
        result = dec_to_bin_rev(num)
        i = 1
        help_add = True
        while help_add:
            add_part = result[-i:len(result)]
            if result[-i] == "0":
                add_part = add_part.replace('1', '2')
                add_part = add_part.replace('0', '1')
                add_part = add_part.replace('2', '0')
                result = result[:-i] + add_part
                help_add = False
            else:
                i += 1
    else:
        result = dec_to_bin_straight(num)
    return result


def dec_to_bin_rev(num):  # Обратный код
    sign = ''
    if num < 0:
        sign += '1'
        result = dec_to_bin_straight(num)
        result = result.replace('1', '2')
        result = result.replace('0', '1')
        result = result.replace('2', '0')
    else:
        sign += '0'
        result = dec_to_bin_straight(num)
    result = sign + result[1:]
    return result


def from_binary_to_decimal(num):
    result = 0
    if num.startswith("1"):
        result += ((-int(num[1])) * pow(2, (len(num) - 2)))
        for i in range(2, len(num)):
            result += ((int(num[i])) * pow(2, (len(num) - (i + 1))))
    elif num.startswith("0"):
        for i in range(0, len(num)):
            result += (int(num[i]) * pow(2, (len(num) - (i + 1))))
    return result


def sum_diff_of_numbers(num1, num2):  # Сумма/разность чисел
    summ = ""
    carry = 0
    num1, num2 = (comparing_length(num1, num2))
    for i in reversed(range(0, len(num1))):
        if (int(num1[i]) + int(num2[i]) == 1) and (carry == 0):
            summ = "1" + summ
        elif (int(num1[i]) + int(num2[i]) == 1) and (carry > 0):
            summ = "0" + summ
        elif (int(num1[i]) + int(num2[i]) == 2) and (carry > 0):
            summ = "1" + summ
        elif (int(num1[i]) + int(num2[i]) == 0) and (carry > 0):
            summ = "1" + summ
            carry -= 1
        elif (int(num1[i]) + int(num2[i]) == 0) and (carry == 0):
            summ = "0" + summ
        elif (int(num1[i]) + int(num2[i]) == 2) and (carry == 0):
            summ = "0" + summ
            carry += 1
    if carry > 0:
        summ = "1" + summ
    return summ


def mul_of_bin_numbers(num1, num2):
    multi_column = []
    result = "0"
    for i in reversed(range(0, len(num2))):
        if num2[i] == "1":
            multi_column.append(num1)
        else:
            element_of_multicolumn = num1.replace("1", "0")
            multi_column.append(element_of_multicolumn)
    multi_column[:] = [multi_column[i] + "0" * i for i in range(0, len(multi_column))]
    for b in range(0, len(multi_column)):
        result = sum_diff_of_numbers(result, multi_column[b])
    return result


def define_operation(num1, num2, operation_command):
    match operation_command:
        case 1:
            pass
        case 2:
            num2 = -num2
        case 3 | 4:
            num1 = abs(num1)
            num2 = abs(num2)
        case 4:
            if num1 < num2:
                num1, mum2 = num2, num1
    return num1, num2, operation_command


def division_of_numbers(num1, num2):
    result = ""
    carry_num1 = ""
    num1 = num1.lstrip("0")
    num2 = num2.lstrip("0")
    for i in range(0, len(num1)):
        carry_num1 += num1[i]
        if int(num2) > int(carry_num1):
            result += "0"
        else:
            surplus = subtraction(carry_num1, num2)
            if surplus == 0:
                carry_num1 = ""
                result += "1"
            else:
                surplus = str(surplus).lstrip("0")
                result += "1"
                carry_num1 = surplus
    return result


def _to_fix(num):
    if num == 0:
        return 0
    int_num = int(num)
    i = 0
    mantissa_size = 23
    fraction_part = num - float(int_num)
    int_result = dec_to_bin_add(int_num)
    if int_result.find("1") == -1:
        result = "0" + "."
    else:
        result = int_result[int_result.find("1"):] + "."
    while i <= (mantissa_size - len(result)):
        fraction_part *= 2
        if int(fraction_part) == 0:
            result += "0"
        elif int(fraction_part) == 1:
            fraction_part -= 1
            result += "1"
            if fraction_part == 0:
                result = result.ljust(23, "0")
    return result


def from_decimal_to_float(num):
    if "1" in num[:num.find(".")]:
        exp_sign = 1
    else:
        exp_sign = -1
    sign_bit = "0"
    if num.find("1", 0, num.find(".")) == -1:
        exp_bits = dec_to_bin_straight(127 + ((num.find("1") - num.find(".")) * exp_sign))[-8:]
    else:
        exp_bits = dec_to_bin_straight(127 + ((num.find(".") - num.find("1") - 1) * exp_sign))[-8:]
    n = num[:num.find(".")] + num[num.find(".") + 1:]
    mantissa = num[num.find("1") + 1:]
    result = sign_bit + " " + exp_bits + " " + mantissa
    print("float_form =" + result)
    return result


def summ_of_floating(num1, num2):  # сумма чисел с плавающей точкой
    num1 = _to_fix(num1)
    num2 = _to_fix(num2)
    unitnum1 = num1.find("1", 0, num1.find("."))
    unitnum2 = num2.find("1", 0, num2.find("."))
    exp1 = num1.find(".") - unitnum1 - 1
    exp2 = num2.find(".") - unitnum2 - 1
    if num1.find("1", 0, num1.find(".")) == -1:
        exp1 = 0
    if num2.find("1", 0, num2.find(".")) == -1:
        exp2 = 0
    if exp1 >= exp2:
        diff_exp = exp1 - exp2  # Таким образом мы находим бОльшее число (число, где запятая находится дальше)
        numsumm2 = "0" * diff_exp + num2[:(num2.find("."))] + num2[(num2.find(".") + 1):(
                len(num2) - diff_exp)]  # Преобразуем меньшее число, смещая его вправо на diff_exp кол-во знаков
        numsumm1 = num1[:(num1.find("."))] + num1[(num1.find(".") + 1):]
    else:
        diff_exp = exp2 - exp1
        numsumm1 = "0" * diff_exp + num1[:(num1.find("."))] + num1[(num1.find(".") + 1):(len(num1) - diff_exp)]
        numsumm2 = num2[:(num2.find("."))] + num2[(num2.find(".") + 1):]
    temp_floating_summ = sum_diff_of_numbers(numsumm1, numsumm2)
    add_numbers = len(temp_floating_summ) - len(numsumm2)
    result = temp_floating_summ[:(max(num1.find("."), num2.find("."))) + add_numbers] + "." + \
             temp_floating_summ[(max(exp1, exp2) + add_numbers + 1):]
    result = from_decimal_to_float(result)
    return result


def from_float_to_decimal(num):
    num = num[:num.find(" ")] + num[(num.find(" ") + 1):num.rfind(" ")] + num[num.rfind(" ") + 1:]
    decimal_mantissa = 0.0
    for i in range(9, len(num)):
        decimal_mantissa += int(num[i]) * pow(2, -(i - 8))
    exp = int(from_binary_to_decimal("0" + num[1:9])) - 127
    if num[0] == "1":
        sign_before = "-"
    else:
        sign_before = ""
    result = sign_before + str((1 + decimal_mantissa) * pow(2, exp))
    result = str(round(float(result), 5))
    return result


def int_or_float(num):
    if "." in num:
        result = float(num)
    else:
        result = int(num)
    return result


while True:
    num1 = (input("Enter the first number:"))
    num2 = (input("Enter the second number:"))
    num1 = int_or_float(num1)
    num2 = int_or_float(num2)
    number1, number2 = "0", "0"
    temp_num_for_change = 0
    operation_command = int(input("Choose the type of operation (1 — summ, 2 — diff, 3 — multiplication, 4 — division, "
                                  "5 — summ of floats):"))

    num1, num2, operation_command = define_operation(num1, num2, operation_command)

    command = int(input("The type of code (1 — straight/reversed, 2 — straight/additional, 3 — additional/reversed, "
                        "4 — float):"))
    match command:
        case 1:
            if num1 < 0 < num2:
                temp_num_for_change = num1
                num1 = num2
                num2 = temp_num_for_change
            number1 = dec_to_bin_straight(num1)
            number2 = dec_to_bin_rev(num2)
            print("first_number = " + dec_to_bin_straight(num1))
            print("second_number = " + dec_to_bin_rev(num2))
        case 2:
            if num1 < 0 < num2:
                temp_num_for_change = num1
                num1 = num2
                num2 = temp_num_for_change
            number1 = dec_to_bin_straight(num1)
            number2 = dec_to_bin_add(num2)
            print("first_number = " + dec_to_bin_straight(num1))
            print("second_number = " + dec_to_bin_add(num2))
        case 3:
            number1 = dec_to_bin_add(num1)
            number2 = dec_to_bin_rev(num2)
            print("first_number = " + dec_to_bin_add(num1))
            print("second_number = " + dec_to_bin_rev(num2))
        case 4:
            pass

    match operation_command:
        case 1 | 2:
            print("summ/diff = " + (str(from_binary_to_decimal(sum_diff_of_numbers(number1, number2)))))
        case 3:
            number1, number2 = (comparing_length(number1, number2))
            print("binary multiplication = " + str(from_binary_to_decimal(mul_of_bin_numbers(number1, number2))))
        case 4:
            number1, number2 = (comparing_length(number1, number2))
            print("binary division = " + str(from_binary_to_decimal(division_of_numbers(number1, number2))))
        case 5:
            print("summ_floating = " + str(from_float_to_decimal(summ_of_floating(num1, num2))))

    if int(input("Do you want to continue? 1 — Continue, 2 — stop: ")) == 1:
        continue
    else:
        break

