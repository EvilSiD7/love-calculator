# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_string = (name1 + name2)
lowercase_string = combined_string .lower()

t = lowercase_string .count("t")
r = lowercase_string .count("r")
u = lowercase_string .count("u")
e = lowercase_string .count("e")

true = (t+r+u+e)
string_true = str(true)
combinedstring = (name1+name2)
lowercasestring = combinedstring .lower()

l = lowercase_string .count("l")
o = lowercase_string .count("o")
v = lowercase_string .count("v")
e = lowercase_string .count("e")
 
love = ( l + o + v + e )
string_love = str(love)

love_score = (string_true + string_love)
intlovescore = int(love_score)

if (intlovescore < 10) or (intlovescore > 90):
  print(f"Your score is {intlovescore}, you go together like coke and mentos")
elif (intlovescore >= 40) or (intlovescore <= 50):
  print(f"Your score is {intlovescore}, you go together")
else:
  print(f"Your score is {intlovescore} ")







