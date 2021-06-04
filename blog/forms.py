from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields= ('name','body')
		widgets = {
			'Name' : forms.TextInput(attrs={'class':'form-control'}),
			'body' : forms.TextInput(attrs={'class':'form-control'}),
		}
