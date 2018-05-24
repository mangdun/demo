@route('/')
def index():
	return 'hello world'

@route('/login')
def login():
	return 'login'

@route('/register')
def register():
	return 'register'

@route('/new')
def new():
	num = 0
	return 'new'


