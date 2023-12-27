from django.forms import ModelForm
from red.models import FormModel
    
class FormForm(ModelForm):
    class Meta:
        model = FormModel
        fields = "__all__"

