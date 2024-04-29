from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class Userform(FlaskForm):

    title = StringField(
        "제 목",
        validators=[DataRequired(message="제목을 적어주세요"),Length(max=30, message="30자 이내로 작성바랍니다.")],
    )
    author = StringField(
        "작 가",
        validators=[DataRequired(message="작가명을 적어주세요")],
    )
    genre = StringField(
        "장 르",
        validators=[DataRequired(message="장르를 적어주세요")],
    )
    link = StringField(
        "링크주소",
        validators=[DataRequired(message="링크주소를 적어주세요")],
    )

    submit = SubmitField("UpDate!")
    