from flask import Flask, render_template, Response
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/form', methods=['GET', 'POST'])
def form():
    name = None
    new_form = NameForm()
    if new_form.validate_on_submit():
        name = new_form.name.data
        return '<h1>Thanks for sharing, {} ~</h1>'.format(name)

    return render_template('form.html', form=new_form)


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


if __name__ == '__main__':
    app.run()
