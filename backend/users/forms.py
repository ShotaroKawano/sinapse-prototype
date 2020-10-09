from django_registration.forms import RegistrationForm
from .models import CustomUser


#formの存在意義とは？
class CustomUserForm(RegistrationForm):

    class Meta(RegistrationForm.Meta):
        model = CustomUser