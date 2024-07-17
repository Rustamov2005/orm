from django import forms

from book.models import Book


# class BookForm(forms.ModelForm):
#     title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=200)
#     description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     mentor = forms.IntegerField()
#     img = forms.ImageField()
#     price = forms.FloatField()
#     reting = forms.FloatField()

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'discriptions', 'author', 'img', 'count']