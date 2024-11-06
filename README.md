
# QuanLyTrangBi

Hệ thống cung cấp cơ sở hạ tầng nền tảng cho việc quản lý và kiểm soát các tài sản công nghệ thông tin trong tổ chức. Hệ thống này giúp tổ chức theo dõi, bảo trì và cập nhật các thiết bị, phần mềm, và tài nguyên kỹ thuật số một cách hiệu quả. Điều này đảm bảo hiệu suất hoạt động liên tục và ổn định, tăng cường bảo mật dữ liệu và giảm thiểu rủi ro mất mát hay hư hỏng tài sản. Đồng thời, việc quản lý hiệu quả giúp tối ưu hóa chi phí và cải thiện khả năng ra quyết định thông qua thông tin chi tiết và báo cáo đầy đủ..

## Tính năng
- **Hệ thống xác thực người dùng (authentication)**: Người dùng có thể đăng ký và đăng nhập vào hệ thống.
- **Trang chủ (home)**: Giao diện chính cung cấp thông tin và các chức năng cơ bản của hệ thống.

## Cài đặt

### 1. Clone repository
```bash
git clone https://github.com/congminh410/quanlytrangbi.git
cd quanlytrangbi
```

### 2. Cài đặt các phụ thuộc
Tạo môi trường ảo và cài đặt các phụ thuộc:
```bash
virtualenv env
source env/bin/activate  # Trên Windows dùng `.\env\Scriptsctivate`
pip install -r requirements.txt
```

### 3. Cài đặt cơ sở dữ liệu
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Chạy ứng dụng
```bash
python manage.py runserver
```
Ứng dụng sẽ chạy tại `http://127.0.0.1:8000/`.

## Cấu trúc mã nguồn

- **`quanlytrangbi/`**: Thư mục chính chứa toàn bộ mã nguồn của dự án.
  - **`authentication/`**: Ứng dụng xử lý chức năng đăng ký, đăng nhập và quản lý phiên làm việc của người dùng.
    - Chứa các mẫu (templates) và tệp cấu hình liên quan đến xác thực người dùng.
    - Cung cấp các view để người dùng đăng nhập và đăng ký tài khoản.
  - **`home/`**: Ứng dụng quản lý giao diện chính của hệ thống.
    - Trang quản lý trang bị, cho phép thêm, sửa, xóa trang bị của cá nhân.
    - Trang quản lý nhân viên (đối với quản trị viên của hệ thống).
    - Trang quản lý bàn giao, cho phép ghi lại các thay đổi khi thiết bị được bàn giao.
    - Trang quản lý sửa chữa, cho phép theo dõi quá trình sửa chữa của thiết bị.

## Giấy phép
Dự án này sử dụng giấy phép MIT.

## Đóng góp
Nếu bạn muốn đóng góp cho dự án, vui lòng fork và tạo pull request. Mọi đóng góp đều được hoan nghênh!
