from django import forms
from .models import TrangBi, NhanVien, BanGiao, SuaChua

class TrangBiForm(forms.ModelForm):
    class Meta:
        model = TrangBi
        fields = ['ma_trang_bi', 'ten', 'nguoi_quan_ly', 'tinh_trang', 'loai']

class NhanVienForm(forms.ModelForm):
    class Meta:
        model = NhanVien
        fields = ['ma_nhan_vien', 'ho_ten', 'don_vi', 'vai_tro', 'ten_dang_nhap']

class BanGiaoForm(forms.ModelForm):
    class Meta:
        model = BanGiao
        fields = ['ma_ban_giao', 'ngay', 'ben_giao', 'ben_nhan', 'ma_trang_bi']

class SuaChuaForm(forms.ModelForm):
    class Meta:
        model = SuaChua
        fields = ['ma_sua_chua', 'ngay', 'nguoi_sua', 'noi_dung', 'ma_trang_bi']