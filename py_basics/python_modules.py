print('hello world') # this prints the hello world.
def abc():
    print('this message is from abc function') #this defines that function named abc(), when called and and print's the
     #'this message is from abc function'

def main():
    print('this message is from main function') 
    abc() # this defines that function named main(), and print's the 'this message is from main function',calls the main() 
    #funtion

if __name__ == '__main__': #this is a conditinal statement. it checks if the script is running directly, if that is running
    #directly, __name__ is set to '__main__' so the condition evaluates True or False 
    main() # since the condition is True it prints "this message is from abc function."
    print('now __name__ is %s' %__name__) # this prints the current value.
