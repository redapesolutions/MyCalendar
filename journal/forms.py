from django import forms
from django.forms import ModelForm
from .models import Plans
from django.utils.translation import ugettext_lazy as _

class PlansForm(forms.ModelForm):
	class Meta:
		model = Plans
		fields = "__all__"
		labels = {
			'date': _("Chose"),
            'activity': _("Name it:"),
			'description': _("Describe it:")
        }
		help_texts = {
			'significance': _("Importants will appear first on the list")
		}
		widgets = {
			'date': forms.SelectDateWidget()
		}
	
class UpdateForm(forms.ModelForm):
	class Meta:
		model = Plans
		exclude = ["date"]