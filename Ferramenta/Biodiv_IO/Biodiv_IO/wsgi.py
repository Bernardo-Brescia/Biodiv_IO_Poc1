"""
WSGI config for Biodiv_IO project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Biodiv_IO.settings")

application = get_wsgi_application()
