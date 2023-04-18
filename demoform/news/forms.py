from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', )
        widgets = {
            'title' : forms.TextInput(attrs = {'class': 'titleForm'}),
            'content': forms.Textarea(attrs = {'class': 'contentForm'}),
        }


class SendEmail(forms.Form):
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'title'}))
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'zero', 'id': 'content'}))
    cc_email = forms.BooleanField(required=False)
