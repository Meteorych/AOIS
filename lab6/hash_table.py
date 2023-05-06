from prettytable import PrettyTable
from copy import deepcopy


class TableElement:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Hash:
    def __init__(self, table_elements):
        self.table_size = 16
        self.table_elements = table_elements
        self.table_list = []

    def making_model(self):
        for num in range(self.table_size):
            self.table_list.append([])
        return self.table_list

    def indexing_hash(self, key):
        hash = 0
        for number, letter in enumerate(key):
            hash += number + ord(letter)
        return hash

    def calculating_index(self, key):
        hash = self.indexing_hash(key)
        index = hash % self.table_size
        return index


    def making_table(self):
        for element in self.table_elements:
            self.step_of_making_table(element)
        self.visual_modeling()

    def step_of_making_table(self, element):
        self.table_list = self.making_model()
        for num in range(self.table_size):
            if num == self.calculating_index(element.key):
                self.table_list[num].append(element)


    def visual_modeling(self):
        table = PrettyTable()
        table.field_names = ["Index", "Key", "Value"]
        for num_of_string in range(self.table_size):
            if len(self.table_list[num_of_string]) == 0:
                continue
            elif len(self.table_list[num_of_string]) == 1:
                table.add_row([num_of_string, self.table_list[num_of_string][0].key, self.table_list[num_of_string][0].value])
            else:
                for length in range(len(self.table_list[num_of_string])):
                    table.add_row([num_of_string, self.table_list[num_of_string][length].key,self.table_list[num_of_string][length].value])
        print(table)

    def deleting_element(self, key):
        element_deleted = self.finding_element(key)
        if element_deleted is not None:
            if len(element_deleted) == 1:
                self.table_list.pop(self.finding_element(key)[0])
            else:
                self.table_list[element_deleted[0]].pop(element_deleted[1])
        self.visual_modeling()

    def add_element(self):
        key = input("Input key of element: ")
        value = input("Input value of element: ")
        new_element = TableElement(key, value)
        self.table_list[self.calculating_index(key)].append(new_element)
        self.visual_modeling()


    def finding_element(self, key):
        index_of_search_element = self.calculating_index(key)
        try:
            if len(self.table_list[index_of_search_element]) == 1:
                if self.table_list[index_of_search_element][0].key == key:
                    print(f"Value of searching element {self.table_list[index_of_search_element][0].value}")
                    return [index_of_search_element]
                else:
                    print("Element doesn't exist")
            else:
                for index, element in enumerate(self.table_list[index_of_search_element]):
                    if element.key == key:
                        print(f"Value of searching element {element.value}")
                        return [index_of_search_element, index]
                print("Element doesn't exist")
                return None
        except IndexError:
            print("Element doesn't exist")
