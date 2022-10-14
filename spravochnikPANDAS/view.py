
def show_menu():
    print('Welcome to phonebook, please take your choose: \n '
          '1.Import name \n ' #pass
          '2.Find employee \n '
          '3.Find employee by position \n'
          ' 4.Find employee by salary range \n' #pass
          ' 5.Delete employee \n'
          ' 6.Update employee data \n'
          ' 7.Export data \n'
          ' 8.Exit programm')
    return int(input('Make a choice: '))

def get_last_name():
    return input("Insert last_name: ")

def get_name():
    return input("Insert name: ")

def get_position():
    return input("Insert position: ")

def get_phone():
    return int(input("Insert phone: "))

def get_salary():
    return float(input("Insert salary: "))

def get_salary_range():
    lo = float(input("Insert low salary range: "))
    hi = float(input("Insert high salary range: "))
    return lo, hi

def get_salary_low():
    return float(input("Insert salary low: "))

def get_salary_higt():
    return float(input("Insert salary high: "))

def show_find_menu():
    print('This is find menu, please take a choise\n'
          '1.Find employee by last_name\n'
          '2.Find employee by phone\n'
          '3.Back to menu')
    return int(input('Please make a choice: '))

def sure_question():
    return int(input('Are you sure?\n'
                  '1.Yes\n'
                  '2.No (Back to menu)\n'
                  'Make a choice:  '))

def update_question():
    return int(input('What data must update\n'
                     '1.Last name\n'
                     '2.First name\n'
                     '3.Phone\n'
                     '4.Position\n'
                     '5.Salary\n'
                     '6.Back to menu\n'
                     'Make a choice: '))

def show_export_menu():
    return int(input('This is export menu\n'
                     '1.Exoprt to CSV\n'
                     '2.Export to JSON\n'
                     '3.Back to menu\n'
                     'Make a choice: '))