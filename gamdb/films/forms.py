from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(required=False, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Pepa z Depa" }))
    text = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows":5, "class":"form-control" }))
    rating = forms.IntegerField(required=False, widget=forms.NumberInput(attrs= {"class":"form-control"}))
    