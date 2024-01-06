import os

def create_to_do_list(filepath: str="data/to_dos.txt"):
    with open(filepath, "w") as file_local:
        pass

def get_to_do_list(filepath: str="data/to_dos.txt") -> list:
    """
    Reads a text file and return a list of to do items.
    """
    with open(filepath, "r") as file_local:
        to_do_list_local = file_local.readlines()
    return to_do_list_local

def write_to_do_list(output_list: list, filepath: str="data/to_dos.txt") -> None:
    """
    Overwrites a text file and writes a list to a new version of the text file.
    """
    with open(filepath, "w") as file_local:
        file_local.writelines(output_list)

if __name__ == "__main__":
    create_to_do_list()
    to_do_list = get_to_do_list()
    print(to_do_list)
    write_to_do_list(to_do_list)