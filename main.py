# Import modules
import recommender
import Object
import pandas as pd

# Movie recommendation 
recommender.movie_recommender()


# Check out using a while loop to keep asking for input
Selected_Movie = input('Please enter the movie you would like to watch')
print('\nAdult Tickets...10$') 
print('\nKids Tickets...6$')
print('\nSenior Citizen Tickets...8$')
while True:
  try:
    adult= int(input('\nHow many Adult Tickets would you like to purchase?\n')) #ask users for adult tickets 
    kids= int(input('\nHow many Kids Tickets would you like to purchase?\n')) #asks users for kids tickets 
    sc= int(input('\nHow many Seinor Citizen Tickets would you like to purchase?')) #ask users for senious citizens tickets 
  except ValueError:
    print('\nSorry you did not enter a valid number.\n\nPlease enter the number of tickets you would like to purchase.\n\n') #catches any input errors
  else:
    break
# tix type and price 
adult_tix = 10 
kids_tix = 6
sc_tix = 8
tix_price = adult_tix * adult + kids_tix * kids + sc_tix * sc #calculates ticket prices 
tix_num = adult+kids+sc #calculates number of tickets 
customer = Object.Menu(tix_price)
print("\n\nThe total of price for the {} tikcets that you purchased is {:.2f} dollars for {}.".format(tix_num,customer.total_taxed(.04),Selected_Movie))
print()

Input = str(input('Would you like to also purchase food and drinks, enter "yes" if you do or enter anything else if you do not.\n'))
bul = 1
while bul:
# order food using a while loop to keep asking for input on food and drink items
  if Input == 'yes':
    food = [['pop',7.50],['pretz',5.50],['nacho',5.50],['candy',4.50],['hot_dog',4.25],['burg',5.75]]
    drink= [['water',1.5],['soda',2],['juice',2.50],['beer',4],['wine',7]]
    df = pd.DataFrame(data = food,columns=['food','price'])
    df.set_index('food', inplace=True)
    print(df)
    df1 = pd.DataFrame(data = drink,columns=['drink','price'])
    df1.set_index('drink', inplace=True)
    print(df1)
    df3 = pd.concat([df, df1])
    Food_drink = []
    Price = []
    while True:
      Food1 = str(input('Please enter the food and drinks you would like, enter 0 when you are done\n'))
      if Food1 in list(df3.index):
        Food_drink.append(Food1)
        Price.append(df3.loc[Food1])
      elif Food1 == '0':
        break
      else:
        print('please enter our avaliable food/drink items exactly how you see them'.upper())
    bul-=1
  else:
    Price = []
    break
# Calc total using class and show user 
total = tix_price+sum(Price)
customer = Object.Menu(total)
print('\nyour total is {} dollars,\n please look at the touch screen for directions to pay, and your theater location,\n Thank You for coming to The Smart Theater!'.format(customer.total_taxed(.04)))
      
      
      
    











