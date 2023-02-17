
from flask import Flask, request, jsonify, make_response, request, render_template, session, flash
import jwt
from datetime import datetime, timedelta
from functools import wraps

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a9ea845876aa4e4ea6e65ac196752d69'

# pulling token from querystring in this scenerio
def token_required(func):
    # decorator factory which invoks update_wrapper() method and passes decorated function as an argument
    # http://...url?token=slslkdlkjlk4556lkj67lkjl
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.args.get('token')       
        if not token:
            return jsonify({'Alert!': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except (jwt.InvalidTokenError, jwt.ExpiredSignatureError, jwt.DecodeError) as exc:
            return ({'Message': str(exc.args)})
        return func(*args, **kwargs)
    return decorated


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return 'logged in currently'


# Just to show you that a public route is available for everyone
@app.route('/public')
def public():
    return 'For Public'


# auth only if you copy your token and paste it after /auth?query=XXXXXYour TokenXXXXX
# Hit enter and you will get the message below.
@app.route('/auth')
@token_required
def auth():
    return 'JWT is verified. Welcome to your dashboard !  '


# Login page
@app.route('/login', methods=['POST'])
def login():
    if request.form['username'] and request.form['password'] == '123456':
        session['logged_in'] = True

        token = jwt.encode({ 'user': request.form['username'] , 'expiration': str(datetime.utcnow() + timedelta(seconds=60))} , app.config['SECRET_KEY'] )
        return jsonify({'token': token})
        # return jsonify({'token': token.decode('utf-8')})
    else:
        return make_response('Unable to verify', 403, {'WWW-Authenticate': 'Basic realm: "Authentication Failed "'})


# try to create a logout page
@app.route('/logout', methods=['POST'])
def logout():
    pass
# code here


if __name__ == "__main__":
    app.run(debug=True)