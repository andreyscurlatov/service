from django import forms
from .models import Question


# Create your views here.

class TestForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)

        self.questions = Question.objects.all()

        choice_list=( (True, 'Да'), (False, 'Нет') )

        if self.questions:
            for question in self.questions:
                self.fields['q_%s' % question.pk] = forms.ChoiceField(\
                label=question.text, choices=choice_list,
                widget=forms.RadioSelect, required=True)





