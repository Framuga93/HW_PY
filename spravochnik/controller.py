import imp_data as id
import view
import csv_create
import read
import find_export

def button_click():
     view.menu()
     c = view.choose()
     if c == 1 :
          csv_create.do_csv(id.import_bio())
          button_click()
     elif c == 2 :

          find_export.find_chose(find_export.find_s_name())
          button_click()
     elif c == 3 :
          find_export.find_chose(find_export.find_phone())
          button_click()
     elif c == 4 :
          read.view_list()
          button_click()
     elif c == 5:
          exit(0)
     else: print('Please insert valid number')
     return c



