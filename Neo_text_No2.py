filei = open("Neo_text.txt","w")
filei.write("string chage\n")

for i in range(0,5):
    xc = input("Real Number is  a :")
    filei.write("\n" + xc + "\n")



filei = open("hello_world.txt","r")
print(filei.read())
filei.close()

