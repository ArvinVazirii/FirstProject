import json, os, msvcrt, time, mysql.connector as mysql


class Game :

    # gamesName = {}

    @staticmethod
    def getGameList() :
        # if(os.path.exists("gameList.txt")) :
        #     with open("gameList.txt", "r") as game :
        #         games = json.loads(game.read())

        myc.execute("select name, count from gamelist")
        gamesName = dict(myc.fetchall())

        return gamesName


    @staticmethod
    def gameplayed(name):
        timeplayed = int(gamesName[name])
        gamesName[name] = str(timeplayed + 1)
        code = "update gamelist set count = %s where name = %s"
        myc.execute(code, [(gamesName[name], name)])
        myc.commit()

    @staticmethod
    def gameUnplayed(name):
        timeplayed = int(gamesName[name])
        gamesName[name] = str(timeplayed - 1)
        code = "update gamelist set count = %s where name = %s"
        myc.execute(code, [(gamesName[name], name)])
        myc.commit()

    @staticmethod
    def addGame(name):

        global gamesName

        if not name in gamesName:
            gamesName.update({name : "0"})
            code = "insert into gamelist(name, count) values(%s, 0)"
            myc.execute(code, [(name)])
        else :
            print("!!This game already exists!!")
            time.sleep(1)

    @staticmethod
    def removeAGame(name):
        global gamesName

        if name in gamesName:

            gamesName.pop(name)
            code = "delete from gamelist where gamelist.name = %s"
            myc.execute(code, [(name)])

        else :
            print("!!There is no game with that name!!")
            time.sleep(1)

class Food :

    # get menu using json from "menu.txt" and save it on foodmenu and return it
    @staticmethod
    def getmenu() :

        # if(os.path.exists("menu.txt")) :
        #     with open("menu.txt", "r") as menu :
        #         foodmenu = json.loads(menu.read())
        myc.execute("select name, count from menu")
        menu = dict(myc.fetchall())

        return menu


    @staticmethod
    def order(name):
        timeplayed = int(menu[name])
        menu[name] = str(timeplayed + 1)
        code = "update menu set count = %s where name = %s"
        myc.execute(code, [(menu[name], name)])
        myc.commit()
        # getLog()

    @staticmethod
    def unOrdered(name):
        timeplayed = int(gamesName[name])
        gamesName[name] = str(timeplayed - 1)
        code = "update menu set count = %s where name = %s"
        myc.execute(code, [(menu[name], name)])
        myc.commit()
        # getLog()

    @staticmethod
    def addFood(name):
        global menu

        if not name in menu:
            menu.update({name : "0"})
            code = "insert into menu(name, count) values(%s, 0)"
            myc.execute(code, [(name)])

        else:
            print("!!This food already exists on menu!!")
            time.sleep(1)

        # getLog()

    @staticmethod
    def removeAFood(name):
        global menu
        if name in menu:

            menu.pop(name)
            code = "delete from menu where menu.name = %s"
            myc.execute(code, [(itemname)])
        else :
            print("!!There is no item with that name!!")
            time.sleep(1)

        # getLog()

class person :
    def __init__(self, name, lastname) :
        self.name = name
        self.lastname = lastname

    def changeName(self, name) :
        self.name = name

    def changeLastName(self, lastname) :
        self.lastname = lastName

    def getName(self):
        return self.name
    def getLastName(self):
        return self.lastname

class customer(person) :


    def __init__(self, name, lastname, tablenumber) :
        super().__init__(name, lastname)
        self.checkInTime = time.strftime("%H:%M:%S", time.localtime())
        self.tablenumber = tablenumber
        self.gameList = []
        self.orders = []
        self.checkInTime = ""
        self.checkOutTime = ""
        self.costs = 0
        infos = self.getInfos()
        code = "insert into customers values(%s, %s, %s, %s, %s, %s, %s, %s)"
        temp = []
        temp.append(infos)
        myc.executemany(code, temp)

    def addNewGame(self, gameName) :

        self.gameList.append(gameName)
        code = "update customers set gamecount = %s where name = %s and lastname = %s"
        myc.execute(code, (len(self.gameList), self.name, self.lastname))
        Game.gameplayed(gameName)

    def addNewGame_List(self, gameList) :
        self.gameList.extend(gameList)
        for i in self.gameList :
            Game.gameplayed(gamename)

    def removeAGame(self, gamename) :
        self.gameList.pop()
        Game.gameUnplayed(gamename)

    def orderFood(self, name) :
        self.orders.append(name)
        code = "update customers set orderscount = %s where name = %s and lastname = %s"
        myc.execute(code, [(len(orders), self.name, self.lastname)])
        Food.order(name)

    def removeOrder(self, name) :
        self.orders.pop()
        Food.unOrdered(name)

    def checkOut():
        self.checkOutTime = time.strftime("%H:%M:%S", time.localtime())

    def getInfos(self):
        infos = (self.tablenumber, self.name, self.lastname, self.checkInTime, self.checkOutTime, len(self.gameList), len(self.orders), self.costs)
        return infos

    def getName(self):
        return self.name

    def getLastName(self):
        return self.lastname

    def getFullName(self):
        return self.name + self.lastname

    def getCheckInTime(self):
        return self.checkInTime

    def getCheckOutTime(self):
        return self.checkOutTime

    def getGamesPlayed(self):
        return self.gameList

    def getOrderes(self):
        return self.orders

    def getCosts(self):
        return str(self.costs) + "$"


class table :

    def __init__(self, count, numberOfTheTable) :

        self.numberOfTheTable = numberOfTheTable
        self.count = count
        self.empty = True
        self.customerList = []

        if self.count > 0 :
            empty = False

        for i in range(count) :
            getCustomerInfo()
            location = "startMenu"

        code = "insert into tablesInfo(tablenumber, count, emptyness) values(%s, %s, %s)"
        myc.execute(code, (self.numberOfTheTable, self.count, self.empty))

    def changeTableNumber(self, num):
        self.numberOfTheTable = num

    def getTableInfo(self):
        return str(self.count) + " / " + str(self.empty)

    def getinfos(self):

        return (self.count, self.empty)


    def addCustomer(self, name, lastname) :
        self.customerList.append(customer(name, lastname, self.numberOfTheTable))
        self.count += 1
        self.empty = False
        code = "update tablesInfo set count = %s, emptyness = 0 where tablenumber = %s"
        myc.execute(code, (self.count, self.numberOfTheTable))

    def nameExist(self, name):
        for i in self.customerList:
            if(i.getName() == name):
                return True
        return False

    def lastnameExists(self, lastname):
        for i in self.customerList:
            if(i.geLastName() == lastname):
                return True
        return False

    def removeCustomer(self, name, lastname) :
        for i in self.customerList :
            if(i.getName() == name and i.getLastName() == lastname) :
                self.customerList.pop(i)
                self.count -= 1
                if(self.count <= 0):
                    self.empty = True
                break

    def addGame(self, name):

        if not name in gamesName :
            print("We don't have this game SORRY!")
            time.sleep(1)
            return

        if (len(self.customerList) == 0):
            print("This table is empty")
            time.sleep(1)

        for i in self.customerList :
            i.addNewGame(name)

    def orderFood(self, name, lastname, order):

        if not order in menu :
            print("We don't have this on menu SORRY!")
            time.sleep(1)
            return

        if (len(self.customerList) == 0):
            print("This table is empty")
            time.sleep(1)


        for i in self.customerList :
            if(i.getName() == name and i.getLastName() == lastname) :
                i.orderFood(name)
                return

        print("There is no customer with that name")
        time.sleep(1)


    def checkout(self, name, lastname) :
        for i in self.customerList :
            if(i.getName() == name and i.getLastName() == lastname) :
                i.checkOut()
        self.count -= 1
        if(self.count <= 0):
            self.empty = True

    def getCustomerCount(self):
        return self.count

def clear() :
    os.system('cls')

def printStartMenu() :
    print("   1.Change table info's\n   2.Show current tables\n   3.Add or Remove table\n   4.Add or remove game\n   5.Add or Remove Food\n   6.Exit\n")

def printChangeMenu() :
    print ("   1.Add Customer to a table\n   2.Add a game to table\n   3.Order food\n   4.Back\n")

def printAddOrRemove() :
    print("   1.Add\n   2.Remove\n")

def startMenuDecide(choose) :

    global location
    match choose:
        case '1' :
            clear()
            printChangeMenu()
            location = "changeMenu"
            getLog()
            choose = str(msvcrt.getch(), "utf-8")
            changeMenuDecide(choose)
            return
        case '2' :
            clear()
            location = "showTables"
            getLog()
            showTableInfos()
            startMenuDecide('0')
            return
        case '3' :
            clear()
            location = "add or remove table"
            printAddOrRemove()
            addOrRemove()
            getLog()
            startMenuDecide('0')
            return
        case '4' :
            clear()
            location = "add or remove game"
            printAddOrRemove()
            addOrRemove()
            getLog()
            startMenuDecide('0')
            return
        case '5' :
            clear()
            location = "add or remove food"
            printAddOrRemove()
            addOrRemove()
            getLog()
            startMenuDecide('0')
            return

        case '6' :
            return

        case '0':
            clear()
            location = "startMenu"
            getLog()
            printStartMenu()
            choose = str(msvcrt.getch(), "utf-8")
            startMenuDecide(choose)
            return


def changeMenuDecide(choose) :
    global location
    match choose:
        case '1' :
            clear()
            location = "addCustomer"
            getCustomerInfo()
            getLog()
            startMenuDecide("0")
            return
        case '2' :
            clear()
            location = "addGame"
            addGameToTable()
            getLog()
            startMenuDecide("0")
            return
        case '3' :
            clear()
            locaton = "orderFood"
            orderFood()
            getLog()
            startMenuDecide("0")
            return

        case '4' :
            startMenuDecide("0")
            return

def addGameToTable():

    tableNumber = input("Please enter wich table wants new game: (Back : enter(-1))")
    try:
        tableNumber = int(tableNumber)
        if tableNumber == -1:
            return
    except Exception as e:
        clear()
        return
    clear()
    if(tableNumber > len(tables)):
        print("There is no table with that number!!")
        time.sleep(1)
        return

    name = input("Please enter game name: ")
    tables[tableNumber - 1].addGame(name)

def orderFood():
    tableNumber = input("Please enter wich table you want to save order: (Back : enter(-1))")
    try:
        tableNumber = int(tableNumber)
        if tableNumber == -1:
            return
    except Exception as e:
        clear()
        return
    clear()

    if(tableNumber > len(tables)):
        print("There is no table with that number!!")
        time.sleep(1)
        return

    name = input("Please enter your name: ")
    clear()
    lastname = input("Please enter your lastname: ")
    clear()
    order = input("Please enter food name: ")
    tables[tableNumber - 1].orderFood(name, lastname, order)


def getCustomerInfo() :

    tableNumber = input("Please enter wich table you want to seat on: (Back : enter(-1))")
    try:
        tableNumber = int(tableNumber)
        if (tableNumber == -1):
            return
    except Exception as e:
        clear()
        return

    clear()

    if(tableNumber > len(tables)):
        print("There is no table with that number!!")
        time.sleep(1)
        return

    name = input("Please enter your name: ")
    for i in tables:
        if(i.nameExist(name)):
            print("!!This name is already exists!!")
            time.sleep(1)
            return
    clear()
    lastname = input("Please enter your lastname: ")
    for i in tables:
        if(i.lastnameExists(lastname)):
            print("!!This lastname is already exists!!")
            time.sleep(1)
            return
    clear()
    tables[tableNumber - 1].addCustomer(name, lastname)

def addOrRemove() :
    clear()
    answer = input("Do you want to add or remove (Add, Remove)")
    answer = answer.lower()

    if(answer == "add") :
        clear()
        decideForAdd()

    elif(answer == "remove"):
        clear()
        decideForRemove()

    clear()

def decideForAdd() :

    global tables
    if (location == "add or remove table"):
        tables.append(table(0, len(tables) + 1))
        print("New table added with the number of ", len(tables))
        time.sleep(1)

    elif(location == "add or remove game") :
        gamename = input("Please enter the new game name: ")
        Game.addGame(gamename)

    elif(location == "add or remove food") :
        itemname = input("Please enter the new item name: ")
        Food.addFood(itemname)

def decideForRemove() :
    global tables
    if (location == "add or remove table"):

        if (len(tables) >= 1):

            if not(tables[len(tables) - 1].getCustomerCount() == 0):
                print("Theres cutomer on this table.It must empty to be removed")
                time.sleep(1)
                return

            tables.pop(len(tables) - 1)

            code = "delete from tablesInfo where tablenumber = %s"
            myc.execute(code, [(len(tables) + 1)])

            print("Last table removed (number : " , len(tables) + 1 , ") (:")
        else :
            print("There is no table!!")

        time.sleep(1)

    elif(location == "add or remove game") :
        gamename = input("Please enter name of the game that you want to remove: ")
        Game.removeAGame(gamename)

    elif(location == "add or remove food") :
        itemname = input("Please enter the item name that you want to remove: ")
        Food.removeAFood(itemname)


def showTableInfos():

    myc.execute("select * from tablesInfo")
    infos = myc.fetchall()
    print(infos)
    input("\n\tPress enter to continue .....")

def saveTableinfos():

    myc.execute("truncate tablesInfo")
    savereport = []
    code = "insert into tablesInfo(tablenumber, count, emptyness) values(%s, %s, %s)"
    for i in tables:
        savereport.append(i.getinfos())

    myc.executemany(code, savereport)
    mydb.commit()


def getLog():

    # if(os.path.exists("log.txt")):
    #     os.remove("log.txt")
    # log = open("log.txt", "a")
    code = "insert into location(name) values(%s)"
    x = [(location, )]
    myc.executemany(code, x)
    mydb.commit()
    # log.write(json.dumps(location, indent = 0))
    # for i in tables :
    #     log.write(json.dumps(i.getTableInfo(), indent = 0))
    #     log.write(json.dumps(i.getTableCustomerInfos(), indent = 0))




mydb = mysql.connect(host = "localhost", user = "root", password = "root", database = "testdp")
myc = mydb.cursor()
myc.execute("""create table if not exists gamelist(
    id int auto_increment primary key,
    name varchar(100),
    count varchar(200)
)""")
myc.execute("""create table if not exists menu(
    id int auto_increment primary key,
    name varchar(200),
    count varchar(200)
)""")
myc.execute("""create table if not exists location(
    name varchar(50)
)""")
myc.execute("""create table if not exists tablesInfo(
    tablenumber int primary key,
    count int,
    emptyness char(5)
)""")
myc.execute("""create table if not exists customers(
    tablenumber int,
    name varchar(200),
    lastname varchar(200),
    checkInTime time,
    checkOuttime time,
    gamecount int,
    ordersCount int,
    paycheck Dec
)""")
gamesName = {}
menu = {}
tables = []

gamesName = Game.getGameList()
menu = Food.getmenu()
saveTableinfos()
location = "startMenu"
printStartMenu()
choose = str(msvcrt.getch(), "utf-8")
startMenuDecide(choose)
