# current_app stores a reference to the global application object.
from flask import Flask, render_template, current_app
import pandas as pd
import os

app = Flask(__name__)
app.exercises_df = pd.read_csv(os.path.join('data', 'exercises_expanded.csv'))  # load data once, bind to app


@app.route('/')
def index():
    print(current_app.exercises_df.head())
    return render_template('index.html')


if __name__ == '__main__':
   app.run(debug=True)
