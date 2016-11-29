
# -*- coding: utf-8 -*-

from django.db import migrations, models
from django.core.management import call_command
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_migrate

def loadfixture(apps, schema_editor):
    call_command('loaddata', 'initial_data.json')

def setup_login_app(sender, **kwargs):
    """
    `allauth` needs tokens for OAuth based providers. So let's
    setup some dummy tokens
    """
    from allauth.socialaccount.providers import registry
    from allauth.socialaccount.models import SocialApp
    from allauth.socialaccount.providers.oauth.provider import OAuthProvider
    from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider
    from django.contrib.sites.models import Site

    site = Site.objects.get_current()
    for provider in registry.get_list():
        if (isinstance(provider, OAuth2Provider)
                or isinstance(provider, OAuthProvider)):
            try:
                SocialApp.objects.get(provider=provider.id,
                                      sites=site)
            except SocialApp.DoesNotExist:
                print ("Installing dummy application credentials for %s.")
                app = SocialApp.objects.create(
                    provider=provider.id,
                    secret='a_eOTgioHCkx1zQ262dMLdUC',
                    client_id='889465312167-v5lgmcjdmpq2h3rvmk2u3o58en47s0is.apps.googleusercontent.com',
                    name='%s app' % provider.id)
                app.sites.add(site)
class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(loadfixture),
    ]
class DemoConfig(AppConfig):
    name = 'labgauth'
    verbose_name = _('labgauth')

    def ready(self):
        post_migrate.connect(setup_login_app, sender=self)