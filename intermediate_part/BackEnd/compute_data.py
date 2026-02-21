import utility.Read_write as R


def compute(path_in,path_out):
    """
    This function take a file locazted at path in, and a path_out location.
    If the path_out file does not exist, it creates it.

    If the Path_out file does exist, it adds the value of path_in to path_out
    , respecting the mathematically logical value of each category.

    warning: all path_in must have the same lines
    TO USE:

    compute(path_in, path_out)
    """
    data=R.read(path_in)
    if not (R.file_exists):
        R.transfer(path_in,path_out)
    else:
        data=R.read(path_in)
        data2=R.read(path_out)
        result = {}
        for key in data:
            result[key] =
            {
                "average": data[key]["average"] + data2[key]["average"],
                "count": data[key]["count"] + data2[key]["count"]
            }
        R.write(path_out,result,R.get_fieldnames(result))

