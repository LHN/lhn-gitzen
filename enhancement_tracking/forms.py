from django.forms import (
    Form, ModelForm, CharField, IntegerField, ModelChoiceField, PasswordInput
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from enhancement_tracking.models import UserProfile, APIAccessData

class NewUserForm(UserCreationForm):
    """Form for creating a new user. Extends django's provided UserCreationForm,
    but removes the help_text from the fields."""
    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password2'].help_text = ''
        self.fields['password2'].label = 'Password Confirmation'

class NewGroupSuperuserForm(NewUserForm):
    """Form for creating a new group superuser. Extends the regular new user
    form, but relabels the username field so that the user knows they are
    creating the group superuser."""
    def __init__(self, *args, **kwargs):
        super(NewGroupSuperuserForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Group Superuser Username'

class APIAccessDataForm(ModelForm):
    """Form for creating a set of access data for the GitHub and Zendesk
    APIs."""
    class Meta:
        model = APIAccessData
        exclude = ('git_token')
        widgets = {
            'zen_token': PasswordInput()
        }

class UserProfileForm(ModelForm):
    """Form to set the two editable fields of a user's profile data."""
    class Meta:
        model = UserProfile
        fields = ('utc_offset', 'view_type')

class ActiveUserSelectionForm(Form):
    """Form for selecting a specific GitZen user's profile. Excludes
    superusers and users who are set as inactive.""" 
    user = ModelChoiceField(queryset=User.objects.\
                            exclude(is_superuser=True).exclude(is_active=False),
                            label='Select User')

class InactiveUserSelectionForm(Form):
    """Form for selecting a specific GitZen user's profile. Excludes superusers
    and users who are set as active."""
    user = ModelChoiceField(queryset=User.objects.\
                            exclude(is_superuser=True).exclude(is_active=True),
                            label='Select User')
