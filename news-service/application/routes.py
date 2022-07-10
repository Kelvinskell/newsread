from application import app
from flask import render_template

# Import modules for API Access
import http.client, urllib.parse

@app.route("/")
@app.route("/news")
def news_page():

    # Connect to Mediastack API
    conn = http.client.HTTPConnection('api.mediastack.com')
    params = urllib.parse.urlencode({
        'access_key': 'ACCESS_KEY',
        'categories': '-general',
        'countries': 'us, gb, ng, ca',
        'languages': 'en',
        'limit': 20,
        })
    conn.request('GET', '/v1/news?{}'.format(params))
    res = conn.getresponse()
    data = res.read()
    return data

    return render_template('news_page.html')

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
