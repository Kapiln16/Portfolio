import random
import time
from tkinter import Tk
list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','@','#','$','1','2','3','5','6','7','8','9']
i = 0


print('Welcome to PassWord Generator')
x = input("Do You want to generate password :  ")
while True :
   if ( x == "yes"):
       j = int(input('Enter No. of digit in password. :  ' ))
       count = 3
       for i in range(4):
         time.sleep(1)
         print("Generating in :",count)
         count -= 1
      
       


   
       print('Pass Generated :')
       for i in range(j):
          generator1 = random.choice(list1)
          i+=1     
          x = print(generator1, end = "")

   print('\nThanks For Using this project!! ')
   print('Program Terminating in 30sec')
   time.sleep(30)
   break

   
else:
  print('Okay!!')
  print('\nThanks For Using this project!! ')



      
   