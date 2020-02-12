from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required


app = Flask(__name__)
app.config['SECRET_KEY'] = 'not_a_good_key'


class NameForm(FlaskForm):
    name = StringField('Enter Name', validators=[Required])
    submit = SubmitField('Submit')


@app.route('/')
def start():
    form = NameForm()
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run()
