from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "mrk_test.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import mrk_test.users.signals  # noqa: F401
        except ImportError:
            pass
