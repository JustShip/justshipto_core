from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'justshipto_core.accounts'
    label = 'accounts'
    verbose_name = 'User Account'
