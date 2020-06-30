from bottle import route, run, template, request, static_file, get, post, response, redirect, error
import bottle
import sqlite3

bottle.TEMPLATE_PATH.insert(0,'./views/posts')

@route('/')
def home():
	return template('home')

# blog

@route('/blog')
def blog():
	return template('blog')

@route('/blog/<post>')
def blog(post):
	return template(post)

# new post

@get('/new')
def new():
	return template('new')

@post('/new')
def new():
	text = request.forms.get('text')

	return template('blank', content=text)

# admin

@get('/admin')
def admin():
	return template('admin', content='')

@post('/admin')
def admin():
	text = request.forms.get('text')

	conn = sqlite3.connect('data.db')
	c = conn.cursor()
	c.execute('INSERT INTO adminGuesses (text) VALUES (?)', (text,))
	conn.commit()
	c.close()

	# admin = True
	# if admin:
	# 	return 'You are an admin! :)'
	# else:
	# 	return "You're not an admin, you're a goose!"

	return template('admin', content='Unfortunately you entered the wrong admin password. Please try again.')

# admin panel to see all the guesses

@route('/adminGuesses')
def adminGuesses():
	conn = sqlite3.connect('data.db')
	c = conn.cursor()
	c.execute('SELECT * FROM adminGuesses;')
	guesses = c.fetchall()
	c.close()

	return template('adminGuesses', guesses=guesses)



# ctf

@route('/ctf')
def ctf():
	return template('blank', content='Genlteman, welcome to Fight Club')







# Signup System

@get('/signup')
def signup():
    return template('signup')

@post('/signup')
def signup():
    username = request.forms.get('username')
    password = request.forms.get('password')

    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    c.close()

    return template('blank', content='Thank you.')



# Login System

@get('/login')
def login():
    return template('login')

@post('/login')
def login():
    username = request.forms.get('username')
    password = request.forms.get('password')

    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT password FROM users WHERE username IS ?', (username,))
    cur_data = c.fetchone()
    c.close()

    if password == cur_data[0]:
        return template('blank', content='Your login information was correct.')
    else:
        return template('blank', content='Login failed.')

# Logout System



# Miscallaneous files

@route('/style.css')
def style():
	return static_file('/style.css', root='./views/misc')

@route('/robots.txt')
def robots():
	return static_file('/robots.txt', root='./views/misc')


# Images

@route('/images/<name>')
def images(name):
	return static_file(name, root='./views/images')


# Functions




# errors

@error(404)
def error404(error):
	return template('blank', content='Nothing here, sorry.')

# for dev
run(host='localhost', port=8080, debug=True, reloader=True)

# for live
# run(host=?, port=80?)