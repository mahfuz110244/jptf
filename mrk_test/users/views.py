from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from .models import Profile
from .forms import UserUpdateForm
from mrk_test.utils.party_id_calculate import calculate_party_id

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    # model = User
    form_class = UserUpdateForm
    # fields = ["name", "father_name", "mother_name", "district_name", "dob"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert self.request.user.is_authenticated  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        print(form.cleaned_data, self.request.user)
        # Calculate jptf_id here (replace with your own calculation logic)
        # jptf_id = calculate_jptf_id(form.cleaned_data['district_name'])
        
        # Add the calculated jptf_id to the form's instance before saving
        form.instance.party_id = calculate_party_id(self.request.user.id, form.cleaned_data['district_name'], form.cleaned_data['party_type'])
        
        # Save the form
        return super().form_valid(form)


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()


class UserProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    slug_field = "user_id"
    slug_url_kwarg = "user_id"


user_profile_detail_view = UserProfileDetailView.as_view()


class UserProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Profile
    fields = ["father_name"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert self.request.user.is_authenticated  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


user_profile_update_view = UserProfileUpdateView.as_view()


class UserProfileRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail_profile", kwargs={"username": self.request.user.username})


user_profile_redirect_view = UserProfileRedirectView.as_view()
