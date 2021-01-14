from flask import Flask, render_template
from flask_caching import Cache


app = Flask(__name__)
# disables caching on the server
cache = Cache(app, config={'CACHE_TYPE': 'null'})


@app.route('/advanced')
def search():
    return render_template("index.html")

@app.route('/image')
def image_search():
    return render_template("image.html")

@app.route('/')
def advanced_search():
    return render_template("advanced_search.html")
#
# # https://www.google.com/advanced_search
#
# @app.route('/')
# def advanced_image_search():
#     return render_template("index.html")

# https://www.google.com/advanced_image_search

if __name__ == "__main__":
    app.run(debug=True)