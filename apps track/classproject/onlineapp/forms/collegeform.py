from django.forms import ModelForm,TextInput,DateInput,EmailInput,CheckboxInput,NumberInput
from onlineapp.models import *

class clgfor(ModelForm):

    class Meta:
        model=College

        fields=['name','location','acronym','contact']
        widgets={
            'name':TextInput(attrs={'class':'input is-primary','placeholder':"write college name"}),
            'location': TextInput(attrs={'class': 'input is-primary', 'placeholder': "give college location"}),
            'contact': TextInput(attrs={'class': 'input is-primary', 'placeholder': "give college contact details"}),
            'acronym': TextInput(attrs={'class': 'input is-primary', 'placeholder': "mention your college acronym"}),
        }
class studentform(ModelForm):
    class Meta:
        model=Student
        fields=['name','email','db_folder','dropped_out']
        widgets={
            'name':TextInput(attrs={'class':'input is-primary','placeholder':"write your name"}),
            'email':EmailInput(attrs={'class':'input is-primary','placeholder':"write your mail"}),
            'db_folder':TextInput(attrs={'class':'input is-primary','placeholder':"write your name"}),
            'dropped_out':CheckboxInput(attrs={'class':'input is-primary'}),
        }


class Mocklistform(ModelForm):
    class Meta:
        model=MockTest1

        fields=['problem1','problem2','problem3','problem4']

        widgets={
            'problem1':NumberInput(attrs={'class':'input is-primary','placeholder':" problem1 marks"}),
            'problem2':NumberInput(attrs={'class':'input is-primary','placeholder':"problem2 marks"}),
            'problem3': NumberInput(attrs={'class': 'input is-primary', 'placeholder': "problem3 marks"}),
            'problem4': NumberInput(attrs={'class': 'input is-primary', 'placeholder': "problem4 marks"}),

        }