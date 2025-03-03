from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["username", "user_email", "text"]
        # exclude = ["post"]
        labels = {
            "username": "Your Name",
            "user_email": "Your Email",
            "text": "Enter Your Comment",
        }
