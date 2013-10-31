import random
import re
from sys import exit

class Code():
    def shufflize(self):
        repository = ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', \
        'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D', 'E', 'E', 'E', \
        'E', 'F', 'F', 'F', 'F']
        random.shuffle(repository)
	return repository

    def get_secret_code(self, repository):
        secret_code = repository[1:5]
        return secret_code

    def get_guess_code(self):
        guess_code = []

        index = 0
        print "Enter a sequence of uppercase letters, A - F"
        while index < 4: 
            value = raw_input("%s: " % index)
            if re.search(r"[ABCDEF]", value):
                guess_code.append(value)
                index += 1 
            else:
                print "Input must be a capital letter A - F."

        print "Your guess: %s" % guess_code
        return guess_code

    def test_code(self, secret_code, guess_code):
        n = 0
	perfect = 0
	imperfect = 0

        for n in range(len(secret_code)):
            if guess_code[n] == secret_code[n]:
                perfect += 1
                guess_code[n] = 'Y'
                secret_code[n] = 'X'
            else:
                pass
            n += 1
        
        for n in range(len(secret_code)):
	    for i in range(len(secret_code)):
                if guess_code[n] == secret_code[i]:
                    imperfect += 1
		    secret_code[i] = 'X'
                else:
                    pass
		i += 1
            n += 1

        print "Perfect: %d" % perfect
        print "Imperfect: %d" % imperfect
        
	return perfect 

def main():
    code = Code()
    repository = code.shufflize()
    for n in xrange(10):
        secret_code = code.get_secret_code(repository)
	guess_code = code.get_guess_code()
	perfect = code.test_code(secret_code, guess_code)	
	if perfect == 4:
	    secret_code = code.get_secret_code(repository)
	    print "Secret code: %s" % secret_code
	    print "You WIN!"
	    exit(0)
	else:
	    pass
    secret_code = code.get_secret_code(repository)
    print secret_code
    print "YOU'RE A LOOOOOOOOOOSSSSEEERRRR!"

if __name__ == '__main__':
    main()
