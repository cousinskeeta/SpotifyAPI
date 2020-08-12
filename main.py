from flask import Flask, render_template, Response, request, session
from spotify_client import SpotifyAPI
import requests 

client_id = ''
client_secret = ''

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is a very long secret keep that i hope no one figures out'

global spotify
spotify = SpotifyAPI(client_id, client_secret)


@app.route('/')
def index():
    # rendering webpage
    return render_template('index.html')

@app.route('/artist_info', methods=['GET','POST'])
def artist_info():
    ID = str(request.form['id'])
    print(ID)
    session['results'] = spotify.get_artist(ID)
    print(type(session['results']))
    print(session['results'].items())
    session.modified = True
    return render_template('index.html', results=session.get('results'))

if __name__ == '__main__':
    # defining server ip address and port
    app.run(host='0.0.0.0',port='5000', debug=True)
