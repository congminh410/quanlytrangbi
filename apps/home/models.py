# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Bảng Nhân viên
class NhanVien(models.Model):
    ma_nhan_vien = models.CharField(max_length=10, primary_key=True)
    ho_ten = models.CharField(max_length=100)
    don_vi = models.CharField(max_length=100)
    vai_tro = models.CharField(max_length=50)
    ten_dang_nhap = models.CharField(max_length=50, default=None, null=True, blank=True)

    def __str__(self):
        return self.ho_ten

# Bảng Trang bị
class TrangBi(models.Model):
    LOAI_LUA_CHON = [
        ('PC', 'PC'),
        ('Laptop', 'Laptop'),
        ('ThietBiMang', 'Thiết bị mạng'),
    ]

    ma_trang_bi = models.CharField(max_length=10, primary_key=True)
    ten = models.CharField(max_length=100)
    nguoi_quan_ly = models.ForeignKey(NhanVien, on_delete=models.SET_NULL, null=True, related_name='quan_ly_trang_bi')
    tinh_trang = models.CharField(max_length=50)
    loai = models.CharField(max_length=20, choices=LOAI_LUA_CHON)

    def __str__(self):
        return self.ten

# Bảng Bàn giao
class BanGiao(models.Model):
    ma_ban_giao = models.CharField(max_length=10, primary_key=True)
    ngay = models.DateField()
    ben_giao = models.ForeignKey(NhanVien, on_delete=models.CASCADE, related_name='ban_giao')
    ben_nhan = models.ForeignKey(NhanVien, on_delete=models.CASCADE, related_name='nhan_giao')
    ma_trang_bi = models.ForeignKey(TrangBi, on_delete=models.CASCADE)

    def __str__(self):
        return f"Bàn giao {self.ma_ban_giao}"

# Bảng Sửa chữa
class SuaChua(models.Model):
    ma_sua_chua = models.CharField(max_length=10, primary_key=True)
    ngay = models.DateField()
    nguoi_sua = models.ForeignKey(NhanVien, on_delete=models.CASCADE, related_name='sua_chua')
    noi_dung = models.TextField()
    ma_trang_bi = models.ForeignKey(TrangBi, on_delete=models.CASCADE)

    def __str__(self):
        return f"Sửa chữa {self.ma_sua_chua}"

