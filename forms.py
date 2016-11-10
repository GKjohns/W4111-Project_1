from wtforms import Form, StringField, PasswordField, SelectField,\
                    TextAreaField, IntegerField, validators
from wtforms.widgets import TextArea

class LoginForm(Form):
    username = StringField('username', [validators.DataRequired()])
    password = PasswordField('password', [validators.DataRequired()])

class RegistrationForm(Form):
    username = StringField('username', [validators.DataRequired()])
    first_name = StringField('first_name', [validators.DataRequired()])
    last_name = StringField('last_name', [validators.DataRequired()])
    password = PasswordField('password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('confirm')

dummy_shows = ['The Fairly Odd Parents', 'Double Dare', 'Boy Meets World']
dummy_shows = [(x, x) for x in dummy_shows]

class AddShowReviewForm(Form):
    show = SelectField('show_name_sid', choices=dummy_shows)   # add choices in controller
    review_text = TextAreaField('review_text', render_kw={"rows": 15, "cols": 70})#widgets=TextArea(row=70, cols=11))
    rating = SelectField('rating', choices=[(i, i) for i in xrange(1,6)])
