from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Profile

User = get_user_model()


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User
        error_messages = {
            "username": {"unique": _("This username has already been taken.")},
        }


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        exclude = ('email',)  # Exclude the email field from the form
    username = forms.CharField(required=True, label="Mobile Phone", max_length=11)


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "name", 
            "father_name", 
            "father_mobile_number",
            "mother_name",
            "mother_mobile_number",
            "district_name", 
            "dob", 
            "party_type",
            "party_designation", 
            "party_join_date", 
            "profession", 
            "education_qualification",
            "present_education", 
            "present_address", 
            "permanent_address", 
            "blood_group", 
            "nationality",
            "religion", 
            "nid", 
            "birth_certificate_number", 
            "profile_picture",
            "signature_picture",
            ]

    # def __init__(self, *args, **kwargs):
    #     super(UserUpdateForm, self).__init__(*args, **kwargs)
    #     if self.instance:
    #         self.fields['jptf_id'].initial = self.calculate_jptf_id()  # Calculate jptf_id for the current user
    
    BANGLADESH_DISTRICTS = [
        ('Bagerhat', 'Bagerhat'),
        ('Bandarban', 'Bandarban'),
        ('Barguna', 'Barguna'),
        ('Barishal', 'Barishal'),
        ('Bhola', 'Bhola'),
        ('Bogra', 'Bogra'),
        ('Brahmanbaria', 'Brahmanbaria'),
        ('Chandpur', 'Chandpur'),
        ('Chapai Nawabganj', 'Chapai Nawabganj'),
        ('Chattogram', 'Chattogram'),
        ('Chuadanga', 'Chuadanga'),
        ('Cumilla', 'Cumilla'),
        ('CoxsBazar', 'CoxsBazar'),
        ('Dhaka', 'Dhaka'),
        ('Dinajpur', 'Dinajpur'),
        ('Faridpur', 'Faridpur'),
        ('Feni', 'Feni'),
        ('Gaibandha', 'Gaibandha'),
        ('Gazipur', 'Gazipur'),
        ('Gopalganj', 'Gopalganj'),
        ('Habiganj', 'Habiganj'),
        ('Jamalpur', 'Jamalpur'),
        ('Jashore', 'Jashore'),
        ('Jhalokati', 'Jhalokati'),
        ('Jhenaidah', 'Jhenaidah'),
        ('Joypurhat', 'Joypurhat'),
        ('Khagrachari', 'Khagrachari'),
        ('Khulna', 'Khulna'),
        ('Kishoreganj', 'Kishoreganj'),
        ('Kurigram', 'Kurigram'),
        ('Kushtia', 'Kushtia'),
        ('Lakshmipur', 'Lakshmipur'),
        ('Lalmonirhat', 'Lalmonirhat'),
        ('Madaripur', 'Madaripur'),
        ('Magura', 'Magura'),
        ('Manikganj', 'Manikganj'),
        ('Meherpur', 'Meherpur'),
        ('Moulvibazar', 'Moulvibazar'),
        ('Munshiganj', 'Munshiganj'),
        ('Mymensingh', 'Mymensingh'),
        ('Naogaon', 'Naogaon'),
        ('Narail', 'Narail'),
        ('Narayanganj', 'Narayanganj'),
        ('Narsingdi', 'Narsingdi'),
        ('Natore', 'Natore'),
        ('Netrokona', 'Netrokona'),
        ('Nilphamari', 'Nilphamari'),
        ('Noakhali', 'Noakhali'),
        ('Pabna', 'Pabna'),
        ('Panchagarh', 'Panchagarh'),
        ('Patuakhali', 'Patuakhali'),
        ('Pirojpur', 'Pirojpur'),
        ('Rajbari', 'Rajbari'),
        ('Rajshahi', 'Rajshahi'),
        ('Rangamati', 'Rangamati'),
        ('Rangpur', 'Rangpur'),
        ('Satkhira', 'Satkhira'),
        ('Shariatpur', 'Shariatpur'),
        ('Sherpur', 'Sherpur'),
        ('Sirajganj', 'Sirajganj'),
        ('Sunamganj', 'Sunamganj'),
        ('Sylhet', 'Sylhet'),
        ('Tangail', 'Tangail'),
        ('Thakurgaon', 'Thakurgaon'),
    ]
    BLOOD_GROUPS = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('Other', 'Other'),
        ('Unknown', 'Unknown')
    ]
    NATIONALITIES = [
        ('Bangladeshi', 'Bangladeshi'),
        ('Afghan', 'Afghan'),
        ('Algerian', 'Algerian'),
        ('American', 'American'),
        ('Bahraini', 'Bahraini'),
        ('British', 'British'),
        ('Canadian', 'Canadian'),
        ('Dutch', 'Dutch'),
        ('Egyptian', 'Egyptian'),
        ('Emirati', 'Emirati'),
        ('Indian', 'Indian'),
        ('Indonesian', 'Indonesian'),
        ('Iranian', 'Iranian'),
        ('Iraqi', 'Iraqi'),
        ('Jordanian', 'Jordanian'),
        ('Kazakh', 'Kazakh'),
        ('Kuwaiti', 'Kuwaiti'),
        ('Lebanese', 'Lebanese'),
        ('Libyan', 'Libyan'),
        ('Malaysian', 'Malaysian'),
        ('Moroccan', 'Moroccan'),
        ('Nigerian', 'Nigerian'),
        ('Omani', 'Omani'),
        ('Pakistani', 'Pakistani'),
        ('Palestinian', 'Palestinian'),
        ('Qatari', 'Qatari'),
        ('Saudi', 'Saudi'),
        ('Somali', 'Somali'),
        ('Sudanese', 'Sudanese'),
        ('Syrian', 'Syrian'),
        ('Tunisian', 'Tunisian'),
        ('Turkish', 'Turkish'),
        ('Uighur', 'Uighur'),
        ('Uzbek', 'Uzbek'),
        ('Yemeni', 'Yemeni'),
        ('Other', 'Other')
    # Add more nationalities as needed...
    ]
    PART_TYPES = [
        ('Jaker Party', 'Jaker Party'),
        ('Jaker Party Teenager Front', 'Jaker Party Teenager Front')
    ]
    RELIGIONS = [
        ('Islam', 'Islam'),
        ('Buddhism', 'Buddhism'),
        ('Christianity', 'Christianity'),
        ('Hinduism', 'Hinduism'),
        ('Judaism', 'Judaism'),
        ('Sikhism', 'Sikhism'),
        ('Other', 'Other')
        # Add other religions as needed
    ]
    name = forms.CharField(required=True, label="Name of User", max_length=255)
    father_name = forms.CharField(required=True, label="Father's Name", max_length=255)
    mother_name = forms.CharField(required=True, label="Mother's Name", max_length=255)
    religion = forms.ChoiceField(choices=RELIGIONS, label='Religion', initial="Islam")
    district_name = forms.ChoiceField(choices=BANGLADESH_DISTRICTS, label='District Name')
    blood_group = forms.ChoiceField(choices=BLOOD_GROUPS, label='Blood Group')
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Date of Birth')
    nationality = forms.ChoiceField(choices=NATIONALITIES, label='ationality', initial='Bangladeshi')  
    party_type = forms.ChoiceField(choices=PART_TYPES, label='Party Type')  
    party_join_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Party Join Date', required=False)
    # jptf_id = forms.CharField(max_length=20, disabled=True)  # Adjust field type and max_length as needed


class CustomUserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """

class UserProfileForm:
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """
    class Meta:
        model = Profile
        fields = ('username', 'password1', 'password2')
