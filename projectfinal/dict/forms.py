from django import forms
from .models import Word


class CommentForm(forms.Form):
    comment = forms.CharField(max_length=255,
                              widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'เขียนความคิดเห็นที่นี่...'}))

    def clean_comment(self):
        data = self.cleaned_data['comment']
        return data

class CrudForm(forms.ModelForm):
    
    class Meta:
         model = Word
         fields = ('eentry','tentry','ecat','esyn','eant')
         labels = {
             'eentry' : 'Word',
             'tentry' : 'Meaning',
             'ecat' : 'Category',
             'esyn' : 'Synonym',
             'eant' : 'Antonym',
         }

    def __init__(self, *args, **kwargs):
         super(CrudForm,self).__init__(*args, **kwargs)
         self.fields['esyn'].required = False
         self.fields['eant'].required = False
