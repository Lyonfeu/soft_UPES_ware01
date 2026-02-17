import csv


# This file is written in a way that the code will be written such that
# we only need to change this file if we change of datatype( sql, others...)
# --> we don't need to update all code, only this file
#
#
# to use thoses methods in other files, please use: "import filename"


def read(filename):
    """"
     how it works:
                    You create a variable (dictionary) like " data= read(filename)"
                    data is a dictionary containing the data in the csv file

        This form is optimous because it mimics the way a exel file would be anlysed

    """"
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print("File not found.")
        return []






def write(filename, data, fieldnames):
    """
    To add something to a csv file, please use this syntax:

    data = [
        {"Name": "Alice", "Age": 25, "City": "New York"},
        {"Name": "Bob", "Age": 30, "City": "London"}
            ]

    fieldnames = ["Name", "Age", "City"]

    write("people.csv", data, fieldnames)

    """
    

    try:
        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print("File written successfully.")
    except Exception as e:
        print("Error writing file:", e)
