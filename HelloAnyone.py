# You can run this code by typing on the command line:
#   python HelloAnyone.py Catherine

import sys 

def main(argv):

    if(len(argv) != 1):
        print "Goodbye"
    else:
        name = argv[0]
        print "Hello, " + name + "!"

if __name__ == "__main__":
   main(sys.argv[1:])
