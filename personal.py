from flask import Flask, render_template, url_for, flash, redirect,render_template_string,get_template_attribute
from flaskext.wtf import Form, TextField, validators, TextAreaField
from flaskext.wtf.html5 import EmailField
import urllib2,json,copy,re
#from jinja2 import evalcontextfilter,Environment
from flaskext.mail import Mail, Message


app = Flask(__name__)
app.secret_key = 'm\xb2q\x19=\xc0S\xe9w\x19\xcd\x14\xb7\xa7x\xa4U\xdb<\xfb\x87\xc7C)'
mail = Mail(app)

class contactForm(Form):
	name = TextField('Name:',[validators.Required()])
	email = EmailField('email:',[validators.Required()])
	message = TextAreaField('Message:',[validators.Required()])
	
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))

@app.template_filter('split')
def split(value,contact):
	pattern = '(\{\{[a-zA-Z\.\_\(\)\ ]*\}\})'
	result = re.split(pattern,value)
	render_field = get_template_attribute('_helper.html','render_field')
	t = ''
	for i in result:
		if len(i):
			t = '%s%s' % (t,render_template_string(i,contact=contact,render_field=render_field))
	return t

@app.route('/')
def index():
	links = {'home':('home',url_for('index')),'contact':('contact',url_for('contact')),'blog':('blog',url_for('blog'))}
	content = open('./static/index.json','r')
	return render_template('index.html',links=links, content=content)

@app.route('/contact', methods=("GET", "POST"))
def contact():
	contactf = contactForm()
	links = {'home':('home',url_for('index')),'contact':('contact',url_for('contact')),'blog':('blog',url_for('blog'))}
	content = json.loads(''.join(''.join(open('./static/contact.json','r').read().splitlines()).split('\t')))
	if contactf.validate_on_submit():
		msg = Message("New mail from %s" % contactf.data['name'],sender=contactf.data['email'],recipients=["info@akmiller.co.uk"],body=contactf.data['message'])
		mail.send(msg)
		return redirect(url_for("index"))
		#pass #send an email to me & alter content to display success of some kind
	return render_template('index.html',links=links, content=content,contact=contactf)

@app.route('/test')
def test():
	return render_template('test.html')

@app.route('/blog')
def blog():
	links = {'home':('home',url_for('index')),'contact':('contact',url_for('contact')),'blog':('blog',url_for('blog'))}
	content = {}
	return render_template('index.html',links=links, content=content)

if __name__ == '__main__':
	#app.run(debug=True,host='0.0.0.0')
	app.run(host='0.0.0.0')
