import sqlite3 as db
c = db.connect(database="Football")
cu = c.cursor()
flag = False

def deleteTable():
    try:
        cu.execute("""DROP TABLE FC;""")
    except db.DatabaseError as x:
        print("Hi: ", x)
        c.commit()
        c.close()

def createTable():
    try:
        cu.execute("""
            CREATE TABLE FC (
                id INTEGER PRIMARY KEY,
                FCname VARCHAR(30),
                country VARCHAR(30),
                year INTEGER,
                founderInfo VARCHAR(6),
                budget INTEGER,
                trophy INTEGER
                );
            """)
    except db.DatabaseError as x:
        print("Hi: ", x)
        c.commit()
#deleteTable()
createTable()


def add_club(FCname,country,year,founderInfo,budget,trophy):
    c.execute("INSERT INTO FC (FCname,country,year,founderInfo,budget,trophy) VALUES ('%s','%s','%d','%s','%d','%d')"
              %(FCname,country,year,founderInfo,budget,trophy))
    c.commit()

def handsInput():
    FCname = input("Назва клубу:\n")
    country = input("Країна:\n")
    year = int(input("Рік заснування:\n"))
    founderInfo = input("Прізвища та ім'я засновника:\n")
    budget = int(input("Бюджет на рік:\n"))
    trophy = int(input("Кількість трофеїв:\n"))
    print('\n')
    add_club(FCname,country,year,founderInfo,budget,trophy)
    menu()

def printOutOut():
    cu.execute('SELECT * FROM FC')
    row = cu.fetchone()

    while row is not None:
       print("id:"+str(row[0])+" Назва клубу: "+row[1]+" | Країна: "+row[2]+" | Рік заснування: "+str(row[3])+" | Засновник: "+row[4]+" | Бюджет: "+str(row[5])+" | Кількість трофеїв: "+str(row[6]))
       row = cu.fetchone()
    menu()

def clubsBudget():
    countryInput = input("Країна: ")
    cu.execute('SELECT sum(budget) FROM FC WHERE country LIKE "{inp}"'.format(inp = countryInput)) 
    for rec in cu.fetchall():
         print("Cума бюджету всіх клубів у цій країні:",rec[0], "USD")
    menu()

def trophyCount():
    cu.execute('SELECT FCname,country,max(trophy) FROM FC')
    for rec in cu.fetchall():
         print("Найбільше трофеїв:",rec)
    menu()

def menu():
    print("------------------------------------")
    print("1] Додати новий клуб")
    print("2] Вивести БД")
    print("3] Загальний бюджет клубів за країною")
    print("4] Клуб із найбільшою кількістю трофеїв")
    print("------------------------------------")
    inputValue = input("Швидше плес...")
    if inputValue == "1":
        handsInput()
    if inputValue == "2":
        printOutOut()
    if inputValue == "3":
        clubsBudget()
    if inputValue == "4":
        trophyCount()
    else:
        print("BAKA")
    
menu()
cu.close()
c.close()
