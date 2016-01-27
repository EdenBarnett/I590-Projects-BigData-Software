import sys
 
n =int(sys.argv[1])                           
NUMBERS=range(1,n+1)

def fizzbuzz():
    
    for i in NUMBERS:

        if (i % 2 == 0) and (i % 3 == 0):
           print ("fizzbuzz")
        elif i % 2 == 0:
            print ("fizz")
        elif i % 3 == 0:
            print ("buzz")
        else:
            print (i)

if __name__=='__main__':
     fizzbuzz()
