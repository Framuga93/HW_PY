import csv
import controller
def find_s_name():
    with open('sprav.csv') as f:
        reader = csv.reader(f)
        second_name = input('Insert second name: ')
        for row in reader:
            if second_name == row[1]:
                k = row
                print(k)
    return k


def find_phone():
    with open('sprav.csv') as f:
        reader = csv.reader(f)
        phone = input('Insert phone number: ')
        for row in reader:
            if phone == row[2]:
                k = row
                print(row)
    return k

def export_data_csv(n):
    s = input('Write file name: ')
    with open(f'{s}.csv','a') as file:
        file.write(f'{n}\n')
    file.close()

def export_data_txt(n):
    s = input('Write file name: ')
    with open(f'{s}.txt','a') as file:
        file.write(f'{n}\n')
    file.close()

def export_data_json(n):
    s = input('Write file name: ')
    with open(f'{s}.json','a') as file:
        file.write(f'{n}\n')
    file.close()

def find_chose(n):
    ch = int(input('Chose format:\n 1.csv\n 2.txt\n 3.json\n'))
    if ch == 1:
        export_data_csv(n)
    elif ch == 2:
        export_data_txt(n)
    elif ch == 3:
        export_data_json(n)
    else:
        print('Please insert valid number')
        find_chose(n)
