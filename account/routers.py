# -*- coding: utf-8 -*-
'''This urls.py is for all API related URLs.

URL Naming Pattern (lowercased & underscored)
<app_name>_<model_name> or
<app_name>_<specific_action>

For base name use:
<app_name>
'''

# Third Party Stuff
from rest_framework import routers
from .api import UserAuthViewSet


# Electric_Soul Stuff
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'register', UserAuthViewSet, base_name='auth')
router.register(r'login', UserAuthViewSet, base_name='auth')

