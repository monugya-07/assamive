from django.forms import ModelForm
from .models import Comment


class commentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
