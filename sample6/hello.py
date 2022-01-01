from flask import Flask, render_template

app = Flask(__name__,static_folder='.',static_url_path="")


# @app.route('/')
# def hello():
#     name = "Hello World"
#     return name


@app.route('/')
def good():
    name = "Good"
    # return name
    return render_template('hello.html', title='flask test', name=name)


if __name__ == '__main__':
    app.run(debug=True)
