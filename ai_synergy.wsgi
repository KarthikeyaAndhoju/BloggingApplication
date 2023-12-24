import os
from django.core.wsgi import get_wsgi_application

# Adjust the Python path to include your project's directory
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Production')  # Optional, if you're using django-configurations

# Initialize Django application
application = get_wsgi_application()
