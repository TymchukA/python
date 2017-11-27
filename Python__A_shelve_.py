import shelve
import pprint
import datetime

def init():
    s = shelve.open('Football.db')
    try:
        s['key1'] = { 'FCname': 'TestFC', 'country':'Ukraine', 'year':datetime.date(1997,6,11), 'founderInfo':'Test Subject1','budget': 125412312,'trophy': 88}
        s['key2'] = { 'FCname': 'TestFC1', 'country':'Une', 'year':datetime.date(1945,1,22), 'founderInfo':'Test Subject1','budget': 1215,'trophy': 102 }
        s['key3'] = { 'FCname': 'TestFC', 'country':'Ukrne', 'year':datetime.date(1997,6,11), 'founderInfo':'Test Subject1','budget': 125,'trophy': 899}
    finally:
        s.close()

def change_db():
    with shelve.open('Football.db', writeback=True) as s:
        print('Initial data:')
        pprint.pprint(s['key1'])
        s['key1']['new_value'] = 'this was not here before'
        print('\nModified:')
        pprint.pprint(s['key1'])

def printDB():    
    with shelve.open('Football.db', writeback=True) as s:
        for obj in s:
            print('\n')
            pprint.pprint(s[obj])

def countrySumm():
    country = input("Введіть назву країни (англійською): ")
    existFlag = False
    with shelve.open('Football.db', writeback=True) as s:
        summ = 0
        for obj in s:
            if country == s[obj]['country']:
               existFlag = True
               summ += s[obj]['budget']
        if existFlag == False:
            print("Країна відсутня у БД")
    print("Загальний бюджет футбоьних клубів у країні ", country, " =", summ, " USD")
    repeat = input("input again? Y/N ")
    if repeat == "Y":
        countrySumm()
    else:
        print("BAKA")

with shelve.open('Football.db', writeback=True) as s:
    maxTrophy = s['key1']['trophy']
    for obj in s:
        if maxTrophy < s[obj]['trophy']:
            maxTrophy = s[obj]['trophy']
    print("-------------")
    print("Найбільша кількість трофеїв у ", s[obj]['FCname'], "(", maxTrophy, ")")   
    print("-------------")

init()
countrySumm()