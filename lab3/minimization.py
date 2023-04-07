from mccluskey_method import *
from karno_map import *


def choosing_method_of_minimization(sdnf, scnf, res_table_values):
    sdnf, scnf = sdnf.split("+"), scnf.split("*")
    sdnf[:] = [char.strip("(").strip(")") for char in sdnf]
    scnf[:] = [char.strip("(").strip(")") for char in scnf]
    while True:
        command = input("Method of minimization (calculating, mccluskey, table, end):").lower()
        match command:
            case "calculating":
                res = "Minimized:\nSDNF:" + str(calculating_method(sdnf)) + "\nSCNF:" + str(calculating_method(scnf))
                print(res)
            case "mccluskey":
                res = "Minimized:\nSDNF:" + str(mccluskey_method(sdnf)) + "\nSCNF:" + str(mccluskey_method(scnf))
                print(res)
            case "table":
                res = "Minimized:" + str(table_method(res_table_values))
                print(res)
            case "end":
                break
            case _:
                print("Wrong variant!")
