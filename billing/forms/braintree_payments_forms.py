from django import forms
from django.conf import settings
import braintree

class BraintreePaymentsForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BraintreePaymentsForm, self).__init__(*args, **kwargs)
        test_mode = getattr(settings, "MERCHANT_TEST_MODE", True)
        if test_mode:
            env = braintree.Environment.Sandbox
        else:
            env = braintree.Environment.Production
        braintree.Configuration.configure(
            env,
            settings.BRAINTREE_MERCHANT_ACCOUNT_ID,
            settings.BRAINTREE_PUBLIC_KEY,
            settings.BRAINTREE_PRIVATE_KEY
            )

    transaction__customer__first_name = forms.CharField(max_length=50, required=False)
    transaction__customer__last_name  = forms.CharField(max_length=50, required=False)
    transaction__customer__company    = forms.CharField(max_length=100, required=False)
    transaction__customer__email      = forms.EmailField(required=False)
    transaction__customer__phone      = forms.CharField(max_length=15, required=False)
    transaction__customer__fax        = forms.CharField(max_length=15, required=False)
    transaction__customer__website    = forms.URLField(verify_exists=True, required=False)
    transaction__credit_card__cardholder_name = forms.CharField(max_length=100)
    transaction__credit_card__number  = forms.CharField()
    transaction__credit_card__cvv     = forms.CharField(max_length=4)
    transaction__credit_card__expiration_date = forms.CharField(max_length=7)

    transaction__billing__first_name = forms.CharField(max_length=50, required=False)
    transaction__billing__last_name  = forms.CharField(max_length=50, required=False)
    transaction__billing__company    = forms.CharField(max_length=100, required=False)
    transaction__billing__street_address = forms.CharField(widget=forms.Textarea(), required=False)
    transaction__billing__extended_address = forms.CharField(widget=forms.Textarea(), required=False)
    transaction__billing__locality = forms.CharField(max_length=50, required=False)
    transaction__billing__region   = forms.CharField(max_length=50, required=False)
    transaction__billing__postal_code = forms.CharField(max_length=10, required=False)
    transaction__billing__country_code_alpha2 = forms.CharField(max_length=2, required=False)
    transaction__billing__country_code_alpha3 = forms.CharField(max_length=3, required=False)
    transaction__billing__country_code_numeric = forms.IntegerField(required=False, min_value=0)
    transaction__billing__country_name = forms.CharField(max_length=50, required=False)

    transaction__shipping__first_name = forms.CharField(max_length=50, required=False)
    transaction__shipping__last_name = forms.CharField(max_length=50, required=False)
    transaction__shipping__company = forms.CharField(max_length=100, required=False)
    transaction__shipping__street_address = forms.CharField(widget=forms.Textarea(), required=False)
    transaction__shipping__extended_address = forms.CharField(widget=forms.Textarea(), required=False)
    transaction__shipping__locality = forms.CharField(max_length=50, required=False)
    transaction__shipping__region   = forms.CharField(max_length=50, required=False)
    transaction__shipping__postal_code = forms.CharField(max_length=10, required=False)
    transaction__shipping__country_code_alpha2 = forms.CharField(max_length=2, required=False)
    transaction__shipping__country_code_alpha3 = forms.CharField(max_length=3, required=False)
    transaction__shipping__country_code_numeric = forms.IntegerField(required=False, min_value=0)
    transaction__shipping__country_name = forms.CharField(max_length=50, required=False)

    transaction__options__add_billing_address_to_payment_method = forms.BooleanField(required=False)
    transaction__options__store_shipping_address_in_vault       = forms.BooleanField(required=False)
    transaction__options__store_in_vault_on_success             = forms.BooleanField(required=False)
    transaction__options__submit_for_settlement = forms.BooleanField(required=False)

    transaction__type            = forms.CharField(max_length=10)
    transaction__amount          = forms.DecimalField(required=False)
    transaction__order_id        = forms.CharField(max_length=50)
    transaction__customer__id    = forms.CharField(max_length=50, required=False)
    transaction__credit_card__token = forms.CharField(max_length=50, required=False)
    transaction__payment_method_token = forms.CharField(max_length=50, required=False)

    tr_data = forms.CharField(widget=forms.HiddenInput())
