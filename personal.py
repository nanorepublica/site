from flask import Flask, render_template, url_for
import urllib2

app = Flask(__name__)

@app.route('/')
def index():
	links = {'home':('home',url_for('index')),'contact':('contact',url_for('contact')),'blog':('blog',url_for('blog'))}
	content = {about me,picture,qualification,experience,interest}
	return render_template('index.html',links=links, content=content)

@app.route('/contact')
def contact():
	links = {'home':('home',url_for('index')),'contact':('contact',url_for('contact')),'blog':('blog',url_for('blog'))}
	content = {'quick':{'email':'info@akmiller.co.uk','twitter':'@nanorepublica','' linkedin}}
	return render_template('index.html',links=links, content=content)

@app.route('/blog')
def blog():
	links = {'home':('home',url_for('index')),'contact':('contact',url_for('contact')),'blog':('blog',url_for('blog'))}
	content = {}
	return render_template('index.html',links=links, content=content)

if __name__ == '__main__':
	app.run(debug=True)
