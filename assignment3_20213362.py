import pickle

dbfilename = 'assignment3.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb =  pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        #ADD
        if parse[0] == 'add':
            if len(parse) == 4:
                record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
                scdb += [record]
            else: print("Invalid Command, Type again...")
        #DEL
        elif parse[0] == 'del':  
            if len(parse) == 2:
                for p in scdb:
                    if p['Name'] == parse[1]:
                            scdb.remove(p)  
                            continue
            else: print("Invalid Command, Type again...")
        #SHOW
        elif parse[0] == 'show':
                if len(parse) == 1:
                    sortKey ='Name'
                    showScoreDB(scdb, sortKey)
                elif len(parse) == 2 :
                    if parse[1] == "Name":
                        sortKey = parse[1]
                        showScoreDB(scdb, sortKey)
                    elif parse[1] == "Age":
                        sortKey = parse[1]
                        showScoreDB(scdb, sortKey)
                    elif parse[1] == "Score":
                        sortKey = parse[1]
                        showScoreDB(scdb, sortKey)
                    else: print("Invalid SortKey")
                else: print("Invalid SortKey")
        #FIND
        elif parse[0] == 'find':
            if len(parse) == 2:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        print("Age="+str(p['Age'])+" "+"Name="+ str(p['Name'])+" "+"Score="+str(p['Score']))
            else: print("Invalid Command, Type again...")
        #INC
        elif parse[0] == 'inc':
            if len(parse) == 3:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        k = int(p['Score']) + int(parse[2])
                        p['Score'] = str(k)
            else: print("Invalid Command, Type again...")
        #QUIT
        elif parse[0] == 'quit':
            break
        else:
            print("Invalid Command: " + str(parse[0]))

            
def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(str(attr) + "=" + str(p[attr]), end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)

