import csv
import pandas as pd

# Veri setinde 1011958 satir 24 sutundan olusmakta #
# dataset = "TMDB_movie_dataset_v11.csv" #

def open_csv():
    dataset = "netflix_titles.csv"
    
    file = open(dataset,"r",encoding="utf8")
    data = list(csv.reader(file,delimiter=","))
    file.close()

    df = pd.read_csv("netflix_titles.csv")
    df = df[df['type'].str.contains('Movie')] # Print only movies # 
    print(df[['title','cast']])
    #print(df[['title', 'genres']])
    #print(data)
