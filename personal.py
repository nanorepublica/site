from flask import Flask, render_template, url_for, flash, redirect
from flaskext.wtf import Form, TextField, validators, TextAreaField
from flaskext.wtf.html5 import EmailField
import urllib2,json,copy
from jinja2 import evalcontextfilter,Environment

app = Flask(__name__)
app.secret_key = 'm\xb2q\x19=\xc0S\xe9w\x19\xcd\x14\xb7\xa7x\xa4U\xdb<\xfb\x87\xc7C)'

class contactForm(Form):
	name = TextField('Name:',[validators.Required()])
	email = EmailField('email:',[validators.Required()])
	message = TextAreaField('Message:',[validators.Required()])

#@evalcontextfilter
def split(value):
	lines = value.split('\n')
	for line in lines:
		if line.startswith('{{') and line.endswith('}}'):
			line = "WORKS"
	return '\n'.join(lines)



@app.route('/')
def index():
	links = {'home':('home',url_for('index')),'contact':('contact',url_for('contact')),'blog':('blog',url_for('blog'))}
	content = json.load(open('./static/index.json','r'))
	return render_template('index.html',links=links, content=content)

@app.route('/contact', methods=("GET", "POST"))
def contact():
	contact = contactForm()
	links = {'home':('home',url_for('index')),'contact':('contact',url_for('contact')),'blog':('blog',url_for('blog'))}
	#content = open('./static/contact.content','r').read()
	content = json.loads(''.join(open('./static/contact.content','r').read().split()))
	if contact.validate_on_submit():
		flash("Success")
		return redirect(url_for("index"))
		#pass #send an email to me & alter content to display success of some kind
	return render_template('index.html',links=links, content=content,contact=contact)

@app.route('/test')
def test():
	return render_template('test.html')

@app.route('/blog')
def blog():
	links = {'home':('home',url_for('index')),'contact':('contact',url_for('contact')),'blog':('blog',url_for('blog'))}
	content = {}
	return render_template('index.html',links=links, content=content)

if __name__ == '__main__':
	env = Environment()
	env.filters['split'] = split
	app.run(debug=True,host='0.0.0.0')
