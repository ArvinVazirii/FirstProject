import time

class Game :

    gamesName = {}

    def getGameList(myc) :

        global gamesName
        myc.execute("select name, count from gamelist")
        gamesName = dict(myc.fetchall())

        return gamesName

    def gameplayed(name, myc):

        global gamesName
        timeplayed = int(gamesName[name])
        gamesName[name] = str(timeplayed + 1)
        code = "update gamelist set count = %s where name = %s"
        myc.execute(code, (gamesName[name], name))

    def gameUnplayed(name, myc):
        global gamesName
        timeplayed = int(gamesName[name])
        gamesName[name] = str(timeplayed - 1)
        code = "update gamelist set count = %s where name = %s"
        myc.execute(code, [(gamesName[name], name)])

    def addGame(name, myc):

        global gamesName
        name = name.lower()
        if not name in gamesName:
            gamesName.update({nam : "0"})
            code = "insert into gamelist(name, count) values(%s, 0)"
            myc.execute(code, [(name)])
        else :
            print("!!This game already exists!!")
            time.sleep(1)

    def removeAGame(name, myc):

        global gamesName
        if name in gamesName:

            gamesName.pop(name)
            code = "delete from gamelist where gamelist.name = %s"
            myc.execute(code, [(name)])

        else :
            print("!!There is no game with that name!!")
            time.sleep(1)
