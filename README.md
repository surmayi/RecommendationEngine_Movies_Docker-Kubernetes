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

Steps to run -
1. Clone the repository from github
2. Create your API by creating a TMDB profile as developer.
3. Replace your key at moviesInfo.py, line 5. static/recommend.js, line 15 and 29. 
4. Run pip install -r requirements.txt
5. Run python app.py
6. browse 127.0.0.1:5000 to access the application 

To run on Docker-Kubernetes -
On your GCP terminal -
1. git clone https://github.com/surmayi/RecommendationEngine_Movies_Docker-Kubernetes.git
2. cd RecommendationEngine_Movies_Docker-Kubernetes/
3. export PROJECT_ID=your-current-project
4. docker build -t gcr.io/${PROJECT_ID}/movie_re:v1 .
5. docker images
6. gcloud auth configure-docker gcr.io
7. docker push gcr.io/${PROJECT_ID}/movie_re:v1
8. gcloud config set compute/zone us-central1-c
9. gcloud container clusters create moviere-cluster --num-nodes=1
10. kubectl create deployment movie-re --image gcr.io/${PROJECT_ID}/movie_re:v1
11. kubectl expose deployment movie-re --type LoadBalancer --port 80 --target-port 5000
12. kubectl get services

Get ip with the last command and run it on 5000 port on browser, now it is accessible globally

![image](https://user-images.githubusercontent.com/16138757/109556454-79b00e00-7a9c-11eb-93d4-34b25c1d1992.png)

![image](https://user-images.githubusercontent.com/16138757/109556553-93e9ec00-7a9c-11eb-8251-9fcc238e7da0.png)

![image](https://user-images.githubusercontent.com/16138757/109556589-a106db00-7a9c-11eb-80b2-7401f262d98d.png)

![image](https://user-images.githubusercontent.com/16138757/109556654-b8de5f00-7a9c-11eb-8a3f-cdcb918442bb.png)
