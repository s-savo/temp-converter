luckynumber=8
tries=1
print("Hello, welcome to the guessing game")
print("you have 3 attempts to correctly get the lucky number from 0-10, good luck!!")

while tries <4 :
  r=int(input(" go!!"))
  tries=tries+1
  if  r == luckynumber :
    print("congratulations you got lucky number 8")
    break
else:
  print(f"better luck next time, the lucky number is {luckynumber}")


