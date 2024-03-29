from eve import Eve
from flask import send_from_directory
from flask_sentinel import ResourceOwnerPasswordCredentials, oauth
from oauth2 import BearerAuth

app = Eve(__name__, static_url_path="/static", static_folder="frontend/dist")

# Enabled auth when ready
#app = Eve(__name__, auth=BearerAuth, static_folder="static")
#ResourceOwnerPasswordCredentials(app)

@app.route('/endpoint')
@oauth.require_oauth()
def restricted_access():
    return "You made it through and accessed the protected resource!"


@app.route('/')
def index():
    return send_from_directory("frontend", 'index.html')

if __name__ == '__main__':
	#app.run()
	# for dev only, self signed cert generated by flask
	# to enable chrome to work with it:
	# chrome://flags/#allow-insecure-localhost
	# click enable on it
    app.run(ssl_context='adhoc')