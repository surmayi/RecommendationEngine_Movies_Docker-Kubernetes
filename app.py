from flask import Flask,request, render_template
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import pickle
import numpy as np
import urllib.request
import bs4 as bs

app = Flask(__name__)

nlp_senti = pickle.load(open('nlp_sentiments.pkl','rb'))
vectorizer = pickle.load(open('vectorizer.pkl','rb'))

def get_sentiments_similarity():
    data = pd.read_csv('finaldata.csv')
    count_vector = CountVectorizer()
    model_fit = count_vector.fit_transform(data['combined_text'])
    similarity = cosine_similarity(model_fit)
    return data, similarity

def recommend1(movie):
    movie= movie.lower()
    try:
        data.head()
    except:
        data,simillarity = get_sentiments_similarity()
    if movie not in data['title'].unique():
        return (
            'Sorry! The movie you requested is not in our database. Please check the spelling or try with some other movies')
    row = data.loc[data['title']==movie].index[0]
    print(row)
    lis = list(enumerate(simillarity[row]))
    lis = sorted(lis,key= lambda x:x[1],reverse=True)
    lis=lis[1:11]
    print(lis)
    final_list=[]
    for i in range(10):
        t=lis[i][0]
        final_list.append(data['title'][t])
    print(final_list)
    return final_list

def get_suggestions():
    data = pd.read_csv('finaldata.csv')
    return list(data['title'].str.capitalize())

# converting list of string to list (eg. "["abc","def"]" to ["abc","def"])
def convert_to_list(my_list):
    my_list = my_list.split('","')
    my_list[0] = my_list[0].replace('["','')
    my_list[-1] = my_list[-1].replace('"]','')
    return my_list


def get_reviews(imdbId):
    print(imdbId)
    sauce = urllib.request.urlopen('https://www.imdb.com/title/{}/reviews?ref_=tt_ov_rt'.format(imdbId)).read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    soup_result = soup.find_all("div", {"class": "text show-more__control"})

    movie_reviews = dict()
    for reviews in soup_result:
        if reviews.string:
            token = vectorizer.transform(np.array([reviews.string]))
            review_status = nlp_senti.predict(token)
            review_status = 'Good' if review_status else 'Bad'
            movie_reviews[reviews.string] = review_status
    return movie_reviews

@app.route('/')
@app.route('/home')
def homepage():
    recommendations= get_suggestions()
    return render_template('home.html',suggestions=recommendations)

@app.route('/similarity', methods=['POST'])
def similarity():
    name = request.form['name']
    print(name)
    rc = recommend1(name)
    if type(rc)==type('string'):
        return rc
    else:
        mv = '---'.join(rc)
        return mv

@app.route('/recommend',methods=['POST'])
def recommend2():
    #getting data from request
    title = request.form['title']
    cast_ids = request.form['cast_ids']
    cast_names = request.form['cast_names']
    cast_chars = request.form['cast_chars']
    cast_bdays = request.form['cast_bdays']
    cast_bios = request.form['cast_bios']
    cast_places = request.form['cast_places']
    cast_profiles = request.form['cast_profiles']
    imdb_id = request.form['imdb_id']
    poster = request.form['poster']
    genres = request.form['genres']
    overview = request.form['overview']
    vote_average = request.form['rating']
    vote_count = request.form['vote_count']
    release_date = request.form['release_date']
    runtime = request.form['runtime']
    status = request.form['status']
    rec_movies = request.form['rec_movies']
    rec_posters = request.form['rec_posters']

    # get suggestions for auto complete
    suggestions = get_suggestions()

    # call the convert_to_list function for every string that needs to be converted to list
    rec_movies = convert_to_list(rec_movies)
    rec_posters = convert_to_list(rec_posters)
    cast_names = convert_to_list(cast_names)
    cast_chars = convert_to_list(cast_chars)
    cast_profiles = convert_to_list(cast_profiles)
    cast_bdays = convert_to_list(cast_bdays)
    cast_bios = convert_to_list(cast_bios)
    cast_places = convert_to_list(cast_places)

    # convert string to list (eg. "[1,2,3]" to [1,2,3])
    cast_ids = cast_ids.split(',')
    cast_ids[0] = cast_ids[0].replace("[","")
    cast_ids[-1] = cast_ids[-1].replace("]","")

    # rendering the string to python string
    for i in range(len(cast_bios)):
        cast_bios[i] = cast_bios[i].replace(r'\n', '\n').replace(r'\"', '\"')

    # combining multiple lists as a dictionary which can be passed to the html file so that it can be processed easily and the order of information will be preserved
    movie_tiles = {rec_posters[i]: rec_movies[i] for i in range(len(rec_posters))}

    casts = {cast_names[i]: [cast_ids[i], cast_chars[i], cast_profiles[i]] for i in range(len(cast_profiles))}

    cast_details = {cast_names[i]: [cast_ids[i], cast_profiles[i], cast_bdays[i], cast_places[i], cast_bios[i]] for i in
                    range(len(cast_places))}

    movie_reviews = get_reviews(imdb_id)

    return render_template('recommend.html',title=title,poster=poster,overview=overview,vote_average=vote_average,
        vote_count=vote_count,release_date=release_date,runtime=runtime,status=status,genres=genres,
        movie_cards=movie_tiles,reviews=movie_reviews,casts=casts,cast_details=cast_details)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)

