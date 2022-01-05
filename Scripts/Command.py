import CHaser
import Make_Map

class Command():
    """
    各種行動を起こします。
    """
    run = None
    ready_OK = False
    mapcont = None

    def __init__(self):
        global run
        global mapcont

        run = CHaser.Client()
        mapcont = Make_Map.Make_map()
        """set instance"""

    def move(self,com, dir):
        """
        各種行動を起こします。
        Get_info忘れないで！
        """
        global run
        global ready_OK

        result = [0 for i in range(9)]

        if ready_OK == False: #if didn't get_ready()
            self.get_ready()
            print("Warning!:You didn't get_ready().")

        if com == "put":
            if dir == 1:
                result = run.put_up()
            if dir == 7:
                result = run.put_down()
            if dir == 3:
                result = run.put_left()
            if dir == 5:
                result = run.put_right()

        if com == "walk":
            if dir == 1:
                result = run.walk_up()
                mapcont.mapY -= 1
            if dir == 7:
                result = run.walk_down()
                mapcont.mapY += 1
            if dir == 3:
                result = run.walk_left()
                mapcont.mapX -= 1
            if dir == 5:
                result = run.walk_right()
                mapcont.mapX += 1

        if com == "look":
            if dir == 1:
                result = run.look_up()
            if dir == 7:
                result = run.look_down()
            if dir == 3:
                result = run.look_left()
            if dir == 5:
                result = run.look_right()

        if com == "search":
            if dir == 1:
                result = run.search_up()
            if dir == 7:
                result = run.search_down()
            if dir == 3:
                result = run.search_left()
            if dir == 5:
                result = run.search_right()

        print(com+" "+str(dir))
        ready_OK = False

        return result

    def get_ready(self):
        """Lunch get_ready and return map."""
        global run
        global ready_OK

        ready_OK = True
        result = run.get_ready()
        mapcont.UpData("G",0,result)
        for list in mapcont.map:
            print(list)
        return result
    
    def get_map(self):
        """MAPはこちらからどうぞ"""
        return mapcont.map
        
