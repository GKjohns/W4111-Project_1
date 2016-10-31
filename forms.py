from wtforms import Form, StringField, PasswordField, SelectField,\
                    BooleanField, RadioField, validators

class LoginForm(Form):
    username = StringField('username', [validators.DataRequired()])
    password = PasswordField('password', [validators.DataRequired()])
