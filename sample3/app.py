from flask import Flask

app=Flask(__name__,static_url_path='',static_folder='.')

@app.route('/')
def index():
    return app.send_static_file('index.html')

app.run(port=8000,debug=True)