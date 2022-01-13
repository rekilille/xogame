import turtle
print("Welcome to my XO game. Code by Jon Ander and Iker del Rio.")
ul=0
uc=0
ur=0
cl=0
cc=0
cr=0
dl=0
dc=0
dr=0
picasso=turtle
wn=turtle.Screen()
picasso.speed(0)
def tablero():
picasso.pendown()
for i in range (3):
for j in range(3):
for k in range(4):
picasso.forward(40)
picasso.left(90)
picasso.forward(40)
picasso.left(180)
picasso.forward(120)
picasso.left(180)
if i==2:
break
picasso.right(90)
picasso.forward(40)
picasso.left(90)
picasso.penup()
tablero()
def cross():
picasso.pendown()
picasso.settiltangle(0)
picasso.right(45)
picasso.forward(36)
picasso.left(180)
picasso.forward(18)
picasso.left(90)
picasso.forward(18)
picasso.left(180)
picasso.penup()
picasso.forward(18)
picasso.pendown()
picasso.forward(18)
picasso.penup()
def cercle():
picasso.setheading(0)
picasso.forward(10)
picasso.right(90)
picasso.forward(25)
picasso.left(90)
picasso.pendown()
picasso.circle(15)
picasso.penup()
def check():
if ul==uc and uc==ur:
return ul
if cl==cc and cc==cr:
return cl
if dl==dc and dc==dr:
return dl
if ul==cl and cl==dl:
return ul
if uc==cc and cc==dc:
return uc
if ur==cr and cr==dr:
return ur
if ul==cc and cc==dr:
return ul
if ur==cc and cc==dl:
return ur
return 0
n1victoryroyale=False
i=0
while i<10:
if i%2==0:
instruction=input("Player 1, enter your next move\n")
if instruction=="Top Left":
if ul==0:
picasso.setpos(10,30)
cross()
ul=1
i+=1
else:
print("Please choose another position. Type help if you need help.")
elif instruction=="Top Center":
if uc==0:
picasso.setpos(50,30)
cross()
uc=1
i+=1
else:
print("Please choose another position. Type help if you need help.")
elif instruction=="Top Right":
if ur==0:
picasso.setpos(90,30)
cross()
ur=1
i+=1
else:
print("Please choose another position. Type help if you need help.")
elif instruction=="Center Left":
if cl==0:
picasso.setpos(10,-10)
cross()
cl=1
i+=1
else:
print("Please choose another position. Type help if you need help.")
elif instruction=="Center Center":
if cc==0:
picasso.setpos(50,-10)
cross()
cc=1
i+=1
else:
print("Please choose another position. Type help if you need help.")
elif instruction=="Center Right":
if cr==0:
picasso.setpos(90,-10)
cross()
cr=1
i+=1
else:
print("Please choose another position. Type help if you need help.")
elif instruction=="Bottom Left":
if dl==0:
picasso.setpos(10,-50)
cross()
dl=1
i+=1
else:
print("Please choose another position. Type help if you need help.")
elif instruction=="Bottom Center":
if dc==0:
picasso.setpos(50,-50)
cross()
dc=1
i+=1
else:
print("Please choose another position. Type help if you need help.")
elif instruction=="Bottom Right":
if dr==0:
picasso.setpos(90,-50)
cross()
dr=1
i+=1
else:
print("Please choose another position. Type help if you need help.")
elif instruction=="help":
print("There are 9 possible positions, Top Left, Top Center, Top Right, Center Left, Center Center, Center Right, Bottom Left, Bottom Center and Bottom Right. Please note that both of the words need to be capitalized in order for the computer to understand your command. GLHF!")
else:
print("The position you selected couldn't be read. Please enter a valid position. Type help if you need help.")
elif i%2==1:
instruction=input("Player 2, enter your next move\n")
if instruction=="Top Left":
if ul==0:
picasso.setpos(10,30)
cercle()
ul=2
i+=1
else:
print("Please choose another position. Type help if you need help.")
elif instruction=="Top Center":
if uc==0:
picasso.setpos(50,30)
cercle()
uc=2
i+=1
else:
print("Please choose another position. Type help if you need help.")
elif instruction=="Top Right":
if ur==0:
picasso.setpos(90,30)
cercle()
ur=2
i+=1
else:
print("Please choose another position. Type help if you need help.")
elif instruction=="Center Left":
if cl==0:
picasso.setpos(10,-10)
cercle()
cl=2
i+=1
else:
print("Please choose another position. Type help if you need help.")
elif instruction=="Center Center":
if cc==0:
picasso.setpos(50,-10)
cercle()
cc=2
i+=1
else:
print("Please choose another position. Type help if you need help.")
elif instruction=="Center Right":
if cr==0:
picasso.setpos(90,-10)
cercle()
cr=2
i+=1
else:
print("Please choose another position. Type help if you need help.")
elif instruction=="Bottom Left":
if dl==0:
picasso.setpos(10,-50)
cercle()
dl=2
i+=1
else:
print("Please choose another position. Type help if you need help.")
elif instruction=="Bottom Center":
if dc==0:
picasso.setpos(50,-50)
cercle()
dc=2
i+=1
else:
print("Please choose another position. Type help if you need help.")
elif instruction=="Bottom Right":
if dr==0:
picasso.setpos(90,-50)
cercle()
dr=2
i+=1
else:
print("Please choose another position. Type help if you need help.")
elif instruction=="help":
print("There are 9 possible positions, Top Left, Top Center, Top Right, Center Left, Center Center, Center Right, Bottom Left, Bottom Center and Bottom Right. Please note that both of the words need to be capitalized in order for the computer to understand your command. GLHF!")
else:
print("The position you selected couldn't be read. Please enter a valid position. Type help if you need help.")
if check()==1:
n1victoryroyale=True
print("Congratulations Player 1! You have won!")
if check()==2:
n1victoryroyale=True
print("Congratulations Player 2! you have won!")
if n1victoryroyale==True:
break
wn.mainloop()