from django import forms
from publicaciones.models import Publicaciones

class PublicForm (forms.ModelForm):
	class Meta:
		model = Publicaciones
		fields = '__all__'