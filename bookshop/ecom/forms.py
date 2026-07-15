from django.forms import ModelForm
from ecom.models import Address


class AddressCheckoutForm(ModelForm):
    class Meta:
        model = Address
        exclude = ("user_id",)