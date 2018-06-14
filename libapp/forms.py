from django import forms
from django.core.exceptions import ValidationError

# form to create new/update a book, I created this here so I can add error msgs and text help
#
class bookForm(forms.Form):
    title = forms.CharField(max_length=200, error_messages={'required': 'Please enter book name'})
    description = forms.CharField(max_length=200, required=False)
    author = forms.CharField(max_length=80)
    pic = forms.CharField(max_length=80, help_text='Please choose from img1,2,3,10-22.jpeg')
    author.widget.attrs['placeholder'] = 'Last name is initial'
    author.widget.attrs['class'] = 'class-example'
    # description.widget.attrs['required'] = False

    # custom validation, will be called if form.is_valid() is true in views.py
    def clean_pic(self):
        img_list = ['img/img1.jpeg', 'img/img2.jpeg', 'img/img3.jpeg', 'img/img9.jpeg', 'img/img10.jpeg', 'img/img11.jpeg', 'img/img12.jpeg', 'img/img13.jpeg', 'img/img14.jpeg', 'img/img15.jpeg', 'img/img16.jpeg', 'img/img17.jpeg', 'img/img18.jpeg', 'img/img19.jpeg', 'img/img20.jpeg', 'img/img21.jpeg', 'img/im22.jpeg']
        pic = self.cleaned_data['pic']
        if pic in img_list:
            print 'good img url ', pic
            return pic
        else:
            raise ValidationError('wrong img url')
