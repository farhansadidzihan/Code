#               //Title\\ 
# || Conditiinal Logic || if , elif , else ||
# Favourite,
Actors      = ['Hritik Roshan' , 'Shahruk Khan' , 'Tom Cruise' , 'Crist Evans', 'Crist Hemsworth']
Players     = ['Cristiano Ronaldo' , 'Messi' , 'Neymar JR']
Youtubers   = ['Marshmallow', 'Mr.Beast']
Persons     = ['Mohammad(s)' , 'Elon Mask' , 'Sundar Pichai' , 'Aman Dattarwala']
Billionires = ['Elon Mask ' , 'Jeff Bezoz' , 'Bill Gates' , 'Jack Ma' ]
Companies   = ['Apple' , 'Google' , 'Microsoft' , 'Tesla' , 'Royal Z']
Cars        = ['Rolls Royace' , 'Lamborgini' , 'Farrari' , 'Bugatti' , 'Bentley' , 'Tesla']
Most    = input("Type , What is your most favourite thing ?")
if Most in Actors:
    print("Congratulations !" , "Your most favourite Actor is :-", Most , "!" ) 
elif Most in Players:
    print("Hurrah !" , "Your most favourite Player is :-" , Most)
elif Most in Youtubers:
    print("Congratulaitions !" , "Your most favourite Youtuber is :-" , Most)
elif Most in Persons:
    print("Congratulaitions !" , "Your most favourite Person is :-" , Most)
elif Most in Billionires:
    print("Congratulaitions !" , "Your most favourite billionire is :-" , Most)
elif Most in Companies:
    print("Congratulaitions !" , "Your most favourite company is :-" , Most)
elif Most in Cars:
    print("Congratulaitions ! Your favourite car is :- " , Most)
else: 
    print("Sorry ! That is not your fovourite.")



# || Conditiinal Logic || if , elif , else || Comparision ||
Bangla  = 95
English = 80
Math    = 100
if Bangla > English:
    Higher_Mark = Bangla
elif English > Bangla:
    Higher_Mark = English
if Higher_Mark > Math:
    Highest_Mark = Higher_Mark
elif Higher_Mark < Math:
    Highest_Mark = Math 
print("Your Highest Mark is : " , Highest_Mark)



# || Conditiinal Logic || if , elif , else || Leap year Selection ||
year = input("Type any year :- ")
year = int(year)
if year % 100 != 0 and year % 4 == 0:
    print("This is a Leap Year !")
elif year % 100 == 0 and year % 400 == 0:
    print("This is a Mega Leap Year !")
else:
    print("No!")