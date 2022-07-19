from flask import Flask, render_template, request, redirect, url_for
from blogs import Blog
from news import News

app = Flask(__name__)
posts = Blog()
news = News()

@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html', title='Posts page', header='Welcome to my blog', posts=posts.getPosts())

# TODO: post should added by the route '/post/' with method POST.
@app.route('/home/', methods=['POST'])
def blog_add():
    # TODO: would be good to return a new post from 'add' method if we'd like to use some data.
    posts.addPost(request.form.get('title', ''), request.form.get('date', ''), request.form.get('body', ''))
    return redirect(url_for('postsbydate', date=request.form.get('date')))

@app.route('/posts/<date>')
def postsbydate(date):
    return render_template('posts.html', title='Posts page', header='Posts ' + date, posts=posts.getPostsByDate(date))

@app.route('/post/<sku>.html')
def post(sku):
    return render_template('post.html', title='Post page', header=sku, post=posts.getPostBySku(sku))

@app.route('/news')
def news_list():
    return render_template('news.html', title="News", header="Our news", news=news.getList())

@app.route('/news', methods=['POST'])
def news_add():
    news.addNews(request.form.get('title', ''), request.form.get('date', ''), request.form.get('body', ''))
    return redirect('/news')