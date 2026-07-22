from flask import Flask, render_template, request
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into user (username,email,phone,country_id,fm,employeetype,pic) values (:username,:email,:phone,:country_id,:fm,:employeetype,:pic)",request.form)
        user = query_db('select * from user')
        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")
    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")

@app.route("/add_one_country", methods=["GET","POST"])
def add_one_country():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into country (name) values (:name)",request.form)
        user = query_db('select * from country')
        return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")
    user = query_db('select * from country')
    one_user = query_db("select * from country limit 1", one=True)
    return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")

@app.route("/add_one_quotes", methods=["GET","POST"])
def add_one_quotes():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into quotes (name,author,fm) values (:name,:author,:fm)",request.form)
        user = query_db('select * from quotes')
        return render_template("quotesform.html", quotess=user, one_user=one_user, the_title="add new quotes")
    user = query_db('select * from quotes')
    one_user = query_db("select * from quotes limit 1", one=True)
    return render_template("quotesform.html", quotess=user, one_user=one_user, the_title="add new quotes")

@app.route("/add_one_songs", methods=["GET","POST"])
def add_one_songs():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into songs (artist_id,title) values (:artist_id,:title)",request.form)
        user = query_db('select * from songs')
        return render_template("songsform.html", songss=user, one_user=one_user, the_title="add new songs")
    user = query_db('select * from songs')
    one_user = query_db("select * from songs limit 1", one=True)
    return render_template("songsform.html", songss=user, one_user=one_user, the_title="add new songs")

@app.route("/add_one_artists", methods=["GET","POST"])
def add_one_artists():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into artists (name,fm) values (:name,:fm)",request.form)
        user = query_db('select * from artists')
        return render_template("artistsform.html", artistss=user, one_user=one_user, the_title="add new artists")
    user = query_db('select * from artists')
    one_user = query_db("select * from artists limit 1", one=True)
    return render_template("artistsform.html", artistss=user, one_user=one_user, the_title="add new artists")

@app.route("/add_one_photo_posted", methods=["GET","POST"])
def add_one_photo_posted():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into photo_posted (pic,user_id) values (:pic,:user_id)",request.form)
        user = query_db('select * from photo_posted')
        return render_template("photo_postedform.html", photo_posteds=user, one_user=one_user, the_title="add new photo_posted")
    user = query_db('select * from photo_posted')
    one_user = query_db("select * from photo_posted limit 1", one=True)
    return render_template("photo_postedform.html", photo_posteds=user, one_user=one_user, the_title="add new photo_posted")

