from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import Required
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = 'not_a_good_key'
bootstrap = Bootstrap(app)


class NameForm(FlaskForm):
    name = StringField('Name', validators=[Required])
    address1 = StringField('Address 1', validators=[Required])
    address2 = StringField('Address 2', validators=[Required])
    city = StringField('City', validators=[Required])
    state = StringField('State', validators=[Required])
    zip = IntegerField('Zip Code', validators=[Required])
    submit = SubmitField('Submit')


@app.route('/')
def start():
    form = NameForm()
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run()
