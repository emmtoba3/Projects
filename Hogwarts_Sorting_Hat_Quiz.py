# Write code below 💖
gryffindor=0
ravenclaw=0
hufflepuff=0
slytherin=0
print("Choose the answer wich you feel the most identified by typing the number the answer")
print("Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")
q1=int(input("A: "))

if q1==1:
  gryffindor+=1
  ravenclaw+=1
else:
  hufflepuff+=1
  slytherin+=1

print("When I’m dead, I want people to remember me as:")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")
q2=int(input("A: "))
if q2==1:
  hufflepuff+=2
elif q2==2:
  slytherin+=2
elif q2==3:
  ravenclaw+=2
else:
  gryffindor+=2

print("Which kind of instrument most pleases your ear?")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")
q3=int(input("A: "))
if q3==1:
  slytherin+=4
elif q3==2:
  hufflepuff+=4
elif q3==3:
  ravenclaw+=4
else:
  gryffindor+=4

if gryffindor >= ravenclaw and gryffindor >= hufflepuff and gryffindor >= slytherin:
    print("You are a Gryffindor 🦁")
elif ravenclaw >= hufflepuff and ravenclaw >= slytherin:
    print("You are a Ravenclaw 🦅")
elif hufflepuff >= slytherin:
    print("You are a Hufflepuff 🦡")
else:

    print("You are a Slytherin 🐍")


#Please 
