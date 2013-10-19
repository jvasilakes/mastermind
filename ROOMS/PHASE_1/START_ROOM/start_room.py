class StartRoom(Room):
    def __init__(self):
        self.name = 'First Room'
        
    def interact(self):
        global current_room, black_room, fairy_room, fairy_key_found, first_fairy_room
         
        print "\nThere is a door to your left and a door to your right."
        
        while current_room == start_room:
            next = raw_input("""
            What do you do?
            ---------------
            Open the left door.
            Open the right door.
            Look around this room.
            ? """)
    
            if "left" in next and not left_door_unlocked or \
               "Left" in next and not left_door_unlocked:
                print "\nThe left door is locked. You cannot open it."
            elif "left" in next and left_door_unlocked or \
                 "Left" in next and left_door_unlocked:
                print "\nThe left door is unlocked!"
                print "You open the door."
                current_room = fairy_room
            elif "right" in next or "Right" in next:
                print "\nYou open the right door."
                current_room = black_room
            elif "around" in next and not fairy_key_found or \
                 "look" in next and not fairy_key_found or \
                 "Look" in next and not fairy_key_found:
                print "\nYou search the room."
                ellipsis()
                print "You find a small emerald key in a dark corner."
                fairy_key_found = True
            elif "around" in next and fairy_key_found or \
                 "look" in next and fairy_key_found or \
                 "Look" in next and fairy_key_found:
                print "\nYou find nothing more in the room."
            else:
                print "\nI don't know what you mean. Choose one of the available options."
