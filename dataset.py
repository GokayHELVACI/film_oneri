import csv
import pandas as pd # To print as dataframe #

# Veri setinde 1011958 satir 24 sutundan olusmakta #
# dataset = "TMDB_movie_dataset_v11.csv" #

def open_csv():
    dataset = "test.csv"

    file = open(dataset,"r",encoding="utf8")
    data = list(csv.reader(file,delimiter=","))
    file.close()

    df = pd.read_csv("test.csv")
    print(df[['title', 'genres']])
    #print(data)
