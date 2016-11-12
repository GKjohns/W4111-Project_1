from wtforms import Form, StringField, PasswordField, SelectField,\
                    TextAreaField, IntegerField, validators
from wtforms.widgets import TextArea

class LoginForm(Form):
    username = StringField('username', [validators.InputRequired()])
    password = PasswordField('password', [validators.InputRequired()])

class RegistrationForm(Form):
    username = StringField('username', [validators.InputRequired()])
    first_name = StringField('first_name', [validators.InputRequired()])
    last_name = StringField('last_name', [validators.InputRequired()])
    password = PasswordField('password', [
        validators.InputRequired(),
        validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('confirm', [validators.InputRequired()])

class AddShowReviewForm(Form):
    show = SelectField('show_name_sid')   # add choices in controller
    review_text = TextAreaField('review_text',
        render_kw={"rows": 15, "cols": 70})  #widgets=TextArea(row=70, cols=11))
    rating = SelectField('rating', choices=[(i, i) for i in xrange(1,6)])

class AddEpisodeReviewForm(Form):
    episode = SelectField('episode_name_sid')   # add choices in controller
    review_text = TextAreaField('review_text',
        render_kw={"rows": 15, "cols": 70})  #widgets=TextArea(row=70, cols=11))
    rating = SelectField('rating', choices=[(i, i) for i in xrange(1,6)])
