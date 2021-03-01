# Movie-recommendation-sentiments-analysis

For Recommendation Engine -
1. Collected data from Kaggle movies_dataset.csv, which contains data till 2016.
2. Used wikipedia API to pull data for 2017-2020. Concatanated data of -2016 with 2017-2020
3. Used tmdbv3api package and TmDB user API to pull tmdb id and movie genres respectively.
4. Performed data cleaning and preprocessing to seggregate director, genres and top 3 actors for each movie.
5. Used pairwise cosine similarity on each combination of (director, genres, top 3 actors) to create a similarity matrix.
6. Return the top 10 most similar(least cosin distance) movies for which ever movie is searched.


For sentiments analysis- 
1. COllected data from kaggle, reviews.txt to train the model.
2. Used TfIDF vectorizor to convert the reviews to a TF-IDF matrix
3. Used MultinomialNB naive Baise to train the model against the label as in a good or bad review
4. For every movie searched, use the imdb id to pull the reviews from IMDB API and use the model to predict the review as good or bad.

![image](https://user-images.githubusercontent.com/16138757/109556454-79b00e00-7a9c-11eb-93d4-34b25c1d1992.png)

![image](https://user-images.githubusercontent.com/16138757/109556553-93e9ec00-7a9c-11eb-8251-9fcc238e7da0.png)

![image](https://user-images.githubusercontent.com/16138757/109556589-a106db00-7a9c-11eb-80b2-7401f262d98d.png)

![image](https://user-images.githubusercontent.com/16138757/109556654-b8de5f00-7a9c-11eb-8a3f-cdcb918442bb.png)
