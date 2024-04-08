import csv
import pandas as pd
from sklearn.model_selection import  train_test_split

# Veri setinde 1011958 satir 24 sutundan olusmakta #
# dataset = "TMDB_movie_dataset_v11.csv" #


dataset = "netflix_titles.csv"
dataset2 = "tmdb_5000_movies.csv"
dataset3 = "movies_initial.csv"
    
file = open(dataset3,"r",encoding="utf8")
data = list(csv.reader(file,delimiter=","))
file.close()

df = pd.read_csv("movies_initial.csv")
    #df = df[df['type'].str.contains('Movie')] # Print only movies # 
    #print(df[['title','cast']])
    #print(df[['title', 'genres']])
    #df = df[df['type'].str.contains('name')] # Print only movies # 
#print(df[['title','genre','cast']])

X= df['genre']
print('X:\n',X)
y = df['cast']
print('y:\n',y)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=100)
print('Trained X:\n',X_train)

