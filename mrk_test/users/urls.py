from django.urls import path

from mrk_test.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
    user_profile_detail_view,
    user_profile_update_view,
    user_profile_redirect_view
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path("~profile/update/", view=user_profile_update_view, name="update_profile"),
    path("profile/<str:username>/", view=user_profile_detail_view, name="detail_profile"),
    path("profile/redirect/", view=user_profile_redirect_view, name="redirect_profile"),
]
