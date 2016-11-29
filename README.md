#Installation Guide
It is assumed the reader of this documentation has a basic understanding of Docker and Django.

 1. Install docker-compose
	`docker-compose up --build`
 2. Migrate database (do each time schema changes)
	 `docker-compose run --rm web python manage.py migrate`
 3. Default user is created admin/oooxxxooo
 4. Navigate to localhost:8000/admin - Google does not accept 0.0.0.0
 5. After logging in with gauth, assign staff to your user account

**settings.py**

    #For Django 1.7, use:
    TEMPLATE_CONTEXT_PROCESSORS = (
        ...
        # Required by `allauth` template tags
        'django.core.context_processors.request',
        ...
    )
    #If you are running Django 1.8+, specify the context processors as follows:

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    # Already defined Django-related contexts here

                    # `allauth` needs this from django
                    'django.template.context_processors.request',
                ],
            },
        },
    ]
    LOGIN_REDIRECT_URL = '/admin'
    
	AUTHENTICATION_BACKENDS = (
    ...
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    ...
	)

	INSTALLED_APPS = [
	'django.contrib.sites',
	'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    # keep labgauth above admin to use included templates
    'labgauth',
    'django.contrib.admin',
	]

**requirements.txt**
> django-allauth

**urls.py**

	urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
	]

If no current social login found, default social application is created.

