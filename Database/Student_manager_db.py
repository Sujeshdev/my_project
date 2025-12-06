import mysql.connector as myconn

mydb = myconn.connect(host = "localhost",user = "root",password = "narutoonepiece@2025",database = "learning_db")

class Student:
    def query(self):
        cursur.execute("SELECT std.reg,std.name,std_marks.mark1,std_marks.mark2,std_marks.mark3,std_marks.mark4,std_marks.mark5,std_marks.mark6,std_marks.avg,std_marks.grade FROM std LEFT JOIN std_marks ON std.reg = std_marks.reg")
        self.rows = cursur.fetchall()
        return self.rows


    def grade(self,mark1,mark2,mark3,mark4,mark5,mark6):
        total = mark1+mark2+mark3+mark4+mark5+mark6
        self.avg = total/6
        if self.avg >= 90:
            self.Grade = "A"
        elif self.avg >= 80:
            self.Grade = "B"
        elif self.avg >= 70:
            self.Grade= "C"
        elif self.avg >= 60:
            self.Grade = "D"
        else:
            self.Grade = "E"
        return self.avg,self.Grade


    def Add_student(self):
        while True:
            print("\nSTUDENT MENU")
            print("Add student-->1")
            print("Add student mark--->2")
            print("Back to Main Menu-->0")
            try:
                choice = int(input("Enter your choice:"))
            except Exception as e:
                print("WAR:Enetr your choice\n",e)
            if choice == 1:
                try:
                    reg = input("Enter register number:")
                    name = input("Enter student name:")
                    try:
                        cursur.execute("INSERT INTO std (reg, name) VALUES(%s,%s)",(reg, name))
                        print(reg,name,"Addend succfully")
                        mydb.commit()
                    except:
                        print("WAR:Not working")
                except Exception as e:
                    print("WAR:Not inserted\n",e)
            elif choice == 2:
                    try:
                        reg = input("Enter register number:")
                    except Exception as e:
                        print("WAR:Enter register number\n",e)
                    found = False
                    cursur.execute("SELECT reg FROM std")
                    rows = cursur.fetchall()
                    for i in rows:
                        if reg in i:
                            found = True
                            try:
                                mark1 = float(input("Enter mark1:"))
                                mark2 = float(input("Enter mark2:"))
                                mark3 = float(input("Enter mark3:"))
                                mark4 = float(input("Enter mark4:"))
                                mark5 = float(input("Enter mark5:"))
                                mark6 = float(input("Enter mark6:"))
                                self.grade(mark1,mark2,mark3,mark4,mark5,mark6)
                                avg = round(self.avg,2)
                                char = self.Grade
                                insert_qr = """INSERT INTO std_marks(reg,mark1,mark2,mark3,mark4,mark5,mark6,avg,grade) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                                val = (reg,mark1,mark2,mark3,mark4,mark5,mark6,avg,char)
                                cursur.execute(insert_qr,val)
                                print("Marks inserted sussfully")
                                mydb.commit()
                            except Exception as e:
                                print("WAR:Enter all marks\n",e)
                    if found == False:
                        print("Regiter number not found")

            else:
                return
        
    def show(self):
        print("STUDENT DISPALY")
        while True:
            try:
                print("\nShow All Students-->1")
                print("Show Student Record --->2")
                print("Back to Main Menu--> 0")
                choice = int(input("Enter your choice:"))
                if choice == 1:
                    try:
                        print("===STUDENT DETAIL===")
                        cursur.execute("SELECT std.reg,std.name,std_marks.mark1,std_marks.mark2,std_marks.mark3,std_marks.mark4,std_marks.mark5,std_marks.mark6,std_marks.avg,std_marks.grade FROM std LEFT JOIN std_marks ON std.reg = std_marks.reg")
                        rows = cursur.fetchall()
                        col_name = [desc[0] for desc in cursur.description]
                        # for i in cursur.description:
                        print(" | ".join(col_name))
                        print("-"*70)

                        for i in rows:
                            print(i)
                    except:
                        print("WAR:Not found")
                elif choice == 2:
                    print("===STUDENT DETAIL===")
                    try:
                        reg = input("Enter student register number:")
                        query = "SELECT std.reg,std.name,std_marks.mark1,std_marks.mark2,std_marks.mark3,std_marks.mark4,std_marks.mark5,std_marks.mark6,std_marks.avg,std_marks.grade FROM std LEFT JOIN std_marks ON std.reg = std_marks.reg"
                        found = False
                        cursur.execute(query)
                        rows = cursur.fetchall()
                        col_name = [desc[0] for desc in cursur.description]
                        print(" | ".join(col_name))
                        print("-"*70)
                        for i in rows:
                            if reg in i:
                                found = True
                                print(i)
                        if found == False:
                            print("Register number not found")
                                
                    except Exception as e:
                        print("WAR:Enter valid register\n",e)
                elif choice == 0:
                    return
            except Exception as e:
                print("WAR:Enter valid choice\n",e)
            
    def delete(self):
        try:
            found = False
            query = """DELETE std, std_marks FROM std JOIN std_marks ON std.reg = std_marks.reg WHERE std.reg = %s"""
            reg = input("Enter student register number:")
            self.query()
            for row in cursur:
                if reg in row:
                    found = True
                    choice = input("Conferm you want delete student detail(yes or no):")
                    if choice.lower() == "yes":
                        cursur.execute(query,(reg,))
                        mydb.commit()
                        print("Student deatil succesfully delted")
                    else:
                        print("student detail not delted")
            if found == False:
                print("Register not found")
        except:
            print("WAR:Something went wrong \n Try again later")    

    def std_update(self):
        print("Change Student Name --->1")
        print("Update Student Marks--->2")
        choice = int(input("Enter your choice:"))
        if choice == 1:
            try:
                found = False
                reg = input("Enter student register number:")
                new_name = input("new name:")
                query = "UPDATE std SET name = %s WHERE reg= %s "
                cursur.execute(query,(new_name,reg,))
                mydb.commit()

            except Exception as e:
                print("WAR:Something went wrong \n Try again later\n",e)
        elif choice == 2:
            try:
                found = False
                reg = input("Enter student register number:")
                self.query()
                for row in self.rows:
                    if reg in row:
                        found = True
                        sub = input("Enter subject:")
                        new_mark = float(input("Enter new mark:"))
                        query = f"UPDATE std_marks SET {sub} = %s WHERE reg = %s"
                        cursur.execute(query,(new_mark,reg,))
                        mydb.commit()
                        print(sub," updated sussfully")
                        break
                if found == False:
                    print("Invalid register number")
                
                cursur.execute("SELECT mark1,mark2,mark3,mark4,mark5,mark6 FROM std_marks WHERE reg = %s ",(reg,))
                marks = cursur.fetchone()
                avg = round(sum(marks) / 6,2)
                print(avg)
                if avg >= 90:
                    Grade = "A"
                elif avg >= 80:
                    Grade = "B"
                elif avg >= 70:
                    Grade = "C"
                elif avg >= 60:
                    Grade = "D"
                else:
                    Grade = "E"
                 
                query2 = "UPDATE std_marks SET avg = %s, grade = %s WHERE reg = %s"
                cursur.execute(query2,(avg,Grade,reg))
                mydb.commit()
                print("Marks updated sucfully")
     
                
            except Exception as e:
                print("WAR:Something went wrong \n Try again later \n",e)



cursur = mydb.cursor()

cursur.execute("CREATE DATABASE IF NOT EXISTS learning_db")

table1 = """
CREATE TABLE IF NOT EXISTS std (
reg VARCHAR(20) PRIMARY KEY ,
name VARCHAR(20)
)
"""

cursur.execute(table1)
# mydb.commit()

table2 = """
CREATE TABLE IF NOT EXISTS std_marks(
reg varchar(20) PRIMARY KEY ,
mark1 FLOAT,
mark2 FLOAT,
mark3 FLOAT,
mark4 FLOAT,
mark5 FLOAT,
mark6 FLOAT,
avg FLOAT,
grade VARCHAR(5)
)
"""
cursur.execute(table2)
mydb.commit()
s1 = Student()
print("==MAIN MENU==")
while True:
    print("\n====MENU====")
    print("Add Student-->1")
    print("Show Student Details--->2")
    print("Delete Student-->3")
    print("Update Student-->4")
    print("Exit Application-->0")
    choice = int(input("Enter your choice:"))

    if choice == 1:
        s1.Add_student()
    elif choice == 2:
        s1.show()
    elif choice == 3:
        s1.delete()
    elif choice == 4:
        s1.std_update()
    else:
        break

