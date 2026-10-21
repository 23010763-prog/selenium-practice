# BÁO CÁO THỰC HÀNH KIỂM THỬ TỰ ĐỘNG BẰNG SELENIUM WEBDRIVER

---

## 📌 1. THÔNG TIN CHUNG & DỰ ÁN
* **Môn học:** Kiểm thử phần mềm (Software Testing)
* **Công cụ sử dụng:** Python 3, Selenium WebDriver 4, Pytest Framework
* **Môi trường thực thi:** GitHub Codespaces (Cloud Linux Ubuntu Server)
* **Chế độ trình duyệt:** Google Chrome Headless Mode (`--headless=new`)
* **Mã nguồn Repository:** [Link GitHub Repository của bạn]

---

## 🌐 2. THÔNG TIN TRANG WEB KIỂM THỬ (TEST TARGET)
* **Tên ứng dụng:** **SauceDemo (Swag Labs)**
* **Địa chỉ URL:** [https://www.saucedemo.com/](https://www.saucedemo.com/)
* **Mô tả:** Đây là trang web thương mại điện tử tiêu chuẩn được thiết kế bởi Sauce Labs dành riêng cho học tập và thực hành Automation Testing. Trang web bao gồm các chức năng cốt lõi như đăng nhập, quản lý danh mục sản phẩm, bộ lọc, giỏ hàng, đặt hàng và đăng xuất.

### Tài khoản thử nghiệm (Test Credentials):
| Loại tài khoản | Username | Password | Mục đích kiểm thử |
| :--- | :--- | :--- | :--- |
| **Tài khoản đúng (Valid)** | `standard_user` | `secret_sauce` | Kiểm thử các luồng chức năng hợp lệ (TC01, TC03, TC04, TC05) |
| **Tài khoản sai (Invalid)** | `invalid_user` | `wrong_password` | Kiểm thử luồng ngoại lệ / xử lý lỗi (TC02) |

---

## 🛠️ 3. KIẾN TRÚC MÔI TRƯỜNG & CÀI ĐẶT TRÊN GITHUB CODESPACES

Do GitHub Codespaces hoạt động trên máy chủ Cloud Linux không có giao diện đồ họa (GUI), quy trình cài đặt và cấu hình Selenium như sau:

### Các bước chuẩn bị môi trường:
1. **Cài đặt Google Chrome (Bản ổn định):**
   ```bash
   wget [https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb](https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb)
   sudo apt-get update
   sudo apt-get install -y ./google-chrome-stable_current_amd64.deb
   rm google-chrome-stable_current_amd64.deb