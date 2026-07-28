from flask import Flask, render_template, request, session, redirect
import os
import subprocess
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
app.secret_key="wow"
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
    try:
       connected=session["username"]
    except:
       connected=""
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title",connected=connected)
@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)

    if request.method == 'POST' and request.form["password"] == request.form["password_confirmation"]:

        print(request.form)
        print(request.files)
        x=request.form
        uploaded_file = request.files['pic']
        print(uploaded_file)
        hey=dict(x)
        print(hey)
        print(hey["employeetype"])
        print(hey["employeetype"] == "fake")
        the_username = "anonyme"



        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('static/photos', uploaded_file.filename))

        hey["pic"]=uploaded_file.filename
        one_user = query_db("insert into user (username,email,phone,country_id,fm,employeetype,pic,password) values (:username,:email,:phone,:country_id,:fm,:employeetype,:pic,:password)",hey)
        myuser = query_db("select * from user where username = ? and email = ? and password = ? limit 1", [hey["username"], hey["email"], hey["password"]], one=True)

        if hey["employeetype"] == "fake":
            try:
                x=subprocess.Popen(["/usr/bin/python3.8","addsunglasses.py",hey["pic"]])
            except Exception as e:
                print("ereeeuuuuur!!! ooowow!",e)




        session['fm'] = myuser['fm']
        session['email'] = myuser['email']
        session['user_id'] = myuser['id']
        session['username'] = request.form['username']
        session['employeetype'] = request.form['employeetype']
        print("bug")
        return redirect("/?registered=true")
    elif request.method == 'POST':

        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")

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
    try:
       fm=session["fm"]
    except:
       fm=""
    try:
       username=session["username"]
    except:
       username=""

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into quotes (name,author,fm) values (:name,:author,:fm)",request.form)
        user = query_db('select * from quotes')
        return render_template("quotesform.html", fm=fm, username=username, quotess=user, one_user=one_user, the_title="add new quotes")
    user = query_db('select * from quotes')
    one_user = query_db("select * from quotes limit 1", one=True)
    return render_template("quotesform.html", fm=fm, username=username, quotess=user, one_user=one_user, the_title="add new quotes")

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
    try:
       mytype=session["employeetype"]
    except:
       mytype=""
    try:
       userid=session["user_id"]
    except:
       userid=""

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)
        the_username = "anonyme"
        uploaded_file = request.files['pic']




        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('static/photos', uploaded_file.filename))

        hey["pic"]=uploaded_file.filename

        one_user = query_db("insert into photo_posted (pic,user_id,location) values (:pic,:user_id,:location)",hey)
        user = query_db('select photo_posted.*, user.* from photo_posted left outer join user on user.id = photo_posted.user_id')
        return render_template("photo_postedform.html",userid=userid, mytype=mytype,photo_posteds=user, one_user=one_user, the_title="add new photo_posted")
    user = query_db('select photo_posted.*, user.* from photo_posted left outer join user on user.id = photo_posted.user_id')
    one_user = query_db("select * from photo_posted limit 1", one=True)
    return render_template("photo_postedform.html", userid=userid, mytype=mytype,photo_posteds=user, one_user=one_user, the_title="add new photo_posted")


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        app.run("localhost",port=int(argv[1]))
    else:
        app.run()

