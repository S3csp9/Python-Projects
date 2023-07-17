list_of_all_books = {"TOOLS OF TITAN":"NEWTON LIBRARY",
                     "RICH DAD, POOR DAD":"NEWTON LIBRARY",
                     "START WITH WHY":"ELON LIBRARY",
                     "HOW TO WIN FRIENDS AND INFLUENCE PEOPLE":"JONAS LIBRARY",
                     "THINK & GROW RICH":"ELON LIBRARY",
                     "THE 7 HABITS OF HIGHLY EFFECTIVE PEOPLE":"ELON LIBRARY",
                     "THE 4-HOUR WORK WEEK":"JONAS LIBRARY",
                     "THINKING FAST AND SLOW":"NEWTON LIBRARY",
                     "MEN'S ARE FROM MARS AND WOMEN'S ARE FROM VENUS":"ELON LIBRARY",
                     "THE LEAN START UP":"JONAS LIBRARY",
                     "THE POWER OF POSITIVE THINKING":"ELON LIBRARY",
                     "THE MAGIC OF THINKING BIG":"NEWTON LIBRARY",
                     "THE ALCHEMIST":"JONAS LIBRARY",
                     "IKIGAI":"JONAS LIBRARY",
                     "THE SUBTLE ART OF NOT GIVING A F*CK":"NEWTON LIBRARY",
                     "MEN'S SEARCH FOR MEANING":"MARK LIBRARY",
                     "POWER OF SUBCONSCIOUS MIND":"MARK LIBRARY",
                     "THE GREATEST SALESMAN IN THE WORLD":"NEWTON LIBRARY",
                     "HOW TO STOP WORRYING AND START LIVING":"MARK LIBRARY",
                     "THINK LIKE DA VINCI":"MARK LIBRARY"}
avaiable_books = list_of_all_books.copy()
borrowed_books = {}

class Library:
    def __init__(self, listofbooks, library_name):
        self.listofbooks = listofbooks
        self.library_name = library_name
    
    def librarydetails(self):
        return f"The Book is {self.listofbooks} Available in {self.library_name}.\n"
    
    def all_books():
        print("\nThe list of all Books in Library:-\n")
        for i,j in enumerate(list_of_all_books):
                print(i+1, '-' ,j)
    
    def available_book():
        print("\nThe list of Available Books in Library:-\n")
        for books, libraryname in avaiable_books:
                print(f"The Book - {books},\nAvailable at - {libraryname}")
    
    def borrow_books_list():
        print("\nThe list of Borrowed Books in Library:-\n")
        if len(borrowed_books)!=0:
            for books, userid in borrowed_books:
                print(f"The Book - {books},\nIssued to - {userid}")
        else:
            print('No books are issued')
            
    def borrow_books():
        borrow_book = input("Enter the Name of the Book you want to Borrow - ").upper()
        user_id = input("Enter your Name - ").upper()
        borrowed_books.update({borrow_book:user_id})
        avaiable_books.pop(borrow_book)
        print("You have 15 days to Return the Book")
    
    def donate_books():
        donate_book = input("Enter the Name of the Book you want to Borrow - ").upper()
        print("JONAS LIBRARY \nNEWTON LIBRARY \nELON LIBRARY \nMARK LIBRARY")
        libraryname = input("Enter the Library Name - ").upper()
        list_of_all_books.update({donate_book:libraryname})
        print(borrowed_books)
        print("Thank you so much for Donating the Book")
            
    def return_books():
        return_book = input("Enter the Name of the Book you want to Borrow - ").upper()
        libraryname = input("Enter your UserID - ").upper()
        avaiable_books.update({return_book:libraryname})
        borrowed_books.pop(return_book)
        print(borrowed_books)
        print("Thank you for Returning the Book")
    
    
if __name__ == '__main__':
    while(True):
        print("!! Welcome to our Library Management Program !!")
        print("What do you want to Do?")
        print("1. Display All Books\n"
              "2. Display Available Books\n"
              "3. Display Borrowed Book List\n"
              "4. Borrow Book\n"
              "5. Donate Book\n"
              "6. Return Book\n"
              "7. Quit")
        inp =  int(input("Type Here - "))
        if inp == 1:
            Library.all_books()
        elif inp == 2:
            Library.available_book()
        elif inp == 3:
            Library.borrow_books_list()
        elif inp == 4:
            Library.borrow_books()
        elif inp == 5:
            Library.donate_books()
        elif inp == 6:
            Library.return_books()
        elif inp == 7:
            print("Thank you using our Program")
            break
        else:
            print("Wrong Input")