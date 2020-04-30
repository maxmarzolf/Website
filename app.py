from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import Required
from flask_bootstrap import Bootstrap
from os import environ


app = Flask(__name__)
app.config['SECRET_KEY'] = environ.get('contact_form')
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
    return render_template('home.html')


@app.route('/form.html')
def contact_form():
    form = NameForm()
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run()
