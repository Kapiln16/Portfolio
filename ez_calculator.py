import time
print("\n📊 ✖️ ➗ ➕ ➖ 🟰")
print("\nWelcome To EZ Calculator\n")

wannause = input('Do you want to use? ')

while wannause == "yes":

#number code
   print("ENTER YOUR FIRST NO. \n")
   a = int(input())
   print("ENTER YOUR SECOND NO. \n")
   b = int(input())


#operation code
   print("Choose your Operation ")
   print(" 1.ADD \n 2.SUBS \n 3.Product \n 4.Divide ")
   x = int(input())
# operation detailss
   add =      (1) 
   subs =     (2)
   product =  (3)
   divide =   (4)



#calculator detail code ( operating)

   if (x == add ) :
      print ( 'Sum of Numbers : ', b+a)
      print("\n ⋆.˚✮𝕋𝕙𝕒𝕟𝕜 𝕪𝕠𝕦✮˚.⋆")
     

   if ( x == subs) :
      print ('Substract of Numbers: ', a-b)
      print("\n ⋆.˚✮𝕋𝕙𝕒𝕟𝕜 𝕪𝕠𝕦✮˚.⋆")
    
   if (x == product) :
      print ( 'Product of Numbers : ',a*b)
      print("\n ⋆.˚✮𝕋𝕙𝕒𝕟𝕜 𝕪𝕠𝕦✮˚.⋆")

   if ( x == divide) :
      print ('Division of Numbers : ',a/b)
      print("\n ⋆.˚✮𝕋𝕙𝕒𝕟𝕜 𝕪𝕠𝕦✮˚.⋆")

   

   if (x >= 4) :
    print ("\nSORRY OUT OF OPERATION" , "\n⋆.˚✮𝕋𝕙𝕒𝕟𝕜 𝕪𝕠𝕦✮˚.⋆", "\n📊 ✖️ ➗ ➕ ➖ 🟰")
   j =input("\n Use again? y or n :")
   if j == 'n': 
      print('Thanks For Using!')
      print('\nProject by Kapil Neela')
      break


else :
   print('\nThanks For Using!')
   print('Project by Kapil Neela')
   print('\n \n Exiting in 10sec')
   
time.sleep(10)