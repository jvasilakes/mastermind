import time
import sys
import functions
import rooms
import bosses


# ------------------------------ GAME ENGINE ---------------------------------------------GAME ENGINE -------------------------               
class Engine(object):

    def __init__(self, room_name, map_name):
	self.room_name = room_name
	self.map_name = map_name

    def opening_scene(self):
        print """
        __   __ _____ ____ ___       _____       __   
 |\  /|/  \ /  \  |  |    |   ||\  /|  |  |\   ||  \  
 | \/ ||__| |__   |  |___ |___|| \/ |  |  | \  ||   | 
 |    ||  |    |  |  |    | \  |    |  |  |  \ ||   | 
 |    ||  | \__/  |  |____|  \ |    |__|__|   \||__/  
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@_|__|_@@@@@@@@ || @@@@@@@@_|__|_@@@@@@@@@@@
@@@@@@@@@@/      \@@@@@@ -  - @@@@@@/      \@@@@@@@@@@
@@@@@@@@@@|      |@@@@@@@@||@@@@@@@@|      |@@@@@@@@@@
@@@@@@@@@@|     *|@@@@@@@@\/@@@@@@@@|     *|@@@@@@@@@@
@@@@@@@@@@|      |@@@@@@@@@@@@@@@@@@|      |@@@@@@@@@@
@@@@@@@@@@|______|@@@@@@@@@@@@@@@@@@|______|@@@@@@@@@@
------------------------------------------------------
              """
        time.sleep(2)
        raw_input("Press RETURN to begin.")
        print
        print "You awake in a dark room."
        functions.ellipsis()
        current_room = self.map_name.next_room(self.room_name)
        while True:
	    next_room_name = current_room.interact()
	    current_room = self.map_name.next_room(next_room_name)


class Map(object):

    rooms = { 
    'start room' : rooms.StartRoom(),
    'black room' : rooms.BlackRoom(),
    'fairy room' : rooms.FairyRoom(),
    'fairy garden' : rooms.FairyGarden(),
    'sign room' : rooms.SignRoom(),
    'boss1': bosses.Mastermind1() 
    }

    def __init__(self):
	pass

    def next_room(self, room_name):
	return Map.rooms.get(room_name)

def reset_game():
    global your_name
    your_name = ''

def main():
    reset_game()
    mapA = Map()
    game = Engine('start room', mapA)
    game.opening_scene()

if __name__ == '__main__':
    main()
