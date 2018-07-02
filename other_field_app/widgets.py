from django.forms import widgets


class OtherTextInput(widgets.TextInput):
    is_required = False

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['attrs'].pop('required')
        return context


class OtherSelectorWidget(widgets.MultiWidget):
    template_name = 'widgets/multiwidget.html'

    def __init__(self, choices=None, attrs=None):
        self.choices = choices
        _widgets = (
            widgets.RadioSelect(choices=choices, attrs={'class': 'other_wg_radio_group'}),
            OtherTextInput(attrs={'class': 'hidden_text_group', }, ),
        )
        super().__init__(_widgets, attrs)




    def get_context(self, name, value, attrs):
        con = super().get_context(name, value, attrs)
        con['wrap_label'] = True
        flat_choices = [i for i, j in self.widgets[0].choices]
        # TODO: hide class based on self.name
        con['show_other_inbox'] = not (value in flat_choices or value is None)
        return con

    def decompress(self, value):
        if value:
            bare_choices = [i for i, j in self.choices]
            if value in bare_choices:
                return [value, '']
            else:
                # TODO: fixing other var
                return ['other', value]
        return [None, None, ]

    def format_output(self, rendered_widgets):
        return ''.join(rendered_widgets)

    def value_from_datadict(self, data, files, name):
        radio_data = self.widgets[0].value_from_datadict(data, files, name + '_0')
        text_data = self.widgets[1].value_from_datadict(data, files, name + '_1')
        return [radio_data, text_data]
