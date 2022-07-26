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
    def saveGameList() :

        # gamelist = open("gameList.txt", "w")
        # saveText = json.dumps(gamesName, indent = 0)
        # gamelist.write(saveText)
        myc.execute("truncate gamelist")
        code = "insert into gamelist(name, count) values(%s, %s)"
        myc.executemany(code, list(gamesName.items()))
        mydb.commit()


    @staticmethod
    def gameplayed(name):
        timeplayed = int(gamesName[name])
        gamesName[name] = str(timeplayed + 1)
        getLog()

    @staticmethod
    def gameUnplayed(name):
        timeplayed = int(gamesName[name])
        gamesName[name] = str(timeplayed - 1)
        getLog()

    @staticmethod
    def addGame(name):

        global gamesName

        if not name in gamesName:
            gamesName.update({name : "0"})
        else :
            print("!!This game already exists!!")
            time.sleep(1)

        getLog()

    @staticmethod
    def removeAGame(name):
        global gamesName

        if name in gamesName:

            gamesName.pop(name)
        else :
            print("!!There is no game with that name!!")
            time.sleep(1)

        getLog()

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

    # save menu with previous and new items on "menu.txt"
    @staticmethod
    def savemenu() :

        # menulist = open("menu.txt", "w")
        # menulist.write(json.dumps(menu, indent = 0))
        myc.execute("truncate menu")
        code = "insert into menu(name, count) values(%s, %s)"
        myc.executemany(code, list(menu.items()))
        mydb.commit()

    @staticmethod
    def order(name):
        timeplayed = int(menu[name])
        menu[name] = str(timeplayed + 1)
        # getLog()

    @staticmethod
    def unOrdered(name):
        timeplayed = int(gamesName[name])
        gamesName[name] = str(timeplayed - 1)
        # getLog()

    @staticmethod
    def addFood(name):
        global menu

        if not name in menu:
            menu.update({name : "0"})

        else:
            print("!!This food already exists on menu!!")
            time.sleep(1)

        # getLog()

    @staticmethod
    def removeAFood(name):
        global menu
        if name in menu:
            menu.pop(name)
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

    def addNewGame(self, gameName) :

        self.gameList.append(gameName)
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

    def getTableInfo(self):
        return str(self.count) + " / " + str(self.empty)

    # def getTableCustomerInfos(self) :
    #     infolist = []
    #     for i in self.customerList:
    #         infolist.append(i.getFullName())
    #         infolist.extend(i.getOrderes())
    #         infolist.extend(i.getGamesPlayed())
    #         infolist.append(i.getCheckInTime())
    #         infolist.append(i.getCheckOutTime())
    #         infolist.append(i.getCosts())
    #     return infolist

    def getinfos(self):
        # code = "insert into tablesInfo(count, emptyness) values(%s, %s)"
        return (self.count, self.empty)
        # myc.executemany(code, x)
    def saveCustomerInfos(self):

        myc.execute("truncate customers")
        infos = []
        for i in self.customerList:
            infos.append(i.getInfos())
             #    tablenumber int,
             #    name varchar(200),
             #    lastname varchar(200),
             #    checkInTime time,
             #    checkOuttime time,
             #    gamecount int,
             #    ordersCount int,
             #    paycheck Dec
        code = "insert into customers values(%s, %s, %s, %s, %s, %s, %s, %s)"
        myc.executemany(code, infos)

    def addCustomer(self, name, lastname) :
        self.customerList.append(customer(name, lastname, self.numberOfTheTable))
        self.count += 1
        self.empty = False

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
            else :
                print("There is no customer with that name")
                time.sleep(1)

    def checkout(self, name, lastname) :
        for i in self.customerList :
            if(i.getName() == name and i.getLastName() == lastname) :
                i.checkOut()
        self.count -= 1
        if(self.count <= 0):
            self.empty = True


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
            choose = str(msvcrt.getch(), "utf-8")
            changeMenuDecide(choose)
            return
        case '2' :
            clear()
            location = "showTables"
            choose = str(msvcrt.getch(), "utf-8")
            showTableInfos()
            return
        case '3' :
            clear()
            location = "add or remove table"
            printAddOrRemove()
            addOrRemove()
            getLog()
            return
        case '4' :
            clear()
            location = "add or remove game"
            printAddOrRemove()
            addOrRemove()
            getlog()
            return
        case '5' :
            clear()
            location = "add or remove food"
            printAddOrRemove()
            addOrRemove()
            gtelog()
            return

        case '6' :
            return

        case '0':
            clear()
            location = "startMenu"
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
    startMenuDecide("0")

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

        number = input("Wich table you want to remove :(Enter number)")
        number = int(number)

        if (number <= len(tables)):

            tables.pop(number - 1)
        else :
            print("There is no table with that name")
            time.sleep(1)

    elif(location == "add or remove game") :
        gamename = input("Please enter name of the game that you want to remove: ")
        Game.removeAGame(gamename)

    elif(location == "add or remove food") :
        itemname = input("Please enter the item name that you want to remove: ")
        Food.removeAFood(itemname)

def showTableInfos():

    myc.execute("select * from tables")
    info = myc.fetchall()
    pritn(json.dumps(info, indent = 1))
    input("\n\tPress enter to continue .....")

def getLog():

    # if(os.path.exists("log.txt")):
    #     os.remove("log.txt")
    # log = open("log.txt", "a")
    Game.saveGameList()
    Food.savemenu()
    code = "insert into location(name) values(%s)"
    x = [(location, )]
    myc.executemany(code, x)

    myc.execute("truncate tablesInfos")
    savereport = []
    code = "insert into tablesInfo(count, emptyness) values(%s, %s)"
    for i in tables:
        savereport.append(i.getinfos())
        i.saveCustomerInfos()

    myc.executemany(code, savereport)
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
    tablenumber int auto_increment primary key,
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

gamesName = Game.getGameList()
menu = Food.getmenu()

location = "startMenu"
tables = []
tables.append(table(0, len(tables) + 1))
tables.append(table(0, len(tables) + 1))
getLog()
printStartMenu()
choose = str(msvcrt.getch(), "utf-8")
startMenuDecide(choose)
