from django import forms
from django.core import validators


# # create custom validation method
# def check_for_z(value):
#     if value[0] != 'z':
#         raise forms.ValidationError('NEEDS TO START WITH Z')


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)

    # adds a hidden input invisible to the user that checks for bot access to the wesbite
    # bot_catcher = forms.CharField(required=False,
    #                               widget=forms.HiddenInput,
    #                               validators=[validators.MaxLengthValidator(0),
    #                                           ])  # typical user cannot see this

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH")

            # def clean_bot_catcher(self):
            #     bot_catcher = self.cleaned_data['bot_catcher']
            #     if len(bot_catcher) > 0:
            #         raise forms.ValidationError('GOTCHA, BITCH')
            #     return bot_catcher
