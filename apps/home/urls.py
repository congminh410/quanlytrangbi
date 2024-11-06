# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('index.html', views.index, name='home'),

    path('them-trang-bi/', views.them_trang_bi, name='them_trang_bi'),
    path('sua-trang-bi/', views.sua_trang_bi, name='sua_trang_bi'),
    path('xoa-trang-bi/', views.xoa_trang_bi, name='xoa_trang_bi'),

    path('them-nhan-vien/', views.them_nhan_vien, name='them_nhan_vien'),
    path('sua-nhan-vien/', views.sua_nhan_vien, name='sua_nhan_vien'),
    path('xoa-nhan-vien/', views.xoa_nhan_vien, name='xoa_nhan_vien'),

    path('them-ban-giao/', views.them_ban_giao, name='them_ban_giao'),
    path('sua-ban-giao/', views.sua_ban_giao, name='sua_ban_giao'),
    path('xoa-ban-giao/', views.xoa_ban_giao, name='xoa_ban_giao'),

    path('them-sua-chua/', views.them_sua_chua, name='them_sua_chua'),
    path('sua-sua-chua/', views.sua_sua_chua, name='sua_sua_chua'),
    path('xoa-sua-chua/', views.xoa_sua_chua, name='xoa_sua_chua'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
]
