class FairyRoom(Room):
    def __init__(self):
        self.name = 'Fairy Room'

    def show_key(self):
        global your_name
        print "\nYou show her the key."
        ellipsis()
        print """
        \"What luck we have today, all these fairies and I!
        That's it, that's the one! Now I shall tell you
        our tale. So full of grief and of sorrow and utter
        misfortune it is.\"
        """
        raw_input()
        
        print """
        Many ages ago we fairies ruled both earth and sky in the land above.
        The garden you see before you in which we now reside is a mere
        fraction of the empire we once held.
        """
        raw_input()
        print """
        All lived in peace under a just ruler, the Great Fairy Daphnis, who
        brought us magnificent prosperity and great joy. 
        The rivers flowed with water sweet and clear.
        The trees swayed in breezes cool and slow.
        All the world rejoiced in His justice and piety.
        """
        raw_input()
        print """
        He built grand temples for the gods, great stadiums for the people, 
        and glorious palaces for the gentry.
        """
        raw_input()
        print """
        For the poor He donated food, for their animals He donated fodder;
        during droughts He donated water 
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
        """ % your_name
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
                current_room = fairy_garden
            elif "n" in next or "N" in next:
                lose("You decided to not help the fairies. Shame on you!")
            else:
                print "You must enter either \'y\' or \'n\'."
            
    def first_fairy(self):
        global current_room, start_room, fairy_key_found, first_fairy_room
        first_fairy_room = False
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
        brightly.You realize that there are fairies all around you hiding
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
	while current_room == fairy_room:
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
            
                while current_room == fairy_room:
                    next2 = raw_input("""
        \"Have you perchance come across a small emerald 
        key in the course of your travels?\" 
        y/n """)
                
                    if next2 == "y" and fairy_key_found:
                        self.show_key()
                    elif next2 == "y" and not fairy_key_found:
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
                        current_room = start_room
                    elif next2 == "n":
                        print """
        \"I see. I see. We welcome you to stay, yet no 
        farther may you go without the emerald key that 
        we seek.\"
                        """
                        raw_input()
                        print "You return to the previous room."
                        current_room = start_room
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
                current_room = start_room
            
            else:
                print "Type \"y\" or \"n\"."
                            
    def second_fairy(self):
        global current_room, start_room, fairy_key_found
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
        while current_room == fairy_room:
            next = raw_input("\"Do you have the small emerald key?\" y/n ")
            if next == "y" and fairy_key_found:
                self.show_key()
            elif next == "y" and not fairy_key_found:
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
                current_room = start_room
            elif next == "n":
                print """
        \"I see. I see. We welcome you to stay, yet no 
        farther may you go without the emerald key that 
        we seek.\"
                """
                raw_input()
                print "You return to the previous room."
                current_room = start_room
            else:
                print "Type \"y\" or \"n\"."

    def interact(self):
        global first_fairy_room
            
        if first_fairy_room:
            self.first_fairy()
        elif not first_fairy_room:
            self.second_fairy()
	else:
            print "FATAL ERROR!"
            exit(0)
