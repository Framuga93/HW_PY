import csv
def view_list():
    with open('sprav.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
