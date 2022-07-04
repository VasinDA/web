from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/home/')
def home():
    return render_template('base.html', title='Home page', header='Welcome to my blog', 
    content_header='About my blog')

@app.route('/posts/<data>')
def postsbydata(data):
    return render_template('base.html', title='Posts page', header='Posts', 
    content_header='2022-10-12')

@app.route('/post/my_post.html')
def mypost():
    return render_template('base.html', title='Post page', header='My Post', 
    content_header='My firt post')