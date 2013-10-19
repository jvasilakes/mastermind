class SignRoom(object):

    def __init__(self):
	pass

#---------------INTERACT----------------------------------------------INTERACT----------------------------

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
	        return(self.examine())
	    elif "search" in next or "Search" in next or "this" in next or "This" in next:
	        print "self.search()"
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
		        _/ /
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

	def wheel_of_fortune(self):
	    correct = 0
	    while correct == 0:
	        print """
	
         ___       __       _^_    __
          __  \ __/  \     / | | /    \  \__
	++---\__  _/ \|----|  /---------\   _\     		   
      \ \+------\ \--------|/------------| | \|                     _/ /
       | |      //                      /  |        __   _  ___     /  \ 
      / \ \  BEYOND RESIDE THE ELDERS, //| \         -\_ \---------|/^\ |-
     |  ||\|                             |\ |       | ===\|===  ===  ==\| |
        ||    KEEPERS OF THE VILLAGE.    | ||       | / \  / \  / \  / \  |
        ||    \                          |//        ||   ||   ||   ||   | |
        ||     |  ONLY THE WISE          ||         | \ /  \ /  \ /  \ /  |
        ||     /\__                _/    ||         | ===  ===  ===  ===  |
        ||   /      MAY PASS.       \_ ___|          -------|\ /| --------
       //_                           <   _\__               \__ /
     _/ _ \/>-----_/-----|\------------\__/
     _/ +\_/-------------| | /|----------++
                          \  / 
		   """

		letter = raw_input("Which letter will you choose from the stone plaque? ")
		if re.search(r"[A-Z]" | "[a-z]", letter):
		    if letter == 'o' or letter == 'O':
			print "Correct!"
		        correct += 1
		    elif letter == 'p' or letter == 'P':
			print "Correct!"
		        correct += 1
		    elif letter == 'e' or letter == 'E':
			print "Correct!"
		        correct += 1
		    elif letter == 'n' or letter == 'N':
			print "Correct!"
		        correct += 1
		    else:
			print "Incorrect!"

signroom = SignRoom()
signroom.interact()
