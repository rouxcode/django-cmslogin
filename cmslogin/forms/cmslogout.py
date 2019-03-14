from __future__ import unicode_literals

from django import forms
from django.contrib.auth import logout
from django.utils.translation import ugettext_lazy as _


class CMSLogoutForm(forms.Form):

    success_url = forms.CharField(
        required=False,
        initial='',
        widget=forms.HiddenInput,
    )
    error_url = forms.CharField(
        required=False,
        initial='',
        widget=forms.HiddenInput,
    )
    formcheck = forms.CharField(
        initial='',
        required=False,
        widget=forms.HiddenInput,
    )

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(CMSLogoutForm, self).__init__(*args, **kwargs)

    def clean_formcheck(self):
        value = self.cleaned_data['formcheck']
        if value:
            raise forms.ValidationError(_('nope'))
        return value

    def is_user(self):
        user = self.request.user
        if user.is_active:
            return True
        return False

    def logout(self):
        logout(self.request)

    def get_success_url(self):
        if self.cleaned_data.get('success_url'):
            return self.cleaned_data.get('success_url')
        return ''

    def get_error_url(self):
        if self.cleaned_data.get('error_url'):
            return self.cleaned_data.get('error_url')
        return ''
