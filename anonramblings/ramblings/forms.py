from django.forms import ModelForm, CharField

from .models import Post

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from markdownx.fields import MarkdownxFormField

from captcha.fields import ReCaptchaField


class PostForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-6 mb-0'),
                Column('body', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Submit')
        )

    captcha = ReCaptchaField()
    title = CharField(min_length=3, max_length=255)
    body = MarkdownxFormField(min_length=3, max_length=10000)

    class Meta:
        model = Post
        fields = ['title', 'body', 'captcha']
