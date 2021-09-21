# current_app stores a reference to the global application object.
from flask import Flask, render_template, current_app, request, redirect
from flask_bootstrap import Bootstrap
import pandas as pd
import copy
import os
import random
from src.workout_info import BodyPart, Equipment, Difficulty
from forms import WorkoutsForm


app = Flask(__name__)
app.exercises_df = pd.read_csv(os.path.join('static', 'data', 'exercises_expanded.csv'))  # load data once, bind to app
bootstrap = Bootstrap(app)

# For the forms
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/', methods=['GET','POST'])
def index():
    form = WorkoutsForm()
    form.set_choices()
    
    if request.method == 'POST' and form.validate_on_submit():    
        body_part_choice = form.body_part_options.data
        equipment_choice = form.equipment_options.data
        difficulty_chocie = form.difficulty_options.data
        number_of_workouts = form.number_of_workouts.data

        # Filter workouts 
        filtered_df = pd.DataFrame()
        for body_part in body_part_choice:
            filtered_df = filtered_df.append(current_app.exercises_df[current_app.exercises_df['body_part__' + body_part] == True])
            
        for equipment in equipment_choice:
            filtered_df = filtered_df[filtered_df['equipment__' + equipment] == True]
            
        filtered_df = filtered_df[filtered_df['difficulty'].isin(difficulty_chocie)]

        # Choose randomly from filtered workouts
        random_indicies = random.sample(range(filtered_df.shape[0]), number_of_workouts)
        chosen_exercises = filtered_df.iloc[random_indicies][['title', 'body_part', 'difficulty', 'equipment', 'image1', 'image2']]
        
        form.set_choices()
    
        return render_template('index.html', 
                               form=form, 
                               chosen_exercises=chosen_exercises.values.tolist(),
                               table_exercises=chosen_exercises[['title', 'body_part', 'difficulty', 'equipment']].to_html(classes=["table-bordered", "table-striped"], header=True, index=False)
                              )
    

    return render_template('index.html', form=form)


if __name__ == '__main__':
   app.run()
