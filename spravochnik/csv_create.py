def do_csv(bio):
    with open('sprav.csv','a') as file:
        file.write(f'{bio}\n')