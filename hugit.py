@route('/')
def index():
	return 'hello world'

@route('/login')
def login():
	return 'login'

@route('/register')
def register():
	return 'register'

<<<<<<< HEAD
@route('/new')
=======
@route('/')
>>>>>>> be23baf0aa16ae2ef27b4e8613999e8e626b82ad
def new():
	return 'new'


