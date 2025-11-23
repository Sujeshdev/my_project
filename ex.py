reg_num = "S2025103"
# name = "brother"
# new_name = "hi"
# with open("student.txt","r") as f:
#     data = f.readlines()
# with open("student.txt","w") as f:
#     for i in data:
#         if reg_num in i:
#             data = i.replace(name,new_name)
#             f.write(data)
#         else:
#             f.write(i)

count = 0
with open("student.txt","r") as f:
    lines = f.readlines()
    for line in lines:
        if reg_num in line:
            print("found")
            count += 1
    if count == 0:
        print("not found")
