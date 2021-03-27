Lister = []
AddFirst = True
def Searcher(Lister):
    search = int(input('Enter the number you want to search'))
    if search in Lister:
        print ('The number is here, and its at', Lister[search])
    else:
        print('Number not found, goodbye')

while AddFirst is True:
    user_input = input("Enter Number, type End to end: ")
    try:
        val = int(user_input)
        Lister.append(val)
    except ValueError:
        try:
            if user_input == 'End':
                Lister.sort()
                print('List is', Lister)
                AddFirst = False
                Searcher(Lister)
        except ValueError:
            print("Invalid Input, try again")