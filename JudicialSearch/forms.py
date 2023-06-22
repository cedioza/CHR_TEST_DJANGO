from django import forms



class DynamicForm(forms.Form):
    def __init__(self, *args, **kwargs):
        label = kwargs.pop('label', 'Tribunal')
        dynamic_choices = kwargs.pop('dynamic_choices')
        super(DynamicForm, self).__init__(*args, **kwargs)

        choices = [(choice['id'], choice['item']) for choice in dynamic_choices]
        self.fields[label] = forms.ChoiceField(
            label=label,
            choices=choices,
            widget=forms.Select(attrs={'class': 'form-control'}),
            required=False  # Añade el atributo required=False al campo
        )
