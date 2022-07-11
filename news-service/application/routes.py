from application import app
from flask import render_template
import json
import random

# Import modules for API Access
import http.client, urllib.parse

# Load API Key
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv('SECRET_KEY')

@app.route("/")
@app.route("/news")
def news_page():

    # Connect to Mediastack API
    conn = http.client.HTTPConnection('api.mediastack.com')
    params = urllib.parse.urlencode({
        'access_key': API_KEY,
        'categories': 'general,science,sports,health,technology,entertainment',
        'countries': 'us,ng,gb,ca,au,de,fr,pl',
        'languages': 'en',
        'limit': 100
        })
    conn.request('GET', '/v1/news?{}'.format(params))
    res = conn.getresponse()
    json_object = res.read()

    # Convert json response from api to python object
    python_object = json.loads(json_object)
    data = python_object['data']

    # Use random image from list 
    images = [
            "https://motionarray.imgix.net/preview-328095-gNWCObG9we-high_0004.jpg?w=660&q=60&fit=max&auto=format",
            "https://i.ytimg.com/vi/hBOUjUEY46w/hqdefault.jpg ",
            "https://d1csarkz8obe9u.cloudfront.net/posterpreviews/breaking-news-poster-design-template-232c3f2700b91a0fd6e3a5a2e583a5da_screen.jpg?ts=1610645412",
            "https://media.istockphoto.com/vectors/breaking-news-live-banner-on-dotted-map-of-the-world-background-vector-id1150517899?k=20&m=1150517899&s=612x612&w=0&h=jMz9KZVY_abyiXfjdYfDMw0pUD2iTdNRnFBcHJgsxoI=",
            "https://cdn2.vectorstock.com/i/1000x1000/31/26/breaking-news-logo-icon-for-news-entertaining-vector-28933126.jpg",
            "https://i.pinimg.com/originals/24/39/a6/2439a657128437d7b308e112f05c2b70.png",
            "https://archive.org/download/news-logo/news-logo.png",
            "https://e7.pngegg.com/pngimages/155/416/png-clipart-record-news-logo-identidade-visual-connected-idea-logo-miscellaneous-television.png",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPIs696h2cnMnWZudUbFg5xrhGxzKMJtJFXA&usqp=CAU",
            "https://www.presentation-3d.com/image/maker3d/demos/3dlogo120601.png",
            "https://cdn1.vectorstock.com/i/1000x1000/01/45/world-news-logo-flat-style-vector-20910145.jpg",
            "https://www.vinsighte.com.ng/img/partners-img/world-news.jpg",
            "https://image.shutterstock.com/image-photo/image-260nw-1080857420.jpg"
            ]

    items = []

    for news in data:
        item = {
                'title': news['title'],
                'description': news['description'],
                'url': news['url'],
                'image': random.choice(images)
                }
        items.append(item)

    return render_template('news_page.html', items=items)

@app.route("/")
@app.route("/customize")
def customization_page():
    # Parameters to be accepted from user and fed to the API
    countries = ['Australia', 'Canada', 'China', 'France', 'Germany', 'India', 'Italy', 'Nigeria', 'Poland', 'Singapore', 'United States', 'United Kingdom']
    languages = ['Chinese', 'Dutch', 'English', 'French', 'German', 'Hebrew', 'Italian', 'Norweighian', 'Portuguese', 'Russian', 'Spanish', 'Swedish']
    categories = ['General', 'Business', 'Celebrity Gossip', 'Entertainment', 'Finance', 'Health', 'IT', 'Medicine & Pharmacy', 'Politics', 'Technology', 'Science', 'Sports']
    items = [
            {'country': countries[0], 'language': languages[0], 'category': categories[0]},
            {'country': countries[1], 'language': languages[1], 'category': categories[1]},
            {'country': countries[2], 'language': languages[2], 'category': categories[2]},
            {'country': countries[3], 'language': languages[3], 'category': categories[3]},
            {'country': countries[4], 'language': languages[4], 'category': categories[4]},
            {'country': countries[5], 'language': languages[5], 'category': categories[5]},
            {'country': countries[6], 'language': languages[6], 'category': categories[6]},
            {'country': countries[7], 'language': languages[7], 'category': categories[7]},
            {'country': countries[8], 'language': languages[8], 'category': categories[8]},
            {'country': countries[9], 'language': languages[9], 'category': categories[9]},
            {'country': countries[10], 'language': languages[10], 'category': categories[10]},
            {'country': countries[11], 'language': languages[11], 'category': categories[11]},
            ]

    return render_template('customize_page.html', items=items)
