# Import Modules
import pandas as pd
import numpy as np

# Create suggestion function
def movie_recommender():
  # Create a user interface 
  print('hello welcome to the smart theatre app!\n'.title())
  print('-'*len('hello welcome to the smart theatre app!'))
  # Read in demo csv file, 2/5 of the original dataset
  ratings = pd.read_csv('ratings.csv',index_col='index')
  # Create a pivot tabel w/ movies as the columns, and ratings as rows/values
  ratings_pivot = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
  print('Please start thinking of a movie you recently enjoyed.\n')
  # Create loop to display list (or not)
  while True:
    titles = str(input('If you would like to see our list of over 200 avaliable movies enter 1 (recommended), if not, enter 0:'))
    print()
    if titles == '1':
      for x in ratings['title'].unique():
        print(str(x))
      print('-'*65)
      print()
      break
    elif titles == '0':
      print('-'*65)
      print()
      break
    else:
      print('Please only enter 0 or 1')
      print('-'*65)
      print()
  # Create loop to get watched movie and 5 suggestions
  while True:
    Movie = input('Please enter an avaliable movie title you enjoyed followed by a space and then the year in parenthesies:').strip().title()
    print('-'*(len('Please enter an avaliable movie title you enjoyed followed by a space and then the year in parenthesies:')-8))
    print()
    try:
      # Find movies simular to...
      users_movie = ratings_pivot[Movie]
      suggested_movie = ratings_pivot.corrwith(users_movie)
      suggested_movie = suggested_movie.dropna()
      df = pd.DataFrame(suggested_movie)
      movie = ratings.groupby('title').agg({'rating': [np.size, np.mean]})
      filitered_Movies = movie['rating']['size'] >= 20
      df = movie[filitered_Movies].join(pd.DataFrame(suggested_movie, columns=['similarity']))
      df.sort_values(['similarity'], ascending=False,inplace=True)
      # Display 5 recomended movies
      print('Here are some movies we think you would enjoy, based on your chosen movie:')
      print()
      for x in list(df.index[1:5]):
        print(x)
      print('-'*len(df.index[4]))
      print()
      break
    except:
      print('The movie you have chosen either has insignificant data for an accurate recommendation or it is spelled incorrectly, please try again\n')
      print('-'*73)
      
    