from django.db import models
import json
from .widgets import OtherSelectorWidget
from django.forms.fields import MultiValueField, CharField
from otree.common_internal import expand_choice_tuples


class OtherModelField(models.CharField):
    other_value = None
    other_label = None

    def __init__(self, max_length=10000,
                 blank=False,
                 label=None,
                 *args, **kwargs):
        kwargs.update(dict(label=label, ))
        kwargs.setdefault('help_text', '')
        kwargs.setdefault('null', True)
        kwargs.setdefault('verbose_name', kwargs.pop('label'))
        self.other_value = kwargs.pop('other_value', None)
        self.other_label = kwargs.pop('other_label', None)
        self.inner_choices = kwargs.pop('choices', None)
        super().__init__(max_length=max_length, blank=blank, *args, **kwargs)

    def formfield(self, **kwargs):
        return OtherFormField(other_value=self.other_value, other_label=self.other_label, choices=self.inner_choices,
                              label=self.verbose_name,
                              **kwargs)


class OtherFormField(MultiValueField):
    other_value = 'other'
    other_label = 'Other'

    def __init__(self, other_value=None, other_label=None, label='', **kwargs):

        self.choices = kwargs.pop('choices')
        if other_label:
            self.other_label = other_label
        if other_value:
            self.other_value = other_value
        self.choices = list(expand_choice_tuples(self.choices))
        self.choices += [(self.other_value, self.other_label), ]
        self.widget = OtherSelectorWidget(choices=self.choices, other_val=self.other_value)
        fields = (CharField(required=True), CharField(required=False),)
        super().__init__(fields=fields, require_all_fields=False, label=label, **kwargs)

    def compress(self, data_list):
        if data_list[0] == self.other_value:
            return data_list[1]
        else:
            return data_list[0]

    def clean(self, value):
        ret = super().clean(value)
        return ret
