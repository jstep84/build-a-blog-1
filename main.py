from flask import Flask, request, redirect, render_template, session, flash#can use bcrypt instead of hashlib
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] =  True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:build-a-blog@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(120))
    submitted = db.Column(db.Boolean)
    

    def __init__(self, title, body):
        self.title = title
        self.body = body
        self.submitted = False



@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        blog_name_title = request.form['blog_title']
        blog_name_body = request.form['blog_body']        
        new_blog = Blog(blog_name_title, blog_name_body)        
        db.session.add(new_blog)
        db.session.commit()

    blogs = Blog.query.filter_by(submitted=False).all()
    submitted_blogs = Blog.query.filter_by(submitted=True).all()
    return render_template('todos.html',title="Build a Blog", blogs=blogs, submitted_blogs=submitted_blogs)


@app.route('/newpost', methods=['POST'])
def post_blog():

    blog_id = int(request.form['blog-id-title'])
    blog = Blog.query.get(blog_id)
    blog_body = int(request.form['blog-id-body'])
    blog = Blog.query.get(blog_body)    
    db.session.add(blog)
    db.session.commit()

    return redirect('/')


if __name__ == '__main__':
    app.run()