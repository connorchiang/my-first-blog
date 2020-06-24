from django import forms
from .models import Post,Cv

class CvForm(forms.ModelForm):
	
	class Meta:
		model = Cv
		fields = ('title', 'text', 'contact_details', 'educational_background',
			'award', 'research_experience', 'community_services', 'skills')



class PostForm(forms.ModelForm):
	
	class Meta:
		model = Post
		fields = ('title', 'text',)