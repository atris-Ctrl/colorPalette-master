import os
from flask import Flask, render_template, request, url_for
from flask.cli import load_dotenv
from flask_bootstrap import Bootstrap
from werkzeug.utils import redirect
from form import ImageForm
from colorthief import ColorThief

load_dotenv(".env")

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SecretKey")
Bootstrap(app)


@app.route("/", methods=["POST", "GET"])
def home():
    colors_example = ['#c3b6b7', '#9f1817', '#995f42', '#a97162', '#565a5d']
    form = ImageForm()
    if form.validate_on_submit():
        img = form.image.data
        color_thief = ColorThief(img)
        palette = color_thief.get_palette(color_count=5)
        all_colors = [rgb_to_hex(color) for color in palette]
        print(img)
        return redirect(url_for("color_page", img = img ,imgcolor=all_colors))
    return render_template("index.html", colors=colors_example, form=form)


@app.route("/colors")
def color_page():
    img_color = request.args.getlist("imgcolor")
    img = request.args.getlist("img")
    return render_template("colors.html", img = img, colors=img_color)



if __name__ == '__main__':
    app.run(debug=True)
