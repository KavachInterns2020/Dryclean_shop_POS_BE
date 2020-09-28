from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    '''Configuring account adapter to process and save all of the registration form fields'''
    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        
        user.contact_name=data.get('contact_name')
        user.phone=data.get('phone')
        user.shop_name=data.get('shop_name')
        user.shop_address=data.get('shop_address')
        user.gst_number=data.get('gst_number')
        user.save()
        return user