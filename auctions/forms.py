from cProfile import label
from django.db import models
from django.db.models import fields
from django.forms import *
from django.forms import modelform_factory
from PIL import Image


from .models import Comment, User, Card, Category, Rate


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["categorys", ]


class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = '__all__'
        exclude = ["author", ]
        widgets = {
            'title': TextInput(attrs={
                'type': "text",
                'minlength': 3,
                'class': "form-control",
                'id': "floatingInput"
                }),
            'description': Textarea(attrs={
                'cols': 80,
                'rows': 3,
                'maxlength': 300,
                'minlength': 15,
                'class': "form-control",
                'id': "exampleFormControlTextarea1"
                }),
            'price': NumberInput(attrs={
                'min': 1,
                'max': 999999,
                'class': " form-control form-control-sm",
                'id': "inputZip",
                'aria-label': "Amount (to the nearest dollar)"
            }),
            'image': FileInput(attrs={
                'class': "form-control",
                'type':"file",
                'id':"formFile"
            }),
            'category': CheckboxSelectMultiple(attrs={
                'class': "form-select form-select-lg mb-3",
                'aria-label': "Default select example"
            })

            
        }


class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields=['text', ]
        widgets={
            'text': Textarea(attrs={
                'cols': 80,
                'rows': 10,
                'maxlength': 150,
                'minlength': 3

                }),

        }

class RateForm(ModelForm):
    class Meta:
        model=Rate
        fields=["price", ]
        widgets={
            'price': TextInput(attrs={
                'type': "number",
                'min': 1,
                'max': 999999,
                }),

        }

class StatusForm(ModelForm):
    class Meta:
        model=Card
        fields=["status_lot", ]
