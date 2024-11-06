# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
# from two_factor.urls import urlpatterns as tf_urls

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register

    # path('account/', include(('two_factor.urls', 'two_factor'), namespace='two_factor')),
    # path('account/', include(tf_urls)),

    # Leave `Home.Urls` as last the last line
    path("", include("apps.home.urls"))
]
