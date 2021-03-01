from tmdbv3api import TMDb,Movie
import json
import requests
tmdb = TMDb()
tmdb.api_key = 'api_key'
class MovieInfo:
    def __init__(self):
        self.tmdbObj= Movie()
    def getGenres(self,movie):
        genres=[]
        movieId=0
        try:
            movieId = self.tmdbObj.search(movie)[0]['id']
            response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key={}'.format(movieId,tmdb.api_key))
            response =response.json()
            for g in range(len(response['genres'])):
                genres.append(response['genres'][g]['name'])
        except:
            print(movieId)
            return []
        return genres
    def getDirector(self,crew):
        if '(director)' in crew:
            return crew.split('(director)')[0]
        elif '(directors)' in crew:
            return crew.split('(directors)')[0]
        elif '(director/screenplay)' in crew:
            return crew.split('(director/screenplay)')[0]
        else:
            return 'unknown'
    def actor1(self,crew):
        if 'screenplay);' in crew:
            spl='screenplay);'
        else:
            spl='director);'
        actors= crew.split(spl)[-1].split(',')
        if len(actors)>0:
            return actors[0]
        else: return 'unknown'
    def actor2(self,crew):
        if 'screenplay);' in crew:
            spl='screenplay);'
        else:
            spl='director);'
        actors= crew.split(spl)[-1].split(',')
        if len(actors)>1:
            return actors[1]
        else: return 'unknown'
    def actor3(self,crew):
        if 'screenplay);' in crew:
            spl='screenplay);'
        else:
            spl='director);'
        actors= crew.split(spl)[-1].split(',')
        if len(actors)>2:
            return actors[2]
        else: return 'unknown'
