from flask_wtf import FlaskForm
from wtforms.fields import (
    TextAreaField,
    SubmitField,
    StringField,
    DateField,
    EmailField,
    PasswordField,
    RadioField,
    FileField,
)
from wtforms.validators import InputRequired, Length
from flask_wtf.file import FileRequired, FileAllowed

ALLOWED_FILE = {"PNG", "JPG", "png", "jpg"}

class DestinationForm(FlaskForm):
    name = StringField(
        "Country", render_kw={"placeholder": "Location"}, validators=[InputRequired()]
    )
    # adding two validators, one to ensure input is entered and other to check if the
    # description meets the length requirements
    description = TextAreaField(
        "Description", validators=[Length(min=6), InputRequired()]
    )
    image = FileField(
        "Cover Image", validators=[FileRequired("Image Necessary"),
        FileAllowed(ALLOWED_FILE, message='Only supports JPG or PNG')]
    )
    currency = StringField("Currency", validators=[InputRequired()])
    submit = SubmitField("Create")


class CommentForm(FlaskForm):
    text = TextAreaField("Comment", [InputRequired()])
    submit = SubmitField("Create")
