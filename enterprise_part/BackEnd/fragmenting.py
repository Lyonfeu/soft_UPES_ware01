import utility.Read_Write as R
from random import random



def rand_in_one( numb):
    """
    this function take a n number as argument and give back
    linked chain of n element of wich add up to one

    """
    numbers = [random() for i in range(numb)]
    total = sum(numbers)
    return [x / total for x in numbers]



def add_up (filename, number_of_intermediate):
    """
    this function takes a filename and a number n
    It will takes the data on the file at filename adresse and
    input it randomnly on  n files at the adress
    filename_part_x where x goes from 0 to n-1
    """
    data= R.read(filename)
    new_data= compute_stats(data)
    for Key in new_data.keys():
        rand= rand_in_one(number_of_intermediate)
        rand2= rand_in_one(number_of_intermediate)        
        for i in range(number_of_intermediate):
            a=format_data(new_data, rand[i],rand2[i])
            R.write(filename[:-4] + "_part_" + str(i)+".csv", a )

    
            
def format_data ( data, rand1, rand2):

    """
    This function take a data and 2 numbers and muiltiply the data by rand1 and
    rand2 in desired way.

    """
    rows=[]
    for key, values in data.items():
        rows.append(
                    {
                    "Category": key,
                    "Average": values["average"] * rand1,
                    "Count": values["count"] * rand2
                    }
                   )
    return rows   







    



def compute_stats(data):


    """
    take a dictionary data as an input and give bach another dictionary
    in the form:

    {
    'A': {'average': 20.0, 'count': 3},
    'B': {'average': 10.0, 'count': 2},
    'C': {'average': 8.5, 'count': 4}
    }

    where data=
    {
    "A": [10, 20, 30],
    "B": [5, 15],
    "C": [7, 8, 9, 10]
    }
        
    """
    result = {}
    for category, values in data.items():
        if len(values) == 0:
            avg = 0
            count = 0
        else:
            count = len(values)
            avg = sum(values) / count

        result[category] ={
            "average": avg,
            "count": count
        }

    return result



