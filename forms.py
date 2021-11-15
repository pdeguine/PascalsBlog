from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email
from flask_ckeditor import CKEditorField


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class CommentForm(FlaskForm):
    comment = CKEditorField("Blog Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")


class RegisterForm(FlaskForm):
    email = StringField("E-Mail address", validators=[DataRequired(), Email()])
    password = PasswordField("Choose a password", validators=[DataRequired()])
    name = StringField("What's your name?", validators=[DataRequired()])
    submit = SubmitField("Register!")


class LoginForm(FlaskForm):
    email = StringField("E-Mail address", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log me in!")
