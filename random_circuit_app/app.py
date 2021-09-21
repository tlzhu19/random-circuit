# current_app stores a reference to the global application object.
from flask import Flask, render_template, current_app
import pandas as pd
import os
import random
from src.workout_info import BodyPart, Equipment, Difficulty


app = Flask(__name__)
app.exercises_df = pd.read_csv(os.path.join('data', 'exercises_expanded.csv'))  # load data once, bind to app


@app.route('/')
def index():
    random_indicies = random.sample(range(app.exercises_df.shape[0]), 5)
    chosen_exercises = current_app.exercises_df.iloc[random_indicies][['title', 'body_part', 'difficulty', 'equipment']]
    
    return render_template('index.html', chosen_exercises=chosen_exercises.to_html(classes=["table-bordered", "table-striped"], header=True, index=False))


if __name__ == '__main__':
   app.run(debug=True)
