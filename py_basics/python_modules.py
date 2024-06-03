print('hello world')
#first-- this prints the hello world.
def abc():
    print('this message is from abc function')
#third--then executes the 4th line.
def main():
    print('this message is from main function')
    abc()
#second-- this line executes because("in 3rd linewe use def abc() and again in 8th linewe write abc() ")
if __name__ == '__main__':
    main()
    print('now __name__ is %s' %__name__)
#forth-- 10th line is a conditional statement. thi tells that under what condition the main() method is executed.
