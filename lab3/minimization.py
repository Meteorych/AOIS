from calculating_method import *
from mccluskey_method import *
from karno_map import *


def choosing_method_of_minimization(sdnf, scnf):
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
                return 0
            case "table":
                res = "Minimized:\nSDNF:" + str(table_method(sdnf)) + "\nSCNF:" + str(table_method(scnf))
                print(res)
                return 0
            case "end":
                break
            case _:
                print("Wrong variant!")
