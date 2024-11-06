# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

# Register your models here.
from .models import NhanVien, TrangBi, BanGiao, SuaChua

admin.site.register(NhanVien)
admin.site.register(TrangBi)
admin.site.register(BanGiao)
admin.site.register(SuaChua)
