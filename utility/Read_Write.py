import csv


# This file is written in a way that the code will be written such that
# we only need to change this file if we change of datatype( sql, others...)
# --> we don't need to update all code, only this file
#
#
# to use thoses methods in other files, please use: "import filename"


def read(filename):
    """
     how it works:
                    You create a variable (dictionary) like " data= read(filename)"
                    data is a dictionary containing the data in the csv file

        This form is optimous because it mimics the way a exel file would be anlysed

    """
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



def get_fieldnames (data):
    """
    Intermediate function of function add_up() that take a dictionary
    data and give back a list of the filesname of data  
    """
    result=[]
    for Key in data.keys():
        result.append(Key)
    return result;




    

def transfer(filename1,filename2):
    data=read(filename1)
    field_names=get_fieldnames(data)
    write(filename1, data, field_names)










import csv

# -------------------------------
# Lecture CSV
# -------------------------------
def read(filename):
    """
    Lit un fichier CSV et retourne une liste de dictionnaires (DictReader)
    """
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(f"[ERROR] File '{filename}' not found.")
        return []

# -------------------------------
# Écriture CSV
# -------------------------------
def write(filename, data, fieldnames):
    """
    Écrit une liste de dictionnaires dans un CSV.
    data : list of dicts
    fieldnames : liste des colonnes à écrire
    """
    try:
        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print(f"[INFO] File '{filename}' written successfully.")
    except Exception as e:
        print(f"[ERROR] Writing file '{filename}': {e}")

# -------------------------------
# Récupérer les noms de colonnes
# -------------------------------
def get_fieldnames(data):
    """
    Retourne les clés d'un dictionnaire
    """
    return list(data.keys()) if isinstance(data, dict) else []

# -------------------------------
# Conversion dict <-> list
# -------------------------------
def dict_to_list_of_dicts(data_dict):
    """
    Transforme un dict {categorie: [valeurs]} en liste de dicts pour CSV
    """
    result = []
    for key, values in data_dict.items():
        for v in values:
            result.append({key: v})
    return result

def list_of_dicts_to_dict(data_list):
    """
    Transforme une liste de dicts CSV en dict {categorie: [valeurs]}
    """
    result = {}
    for row in data_list:
        for key, value in row.items():
            if key not in result:
                result[key] = []
            result[key].append(float(value))  # Convertir en float si nécessaire
    return result

# -------------------------------
# Transfert (optionnel)
# -------------------------------
def transfer(filename1, filename2):
    """
    Lit un CSV et le réécrit vers un autre fichier
    """
    data_list = read(filename1)
    field_names = data_list[0].keys() if data_list else []
    write(filename2, data_list, field_names)
