"""
    Мои задания: в процессоре необходим поиск по соответствию и поиск величин, заключенных в интервале
"""

class Associative_processor:
    def __init__(self, data, address):
        self.matrix = data
        self.address = address
        self.g, self.l = 0, 0

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
        if len(example_data) > 16:
            example_data = example_data[0:16]
        elif len(example_data) < 16:
            example_data = example_data.zfill(16)
        print(f"Our data for matching: {example_data}")
        for num in range(self.matrix.shape[0]):
            tick_of_matching.update({f"{self.matrix[num]}": self.reccure_algorithm_for_accordance(self.matrix[num], example_data)})
        print(f"Strings with the highest matching digits: \n{sorted(tick_of_matching.items(), key=lambda item: item[1])[-3:]}\n")


    def searching_in_interval(self):
        self.g, self.l = 0, 0
        min_value = input("Input min value for interval: ").zfill(16)
        max_value = input("Input max value for interval: ").zfill(16)
        max_value, min_value = max_value[0:16], min_value[0:16]
        result = []
        for num_of_string in range(self.matrix.shape[0]):
            if self.reccure_algorithm_for_intervals(self.matrix[num_of_string], min_value, max_value, self.g, self.l) == 1:
                result.append(str(self.matrix[num_of_string]))
        print(f"Words in interval:\n {result}")


    @staticmethod
    def reccure_algorithm_for_accordance(matrix_string, data):
        tick = 0
        for digit, value_of_digit in enumerate(data):
            if value_of_digit == str(matrix_string[digit]):
                tick += 1
            else:
                pass
        return tick

    @staticmethod
    def reccure_algorithm_for_intervals(matrix_string, min, max, g, l):
        for num, value in enumerate(matrix_string):
            prev_g, prev_l = g, l
            g = Associative_processor.calculating_g(prev_g, prev_l, int(min[num]), int(value))
            l = Associative_processor.calculating_l(prev_g, prev_l, int(min[num]), int(value))
        if g == 0 and l == 1:
            return 0
        g, l = 0, 0
        for num, value in enumerate(matrix_string):
            prev_g, prev_l = g, l
            g = Associative_processor.calculating_g(prev_g, prev_l, int(max[num]), int(value))
            l = Associative_processor.calculating_l(prev_g, prev_l, int(max[num]), int(value))
        if g == 1 and l == 0:
            return 0
        return 1
