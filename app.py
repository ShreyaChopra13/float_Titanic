from flask import Flask, render_template, request
app=Flask(__name__)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about_2')
def about_2():
    return render_template('about_2.html')

@app.route('/forgot')
def forgot():
    return render_template('forgot.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/index_2')
def index_2():
    return render_template('index_2.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/pickup')
def pickup():
    return render_template('pickup.html')

@app.route('/pickup_2')
def pickup_2():
    return render_template('pickup_2.html') 

@app.route('/points')
def points():
    return render_template('points.html')

@app.route('/points_2')
def points_2():
    return render_template('points_2.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')


if __name__=="__main__":
    app.run(debug=True)
