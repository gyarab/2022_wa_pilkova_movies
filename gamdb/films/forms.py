from django import forms

class CommentForm(forms.form):
    author = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)
    rating = forms.IntegerField()
    