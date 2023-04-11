from django import forms
from .models import Product,Issued_Items
class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['asset','sno','name','category','quantity','model','price']

class orderform(forms.ModelForm):
    class Meta:
        model=Issued_Items
        fields=['product','issueditem_quantity','location']

class sendemailform(forms.Form):
    title=forms.CharField(label='Title',max_length=250)
    empemail=forms.EmailField(label='Email id of employee')
    message=forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":25}))