from django import forms
from .models import Post,Vaccine,Eartag,NewEartag,MilkRecord,Customer,Product
from django.contrib.auth.models import User

class CustomerUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['address', 'mobile']
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'breed', 'eartag', 'age','type','weight']

class VaccineForm(forms.ModelForm):
    class Meta:
        model = Vaccine
        fields = ['date_of_vaccination']

class EartagForm(forms.ModelForm):
    class Meta:
        model = Eartag
        fields = ['type','previoustag']

class NewEartagForm(forms.ModelForm):
    class Meta:
        model = NewEartag
        fields = ['name','type','age']

class MilkRecordForm(forms.ModelForm):
    class Meta:
        model = MilkRecord
        fields = ['name','userid','address','date','morning_milk_record','evening_milk_record','payment']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'product_image','price', 'quantity' ]


class AddressForm(forms.Form):
    Email = forms.EmailField()
    Mobile = forms.IntegerField()
    Address = forms.CharField(max_length=500)