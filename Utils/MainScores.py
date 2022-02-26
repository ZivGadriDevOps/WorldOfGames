from flask import Flask, render_template, send_from_directory, abort
from HelperMethods import get_user_score, get_repaired_name

app = Flask(__name__)

app.config["TEMPLATES_PATH/vendor/"] = "C:/Users/ziv/PycharmProjects/WorldOfGames/Utils/templates/vendor/"
app.config["TEMPLATES_PATH/css/"] = "C:/Users/ziv/PycharmProjects/WorldOfGames/Utils/templates/css/"
app.config["TEMPLATES_PATH/img/"] = "C:/Users/ziv/PycharmProjects/WorldOfGames/Utils/templates/img/"


@app.route('/score/<string:name>')
def get_scores(name: str):
    score = get_user_score(name)
    return render_template('scores.html', USER_NAME=get_repaired_name(name), SCORE=score)


@app.route('/score/vendor/<path:path_to_file>')
def send_css_vendor(path_to_file):
    file_name_ = path_to_file.split('/')
    file_name = file_name_[-1]
    path_to_file = app.config["TEMPLATES_PATH/vendor/"] + file_name_[0]
    try:
        return send_from_directory(path_to_file, file_name, as_attachment=False)
    except FileNotFoundError:
        abort(404)


@app.route('/score/css/<path:file_name>')
def send_css(file_name):
    try:
        return send_from_directory(app.config["TEMPLATES_PATH/css/"], str(file_name), as_attachment=False)
    except FileNotFoundError:
        abort(404)


@app.route('/score/img/<path:file_name>')
def send_img(file_name):
    try:
        return send_from_directory(app.config["TEMPLATES_PATH/img/"], str(file_name), as_attachment=False)
    except FileNotFoundError:
        abort(404)


print("Flask server is running and listening on port 5000")
app.run(host="0.0.0.0", port=5000, debug=True)
