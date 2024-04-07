from django import forms
from books.models import Book
class BookForm(forms.Form):
    title = forms.CharField(label="title", max_length=100,required='true')
    author = forms.CharField(label="author",max_length=100,required='true')
    price = forms.IntegerField(label='price',required='true')
    no_of_page =forms.IntegerField(label='no_of_page',required='true')
    image= forms.ImageField(required=False, label='image')


def clean_code(self):
    code = self.cleaned_data["code"]
    code_found = Book.objects.filter(code=code).exits()
    if code_found:
        raise forms.ValidationError('Code used before , please choose another one')

    return code

class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def clean_code(self):
        code = self.cleaned_data['code']
        code_found = Book.objects.filter(code=code).exists()
        if code_found:
            raise forms.ValidationError('Code used before , please choose another one')
    
        return code

    def clean_name(self):
        title = self.cleaned_data['title']
        if len(title)<2:
            raise forms.ValidationError('Title length must be greater than 2 chars')
        return title

