import mysql.connector as ms
import logging
from datetime import datetime
import sys

#connect to database
mydb = "connect database"

#creat cursor object
cursur = mydb.cursor()

#write query to create table and stored in variable
book = """CREATE TABLE IF NOT EXISTS Books_mng(
ind INT AUTO_INCREMENT UNIQUE,
Name VARCHAR(20),
Code VARCHAR(20) UNIQUE,
Status VARCHAR(20) DEFAULT 'AVl',
Borrow_date VARCHAR(20),
Return_date VARCHAR(20),
Pname VARCHAR(20),
Pno VARCHAR(15)
)"""

#excute the query by use the variable which contain query
try:
    cursur.execute(book)
except Exception as a:
    print(a)

#configure logging settings
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("library_log.log"),   # Save to file
        logging.StreamHandler(sys.stdout)         # Show in output window
    ]
)

#Create a class contain laibrary methods
class Laibrary:
    def __init__(self,mydb):
        self.mydb = mydb
        self.cursur = mydb.cursor()

    #A method for reorder index column after delete any row
    def reorder(self):
        self.cursur.execute("SET @count = 0;")
        self.cursur.execute("""UPDATE Books_mng SET ind = (@count := @count + 1) ORDER BY name""")
        self.cursur.execute("""ALTER TABLE Books_mng AUTO_INCREMENT = 1;""")
        self.mydb.commit()

    #A method for add books into database
    def Add_books(self):
        while True:
            try:
                try:
                    #get user input about book name and book code
                    book_name = input("Enter book name(for quit enter 0):")
                    if book_name == "0":
                        break
                    book_code = input("Enter book Code:")

                #catch exception if any error occur in input
                except Exception as e:
                    print("Enter both field")
                    logging.error("Error in input: %s", e)

                #write query to insert book detail and excute the query
                query = "INSERT INTO Books_mng(Name, Code) VALUES(%s,%s)"
                val = (book_name,book_code)
                self.cursur.execute(query,val)
                print("Book addended sussfully")
                logging.info("Book added: %s, %s", book_name, book_code)
                self.mydb.commit()

            except Exception as e:
                print("WAR:Something went wrong\n",e)
                logging.error("Error adding book: %s", e)

    #A method for delete books from database
    def Del_books(self):
          while True:
            try:
                try:
                    i = 0
                    #get user input about book name or book code
                    val = input("Enter book name or book code(for quit enter 0): ")
                    if val == "0":
                        break
                    if not val:
                        print("Please enter a valid book name or code.")
                        continue
                except Exception as e:
                    print("Error in input:", e)
                    continue

                #write query to check book is barrowed or not
                query = """SELECT * FROM Books_mng WHERE Status = 'BARROW' AND (Name = %s OR Code = %s)"""
                params = (val, val)
                self.cursur.execute(query, params)
                rows = cursur.fetchall()

                #if book is barrowed then show barrowed book details and break the loop
                if len(rows) > 0:
                    print("Book is barrowed, can't delete")
                    print("Barrowed book details:")
                    col_name = [desc[0] for desc in self.cursur.description]
                    print(" | ".join(col_name))
                    print("-"*70)
                    for row in rows:
                        print(row)
                    break

                #write query to delete book detail and excute the query 
                query = """SELECT Name, Code FROM Books_mng WHERE Status = 'AVl' AND (Name = %s OR Code = %s)"""
                params = (val, val)
                self.cursur.execute(query, params)
                rows = cursur.fetchall()

                #check how many books found with same name or code
                if len(rows) == 0:
                    print("Not found")
                    break
                else:
                    for row in rows:
                        i += 1
                        print(row)

                #if only one book found then delete directly otherwise ask for book code to delete        
                if i == 1:
                    qr = """DELETE FROM Books_mng WHERE Name = %s OR Code = %s"""
                    par = (val,val)
                    self.cursur.execute(qr,par)
                    print("Book deleted sussfully")
                else:
                    print("Found many books\n Enter book code")
                    cd = input("Enter book code:")
                    qr = """DELETE FROM Books_mng WHERE Code = %s"""
                    self.cursur.execute(qr,(cd,))
                    print("Book deleted sussfully")
                    logging.info("Book deleted with code: %s", cd)
                self.mydb.commit()

                #call reorder method
                self.reorder()
                
            except Exception as e:
                print("WAR: Something went wrong\n", e)
                logging.error("Error deleting book: %s", e)

    #A method for show all books detail
    def show(self):
        self.cursur.execute("SELECT * FROM Books_mng")
        rows = self.cursur.fetchall()
        col_name = [desc[0] for desc in self.cursur.description]
        print(" | ".join(col_name))
        print("-"*70)
        for row in rows:
            print(row)
        logging.info("Displayed all books detail")

    #A method for check book status
    def book_status(self):
        while True:
            try:
                i = 0
                book_code = input("Enter book code to check status(for quit enter 0):")
                if book_code == "0":
                    break
                qr = """SELECT * FROM Books_mng WHERE Code = %s"""
                self.cursur.execute(qr,(book_code,))
                status = self.cursur.fetchall()

                if len(status) == 0:
                    print("Book not found")
                    break
                col_name = [desc[0] for desc in self.cursur.description]
                print(" | ".join(col_name))
                print("-"*70)
                for row in status:
                    print(row)
            except Exception as e:
                print("WAR:",e)
                logging.error("Error checking book status: %s", e)
    
    #A method for update books detail future use
    def Update(self):
        pass

#Create a class contain books methods
class Books:
    def __init__(self,mydb):
        self.mydb = mydb
        self.cursur = mydb.cursor()

    #A method for barrow books
    def barrow(self):
        today = datetime.now().strftime("%d-%m-%Y")
        try:
            print("===ISSUE BOOKS===")
            print("Enter all the information")

            #get user input about there books which they want barrow
            Book_name = input("Enter book name:")
            Book_code = input("Enter book code:")
            name = input("Enter your name:")
            num = input("Enter your phone number:")
            # date = input("Enter date:")
            try:
                if len(num) == 10 or len(num) == 12:
                    print("Enter valid phone number")
                    return
            except Exception as e:
                print("Error in phone number:", e)

            #write qurey and values stored in variable
            qr = """UPDATE  Books_mng SET Status = "BARROW", Borrow_date = %s, Pname = %s, Pno = %s WHERE Name = %s AND Code = %s"""
            val = (today,name,num,Book_name,Book_code)
            print("Sussfully query passed")

            #excute query and commit to database
            self.cursur.execute(qr,val)
            self.mydb.commit()

            #print statment book barrowed sussfully to show user
            print("sussfully Book barrowed ")
            logging.info("Book barrowed: %s by %s", Book_name, name)
        except Exception as e:
            logging.error("Error barrowing book: %s", e,)
            print("WAR:",e)

    #A method for return books
    def Retrun(self):
        today = datetime.now().strftime("%d-%m-%Y")
        try:
            print("Return books")

            #get user input about there books which they want return
            Book_name = input("Enter book name:")
            Book_code = input("Enter book code:")
            # da = input("Enter date:")

            #write qurey and values stored in variable
            qr = """UPDATE Books_mng SET Status = "AVL",Borrow_date = "None", Return_date = %s WHERE Name = %s AND Code = %s"""
            val = (today,Book_name,Book_code)

            #excute query and commit to database
            self.cursur.execute(qr,val)
            self.mydb.commit()

            print("Book return sussfuly")
            logging.info("Book returned: %s", Book_name)
        except Exception as e:
            print("WAR:",e)
            logging.error("Error returning book: %s", e)

    #A method for see available books
    def See(self):
        try:
            print("Available books are:")

            #write query to select available books
            qr = """SELECT Name,Code From Books_mng WHERE Status = "AVL" """
            self.cursur.execute(qr)

            #fetch all available books
            rows = cursur.fetchall()

            print("\n","="*19)
            print("  Name    Code")
            print("="*20)

            #print all available books
            for row in rows:
                print(row)

            #show log information
            logging.info("Displayed available books")

        except Exception as e:
            print("WAR:",e)
            logging.error("Error displaying available books: %s", e)

#Create object of both classes
B1 = Laibrary(mydb)
B2 = Books(mydb)

while True:
    try:
        #design home page menu
        print("\n==WELCOME TO LAIBRARY==")
        print("HOME PAGE")
        print("Update Laibrary-->1")
        print("Enter to laibrary-->2")
        print("Exit -->0")
        choice = int(input("Enter your choice:"))

        #staff login section
        if choice == 1:
            print("\nOnly for staff")
            user = input("Enter password:")

            #check password for login
            if user == "1234":
                print("-login sussfully-")
                print("===WELCOME TO MY LAIBRARY===")
                while True:
                    try:
                        #design staff menu
                        print("\n==MENU==")
                        print("Add books-->1")
                        print("Delete books--->2")
                        print("Show all books detail-->3")
                        print("Check book status-->4")
                        print("Back to home page-->0")
                        choice = int(input("Enter your choice:"))
                        if choice == 1:
                            B1.Add_books()
                        elif choice == 2:
                            B1.Del_books()
                        elif choice == 3:
                            B1.show()
                        elif choice == 4:
                            B1.book_status()
                        else:
                            break
                    except Exception as e:
                        print("WAR:",e)
                        logging.error("Error in staff menu: %s", e)
            else:
                print("Password is incorect")
        
        #User section
        elif choice == 2:
            print("\nWELCOME USER")
            while True:
                try:
                    #design user menu
                    print("\nBarrow books-->1")
                    print("Return boks-->2")
                    print("see books-->3")
                    print("Back to home page-->0")
                    ch = int(input("Enter your choice:"))
                    if ch == 1:
                        B2.barrow()
                    elif ch == 2:
                        B2.Retrun()
                    elif ch == 3:
                        B2.See()
                    else:
                        break
                except Exception as e:
                    print("WAR:",e)
                    logging.error("Error in user menu: %s", e) 
        else:
            break
    except Exception as e:
        print("WAR:",e)
        logging.error("Error in home page menu: %s", e)
