# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit
from django import forms

from skystrata.api.models import Template
from django.urls import reverse, resolve


class TemplateForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = Template

    def __init__(self, *args, **kwargs):
        super(TemplateForm, self).__init__(*args, **kwargs)
        # self.helper = FormHelper()
        self.helper.form_method = 'post'


class AddTemplateForm(TemplateForm):
    def __init__(self, *args, **kwargs):
        super(AddTemplateForm, self).__init__(*args, **kwargs)
        self.helper.form_id = 'add-template-form'
        self.helper.form_action = reverse('skystrata.forms:add_template')
        # self.helper.add_input(Submit('new_template', 'Submit'))


class ModifyTemplateForm(TemplateForm):
    def __init__(self, *args, **kwargs):
        super(ModifyTemplateForm, self).__init__(*args, **kwargs)
        self.helper.form_id = 'modify-template-form'
        #self.helper.form_action = reverse('skystrata.forms:modify_template')
        # self.helper.add_input(Submit('modify_template', 'Submit'))


