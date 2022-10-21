import CHaser
import Make_Map

class Command():
    """
    各種行動を起こします。
    """

    def __init__(self):

        self.run = CHaser.Client()
        self.mapcont = Make_Map.Make_map()
        self.ready_OK = False
        """Set instance"""

    def move(self,com, dir):
        """
        各種行動を起こします。
        Get_info忘れないで！
        """

        result = [0 for i in range(9)]

        if self.ready_OK == False: #if didn't get_ready()
            self.get_ready()
            print("Warning!:You didn't get_ready().")

        if com == "put":
            if dir == 1:
                result = self.run.put_up()
            if dir == 7:
                result = self.run.put_down()
            if dir == 3:
                result = self.run.put_left()
            if dir == 5:
                result = self.run.put_right()

        if com == "walk":
            if dir == 1:
                result = self.run.walk_up()
                self.mapcont.mapY -= 1
            if dir == 7:
                result = self.run.walk_down()
                self.mapcont.mapY += 1
            if dir == 3:
                result = self.run.walk_left()
                self.mapcont.mapX -= 1
            if dir == 5:
                result = self.run.walk_right()
                self.mapcont.mapX += 1

        if com == "look":
            if dir == 1:
                result = self.run.look_up()
            if dir == 7:
                result = self.run.look_down()
            if dir == 3:
                result = self.run.look_left()
            if dir == 5:
                result = self.run.look_right()

        if com == "search":
            if dir == 1:
                result = self.run.search_up()
            if dir == 7:
                result = self.run.search_down()
            if dir == 3:
                result = self.run.search_left()
            if dir == 5:
                result = self.run.search_right()

        print(com+" "+str(dir))
        self.ready_OK = False

        return result

    def get_ready(self):
        """Lunch get_ready and return map."""

        self.ready_OK = True
        result = self.run.get_ready()
        self.mapcont.UpData("G",0,result)
        for list in self.mapcont.map:
            print(list)
        return result
    
    def get_map(self):
        """MAPはこちらからどうぞ"""
        return self.mapcont.map
        
