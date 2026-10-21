# BÁO CÁO BÀI TẬP THỰC HÀNH KIỂM THỬ TỰ ĐỘNG BẰNG SELENIUM

---

## 🌐 1. TRANG WEB THỰC HÀNH KIỂM THỬ

* **Tên ứng dụng:** **SauceDemo (Swag Labs)**
* **Địa chỉ URL:** [https://www.saucedemo.com/](https://www.saucedemo.com/)
* **Mô tả:** SauceDemo là một website thương mại điện tử mô phỏng do Sauce Labs phát triển dành cho việc đào tạo và thực hành Automation Testing. Trang web bao gồm đầy đủ các tính năng cơ bản: Đăng nhập, danh mục sản phẩm, bộ lọc sắp xếp, giỏ hàng và đăng xuất.

### 📸 Giao diện trang web thực hành (Homepage):
![Giao diện Trang web thực hành SauceDemo](./screenshots/saucedemo_homepage.png)

### 🔑 Thông tin Tài khoản Kiểm thử:
| Loại tài khoản | Username | Password | Mục đích kiểm thử |
| :--- | :--- | :--- | :--- |
| **Hợp lệ (Valid)** | `standard_user` | `secret_sauce` | Thực thi các luồng chức năng đúng (TC01, TC03, TC04, TC05) |
| **Không hợp lệ (Invalid)** | `invalid_user` | `wrong_password` | Thực thi luồng bắt lỗi đăng nhập (TC02) |

---

## 🛠️ 2. MÔI TRƯỜNG & CÔNG CỤ SỬ DỤNG
* **Ngôn ngữ lập trình:** Python 3.14
* **Thư viện Automation:** Selenium WebDriver 4.x
* **Framework quản lý Test:** Pytest
* **Môi trường thực thi:** GitHub Codespaces (Linux Cloud Server)
* **Trình duyệt:** Google Chrome Headless Mode (`--headless=new`)

---

## 📋 3. DANH SÁCH 05 KỊCH BẢN KIỂM THỬ (TEST CASES)

| Mã TC | Tên Kịch Bản | Các Bước Thực Hiện | Định Vị Phần Tử (Locators) | Kết Quả Mong Đợi | Trạng Thái |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **TC01** | Đăng nhập thành công | 1. Nhập username & password đúng.<br>2. Click **Login**. | `user-name`<br>`password`<br>`login-button` | Điều hướng đến URL `inventory.html`, hiển thị tiêu đề **Products**. | **PASSED** |
| **TC02** | Đăng nhập thất bại | 1. Nhập thông tin sai.<br>2. Click **Login**. | `//h3[@data-test='error']` | Hiển thị thông báo lỗi cảnh báo không trùng khớp tài khoản. | **PASSED** |
| **TC03** | Thêm sản phẩm vào giỏ | 1. Đăng nhập.<br>2. Click **Add to cart** sản phẩm 1. | `(//button[text()='Add to cart'])[1]` | Icon giỏ hàng hiển thị badge số lượng bằng **`1`**. | **PASSED** |
| **TC04** | Sắp xếp sản phẩm | 1. Đăng nhập.<br>2. Chọn filter **Price (low to high)**. | `product_sort_container`<br>`inventory_item_price` | Sản phẩm đầu tiên hiển thị mức giá rẻ nhất **`$7.99`**. | **PASSED** |
| **TC05** | Đăng xuất tài khoản | 1. Đăng nhập.<br>2. Mở Menu -> Click **Logout**. | `react-burger-menu-btn`<br>`logout_sidebar_link` | Quay lại trang chủ đăng nhập, xuất hiện lại nút **login-button**. | **PASSED** |

---
Hình ảnh 5 test case:
<img width="1481" height="777" alt="image" src="https://github.com/user-attachments/assets/cc016f5b-8909-40b3-a602-49352500c555" />

test case 1 login

<img width="677" height="531" alt="image" src="https://github.com/user-attachments/assets/c7571e36-1edb-4fe2-865e-018d131aa2c6" />

test case 2 error

<img width="1480" height="760" alt="image" src="https://github.com/user-attachments/assets/a0e6ef33-e52b-4c2d-ab09-a4f70d138594" />

test case 3 cart

<img width="1489" height="789" alt="{D0D78E94-38F2-44C4-9EF0-B5DF78CDD247}" src="https://github.com/user-attachments/assets/bf2e04cc-141e-499f-b7e5-8b5d85a5077d" />

test case 4 sort

<img width="695" height="546" alt="image" src="https://github.com/user-attachments/assets/ca54a6c0-d5d1-41c1-80a6-8ad099907b4f" />

test case 5 logout

## 💻 4. HƯỚNG DẪN THỰC THI KIỂM THỬ

1. **Cài đặt Google Chrome trên Codespaces Terminal:**
   ```bash
   wget [https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb](https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb)
   sudo apt-get update
   sudo apt-get install -y ./google-chrome-stable_current_amd64.deb
   rm google-chrome-stable_current_amd64.deb
