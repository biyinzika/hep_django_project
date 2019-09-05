'''
Created on 3 Sep 2019

@author: benjaminsenyonyi
'''
from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1,11)]

class CartAddProductForm(forms.Form):
    '''
    classdocs
    '''
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


    def __init__(self, params):
        '''
        Constructor
        '''
        