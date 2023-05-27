import random

from running import Associative_processor
import numpy as np

def main():
    rows, columns = 16, 16
    matrix = np.random.randint(2, size=(rows, columns))
    address_of_searching = np.random.randint(2, size=16)
    processor = Associative_processor(matrix, address_of_searching)
    print(matrix.T)
    choosing_task(processor)


def choosing_task(processor):
    while True:
        task = int(input("Choose task: \n1 -- searching by accordance\n2 -- convert to diagonal\n3 -- convert to straight\n"
                         "4 -- logic operations\n5 -- summ of digits\n6 -- The End\n"))
        match task:
            case 1:
                processor.searching_by_accordance()
            case 2:
                processor.convert_to_diagonal()
                print(processor.matrix.T)
            case 3:
                processor.convert_to_straight()
                print(processor.matrix.T)
            case 4:
                processor.logic_operations()
            case 5:
                string = input("Choose column: ")
                processor.sum_of_fields(string)
            case 6:
                break


if __name__ == '__main__':
    main()