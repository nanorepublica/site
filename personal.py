from flask import Flask, render_template, url_for
import urllib2,json,copy

app = Flask(__name__)

@app.route('/')
def index():
	links = {'home':('home',url_for('index')),'contact':('contact',url_for('contact')),'blog':('blog',url_for('blog'))}
	content = json.load(open('./static/index.json','r'))
	main_content = copy.deepcopy(content)
#	del['page']
	return render_template('index.html',links=links, content=content)

@app.route('/contact')
def contact():
	links = {'home':('home',url_for('index')),'contact':('contact',url_for('contact')),'blog':('blog',url_for('blog'))}
	content = json.load(open('./static/contact.json','r'))
	return render_template('index.html',links=links, content=content)

@app.route('/test')
def test():
	return render_template('test.html')

@app.route('/blog')
def blog():
	links = {'home':('home',url_for('index')),'contact':('contact',url_for('contact')),'blog':('blog',url_for('blog'))}
	content = {}
	return render_template('index.html',links=links, content=content)

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')
