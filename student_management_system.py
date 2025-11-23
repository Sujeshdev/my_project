import random

class Student:
    def grade(self,mark1,mark2,mark3,mark4,mark5,mark6):
        self.total = mark1 + mark2 + mark3 + mark4 + mark5 + mark6
        self.avg = round(self.total / 6,2)
        # self.grade = None
        if self.avg >= 90:
            self.grade = "A"
        elif 80 <= self.avg < 90:
            self.grade = "B"
        elif 60 <= self.avg < 80:
            self.grade = "C"
        elif 40 <= self.avg < 60:
            self.grade = "D"
        else:
            self.grade = "Fail"
        return

    def check_reg(self,reg_num):
        self.found = False
        self.reg_num = reg_num
        count = 0
        with open("student.txt","r") as f:
                self.lines = f.readlines()
                for line in self.lines:
                    if self.reg_num in line:
                        self.found = True
                        temp = line.strip().split(",")
                        self.old_name = temp[0].split(":")[1]
                        count += 1
                        break
                if count == 0:
                    print("ERROR:Invalid register number")
                    return
           
                
    def add_student(self):
            try:
                print("=====Welcome User=====")
                dept_name = str(input("Enter department name(like s,c,a):"))
                name = str(input("Enter student name:"))
                reg_num = input("Enter register number:")
                print("Enter marks")
                mark1 = float(input("kannada:"))
                mark2 =  float(input("English:"))
                if dept_name == "s":
                    mark3 = float(input("mathametic:"))
                    mark4 = float(input("physics:"))
                    mark5 = float(input("chemecitry:"))
                    mark6 = float(input("computer science:"))

                    #calling grade function
                    self.grade(mark1,mark2,mark3,mark4,mark5,mark6)
                    

                    with open("student.txt","a") as f:
                        f.write(f"Name:{name},Regnum:S2025{reg_num},kannada:{mark1},english:{mark2},mathametics:{mark3},physics:{mark4},chemistry:{mark5},computerscience:{mark6},Total:{self.total},Average:{self.avg},Grade:{self.grade}\n")
                elif dept_name == "c":
                    mark3 = float(input("economic:"))
                    mark4 = float(input("accotence:"))
                    mark5 = float(input("chemecitry:"))
                    mark6 = float(input("computer science:"))

                    #calling grade function
                    self.grade(mark1,mark2,mark3,mark4,mark5,mark6)

                    with open("student.txt","a") as f:
                        f.write(f"Name:{name},Regnum:C2025{reg_num},kannada:{mark1},english:{mark2},economic:{mark3},accotence:{mark4},chemicitry:{mark5},computerscienceeconomic:{mark6},Total:{self.total},Average:{self.avg},Grade:{self.grade}\n")
                else:
                    mark3 = float(input("mathameti:"))
                    mark4 = float(input("physics:"))
                    mark5 = float(input("chemecitry:"))
                    mark6 = float(input("computer science:"))

                    #calling grade function
                    self.grade(mark1,mark2,mark3,mark4,mark5,mark6)

                    with open("student.txt","a") as f:
                        f.write(f"Name:{name},Regnum:A2025{reg_num},kannada:{mark1},english:{mark2},mathameti:{mark3},physics:{mark4},chemicitry:{mark5},computerscience:{mark6},Total:{self.total},Average:{self.avg},Grade:{self.grade}\n")
                print("Student info add susfully \n")
            except:
                print("ERROR:Enter every field \n")

    def stu_update(self):
        while True:
            try:
                print("\n Student Database")
                print("Change name --> 1")
                print("Update mark --> 2")
                print("Delete ---> 3")
                print("Back---> 4")
                choice = int(input("enter your choice:"))
                if choice == 1:
                    try:
                        ran_num = random.randint(1000,9999)
                        reg_num = input("Enter your register num:")

                        #calling reg check function
                        self.check_reg(reg_num)
                        pre_name = self.old_name

                        print("OTP:",ran_num)
                        st_otp = int(input("Enter your otp:"))
                        if st_otp == ran_num:
                            new_name = input("Enter new name:")

                            with open("student.txt","w") as f:
                                for line in self.lines:
                                    if self.reg_num in line:
                                        new_line = line.replace(pre_name,new_name)
                                        f.write(new_line)
                                    else:
                                        f.write(line)
                    except:
                        print("try again")
            
                
                elif choice == 2:
                    try:
                        reg_num = input("Enter your register num:")

                        # #calling check function
                        # self.check_reg(reg_num)
                        with open("student.txt","r") as f:
                            lines = f.readlines()
                        new_line = []
                        found = False
                        sub_name = input("Enter subject name:")
                        new_mark = input("Enter new marks:")
                        
                        for line in lines:
                            temp = line.strip().split(",")
                            data = dict(item.split(":") for item in temp)
                            if data.get("Regnum") == reg_num:
                                found = True
                                if sub_name not in data:
                                    print("ERROR:subject not found")
                                    return
                                data[sub_name] = new_mark
                                new_lines = ",".join(f"{k}:{v}" for k,v in data.items())
                                new_line.append(new_lines+"\n")
                            else:
                                new_line.append(line)
                        if not found:
                            print("Invalid register number")
                        
                        with open("student.txt","w") as f:
                            f.writelines(new_line)

                    except:
                        print("ERROR")
                    
                elif choice == 3:
                    try:
                        update_line = []
                        reg_num = input("Enter your register num:")
                        self.check_reg(reg_num)
                        lines = self.lines
                        if self.found == True:
                            for line in lines:
                                new_line = line.strip().split(",")
                                reg = new_line[1].split(":")[1]
                                if reg == reg_num:
                                    pass
                                else:
                                    update_line.append(line)
                                    with open("student.txt","w") as f:
                                        f.writelines(update_line)
                    except:
                        print("ERROR:invalid register number")
                elif choice == 4:
                    return
            except:
                print("Error:Enter your choice")
    
    def show(self):
        print("=====STUDENT DATABSE=====")
        with open("student.txt","r") as f:
            data = lines = f.readlines()
            for line in data:
                data = line.strip()
                print(data)   

print("======STUDENT MANEGMENT SYSTEM======")
while True:
    try:
        print("\n")
        print("-MENU-")
        print("Show deatail---> 1")
        print("Add student----> 2")
        print("Update-----> 3")
        print("Exit----> 4")
        choice = int(input("Enter your choice:"))     
        s1 = Student()

        if choice == 1:
            s1.show()
        elif choice == 2:
            s1.add_student()
        elif choice == 3:
            s1.stu_update()
        elif choice == 4:
            break
    except:
        print("ERROR:Enter your choice")

