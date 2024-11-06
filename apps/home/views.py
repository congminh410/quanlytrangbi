# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.urls import reverse
from .models import TrangBi, NhanVien, BanGiao, SuaChua
from .forms import TrangBiForm, NhanVienForm, BanGiaoForm, SuaChuaForm
import logging
from datetime import datetime

logger = logging.getLogger('user_activity')

@login_required(login_url="/login/")
def index(request):
    logger.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: User {request.user.username} accessed {request.path}")
    # print(request.user.get_all_permissions())
    groups = list(request.user.groups.values_list('name',flat = True))
    
    if request.user.is_superuser:
            # Nếu là superuser, lấy tất cả dữ liệu
            trang_bi_list = TrangBi.objects.all()
            nhan_vien_list = NhanVien.objects.all()
            ban_giao_list = BanGiao.objects.all()
            sua_chua_list = SuaChua.objects.all()
    else:
        # Lấy thông tin nhân viên từ user đang đăng nhập
        nhan_vien = NhanVien.objects.filter(ten_dang_nhap=request.user.username).first()

        if nhan_vien:
            if 'SQHĐ' in groups:
                # Lọc các bản ghi liên quan đến nhân viên
                trang_bi_list = TrangBi.objects.filter(nguoi_quan_ly=nhan_vien)
                ban_giao_list = BanGiao.objects.filter(ben_giao=nhan_vien) | BanGiao.objects.filter(ben_nhan=nhan_vien)
                sua_chua_list = SuaChua.objects.filter(nguoi_sua=nhan_vien)
            else:
                # Hiển thị tất cả nếu không có nhóm 'SQHĐ'
                trang_bi_list = TrangBi.objects.all()
                ban_giao_list = BanGiao.objects.all()
                sua_chua_list = SuaChua.objects.all()

            # Chỉ hiển thị thông tin của chính user đăng nhập
            nhan_vien_list = [nhan_vien]
        else:
            # Nếu không tìm thấy nhân viên, không hiển thị gì
            trang_bi_list = TrangBi.objects.none()
            ban_giao_list = BanGiao.objects.none()
            sua_chua_list = SuaChua.objects.none()
            nhan_vien_list = NhanVien.objects.none()

    for nhan_vien in nhan_vien_list:
        nhan_vien.so_luong_trang_bi = TrangBi.objects.filter(nguoi_quan_ly=nhan_vien).count()

    trang_bi_list.so_luong_pc = trang_bi_list.filter(loai='PC').count()
    trang_bi_list.so_luong_laptop = trang_bi_list.filter(loai='Laptop').count()
    trang_bi_list.so_luong_thietbimang = trang_bi_list.filter(loai='ThietBiMang').count()

    context = {
        'segment': 'index',
        'trang_bi_list': trang_bi_list,
        'nhan_vien_list': nhan_vien_list,
        'ban_giao_list': ban_giao_list,
        'sua_chua_list': sua_chua_list,
    }
    # if not request.user.has_perm('home.view_trang_bi'):
    #     return render(request, 'home/index_user.html', context)
    return render(request, 'home/index.html', context)

@login_required(login_url="/login/")
def them_trang_bi(request):
    logger.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: User {request.user.username} add TrangBi")
    if request.method == "POST":
        form = TrangBiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))  # Chuyển hướng sau khi lưu thành công
    else:
        form = TrangBiForm()

    context = {
        'segment': 'index',
        'form': form
    }

    return render(request, 'home/index.html', context)

@login_required(login_url="/login/")
def sua_trang_bi(request):
    logger.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: User {request.user.username} change TrangBi")
    if request.method == "POST":
        ma_trang_bi = request.POST.get("ma_trang_bi")
        trang_bi = get_object_or_404(TrangBi, ma_trang_bi=ma_trang_bi)
        form = TrangBiForm(request.POST, instance=trang_bi)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f"{reverse('home')}?tab=trangbi")  # Quay lại trang index sau khi lưu thành công
    return redirect('home')  # Quay lại trang index nếu có lỗi

@login_required(login_url="/login/")
def xoa_trang_bi(request):
    logger.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: User {request.user.username} delete TrangBi")
    if request.method == "POST":
        ma_trang_bi = request.POST.get("ma_trang_bi")
        trang_bi = get_object_or_404(TrangBi, ma_trang_bi=ma_trang_bi)
        trang_bi.delete()
        return redirect('home')  # Quay lại trang index sau khi xóa thành công
    return redirect('home')  # Quay lại trang index nếu có lỗi

@login_required(login_url="/login/")
def them_nhan_vien(request):
    logger.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: User {request.user.username} add NhanVien")
    if request.method == "POST":
        form = NhanVienForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))  # Chuyển hướng sau khi lưu thành công
    else:
        form = NhanVienForm()

    context = {
        'segment': 'index',
        'form': form
    }

    return render(request, 'home/index.html', context)

@login_required(login_url="/login/")
def sua_nhan_vien(request):
    logger.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: User {request.user.username} change NhanVien")
    if request.method == "POST":
        ma_nhan_vien = request.POST.get("ma_nhan_vien")
        nhan_vien = get_object_or_404(NhanVien, ma_nhan_vien=ma_nhan_vien)
        form = NhanVienForm(request.POST, instance=nhan_vien)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f"{reverse('home')}?tab=nhanvien")  # Quay lại trang index sau khi lưu thành công
    return redirect('home')  # Quay lại trang index nếu có lỗi

@login_required(login_url="/login/")
def xoa_nhan_vien(request):
    logger.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: User {request.user.username} delete NhanVien")
    if request.method == "POST":
        ma_nhan_vien = request.POST.get("ma_nhan_vien")
        nhan_vien = get_object_or_404(NhanVien, ma_nhan_vien=ma_nhan_vien)
        nhan_vien.delete()
        return redirect('home')  # Quay lại trang index sau khi xóa thành công
    return redirect('home')  # Quay lại trang index nếu có lỗi

@login_required(login_url="/login/")
def them_ban_giao(request):
    logger.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: User {request.user.username} added BanGiao")
    if request.method == "POST":
        form = BanGiaoForm(request.POST)
        if form.is_valid():
            ban_giao = form.save()
            # Cập nhật người quản lý trong bảng TrangBi
            trang_bi = ban_giao.ma_trang_bi
            trang_bi.nguoi_quan_ly = ban_giao.ben_nhan
            trang_bi.save()
            form.save()
            return redirect(reverse('home'))
    else:
        form = BanGiaoForm()
    context = {'form': form, 'segment': 'index'}
    return render(request, 'home/index.html', context)

@login_required(login_url="/login/")
def sua_ban_giao(request):
    logger.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: User {request.user.username} changed BanGiao")
    if request.method == "POST":
        ma_ban_giao = request.POST.get("ma_ban_giao")
        ban_giao = get_object_or_404(BanGiao, ma_ban_giao=ma_ban_giao)

        # Lưu lại thông tin người nhận cũ
        old_ben_nhan = ban_giao.ben_nhan

        form = BanGiaoForm(request.POST, instance=ban_giao)
        if form.is_valid():
            form.save()
            # Kiểm tra sự thay đổi của ben_nhan và cập nhật lại nguoi_quan_ly trong TrangBi
            trang_bi = ban_giao.ma_trang_bi
            if old_ben_nhan != ban_giao.ben_nhan:
                trang_bi.nguoi_quan_ly = ban_giao.ben_nhan
                trang_bi.save()
            return HttpResponseRedirect(f"{reverse('home')}?tab=bangiao")
    return redirect('home')

@login_required(login_url="/login/")
def xoa_ban_giao(request):
    logger.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: User {request.user.username} deleted BanGiao")
    if request.method == "POST":
        ma_ban_giao = request.POST.get("ma_ban_giao")
        ban_giao = get_object_or_404(BanGiao, ma_ban_giao=ma_ban_giao)
        
        # Lấy thông tin người bàn giao
        trang_bi = ban_giao.ma_trang_bi
        trang_bi.nguoi_quan_ly = ban_giao.ben_giao
        trang_bi.save()

        ban_giao.delete()
        return redirect('home')
    return redirect('home')

@login_required(login_url="/login/")
def them_sua_chua(request):
    logger.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: User {request.user.username} added SuaChua")
    if request.method == "POST":
        form = SuaChuaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    else:
        form = SuaChuaForm()
    context = {'form': form, 'segment': 'index'}
    return render(request, 'home/index.html', context)

@login_required(login_url="/login/")
def sua_sua_chua(request):
    logger.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: User {request.user.username} changed SuaChua")
    if request.method == "POST":
        ma_sua_chua = request.POST.get("ma_sua_chua")
        sua_chua = get_object_or_404(SuaChua, ma_sua_chua=ma_sua_chua)
        form = SuaChuaForm(request.POST, instance=sua_chua)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f"{reverse('home')}?tab=suachua")
    return redirect('home')

@login_required(login_url="/login/")
def xoa_sua_chua(request):
    logger.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: User {request.user.username} deleted SuaChua")
    if request.method == "POST":
        ma_sua_chua = request.POST.get("ma_sua_chua")
        sua_chua = get_object_or_404(SuaChua, ma_sua_chua=ma_sua_chua)
        sua_chua.delete()
        return redirect('home')
    return redirect('home')

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
