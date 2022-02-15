
#page one--------------------------------------------------------------------------------------------------------
def page_one():
    key = 0
    print ("""------------------------------------------
THIS IS PAGE ONE""")
    while key == 0:
        exit = input("""CLICK "0" TO RETURN TO MAIN MENU: """)
        if exit == 0 or exit == 0:
            key = 1
            menu()
        else:
            print ("Invalid input")
            page_one()
def page_two():
    import csv
    key = 0

    with open('Book.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
        print ("""-------------------PAGE2-------------------
    1) parce data
    2) exit
    """)
    while key == 0:
        parce = input("""Please choose a page option: """)
        if parce == "1":
            print(data)
            
        elif parce == "2":
            key = 1
            menu()
        else:
            print ("Invalid input")
    

#main menu-------------------------------------------------------------------------------------------------------    
def menu():
    print ("""-------------------MENU-------------------
    1) page test
    2) csv test
    3) ...
    4) EXIT
    """)
    main_choice()
def main_choice():   
    choose = input("Please choose a menu option: ")
    if choose == 1:
        print ("001")
        page_one()
    elif choose == 2:
        print ("010")
        page_two()
    elif choose == 3:
        print ("011")
    elif choose == 4:
        exit()
    else:
        print ("error")
        main_choice()

menu()
