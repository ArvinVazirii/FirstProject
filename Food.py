import time

class Food :

    menu = {}
    # get menu using json from "menu.txt" and save it on foodmenu and return it
    @staticmethod
    def getmenu(myc) :

        global menu
        myc.execute("select name, count from menu")
        menu = dict(myc.fetchall())

        return menu

    @staticmethod
    def order(name, myc):
        timeplayed = int(menu[name])
        menu[name] = str(timeplayed + 1)
        code = "update menu set count = %s where name = %s"
        myc.execute(code, [(menu[name], name)])
        myc.commit()

    @staticmethod
    def unOrdered(name, myc):
        timeplayed = int(gamesName[name])
        gamesName[name] = str(timeplayed - 1)
        code = "update menu set count = %s where name = %s"
        myc.execute(code, [(menu[name], name)])
        myc.commit()

    @staticmethod
    def addFood(name, myc):
        global menu

        if not name in menu:
            menu.update({name : "0"})
            code = "insert into menu(name, count) values(%s, 0)"
            myc.execute(code, [(name)])

        else:
            print("!!This food already exists on menu!!")
            time.sleep(1)

    @staticmethod
    def removeAFood(name, myc):
        global menu
        if name in menu:

            menu.pop(name)
            code = "delete from menu where menu.name = %s"
            myc.execute(code, [(itemname)])
        else :
            print("!!There is no item with that name!!")
            time.sleep(1)
