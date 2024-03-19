from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def root():
    return "welcome to IMDb top movies and series"

@app.route('/IMDb')
def IMDb():
    import requests

    movies_url = "https://imdb-top-100-movies.p.rapidapi.com/"
    series_url = "https://imdb-top-100-movies.p.rapidapi.com/series/"

    movies_headers = {
        "X-RapidAPI-Key": "3e457e6f7bmsh836bc401628bc0ep11683djsn9fd256d7b7cd",
        "X-RapidAPI-Host": "imdb-top-100-movies.p.rapidapi.com"
    }
    series_headers = {
	    "X-RapidAPI-Key": "5c687ac1d6mshcf92852aee59873p102533jsne9ca084eda08",
	    "X-RapidAPI-Host": "imdb-top-100-movies.p.rapidapi.com"
    }

    movies_response = requests.get(movies_url, headers=movies_headers)
    series_response = requests.get(series_url, headers=series_headers)
    
    movies_data = movies_response.json()
    series_data = series_response.json()

    return render_template("IMDb.html", movies_data=movies_data, series_data=series_data)

if __name__ == '__main__':
    app.run(debug=True)