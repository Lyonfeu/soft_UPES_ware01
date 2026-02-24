import csv


# This file is written in a way that the code will be written such that
# we only need to change this file if we change of datatype( sql, others...)
# --> we don't need to update all code, only this file
#
#
# to use thoses methods in other files, please use: "import filename"




def convert_value(value):
    if value == "" or value is None:
        return None
    try:
        if "." in value:
            return float(value)
        return int(value)
    except:
        return value






def read(file_path):
    """
     how it works:
                    You create a variable (dictionary) like " data= read(filename)"
                    data is a dictionary containing the data in the csv file

        This form is optimous because it mimics the way a exel file would be anlysed

    """
    data = {}

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        # initialize columns
        for field in reader.fieldnames:
            data[field] = []

        # read values
        for row in reader:
            for field in reader.fieldnames:
                value = convert_value(row[field])

                if value is not None:
                    data[field].append(value)

    return data



def write(filename, data):
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
        fieldnames = list(data[0].keys())

        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        print("Error writing file:", e)




    

def transfer(filename1,filename2):
    data=read(filename1)
    field_names=get_fieldnames(data)
    write(filename1, data, field_names)

