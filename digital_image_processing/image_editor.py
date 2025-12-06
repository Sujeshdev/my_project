"""Built an interactive OpenCV image editor with a menu-driven interface to draw shapes and text on images, learning OOP design patterns and OpenCV drawing functions"""

import cv2

#function to take user input for color, thikness and save option
def input_user():
    try:
        col = []
        for i in range(3):
            col.append(int(input("Enter color value:")))
        thik = int(input("Enter thikness:"))
        s = input("you wnat save piture(yes or no):")
        s = s.lower()
        return col,thik,s
    except Exception as e:
        print("War:",e)

#class to handle photo operations
class Photo:
    #constructor to initialize image path and read image
    def __init__(self,img_path):
        self.img_path = img_path
        self.img = cv2.imread(self.img_path)
        self.img = cv2.resize(self.img,(600,400))

    #method to save edited image
    def save(self,img):
        try:
        save_path = input("Enter folder path:")
        cv2.imwrite(save_path,img)
        print("Piture saved at locattion:..save/line.jpg")
        except Exception as e:
            print("War:",e)

    #method to draw line on image
    def line(self,x1,y1,x2,y2,col,thik,s):
        img_line = cv2.line(self.img,(x1,y1),(x2,y2),col,thik)
        cv2.imshow("Drawed img",img_line)
        print("Edited image displaye")
        if s == "no":
            print("Piture not save")
        else:
            self.save(img_line)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    #method to draw rectangle on image
    def rect(self,x1,y1,x2,y2,col,thik,s):
        img = cv2.rectangle(self.img,(x1,y1),(x2,y2),col,thik)
        cv2.imshow("Edited",img)
        print("Edited image displaye")
        if s == "yes":
            self.save(img)
        else:
            print("Edited photo not save")
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    #method to draw circle on image
    def circle(self,radius,col,thick,s):
        h,w = self.img.shape[:2]
        center = w//2,h//2
        cir = cv2.circle(self.img,center,radius,col,thick)
        cv2.imshow("Edited",cir)
        if s == "yes":
            self.save(cir)
        else:
            print("Edited photo not saved")
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    #method to add text on image
    def text(self,text,col,thik,s,x,y,scale):
        font = cv2.FONT_HERSHEY_PLAIN
        text_img = cv2.putText(self.img,text,(x,y),font,scale,col,thik)
        cv2.imshow("Edited",text_img)
        if s == "yes":
            self.save(text_img)
        else:
            print("Edited photo not saved")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
#using while loop to create menu driven program
while True:
    try:
        print("Menu")
        print("Draw line-->1")
        print("Draw squre-->2")
        print("Draw circle-->3")
        print("Text -->4")
        print("Exit-->0")
        choice = int(input("Enter your choice:"))
    
        #variable to take user input image path
        try:
            img_path = input("Enter your image path:")
        except Exception as e:
            print("War:",e)
    
        #create Photo object
        P1 = Photo(img_path)
    
        if choice == 1:
            try:
                #by comprehension take points from user
                x1,y1 = [int(i) for i in input("Enter first point:").split(" ")]
                x2,y2 = [int(i) for i in input("Enter second point:").split(" ")]
    
                #call input_user function to take color,thikness and save option
                col,thik,s = input_user()
    
                #call line method
                P1.line(x1,y1,x2,y2,col,thik,s)
            except Exception as e:
                print("War:",e)
    
        elif choice == 2:
            try:
                x1,y1 = [int(i) for i in input("Enter first point:").split(" ")]
                x2,y2 = [int(i) for i in input("Enter second point:").split(" ")]
                col ,thik, s = input_user()
                P1.rect(x1,y1,x2,y2,col,thik,s)
            except Exception as e:
                print("War:",e)
    
        elif choice == 3:
            try:
                cir_radius = int(input("Enter circle radius:"))
                col,thik,s = input_user()
                P1.circle(cir_radius,col,thik,s)      
            except Exception as e:
                print("War:",e)
    
        elif choice == 4:
            try:
                text = input("Enter your text:")
                x,y = [int(i) for i in input("Enter point:").split(" ")]
                sc = float(input("Enter scale:"))
                col,thik,s = input_user()
                P1.text(text,col,thik,s,x,y,sc)
            except Exception as e:
                print("War:",e)
        else:
            break
    except Exception as e:
        print("War:",e)
