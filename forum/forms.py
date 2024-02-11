from django import forms
from .models import *


class CreateTopicForm(forms.ModelForm):

    class Meta:
        model = ForumTopic
        fields = ['topic_name', 'description']

        labels = {
            'topic_name': 'Название',
            'description': 'Описание темы'
        }

        widgets = {
            'topic_name': forms.TextInput(attrs={'class': 'form',
                                                 'placeholder': 'Изучение состояния берегозащитных сооружений'}),
            'description': forms.TextInput(attrs={'class': 'form',
                                                  'placeholder': '1 марта был шторм, ищу добровольцев'})
        }


class TakePartForm(forms.ModelForm):

    class Meta:
        model = TopicCallback
        fields = ['email']

        labels = {
            "email": 'Ваш email'
        }

        widgets = {
            'email': forms.EmailInput(attrs={'class':'form', 'placeholder':'example@email.com'})
        }