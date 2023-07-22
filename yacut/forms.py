from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional


class URLForm(FlaskForm):
    original_link = URLField(
        'Поле для ссылки',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(1, 512)
        ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[Length(1, 12), Optional()]
    )
    submit = SubmitField('Добавить')
