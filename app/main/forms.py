from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, validators
from wtforms.validators import ValidationError, DataRequired, Length
from flask_babel import _, lazy_gettext as _l
from app.models import User

#Brandon Mailloux - 2023-02-25
#Created two new validators to prevent users from making too complex or malicious username changes

#Added a validator to not allow special chars for HTML injection
def no_angle_brackets(form, field):
    if '<' in field.data or '>' in field.data:
        raise validators.ValidationError('Username cannot contain "<" or ">" characters')

#Added a validator to not allow spaces to make usernames more uniform
def no_spaces(form, field):
    if ' ' in field.data:
        raise validators.ValidationError('Username cannot contain a space')

class EditProfileForm(FlaskForm):
    #Added ristrictions to username length aswell.
    username = StringField(_l('Username'), validators=[DataRequired(), no_angle_brackets, no_spaces, Length(min=0, max=100)])
    about_me = TextAreaField(_l('About me'),
                             validators=[Length(min=0, max=140)])
    submit = SubmitField(_l('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_('Please use a different username.'))


class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    post = TextAreaField(_l('Say something'), validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))


class SearchForm(FlaskForm):
    q = StringField(_l('Search'), validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args
        if 'meta' not in kwargs:
            kwargs['meta'] = {'csrf': False}
        super(SearchForm, self).__init__(*args, **kwargs)


class MessageForm(FlaskForm):
    message = TextAreaField(_l('Message'), validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField(_l('Submit'))


