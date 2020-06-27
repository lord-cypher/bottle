from bottle import route, run, template, request, static_file, get, post, response, redirect

@route('/')
def home():
	return template('home')

@route('/blog')
def blog():
	return template('blog')

@route('/post1')
def blog():
	return template('post1')

@route('/style.css')
def blog():
	return static_file('style.css', root='./views/')

@route('/robots.txt')
def robots():
	return static_file('robots.txt', root='./views/')


# for dev
run(host='localhost', port=8080, debug=True, reloader=True)

# for live
# run(host=?, port=80?)