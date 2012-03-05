from flask import Flask, render_template, url_for, flash, redirect,render_template_string,get_template_attribute, session, request
from flaskext.wtf import Form, TextField, validators, TextAreaField
from flaskext.wtf.html5 import EmailField
import urllib2,json,copy,re
from flaskext.flatpages import FlatPages
from flaskext.mail import Mail, Message
from flaskext.oauth import OAuth, OAuthResponse, OAuthException


app = Flask(__name__)
app.secret_key = 'm\xb2q\x19=\xc0S\xe9w\x19\xcd\x14\xb7\xa7x\xa4U\xdb<\xfb\x87\xc7C)'
pages = FlatPages(app)
mail = Mail(app)
api_key = '9L7mlUckx8GspKCYfsf4OIKvYGQi7iLM4LQcuGa1x4Pu7dmgy5'
oauth = OAuth()
tumblr = oauth.remote_app('tumblr',
		base_url='http://api.tumblr.com/v2/',
		request_token_url='http://www.tumblr.com/oauth/request_token',
		access_token_url='http://www.tumblr.com/oauth/access_token',
		authorize_url='http://www.tumblr.com/oauth/authorize',
		consumer_key='9L7mlUckx8GspKCYfsf4OIKvYGQi7iLM4LQcuGa1x4Pu7dmgy5',
		consumer_secret='FVR2CYA5oB4JOCLyjYAWEZ3put8f9FJXqFauegGkT9xiWyoelK'
		)


@tumblr.tokengetter
def get_tumblr_token():
	return session.get('tumblr_token')


@app.route('/login')
def login():
	return tumblr.authorize(callback=url_for('oauth_authorized',next=request.args.get('next') or request.referrer or None))

@app.route('/oauth_authorized')
@tumblr.authorized_handler
def oauth_authorized(resp):
	next_url = request.args.get('next') or url_for('index')
	if resp is None:
		print 'DENIED!!!!!!'
		return redirect(next_url)

	session['tumblr_token'] = (resp['oauth_token'], resp['oauth_token_secret'])
	return redirect(next_url)

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))
            
class contactForm(Form):
	name = TextField('Name:',[validators.Required()])
	email = EmailField('email:',[validators.Required()])
	message = TextAreaField('Message:',[validators.Required()])
	
################ Page views below ####################

@app.route('/')
def index():
	links = {'home':(0,url_for('index')),
	 'contact':(3,url_for('contact')),
	 'blog':(2,url_for('blog')),
	 'portfolio':(1,url_for('portfolio'))
	}
	page = pages.get_or_404('index')
	return render_template('index.html',links=links, page=page)

@app.route('/contact', methods=("GET", "POST"))
def contact():
	links = {'home':(0,url_for('index')),
	 'contact':(3,url_for('contact')),
	 'blog':(2,url_for('blog')),
	 'portfolio':(1,url_for('portfolio'))
	}
	contactf = contactForm()
	page = pages.get_or_404('contact')
	if contactf.validate_on_submit():
		msg = Message("New mail from %s" % contactf.data['name'],sender=contactf.data['email'],recipients=["info@akmiller.co.uk"],body=contactf.data['message'])
		mail.send(msg)
		return redirect(url_for("index"))
		#pass #send an email to me & alter content to display success of some kind
	render_field = get_template_attribute('_helper.html','render_field')
	page.html = render_template_string(page.html,contact=contactf,render_field=render_field)
	return render_template('index.html',links=links, page=page,contactf=contactf)

@app.route('/blog')
def blog():
	links = {'home':(0,url_for('index')),
	 'contact':(3,url_for('contact')),
	 'blog':(2,url_for('blog')),
	 'portfolio':(1,url_for('portfolio'))
	}
	blog = json.load(urllib2.urlopen('http://api.tumblr.com/v2/blog/nanorepublica.tumblr.com/posts?api_key=%s&limit=10'%api_key))
	if blog['meta']['status'] == 200:
		desc = blog['response']['blog']['description']
		blog = blog['response']['posts']
	else:
		desc = 'Could not retrieve blog information from tumblr'
	return render_template('blog.html',links=links, desc=desc, blog=blog)
	
@app.route('/portfolio')
def portfolio():
	links = {'home':(0,url_for('index')),
	 'contact':(3,url_for('contact')),
	 'blog':(2,url_for('blog')),
	 'portfolio':(1,url_for('portfolio'))
	}
	page = pages.get_or_404('portfolio')
	return render_template('index.html',links=links, page=page)


if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')
#	app.run(host='0.0.0.0')
