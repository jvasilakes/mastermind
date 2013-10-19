import time

class Room(object):
    def __init__(self, name):
        self.name = name

class FairyGarden(Room):
    def __init__(self):
        self.name = 'Fairy Garden'
        self.first_time = True
        self.sign_read = False
        self.have_cake = False
        self.fairy_has_cake = False
        
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
        self.interact_2()

    def interact_2(self):
        global current_room
        print "You are in the fairy garden."
        print "To your left is a very solemn looking fairy guarding a dark archway."
        print "To your right is a large wooden door with a sign next to it."

        while self.fairy_has_cake == False:
            while self.sign_read == False:
                next = raw_input("""
            What do you do?
            ---------------
            Talk to the solemn fairy.
            Open the large wooden door.
            Read the sign.
                ? """)
                if "talk" in next or "Talk" in next or "fairy" in next or "Fairy" in next:
                    if self.have_cake == False:
                        print "You approach the solemn fairy."
                        # ellipsis()
                        print """
                \"Bah!\", the solemn fairy grumbles. \"I\'m
                having a terrible day! Talk to me tomorrow.\"
                              """
                        raw_input()       
                elif "open" in next or "Open" in next or "door" in next or "Door" in next:
                    self.sign_read = True
                    print "You open the large wooden door."
                    time.sleep(1) # ellipsis()
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
                    time.sleep(1) # ellipsis()
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


            while self.sign_read == True:
                next = raw_input("""
            What do you do?
            ---------------
            Talk to the solemn fairy.
            Open the large wooden door.
            Knock on the large wooden door.
            ? """)
                if "talk" in next or "Talk" in next or "fairy" in next or "Fairy" in next:
                    if self.have_cake == False:
                        print "You approach the solemn fairy."
                        # ellipsis()
                        print """
            \"Bah!\", the solemn fairy grumbles. \"I\'m
            having a terrible day! Talk to me tomorrow.\"
                              """
                        raw_input()
                    elif self.have_cake == True:
                        print "You approach the solemn fairy."
                        # ellipsis()
                        print """
            \"Bah!\", the solemn fairy grumbles. \"I\'m
            having a terrible day!\"
                              """
                        raw_input()
                        print """
            \"Oh... What\'s that you have there? That cake
            looks quite tasty!
                              """
                        while current_room == fairy_garden:
                            next = raw_input("\"Would you mind letting me have a slice?\" y/n ")
                            if "y" in next or "Y" in next:
                                print "You hand him a slice of cake."
                                self.fairy_has_cake = True
                                time.sleep(1) # ellipsis()
                                print """
            \"Oh! Thank you! I shall eat it heartily!\"
                                      """
                                raw_input()
                                print "The fairy hurries off with the cake leaving the archway open."
                                next = raw_input("Go through the archway? y/n ")
                                if "y" in next or "Y" in next:
                                    print "THANKS!!!"
                                    current_room = sign_room
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
                    time.sleep(1) # ellipsis()
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
                    print "You knock on the door..."
                    time.sleep(1) # ellipsis()
                    print """
            \"Guh! Uh... yes! Hello!\", the voice behind the door says.
            \"Please do come in!\"
                          """
                    raw_input()
                    print "You open the door."
                    time.sleep(1) # ellipsis()
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
                    time.sleep(1) # ellipsis()
                    
                else:
                    print "I don't know what you mean. Choose one of the available options."
            
        while self.fairy_has_cake == True:
            next = raw_input("""
            What do you do?
            ---------------
            Go through the archway.
            Open the large wooden door.
            Knock on the large wooden door.
            ? """)

            if "go" in next or "Go" in next  or "archway" in next or "Archway" in next:
                print "You go through the archway."
                # ellipsis()
                current_room = sign_room
            elif "open" in next or "Open" in next or "door" in next or "Door" in next:
                print "You open the door."
                time.sleep(1)
                print "The mayor is snoozing comfortably at his desk."
                raw_input()
            elif "knock" in next or "Knock" in next or "door" in next or "Door" in next:
                print "You knock on the door..."
                time.sleep(1)
                print """
            \"Guh! Uh... yes! Hello!\", the voice behind the door says.
            \"I\'m, well, quite busy at the moment. Please come back later.\"
                      """
                raw_input()
            else:
                print "I don't know what you mean. Choose one of the available options."

    def interact(self):
        if self.first_time == True:
            self.intro()
        elif self.first_time == False:
            self.interact_2()
        else:
            print "FATAL ERROR!"
            exit(0)

fairy_garden = FairyGarden()
global current_room
current_room = fairy_garden

fairy_garden.interact()

