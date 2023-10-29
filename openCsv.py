import csv

file = "fatal_shark_attacks.csv"

def read(file):
    """
    This function reads data from a CSV file and returns a list of dictionaries,
    where each dictionary represents a row of data with keys from the CSV header.

    :param file: The path to the CSV file to be read.
    :type file: str

    :return: A list of dictionaries containing the CSV data.
    :rtype: list[dict]
    """
    with open (file, 'r') as csv_read:
        reader = csv.reader(csv_read, delimiter=',')
        header = next(reader)
        data = [dict (zip(header, row)) for row in reader]
        
      
       

    return data


if __name__ == '__main__':
    print(read(file))
