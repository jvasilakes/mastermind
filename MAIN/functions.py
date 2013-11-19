import time
import sys

def lose(reason):
    print reason
    print
    print "Thanks for playing!"
    play_again = raw_input("Try again? y/n ")
    if play_again == "y":
        main()
    elif play_again == "n":
        print "Goodbye!"
        exit(0)
    else:
        print "I'll assume you don't want to play again. Goodbye!"
        exit(0)

def ellipsis():
    time.sleep(0.5)
    sys.stdout.write(".")
    sys.stdout.flush()
    time.sleep(0.5)
    sys.stdout.write(".")
    sys.stdout.flush()
    time.sleep(0.5)
    sys.stdout.write(".")
    sys.stdout.flush()
    time.sleep(0.5)
    print
