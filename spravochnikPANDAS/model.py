import csv
import json
import pandas as pd
import numpy as np
from view import (get_name,get_last_name,get_position,
                  get_salary,get_salary_range,get_salary_low,
                  get_salary_higt,get_phone,show_menu,sure_question,
                  update_question)

df = pd.read_csv('data.csv')

def add_emp(df):
    emp = pd.DataFrame({
        'last_name' : f'{get_last_name()}',
        'name' : f'{get_name()}',
        'position' : f'{get_position()}',
        'phone' : f'{get_phone()}',
        'salary' : f'{get_salary()}',
    }, index = [0])
    imp = pd.concat([df,emp], ignore_index=True)
    imp.to_csv('data.csv',index=False)

def find_emp_name(data,find_function):
    emp = data[data['last_name']==find_function]
    print(emp)
    return emp

def find_emp_phone(data,find_function):
    emp = data[data['phone']==find_function]
    print(emp)
    return emp

def find_emp_position(data,find_function):
    emp = data[data['position']==find_function]
    print(emp)

def find_emp_salary_range(data):
    lo = get_salary_low()
    hi = get_salary_higt()
    emp = data[(data['salary']<=hi) & (data['salary']>=lo)]
    print(emp)
    return emp

def del_emp(data,find_function,get_function):
    emp = find_function(data, get_function)
    inde = emp.index
    a = inde[0]
    b = sure_question()
    if b == 1:
        data.drop(labels=[a], axis=0, inplace=True)
        data.to_csv('data.csv', index=False)
    else: return show_menu()

def update_emp(data,find_function,get_function):
    emp = find_function(data, get_function)
    inde = emp.index
    a = inde[0]
    ch = update_question()
    if ch == 1:
        data.at[a, 'last_name'] = f'{get_last_name()}'
        data.to_csv('data.csv', index=False)
    if ch == 2:
        data.at[a, 'name'] = f'{get_name()}'
        data.to_csv('data.csv', index=False)
    if ch == 3:
        data.at[a, 'phone'] = f'{get_phone()}'
        data.to_csv('data.csv', index=False)
    if ch == 4:
        data.at[a, 'position'] = f'{get_position()}'
        data.to_csv('data.csv', index=False)
    if ch == 5:
        data.at[a, 'salary'] = f'{get_salary()}'
        data.to_csv('data.csv', index=False)
    # if ch == 6:


def export_csv_json(data,a):
    if a == 1:
        name_file = input('Insert file name: ')
        with open(f'{name_file}.csv', 'w', encoding='utf-8') as fout:
            csv_writer = csv.writer(fout)
            for employee in data:
                csv_writer.writerow(employee)
    if a == 2:
        name_file = input('Insert file name: ')
        with open(f'{name_file}', 'w', encoding='utf-8') as fout:
            for employee in data:
                fout.write(json.dumps(employee) + '\n')


# add_emp(df)
# find_emp_salary_range(df)
