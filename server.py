from flask import Flask, redirect, request, render_template, session
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)

# This option will cause Jinja to throw UndefinedErrors if a value hasn't
# been defined (so it more closely mimics Python's behavior)
app.jinja_env.undefined = StrictUndefined

# This option will cause Jinja to automatically reload templates if they've been
# changed. This is a resource-intensive operation though, so it should only be
# set while debugging.
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = 'ABC'

MOST_LOVED_MELONS = {
    'cren': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimRegular/crenshaw.jpg',
        'name': 'Crenshaw',
        'num_loves': 584,
    },
    'jubi': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Jubilee-Watermelon-web.jpg',
        'name': 'Jubilee Watermelon',
        'num_loves': 601,
    },
    'sugb': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Sugar-Baby-Watermelon-web.jpg',
        'name': 'Sugar Baby Watermelon',
        'num_loves': 587,
    },
    'texb': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Texas-Golden-2-Watermelon-web.jpg',
        'name': 'Texas Golden Watermelon',
        'num_loves': 598,
    },
}

@app.route('/')

def homepage():
    
    if 'user_name' in session:
        return redirect('/top-melons')
    return render_template('homepage.html')

# add user_name in a session
@app.route('/get-name')
def get_name():

    user_name = request.args.get("user_name")
    session['user_name'] = user_name
    # print(session['user_name'])

    return redirect('/top-melons')


# Shows our most loved melons page
@app.route('/top-melons')
def top_melons():

    name = []
    number_loves = []
    melon_image = []

    for melons in MOST_LOVED_MELONS:
        name.append(MOST_LOVED_MELONS[melons]['name'])
        number_loves.append(MOST_LOVED_MELONS[melons]['number_loves'])
        melon_image.append(MOST_LOVED_MELONS[melons]['img'])

    most_melons = MOST_LOVED_MELONS

    if 'user_name' in session:
        return render_template("top-melons.html",
                                name = name,
                                number_loves = number_loves,
                                melon_image = melon_image,
                                MOST_LOVED_MELONS = most_mels,
                                user_name = session['user_name']
                                )
    return redirect('/')

@app.route('/')

if __name__ == '__main__':
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    DebugToolbarExtension(app)

    app.run(host='0.0.0.0')
