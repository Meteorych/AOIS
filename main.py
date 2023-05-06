from hash_table import Hash
from hash_table import TableElement

KEYS = ["Ivan", "Mariya", "Vadim", "Timofey", "Dmitriy", "Artemiy", "Isabella", "Ahmed",
        "Mary", "Alex", "William", "Emila", "Olivia", "James",
        "Sophia", "Ethan", "Isabella", "Michael", "Emma", "Benjamin", "Ava"]

VALUES = ["AK-47", "MP4", "MP16", "PM", "Gatling gun", "AK-74", "Challenger", "Leopard", "Type-99",
          "HIMARS", "Marder", "M1 Abrams", "Т-90А", "G3", "Bayraktar", "RPK", "AT4", "RPG-7", "OLHA", "URAGAN",
          "Mil MI-8"]


def main():
    table_elements = []
    for i in range(0, len(KEYS)):
        table_element = TableElement(KEYS[i], VALUES[i])
        table_elements.append(table_element)
    table = Hash(table_elements)
    table.making_table()
    choosing_menu(table)

def choosing_menu(table):
    while True:
        try:
            choice = int(input("1 -- find element\n2 -- delete element\n3 -- add element\n4 -- end program\n"))
        except ValueError:
            print("Wrong variant")
            choice = "_"
        match choice:
            case 1:
                key = input("Input searching key: ")
                table.finding_element(key)
            case 2:
                key = input("Input key of item being deleted: ")
                table.deleting_element(key)
            case 3:
                table.add_element()
            case 4:
                break
            case _:
                print("Wrong choice!")


if __name__ == '__main__':
    main()
