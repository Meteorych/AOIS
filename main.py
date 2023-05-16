import random

from processor import Associative_processor
import numpy as np

def main():
    rows, columns = random.randint(4, 20), 16
    matrix = np.random.randint(2, size=(rows, columns))
    address_of_searching = np.random.randint(2, size=16)
    processor = Associative_processor(matrix, address_of_searching)
    print(matrix)
    choosing_task(processor)


def choosing_task(processor):
    while True:
        task = int(input("Choose task: \n1 -- searching by accordance\n2 -- searching in interval\n3 -- The End\n"))
        match task:
            case 1:
                processor.searching_by_accordance()
            case 2:
                processor.searching_in_interval()
            case 3:
                break


if __name__ == '__main__':
    main()