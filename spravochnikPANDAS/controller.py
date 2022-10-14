import pandas as pd
from view import (get_name,get_last_name,get_position,get_salary,\
                  get_salary_range,get_salary_low,get_salary_higt,\
                  get_phone,show_menu,show_find_menu,update_question,
                  show_export_menu)
from model import (add_emp,find_emp_salary_range,find_emp_position,\
                   find_emp_name,find_emp_phone,del_emp,update_emp,
                   export_csv_json)



def run_work():
    while True:
        df = pd.read_csv('data.csv')
        choice = show_menu()
        if choice == 1:  #add
            add_emp(df)
        if choice == 2:  #find
            ch = show_find_menu()
            if ch == 1:
                find_emp_name(df,get_last_name)
            if ch == 2:
                find_emp_phone(df,get_phone)
            if ch == 3:
                run_work()
            else:
                print('Insert valid number')
                show_find_menu()
        if choice == 3: #find_posit
            find_emp_position(df,find_emp_position)
        if choice == 4: #find_salary range
            find_emp_salary_range(df)
        if choice == 5:  #delete
            find_choice = show_find_menu()
            if find_choice == 1:
                del_emp(df,find_emp_name,get_last_name())
            if find_choice == 2:
                del_emp(df,find_emp_phone,get_phone())
            if find_choice == 3:
                run_work()
        if choice == 6:  #update
            ch = show_find_menu()
            if ch == 1:
                update_emp(df,find_emp_name,get_last_name())
            if ch == 2:
                update_emp(df,find_emp_phone,get_phone())
            if ch == 3:
                run_work()
        if choice == 7:
            df = df.values.tolist()
            a = show_export_menu()
            if a <= 2:
                export_csv_json(df,a)
            else: run_work()
        if choice >= 8: break



