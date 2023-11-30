from flask import Flask, render_template
import pandas as pd
import requests

app = Flask(__name__)

api_url = 'https://stand-by-me.herokuapp.com/api/v1/characters'

def get_characters():
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Turn the JSON into a dataframe
def get_characters_df():
    characters = get_characters()
    df = pd.DataFrame(characters)
    return df

@app.route('/')
def index():
    characters_df = get_characters_df()
    return render_template('index.html', characters=characters_df.to_html())
    
if __name__ == '__main__':
    app.run(debug=True)