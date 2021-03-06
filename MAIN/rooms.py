import time
import sys
import re
import functions
import bosses


class Room(object):
    def __init__(self, name):
        self.name = name
        
class StartRoom(Room):
    def __init__(self):
        self.name = 'First Room'

    def interact(self):
        print "\nThere is a door to your left and a door to your right."

        while True:
            next = raw_input("""
        What do you do?
        ---------------
        Open the left door.
        Open the right door.
        Look around this room.
        ? """)
    
            if "left" in next and not functions.inventory.in_stock('talisman') or \
               "Left" in next and not functions.inventory.in_stock('talisman'):
                print "\nThe left door is locked. There is a hexagonal opening where something can fit."
            elif "left" in next and functions.inventory.in_stock('talisman') or \
                 "Left" in next and functions.inventory.in_stock('talisman'):
                print "\nThere is a hexagonal opening in the door. You place the talisman into it."
		functions.ellipsis()
                print "You hear a loud click as the door unlocks. You open the door..."
		return('fairy room')
            elif "right" in next or "Right" in next:
                print "\nYou open the right door."
		return('black room')
            elif "around" in next and not functions.inventory.in_stock('fairy key') or \
                 "look" in next and not functions.inventory.in_stock('fairy key') or \
                 "Look" in next and not functions.inventory.in_stock('fairy key'):
                print "\nYou search the room."
                functions.ellipsis()
                print "You find a small emerald key in a dark corner."
                functions.inventory.add_item('fairy key') 
            elif "around" in next and functions.inventory.in_stock('fairy key') or \
                 "look" in next and functions.inventory.in_stock('fairy key') or \
                 "Look" in next and functions.inventory.in_stock('fairy key'):
                print "\nYou find nothing more in the room."
            else:
                print "\nI don't know what you mean. Choose one of the available options."
    
class BlackRoom(Room):
    def __init__(self):
        self.name = 'Black Room'
	self.trap_sprung = False
        
    def interact(self):
        
        print "\nYou pass through the right door into a pitch-black room."
        
        while True:
            next = raw_input("""
        What do you do?
        ---------------
        Search the room.
        Return to the previous room.
        ? """)

            if "search" in next and not self.trap_sprung or \
               "Search" in next and not self.trap_sprung:
                print
                print "You start feeling around the room."
                functions.ellipsis()
                print "Your ankle gets caught on a rope on the ground."
		print "You are caught in trap!"
                self.trap_sprung = True
		raw_input()
		boss1 = bosses.Mastermind1()
		boss1.interact()

            elif "search" in next and self.trap_sprung or \
                 "Search" in next and self.trap_sprung:
                print
                print "All you find is the rope you were caught in."

            elif "return" in next or \
                 "Return" in next or \
                 "previous" in next:
		 return('start room')

            else:
                print
                print "I don't know what you mean. Choose one of the available options."
            
class FairyRoom(Room):
    def __init__(self):
        self.name = 'Fairy Room'
	self.first_fairy_room = True

    def show_key(self):
        global your_name
        print "\nYou show her the key."
        functions.ellipsis()
        print """
        \"What luck we have today, all these fairies and I!
        That's it, that's the one! Now I shall tell you
        our tale. So full of grief and of sorrow and utter
        misfortune it is.\"
        """
        raw_input()
        
        print """
        Many ages ago we fairies ruled both earth and sky
        in the land above. The garden you see before you
        in which we now reside is a mere fraction of the
        empire we once held.
        """
        raw_input()
        print """
        All lived in peace under a just ruler, the Great
        Fairy Daphnis, who brought us magnificent
        prosperity and great joy. 
        The rivers flowed with water sweet and clear.
        The trees swayed in breezes cool and slow.
        All the world rejoiced in His justice and piety.
        """
        raw_input()
        print """
        He built grand temples for the gods, great stadiums
        for the people, and glorious palaces for the gentry.
        """
        raw_input()
        print """
        For the poor He donated food, for their animals He
        donated fodder; during droughts He donated water, 
        and during storms He found us shelter.
        """
        raw_input()
        print """
        I was His wife, always loyal and true.
        It was I who saw His fall into darkness
        and I myself have witnessed the Hell 
        from which He shall never return.
        """
        raw_input()
        print """
        It was in the fair season of Spring that His thoughts
        turned toward melancholy.
        He began to speak to me of sad things
        where before he only spoke of prosperity and happiness.
        """
        raw_input()
        print """
        It was in Summer that resentment arose in His mind.
        He began to chastise the poor who, as He said,
        were always taking, never giving.
        """
        raw_input()
        print """
        In Fall His anger turned to hate.
        He imprisoned those who disliked Him
        and tortured those who spoke out against Him.
        """
        raw_input()
        print """
        In winter of that year he turned a solitary soul.
        He pushed us all, even I His wife and Queen,
        into these dark, horrid dungeons
        where we for many ages did reside,
        while He ruled us from the land up above,
        He who had become the Evil Mastermind.
        """
        raw_input()
        print """
        We endured the darkness and the dampness
        for almost 200 years, 'till hearing of our plight
        the Human Queen Guinevere came and blessed us with 
        this small garden and a constant light with which
        to fill it. 
        """
        raw_input()
        print """
        We are grateful for our small home.
        We certainly do love it so.
        Yet we miss the land above with its tall trees,
        lively creatures, and wide meadows.
        """
        raw_input()
        print """
        Thus we request your help, %s, we desire to
        escape this place forthwith! Yet we have no power
        to leave, for the Evil Mastermind and his minions
        keep a constant watch over us. 
        """ % your_name # No name printed here in gameplay - fix
        raw_input()
        print """
        They patrol the dungeons to keep us imprisoned,
        and any fairy found outside this garden they quickly
        and mercilessly murder.
        Yet you are a human and may obtain safe passage,
        if you are able to solve their riddles, puzzles,
        and conundrums.
        """
        raw_input()
        print """
        Therefore we beseech you! Find the evil Mastermind
        in the land above and release us from here.
        Help us return to our garden so that we may again
        find peace, happiness, and unity!
        """

        next = raw_input("Will you help us? y/n ")
        while True: 
            if "y" in next or "Y" in next:
		return('fairy garden')
            elif "n" in next or "N" in next:
                functions.lose("You decided to not help the fairies. Shame on you!")
            else:
                print "You must enter either \'y\' or \'n\'."
    def first_fairy(self):
        global your_name
        self.first_fairy_room = False
        print """
        A bright, clear light shines from within, and, your eyes being by
        now accustomed to the darkness, you are temporarily blinded by it.
        Voices high and soft echo quietly all around you; the sweet scents
        of fruits and herbs fill the air. Still you cannot see clearly,
        but as your eyes adjust to the light, you find that you have
        entered a garden, untamed and wild, yet supremely beautiful. You
        try to discern the source of these soft voices.
        """
        
        raw_input()
        
        print """
        \"Welcome!\" a voice calls, \"Who are you who travels alone in that
        dark dungeon? What is your name, O' courageous traveler?\"
        """
                
        your_name = raw_input("Enter your name: ")
        
        print """
        A quite small fairy flutters out from a nearby bush, shining
        brightly. You realize that there are fairies all around you hiding
        in the vegetation and quietly speaking to each other with an air
        of dismay at the presence of a visitor.
        """
        
        raw_input()

        print """
  ###-----########       ##########
 #/        \#######     ######----###
#/          \###############/      \##    
|            \######--#####/        |#    
|             |###/    \##/         |#    
#\            |##/      |           |#    
##|           |##|      |           /#    
##|           \##\      |        __/##    \"Ah, %s you are called! We delight
##|            \##|   _/        /#####    in your presence! It has been many
 ##\            \_/    \        \#####    an age since a human has entered
  ##\                   \       |#####    our home. We welcome you and bid you
   ##\____----/ /        | _    /#####    to stay, that you might hear of the
   ##/       / /    _    |/ |   \#####    misfortune that has befallen our
  ##|       / /____/ |  /__/    /#####    people since your ancestor, the
  ##\       |_______/   |      /######    Great Queen Guinevere, bequoth to us
  ###|        _         | ____/######     this fair garden in which we now
  ###|    __##/          \##########      reside.\"
   ###\__/###/            \#######
    ########/              \#####
     ######/                |#####
     #####/                 |#######
     #####|                  \########
    ######|  _   _  _  _   _ |########
    ######\_/ \_/ \/ \/ \_/ \|########
   ##########/   /#/  |###############
   #########/   /#/  /################
  #########/   /#/  /#################
  ########/  /#_/ /#################
 #######_/ / /  _/#################
  #####/ _/#|  /###############
   ##/  /###| /###########
   ##| /####|/########
    #|/#######
        
        """ % your_name
        
        raw_input()
	while True:
            next = raw_input("Might you hear our story? y/n ")
            if next == "y":
                print """
        \"Delightful! Although before I begin I have a favor to ask
        of you, %s.\"
                """ % your_name
                raw_input()
            
                print """
        \"Many months ago one of the fairies, nay, the bravest of us all,
        ventured out into the dungeon. She took with her a certain key,
        hoping to discover its purpose, for we know not what lock it
        unlocks or what door it opens.\"
                """
            
                while True:
                    next2 = raw_input("""
        \"Have you perchance come across a small emerald 
        key in the course of your travels?\" 
        y/n """)
                
                    if next2 == "y" and functions.inventory.in_stock('fairy key'):
                        return(self.show_key())
                    elif next2 == "y" and not functions.inventory.in_stock('fairy key'):
                        print """
        \"Nay! O' traveller! It seems a key you hold not. 
        Just the clothes on your back and the scars
        from your adventures, they are the only
        possessions I see!\"
                        """
                        raw_input()
                        print """
        \"We welcome you to stay, yet no farther may you go
        without the emerald key that we seek.\"
                        """
                        raw_input()
                        print "You return to the previous room."
			return('start room')
                    elif next2 == "n":
                        print """
        \"I see. I see. We welcome you to stay, yet no 
        farther may you go without the emerald key that 
        we seek.\"
                        """
                        raw_input()
                        print "You return to the previous room."
			return('start room')
                    else:
                        print "Type \"y\" or \"n\"."

            elif next == "n":
                print """
        \"Oh, I see then that you must depart. Please return
        to us soon so that you might hear our tale.\"
                """
		raw_input()
		print """
	\"Yet while you are away, please, if you are able, 
	search the surrounding rooms for a small emerald
	key. One of our number misplaced it during a venture
	into the dungeons, and we have not been able to 
	recover it since. To have it returned would bring 
	great relief to our community.\"
		"""
		raw_input()
		print "You return to the previous room."
		return('start room')            

            else:
                print "Type \"y\" or \"n\"."
                            
    def second_fairy(self):
        print """
        You pass through the door into the home of the fairies.
        The fairy you met earlier is waiting for you at the
        entrance.
        """
        raw_input()
        
        print """
  ###-----########       ##########
 #/        \#######     ######----###
#/          \###############/      \##    
|            \######--#####/        |#    
|             |###/    \##/         |#    
#\            |##/      |           |#    
##|           |##|      |           /#    
##|           \##\      |        __/##    \"You're back! You've returned!
##|            \##|   _/        /#####    With key in hand perhaps?
 ##\            \_/    \        \#####    I am so eager to see it again,
  ##\                   \       |#####    it having been lost many months 
   ##\____----/ /        | _    /#####    past.\"
   ##/       / /    _    |/ |   \#####    
  ##|       / /____/ |  /__/    /#####    
  ##\       |_______/   |      /######    
  ###|        _         | ____/######     
  ###|    __##/          \##########      
   ###\__/###/            \#######
    ########/              \#####
     ######/                |#####
     #####/                 |#######
     #####|                  \########
    ######|  _   _  _  _   _ |########
    ######\_/ \_/ \/ \/ \_/ \|########
   ##########/   /#/  |###############
   #########/   /#/  /################
  #########/   /#/  /#################
  ########/  /#_/ /#################
 #######_/ / /  _/#################
  #####/ _/#|  /###############
   ##/  /###| /###########
   ##| /####|/########
    #|/#######
        """
        while True:
            next = raw_input("\"Do you have the small emerald key?\" y/n ")
            if next == "y" and functions.inventory.in_stock('fairy key'):
                return(self.show_key())
            elif next == "y" and not functions.inventory.in_stock('fairy key'):
                print """
        \"Nay! O' traveller! It seems a key you hold not. 
        Just the clothes on your back and the scars
        from your adventures, they are the only
        possessions I see!\"
                """
                raw_input()
                print """
        \"We welcome you to stay, yet no farther may you go
        without the emerald key that we seek.\"
                """
                raw_input()
                print "You return to the previous room."
		return('start room')
            elif next == "n":
                print """
        \"I see. I see. We welcome you to stay, yet no 
        farther may you go without the emerald key that 
        we seek.\"
                """
                raw_input()
                print "You return to the previous room."
		return('start room')
            else:
                print "Type \"y\" or \"n\"."

    def interact(self):
        if self.first_fairy_room:
            return(self.first_fairy())
        elif not self.first_fairy_room:
           return(self.second_fairy())


class FairyGarden(Room):
    def __init__(self):
        self.name = 'Fairy Garden'
        self.first_time = True
        self.sign_read = False
        self.have_cake = False
        self.fairy_has_cake = False
        self.met_mayor = False
        
    def intro(self):
        self.first_time = False
        print """
        Marvelous! Just marvelous! I must warn
        you, however, that you are about to
        undertake quite a laborious and trying
        quest. The League of Masterminds is a
        formidable foe indeed; your brain, body,
        and mind must all be in tip-top-shape!
        """
        raw_input()
        print """
        Tip-top-shape indeed! But you certainly
        are quite a bright individual; we need
        not fear failure on your part!
        """
        raw_input()
        print """
        Your first task is to talk to the village
        elders. You will find them beneath the
        ancient Sakura tree."
        """
        raw_input()
        return(self.interact_2())

    def interact_2(self):
        print "You are in the fairy garden."
        print "To your left is a very solemn looking fairy guarding a dark archway."
        print "To your right is a large wooden door with a sign next to it."

        while not self.fairy_has_cake:
            while not self.sign_read:
                next = raw_input("""
        What do you do?
        ---------------
        Talk to the solemn fairy.
        Open the large wooden door.
        Read the sign.
        ? """)
                if "talk" in next or "Talk" in next or "fairy" in next or "Fairy" in next:
                    if not self.have_cake:
                        print "You approach the solemn fairy."
                        functions.ellipsis()
                        print """
        \"Bah!\", the solemn fairy grumbles. \"I\'m
        having a terrible day! Talk to me tomorrow.\"
                              """
                        raw_input()       
                elif "open" in next or "Open" in next or "door" in next or "Door" in next:
                    self.sign_read = True
                    print "You open the large wooden door."
                    functions.ellipsis()
                    print "There is a large, round fairy snoozing behind a large, square desk."
                    raw_input()
                    print """
        \"Guh! Oh! Hey!!\", he booms as you rouse him from his nap.
        \"Who are you! Where are your manners! Don't you know to
        knock before opening a closed door?! Out with you!
        Out! Out!!\"
                          """
                    raw_input()
                    print "You close the door."
                    raw_input()
                elif "read" in next or "Read" in next or "sign" in next or "Sign" in next:
                    self.sign_read = True
                    print "You read the sign next to the door."
                    functions.ellipsis()
                    print """

                +------------------+
                |  MAYOR\'S OFFICE  |
                |   All visitors   |
                |   please knock   |
                |  before entering.|
                +------------------+

                        """
                    raw_input()
                else:
                    print "I don't know what you mean. Choose one of the available options."


            while self.sign_read and not self.met_mayor:
                next = raw_input("""
        What do you do?
        ---------------
        Talk to the solemn fairy.
        Open the large wooden door.
        Knock on the large wooden door.
        ? """)
                if "talk" in next or "Talk" in next or "fairy" in next or "Fairy" in next:
                    if not self.have_cake:
                        print "You approach the solemn fairy."
                        functions.ellipsis()
                        print """
        \"Bah!\", the solemn fairy grumbles. \"I\'m
        having a terrible day! Talk to me tomorrow.\"
                              """
                        raw_input()
                    elif self.have_cake:
                        print "You approach the solemn fairy."
                        functions.ellipsis()
                        print """
        \"Bah!\", the solemn fairy grumbles. \"I\'m
        having a terrible day!\"
                              """
                        raw_input()
                        print """
        \"Oh... What\'s that you have there? That cake
        looks quite tasty!
                              """
                        while True: 
                            next = raw_input("\"Would you mind letting me have a slice?\" y/n ")
                            if "y" in next or "Y" in next:
                                print "You hand him a slice of cake."
                                self.fairy_has_cake = True
                                functions.ellipsis()
                                print """
        \"Oh! Thank you! I shall eat it heartily!\"
                                      """
                                raw_input()
                                print "The fairy hurries off with the cake leaving the archway open."
                                next = raw_input("Go through the archway? y/n ")
                                if "y" in next or "Y" in next:
				    fucntions.ellipsis()
				    return('sign room')
                                elif "n" in next or "N" in next:
                                    break
                                else:
                                    print "FATAL ERROR!"
                                    exit(0)

                            elif "n" in next or "N" in next:
                                print """
        \"Fine! But don't expect me to do any favors for you!\"
                                      """
                                break
                            else:
                                print "Type \"y\" or \"n\"." 
                            break
                        break
                
                        
                elif "open" in next or "Open" in next or "door" in next or "Door" in next:
                    self.sign_read = True
                    print "You open the large wooden door."
                    functions.ellipsis()
                    print "There is a large, round fairy snoozing behind a large, square desk."
                    raw_input()
                    print """
        \"Guh! Oh! Hey!!\", he booms as you rouse him from his nap.
        \"Who are you! Where are your manners! Don't you know to
        knock before opening a closed door?! Out with you!
        Out! Out!!\"
                          """
                    raw_input()
                    print "You close the door."
                    raw_input()

                elif "knock" in next or "Knock" in next or "door" in next or "Door" in next:
                    print "You knock on the door."
                    functions.ellipsis()
                    print """
        \"Guh! Uh... yes! Hello!\", the voice behind the door says.
        \"Please do come in!\"
                          """
                    raw_input()
                    print "You open the door."
                    functions.ellipsis()
                    print "There is a large, round fairy sitting behind a large, square desk."
                    raw_input()
                    print """
        \"Ah! You must be the foreign traveller I have heard about!
        My name is Anduin, and I am the mayor of this fair
        community.\"
                          """
                    raw_input()
                    print """
        \"On behalf of all the citizens I would like to welcome
        you to our village. Please accept this as a token of
        our friendship.\"
                          """
                    raw_input()
                    print "You receive a tasty looking cake from the mayor."
                    raw_input()
                    print """
        \"I hope you will be able to help us.\"
                          """
                    raw_input()
                    print "You exit the mayor\'s office."
                    self.have_cake = True
                    self.met_mayor = True
                    functions.ellipsis()
                    
                else:
                    print "I don't know what you mean. Choose one of the available options."

            while self.sign_read and self.met_mayor:
                next = raw_input("""
        What do you do?
        ---------------
        Talk to the solemn fairy.
        Open the large wooden door.
        Knock on the large wooden door.
        ? """)

                if "talk" in next or "Talk" in next or "fairy" in next or "Fairy" in next:
                        if not self.have_cake:
                            print "You approach the solemn fairy."
                            functions.ellipsis()
                            print """
        \"Bah!\", the solemn fairy grumbles. \"I\'m
        having a terrible day! Talk to me tomorrow.\"
                                  """
                            raw_input()
                        elif self.have_cake:
                            print "You approach the solemn fairy."
                            functions.ellipsis()
                            print """
        \"Bah!\", the solemn fairy grumbles. \"I\'m
        having a terrible day!\"
                                  """
                            raw_input()
                            print """
        \"Oh... What\'s that you have there? That cake
        looks quite tasty!
                                  """
                            while True:
                                next = raw_input("\"Can I have a slice?\" y/n ")
                                if "y" in next or "Y" in next:
                                    print "You hand him a slice of cake."
                                    self.fairy_has_cake = True
                                    functions.ellipsis()
                                    print """
        \"Oh! Thank you! I shall eat it heartily!\"
                                          """
                                    raw_input()
                                    print "The fairy hurries off with the cake leaving the archway open."
                                    while True:
                                        next = raw_input("Go through the archway? y/n ")
                                        if "y" in next or "Y" in next:
					    return('sign room')
                                        elif "n" in next or "N" in next:
                                            break
                                        else:
                                            print "You must enter either \'y\' or \'n\'."

                                elif "n" in next or "N" in next:
                                    print """
        \"Fine! But don't expect me to do any favors for you!\"
                                          """
                                    break
                                else:
                                    print "Type \"y\" or \"n\"." 
                                break
                            break
                elif "open" in next or "Open" in next or "door" in next or "Door" in next:
                    print "You open the door."
                    functions.ellipsis()
                    print "The mayor is snoozing comfortably at his desk."
                    raw_input()
                elif "knock" in next or "Knock" in next or "door" in next or "Door" in next:
                    print "You knock on the door."
                    functions.ellipsis()
                    print """
        \"Guh! Uh... yes! Hello!\", the voice behind the door says.
        \"I\'m, well, quite busy at the moment. Please come back later.\"
                          """
                    raw_input()
                else:
                    print "I don't know what you mean. Choose one of the available options."
            
        while self.fairy_has_cake:
            next = raw_input("""
        What do you do?
        ---------------
        Go through the archway.
        Open the large wooden door.
        Knock on the large wooden door.
        ? """)

            if "go" in next or "Go" in next  or "archway" in next or "Archway" in next:
                print "You go through the archway."
                functions.ellipsis()
                return('sign room')
            elif "open" in next or "Open":
                print "You open the door."
                functions.ellipsis()
                print "The mayor is snoozing comfortably at his desk."
                raw_input()
            elif "knock" in next or "Knock":
                print "You knock on the door..."
                functions.ellipsis()
                print """
        \"Guh! Uh... yes! Hello!\", the voice behind the door says.
        \"I\'m, well, quite busy at the moment. Please come back later.\"
                      """
                raw_input()
            else:
                print "I don't know what you mean. Choose one of the available options."

    def interact(self):
        if self.first_time:
            return(self.intro())
        elif not self.first_time:
            return(self.interact_2())
        else:
            print "FATAL ERROR!"
            exit(0)


class SignRoom(Room):
    def __init__(self):
	pass

    def entrance(self):
	print """
	You enter a small room whose walls are
	covered in ivy and tree roots.
	      """
	raw_input()
	return(self.plaque())

    def plaque(self):
	print """
	There is a large stone plaque on the wall.
	      """
	raw_input()

	print """

         ___       __       _^_    __
          __  \ __/  \     / | | /    \  \__
	++---\__  _/ \|----|  /---------\   _\ 
      \ \+------\ \--------|/------------| | \|
       | |      //                      /  | 
      / \ \  BEYOND RESIDE THE ELDERS, //| \ 
     |  ||\|                             |\ |
        ||    KEEPERS OF THE VILLAGE.    | ||
        ||    \                          |//
        ||     |  ONLY THE WISE          ||
        ||     /\__                _/    ||
        ||   /      MAY PASS.       \_ ___|
       //_                           <   _\__
     _/ _ \/>-----_/-----|\------------\__/
     _/ +\_/-------------| | /|----------++
                          \  / 

              """
	while True:
	    next = raw_input(
	   """
	What do you do?
	---------------
	Return to the previous room.
	Examine the stone plaque.
	Search this room.
	?  """)

	    if "return" in next or "Return" in next or "previous" in next or "Previous" in next:
	        return('fairy garden')
	    elif "examine" in next or "Examine" in next or "plaque" in next or "Plaque" in next:
	        return(self.examine())
	    elif "search" in next or "Search" in next or "this" in next or "This" in next:
	        self.search()
	    else:
	        print "\nI don't know what you mean. Choose one of the available options."	

    def examine(self):
	print "\nYou examine the stone plaque."
	functions.ellipsis()
	print """
	It seems that each letter on the stone 
	plaque is cut loose and can be taken out.
	      """
	raw_input()
	print """
	You brush away the leaves around the plaque
	and find four small slots in the wall.
	      """
	functions.ellipsis()
	
	print """       
		        ./ /
	__   _  ___     /  \ 
	 -\_ \---------|/^\ |-
	| ===\|===  ===  ==\| |
	| / \  / \  / \  / \  |
        ||   ||   ||   ||   | |
	| \ /  \ /  \ /  \ /  |
	| ===  ===  ===  ===  |
	 -------|\ /| --------
                \__ /
               """    
	
	ans = ''
	while ans != 'n' and ans != 'N':
            print "Try to guess the code? y/n "
	    ans = raw_input()
	    if ans == 'y' or ans == 'Y':
		return(self.wheel_of_fortune())
	    elif ans == 'n' or ans == 'N':
		return(self.plaque())
	    else:
		print "You must enter either 'y' or 'n'."
	


    def search(self):
	print "\nYou search the room."
	functions.ellipsis()
	print "\nYou find a roll of parchment hidden amongst the foliage.\n"
	print "It reads...\n"
	functions.ellipsis()
	print """
	   -----------------.
	-|'________________\ |
	   |               |
           |               |
           |  Bid it open  |
	   | and you shall |
	   |	 pass      |
	  |'	          /
	-|-------------- |`-
	 \---------------\/
	
	      """	
	raw_input()


    def wheel_of_fortune(self):
	insertions = [' ', ' ', ' ', ' ']
	removals = ['O', 'E', 'N', 'P']
	correct = 0
	print "\nType \"stop\" at any time to quit guessing."
	while correct < 4:
	    print """
	
         ___       __       _^_    __
          __  \ __/  \     / | | /    \  \__
	++---\__  _/ \|----|  /---------\   _\     		   
      \ \+------\ \--------|/------------| | \|                     _/ /
       | |      //                      /  |        __   _  ___     /  \ 
      / \ \  BEY%sND RESIDE THE ELDERS, //| \         -\_ \---------|/^\ |-
     |  ||\|                             |\ |       | ===\|===  ===  ==\| |
        ||    KEEPERS OF TH%s VILLAGE.    | ||       | / \  / \  / \  / \  |
        ||    \                          |//        || %s || %s || %s || %s | |
        ||     |  O%sLY THE WISE          ||         | \ /  \ /  \ /  \ /  |
        ||     /\__                _/    ||         | ===  ===  ===  ===  |
        ||   /      MAY %sASS.       \_ ___|          -------|\ /| --------
       //_                           <   _\__               \__ /
     _/ _ \/>-----_/-----|\------------\__/
     _/ +\_/-------------| | /|----------++
                          \  / 
		   """ % (removals[0], removals[1], insertions[0], insertions[1], insertions[2], insertions[3], removals[2], removals[3])

	    letter = raw_input("Which letter will you choose from the stone plaque? ")
	    if letter == 'stop':
		print "You stop guessing."
		return(self.plaque())
	    elif re.search(r"[A-Z]", letter):
		if letter == 'o' or letter == 'O':
		    if letter in insertions:
			print "You already tried that letter.\n"
		        raw_input()
		    else:
			print "It fits!"
			correct += 1
			insertions[0] = 'O'
			removals[0] = '#'
			raw_input()
		elif letter == 'p' or letter == 'P':
		    if letter in insertions:
			print "You already tried that letter.\n"
		        raw_input()
		    else:
			print "It fits!"
			correct += 1
			insertions[1] = 'P'
			removals[3] = '#'
			raw_input()
		elif letter == 'e' or letter == 'E':
		    if letter in insertions:
			print "You already tried that letter.\n"
		        raw_input()
		    else:
			print "It fits!"
			correct += 1
			insertions[2] = 'E'
			removals[1] = '#'
			raw_input()
		elif letter == 'n' or letter == 'N':
		    if letter in insertions:
			print "You already tried that letter.\n"
		        raw_input()
		    else:
			print "It fits!"
			correct += 1
			insertions[3] = 'N'
			removals[2] = '#'
			raw_input()
		else:
		    print "It doesn't seem to fit..."
		    raw_input()

	    else:
		print "You must enter a letter.\n"

	print """
         ___       __       _^_    __
          __  \ __/  \     / | | /    \  \__
	++---\__  _/ \|----|  /---------\   _\     		   
      \ \+------\ \--------|/------------| | \|                     _/ /
       | |      //                      /  |        __   _  ___     /  \ 
      / \ \  BEY%sND RESIDE THE ELDERS, //| \         -\_ \---------|/^\ |-
     |  ||\|                             |\ |       | ===\|===  ===  ==\| |
        ||    KEEPERS OF TH%s VILLAGE.    | ||       | / \  / \  / \  / \  |
        ||    \                          |//        || %s || %s || %s || %s | |
        ||     |  O%sLY THE WISE          ||         | \ /  \ /  \ /  \ /  |
        ||     /\__                _/    ||         | ===  ===  ===  ===  |
        ||   /      MAY %sASS.       \_ ___|          -------|\ /| --------
       //_                           <   _\__               \__ /
     _/ _ \/>-----_/-----|\------------\__/
     _/ +\_/-------------| | /|----------++
                          \  / 
		   """ % (removals[0], removals[1], insertions[0], insertions[1], insertions[2], insertions[3], removals[2], removals[3])

	functions.ellipsis()
	print """
	The room begins to shake. Dust that has clung to the stones and vines
	since time out of mind is thrown loose and soon the entire room is opaque
	with dust. 
	     """
	return('sakura tree')

    def interact(self):
	return self.entrance()

