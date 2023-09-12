# Create software that will provide 
# an ATM user with the proper change 
# for any dollar amount up to $200.

# Example: Run the code for $19, 
# $55, and $200.
#
#Eric Dixon
#assuming change is in $20, $10, $5, $1s 
import math
#Change for any amount above $20 
changeFor = int(input("Please enter amount: "))
if changeFor >= 20:
  numOfTwenties = math.floor(changeFor/20)
  remaining = (changeFor%20)
  if remaining == 0: 
    print ("Number of $20s: ", numOfTwenties)
  else: 
    numOfTens = math.floor(remaining/10)
    getFives = (remaining - (10*numOfTens))
    numOfFives = math.floor(getFives/5)
    numOfOnes = (remaining - (10*numOfTens)- (5*numOfFives))
    print("Number of $20s:", numOfTwenties)
    print("Number of $10s:", numOfTens)
    print("Number of $5s: ", numOfFives)
    print("Number of $1s: ", numOfOnes)    
#Change for any amount between $10 - $19 
elif changeFor >= 10:
    numOfTens = math.floor(changeFor/10)
    remaining = (changeFor%10)
    print("Number of $10s:", numOfTens)
    if remaining >= 5:
      numOfFives = math.floor(remaining/5)
      numOfOnes = (remaining - (5*numOfFives))
      print("Number of $5s:",numOfFives)
      print("Number of $1s: ", numOfOnes)
    else: 
      print("Number of $1s:", remaining)
#Change for any amount between $5 - 9$ 
elif changeFor >= 5:
  numofFives = math.floor(changeFor /5)
  remaining = (changeFor%5)
  print("Number of $5s: ",numofFives)
  print("Number of $1s: ",remaining)
#change for $1-$4 
elif changeFor >0:
  numOfOnes = changeFor
  print("Number of $1s:",numOfOnes)
# Can't get change for <=0 
else:
  print("Amount must be greater than zero!")
