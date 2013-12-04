import re

class SignRoom(object):

    def __init__(self):
	pass

    def interact(self):
	print """
	You enter a small room whose walls are
	covered in ivy and tree roots.
	      """
	raw_input()

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
	        self.examine()
	    elif "search" in next or "Search" in next or "this" in next or "This" in next:
	        self.search()
	    else:
	        print "\nI don't know what you mean. Choose one of the available options."	

#-----------FUNCTIONS------------------------------------------------FUNCTIONS-------------------------------------

    def examine(self):
	print "\nYou examine the stone plaque."
	raw_input() # ellipsis()
	print """
	It seems that each letter on the stone 
	plaque is cut loose and can be taken out.
	      """
	raw_input()
	print """
	You brush away the leaves around the plaque
	and find four small slots in the wall.
	      """
	raw_input() # ellipsis
	
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
	self.wheel_of_fortune()

    def search(self):
	print "\nYou search the room."
	raw_input() # ellipsis()
	print "\nYou find a roll of parchment hidden amongst the foliage.\n"
	print "It reads...\n"
	raw_input() # ellipsis()
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
	    if re.search(r"[A-Z]", letter):
		if letter == 'o' or letter == 'O':
		    if letter in insertions:
			print "You already guessed that letter.\n"
		        raw_input()
		    else:
			print "Correct!"
			correct += 1
			insertions[0] = 'O'
			removals[0] = '#'
			raw_input()
		elif letter == 'p' or letter == 'P':
		    if letter in insertions:
			print "You already guessed that letter.\n"
		        raw_input()
		    else:
			print "Correct!"
			correct += 1
			insertions[1] = 'P'
			removals[3] = '#'
			raw_input()
		elif letter == 'e' or letter == 'E':
		    if letter in insertions:
			print "You already guessed that letter.\n"
		        raw_input()
		    else:
			print "Correct!"
			correct += 1
			insertions[2] = 'E'
			removals[1] = '#'
			raw_input()
		elif letter == 'n' or letter == 'N':
		    if letter in insertions:
			print "You already guessed that letter.\n"
		        raw_input()
		    else:
			print "Correct!"
			correct += 1
			insertions[3] = 'N'
			removals[2] = '#'
			raw_input()
		else:
		    print "Incorrect!"
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

signroom = SignRoom()
signroom.interact()
