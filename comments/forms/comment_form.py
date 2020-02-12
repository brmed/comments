from django.forms.models import ModelForm
from comments.models import Comment as CommentModel


class CommentForm(ModelForm):
    class Meta:
        model = CommentModel
        fields = 'message',
