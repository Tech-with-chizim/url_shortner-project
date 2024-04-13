from flask import Flask, render_template, redirect, request
import string
import random

app  = Flask(__name__)
url_mappings  =  {}

def generate_short_url():
    characters =  string.ascii_letters +  string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    return short_url


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url  =  request.form['url']

    if original_url not in url_mappings:
        short_url = generate_short_url()
        url_mappings[original_url] =  short_url
    
 
    return render_template('index.html', original_url=original_url,  short_url=url_mappings[original_url])
@app.route('/<short_url>')
def redirect_to_original(short_url):
    for original_url, generated_short_url in url_mappings.items():
        if generated_short_url == short_url:
            print(f"Original URL: {original_url}, Shortened URL: {generated_short_url}")
            return redirect(original_url)

    return 'URL not found!'

if __name__ == "__main__":
    app.run(debug=True)