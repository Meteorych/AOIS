from copy import deepcopy
import numpy as np

BIT_SIZE = 16


class Associative_processor:
    def __init__(self, data, address):
        self.matrix = data
        self.address = address
        self.g, self.l = 0, 0
        self.diagonal = False

    @staticmethod
    def calculating_g(prev_g, prev_l, digit_a, digit_S):
        g = int(prev_g or (not digit_a and digit_S and not prev_l))
        return g

    @staticmethod
    def calculating_l(prev_g, prev_l, digit_a, digit_S):
        l = int(prev_l or (digit_a and not digit_S and not prev_g))
        return l

    def searching_by_accordance(self):
        self.g, self.l = 0, 0
        tick_of_matching = {}
        example_data = input("Input your example data: ")
        for char in str(example_data):
            if char != '0' and char != '1':
                print("Wrong example data!\n")
                return 0
        if len(example_data) > BIT_SIZE:
            example_data = example_data[0:BIT_SIZE]
        elif len(example_data) < BIT_SIZE:
            example_data = example_data.zfill(BIT_SIZE)
        print(f"Our data for matching: {example_data}")
        copy_of_matrix, diagonal_data = deepcopy(self.matrix), self.diagonal
        if diagonal_data is True:
            self.convert_to_straight()
        for num in range(self.matrix.shape[0]):
            tick_of_matching.update(
                {f"{self.matrix[num]}": self.reccure_algorithm_for_accordance(copy_of_matrix[num], example_data, num)})
        if diagonal_data is True:
            self.convert_to_diagonal()
        print(
            f"Strings with the highest matching digits: \n{sorted(tick_of_matching.items(), key=lambda item: item[1])[-3:]}\n")

    def convert_to_straight(self):
        copy_of_matrix = deepcopy(self.matrix)
        self.matrix = []
        for num_of_string, string in enumerate(copy_of_matrix):
            string = list(string)
            self.matrix.append(string[num_of_string:] + string[:num_of_string])
        self.matrix = np.array(self.matrix)
        self.diagonal = False

    def convert_to_diagonal(self):
        copy_of_matrix = deepcopy(self.matrix)
        self.matrix = []
        for num_of_string, string in enumerate(copy_of_matrix):
            string = list(string)
            self.matrix.append(string[(len(string) - num_of_string):] + string[:(len(string) - num_of_string)])
        self.matrix = np.array(self.matrix)
        self.diagonal = True

    def logic_operations(self):
        type_of_operations = int(input(
            "Choose type of operation:\n 1 -- constant 1\n 2 -- constant 0\n 3 -- New argument\n 4 -- Negative of new argument\n"))
        num_of_column = int(input("Choose column: "))
        match type_of_operations:
            case 1:
                for digit in range(len(self.matrix[num_of_column])):
                    self.matrix[num_of_column][digit] = 1
                print(self.matrix.T)
            case 2:
                for digit in range(len(self.matrix[num_of_column])):
                    self.matrix[num_of_column][digit] = 0
                print(self.matrix.T)
            case 3:
                self.positive_of_argument(num_of_column)
            case 4:
                self.negative_of_argument(num_of_column)

    def positive_of_argument(self, num_of_column):
        diagonal_data = self.diagonal
        if diagonal_data is True:
            self.convert_to_straight()
        argument = input("Input argument: ")
        if len(argument) > BIT_SIZE:
            argument = argument[0:BIT_SIZE]
        elif len(argument) < BIT_SIZE:
            argument = argument.zfill(BIT_SIZE)
        for num_of_string, digit in enumerate(self.matrix[num_of_column]):
            self.matrix[num_of_column][num_of_string] = argument[num_of_string]
        if diagonal_data is True:
            self.convert_to_diagonal()
        print(self.matrix.T)

    def negative_of_argument(self, num_of_column):
        diagonal_data = self.diagonal
        if diagonal_data is True:
            self.convert_to_straight()
        argument = input("Input argument: ")
        if len(argument) > BIT_SIZE:
            argument = argument[0:BIT_SIZE]
        elif len(argument) < BIT_SIZE:
            argument = argument.zfill(BIT_SIZE)
        argument = argument.replace("1", "2").replace("0", "1")
        argument = argument.replace("2", "0")
        for num_of_string, digit in enumerate(self.matrix[num_of_column]):
            self.matrix[num_of_column][num_of_string] = argument[num_of_string]
        if diagonal_data is True:
            self.convert_to_diagonal()
        print(self.matrix.T)

    @staticmethod
    def sum_diff_of_numbers(num1, num2):  # Сумма/разность чисел
        summ = ""
        carry = 0
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
        elif carry == 0:
            summ = "0" + summ
        summ = np.array([num for num in summ])
        return summ

    def sum_of_fields(self):
        example_data = input("Input your example data: ")[:3]
        diagonal_data = self.diagonal
        if diagonal_data is True:
            self.convert_to_straight()
        for num_of_string, string in enumerate(self.matrix):
            if np.array2string(string, separator='')[1:-1].replace(' ', '')[0:3] == example_data:
                self.matrix[num_of_string][11:16] = Associative_processor.sum_diff_of_numbers(
                    self.matrix[num_of_string][3:7], self.matrix[num_of_string][7:11])
            if diagonal_data is True:
                self.convert_to_diagonal()
        print(self.matrix.T)

    def reccure_algorithm_for_accordance(self, matrix_string, data, num_of_string):
        tick, pos_of_break = 0, 0
        if self.diagonal is False:
            for digit, value_of_digit in enumerate(data):
                if value_of_digit == str(matrix_string[digit]):
                    tick += 1
        if self.diagonal is True:
            for digit, value_of_digit in enumerate(data[num_of_string:]):
                pos_of_break = digit  # Каждый раз помечаем позицию, чтобы запомнить её в случае, если мы дойдем до конца слова
                if value_of_digit == str(matrix_string[digit]):
                    tick += 1
            for digit, value_of_digit in enumerate(data[:num_of_string]):
                if value_of_digit == str(matrix_string[pos_of_break + digit]):
                    tick += 1
        return tick

    def choose_read_or_write(self):
        type_of_operation = int(input("1 -- Read word\n 2 -- Read column\n 3 -- Write word\n 4 -- Write column\n "))
        match type_of_operation:
            case 1:
                self.read_word()
            case 2:
                self.read_column()
            case 3:
                self.write_word()
            case 4:
                self.write_column()

    def read_word(self):
        num_of_word = int(input("Number of word: "))
        diagonal_info = self.diagonal
        if self.diagonal is True:
            self.convert_to_straight()
        print(self.matrix[num_of_word])
        if diagonal_info is True:
            self.convert_to_diagonal()

    def read_column(self):
        num_of_col = int(input("Number of column: "))
        print(self.matrix[num_of_col])

    def write_word(self):
        word = np.array(list(input("Word:").zfill(16)[:16]), dtype=int)
        num_of_word = int(input("Number of word: "))
        diagonal_info = self.diagonal
        if self.diagonal is True:
            self.convert_to_straight()
        self.matrix[num_of_word] = word
        if diagonal_info is True:
            self.convert_to_diagonal()
        print(self.matrix.T)

    def write_column(self):
        column = np.array(list(input("Column:").zfill(16)[:16]), dtype=int)
        num_of_col = int(input("Number of column: "))
        self.matrix[num_of_col] = column
        print(self.matrix.T)
