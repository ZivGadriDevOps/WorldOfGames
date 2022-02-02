from flask import Flask, redirect, render_template
from HelperMethods import get_user_score

app = Flask(__name__)


@app.route('/')
def get_scores():
    return render_template('scores.html', SCORE=get_user_score())


app.run(host="0.0.0.0", port=5001, debug=True)
