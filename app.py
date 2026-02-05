# from flask import Flask, render_template, send_from_directory
# import os

# app = Flask(__name__, static_folder='static', template_folder='templates')

# @app.route('/')
# def index():
#     # You can pass the filenames if you want dynamic selection
#     return render_template('index.html',
#                            cake_model='static/models/cake.glb',
#                            music_file='static/music/romantic.mp3',
#                            daryl_image='static/images/daryl.jpg')

# # Optional: serve favicon or other static endpoints if needed
# if __name__ == '__main__':
#     port = int(os.environ.get("PORT", 5000))
#     app.run(host='0.0.0.0', port=port, debug=True)

from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    cake_model = url_for("static", filename="models/cake.glb")
    return render_template("index.html", cake_model=cake_model)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
