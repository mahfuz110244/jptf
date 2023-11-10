from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ForeignKey, CASCADE, DateField, ImageField, BooleanField, BigIntegerField, TextField, DecimalField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator



class User(AbstractUser):
    """
    Default custom user model for mrk test.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """
    
    # First and last name do not cover name patterns around the globe
    username = CharField(_("Mobile Number"), max_length=11, unique=True)
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    father_name = CharField(_("Father's Name"), blank=True, max_length=255)
    father_mobile_number = CharField(_("Father's Mobile Number"), blank=True, max_length=11)
    mother_name = CharField(_("Father's Name"), blank=True, max_length=255)
    mother_mobile_number = CharField(_("Mother's Mobile Number"), blank=True, max_length=11)
    district_name = CharField(_("District's Name"), blank=True, max_length=255)
    dob = DateField(_("Date of Birth"), blank=True, null=True)
    party_type = CharField(_("Party Type"), blank=True, max_length=255)
    party_id = CharField(_("Party ID"), blank=True, max_length=255)
    party_designation = CharField(_("Party Designation"), blank=True, max_length=255)
    party_join_date = DateField(_("Party Join Date"), blank=True, null=True)
    profession = CharField(_("Profession"), blank=True, max_length=255)
    education_qualification = CharField(_("Education Qualification"), blank=True, max_length=255)
    present_education= CharField(_("Present Education"), blank=True, max_length=255)
    present_address = TextField(_("Present Address"), blank=True, max_length=500)
    permanent_address = TextField(_("Permanent Address"), blank=True, max_length=500)
    blood_group = CharField(_("Blood Group"), blank=True, max_length=255)
    nationality = CharField(_("Nationality"), blank=True, max_length=255)
    religion = CharField(_("Religion"), blank=True, max_length=255)
    nid = BigIntegerField(_("NID"), blank=True, null=True)
    birth_certificate_number = BigIntegerField(_("Birth Certificate Number"), blank=True, null=True)
    profile_picture = ImageField(upload_to='profile_pictures/', null=True, blank=True)
    signature_picture = ImageField(upload_to='signature_pictures/', null=True, blank=True)
    is_verified = BooleanField(_("Is Verified"), default=False)


    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
    
    class Meta:
        # db_table = 'users'
        verbose_name_plural = 'Users'
        verbose_name = 'User'


class Profile:
    """
    Default custom user profile model for mrk test.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """
    user_id = ForeignKey(User, related_name='user_profile', on_delete=CASCADE, blank=False, verbose_name='User Profilr')
    father_name = CharField(_("Father's Name"), blank=True, max_length=255)
    mother_name = CharField(_("Father's Name"), blank=True, max_length=255)

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("profiles:detail", kwargs={"user_id": self.user_id})

    class Meta:
        db_table = 'profiles'
        verbose_name_plural = 'profiles'
        verbose_name = 'Profiles'
