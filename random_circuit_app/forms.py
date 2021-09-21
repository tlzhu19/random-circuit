from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, IntegerField, SubmitField
from random_circuit_app.src.workout_info import BodyPart, Equipment, Difficulty


class WorkoutsForm(FlaskForm):
    body_part_options = SelectMultipleField('Body Part')
    equipment_options = SelectMultipleField('Equipment')
    difficulty_options = SelectMultipleField('Difficulty')
    number_of_workouts = IntegerField('Number of Workouts')
    submit = SubmitField('Randomize')
    
    def set_choices(self):
        self.body_part_options.choices = zip(BodyPart.list(), BodyPart.list())
        self.equipment_options.choices = zip(Equipment.list(), Equipment.list())
        self.difficulty_options.choices = zip(Difficulty.list(), Difficulty.list())
    