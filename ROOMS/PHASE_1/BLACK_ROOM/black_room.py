class BlackRoom(Room):
    def __init__(self):
        self.name = 'Black Room'
        
    def interact(self):
        global current_room, start_room, left_door_unlocked, switch_pressed, boss1
        switch_pressed = False
        
        print "\nYou pass through the right door into a pitch-black room."
        
        while current_room == black_room:
            next = raw_input("""
            What do you do?
            ---------------
            Search the room.
            Return to the previous room.
            ? """)

            if "search" in next and not switch_pressed or \
               "Search" in next and not switch_pressed:
                print
                print "You start feeling around the room."
                ellipsis()
                print "You feel something like a switch."
		while True:
                    ans_switch = raw_input("Flip the switch? y/n: ")
                    if ans_switch == "y":
                        print "You flip the switch."
                        switch_pressed = True
                        boss1.interact()
			break
                    elif ans_switch == "n":
                        print "You don't flip the switch."
                    else:
                        print "Type \"y\" or \"n\"."
            elif "search" in next and switch_pressed or \
                 "Search" in next and switch_pressed:
                print
                print "All you find is the switch you already flipped."
            elif "return" in next or \
                 "Return" in next or \
                 "previous" in next:
                current_room = start_room
            else:
                print
                print "I don't know what you mean. Choose one of the available options."


class Mastermind1(Boss):
    def __init__(self):
        pass
        
    def interact(self):
        global left_door_unlocked
        
        print """
        You hear the sudden click of a lock as the door through which you came
        into this room is bolted shut. Torches ignite along the walls and you 
        find yourself in a dank cell surrounded by dark, mishapen figures. As 
        the torch light flickers you discern that these figures are in fact 
        repulsive goblins, quietly snickering and whispering to each other in 
        a hideous language. 
        """
        raw_input()
       
        print """
        A figure emerges from within them, hooded, and with upright posture.
        You cannot make out his face under his cloak.
        """
        
        raw_input()
        
        print """
    ##########    #############
  ########             #########
########                 #########        \"A lost soul enters our midst!\",
######          ###       ########        he sneers, and the goblins' snickers
#####         ######       #########      turn to laughs. 
#####       #########       ##########     
#####       ###########      #########    \"I am the first Mastermind. If
#####       ##  ###  ##         ######    you are able to solve my puzzle
#####       ###########           ####    I may be so gracious as to let you 
######      ###########            ###    pass.
######      ###########             ##
######      ###########              #    If not, my goblins shall rip the
######      ###########          #   #    flesh from your bones.\"
######       ##########           #  #
#####         ########               #
#####          ######                     \"My puzzle is called the 
####             ###                      3-Digit Number Code.\"
###               ##
##                 #
##        ##       #
##         #
"""

        raw_input()
        
        print """
        Each digit is a number 1 through 9. The third digit is 15 less than the
        sum of the first two digits. The first digit is one less than the second
        digit. What is the 3-digit code? You have 3 guesses.
        """

        for x in xrange(3):
            try:
                ans_code = int(raw_input("Enter a 3-digit number: "))
                if ans_code == 892:
                    ellipsis()
                    print "\n"
                    print """
        \"Bah! You figured out my secret code!
        Goblins! Quickly, let us depart!\"
                
        The cloaked man and his horde of goblins are enveloped in a cloud 
        of blue smoke. The goblins' snickers slowly fade away and as the 
        smoke clears you find yourself alone in the room once again.
        
        You hear a loud click as the door is unlocked behind you.
                """
                
                    left_door_unlocked = True
                    break
                elif ans_code != 892:
                    if x == 2:
                        print "\"You've run out of guesses! Now you shall die!\""
                        print "The hideous goblins attack and rip the flesh from your bones."
                        lose("The first Mastermind has defeated you!")
                    else:
                        print """
        \"Ha! Perhaps my puzzle shall defeat you!
        You have %d guesses left.\"
        """ % (2 - x)
            except ValueError:
                print """
        \"You must enter a number!
        Perhaps my puzzle shall defeat you!
        You have %d guesses left.\"
        """ % (2 - x)
