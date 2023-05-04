from django import forms
from rest_framework_api_key.models import APIKey
from django.contrib.admin.widgets import AdminSplitDateTime, AdminDateWidget
class APIkeyForm(forms.ModelForm):
    # expires = forms.DateTimeField(widget = AdminSplitDateTime())
    class Meta:
        model = APIKey
        fields = ['name', 'revoked']
        # widgets = {
        #     'd': AdminDateWidget()
        # }