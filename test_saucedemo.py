import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Tạo thư mục lưu ảnh chụp màn hình nếu chưa tồn tại
SCREENSHOT_DIR = "screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# ----------------------------------------------------
# Cấu hình WebDriver tự động cho GitHub Codespaces
# ----------------------------------------------------
@pytest.fixture
def setup():
    chrome_options = Options()
    
    # Cấu hình bắt buộc khi chạy trên Linux Server/Codespaces
    chrome_options.add_argument("--headless=new")  # Chạy ngầm không giao diện
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    
    yield driver
    
    driver.quit()

# ----------------------------------------------------
# 05 TEST CASE AUTOMATION
# ----------------------------------------------------

def test_01_login_success(setup):
    """TC01: Kiểm thử Đăng nhập thành công"""
    driver = setup
    driver.get("https://www.saucedemo.com/")

    # Điền Username & Password hợp lệ
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Kiểm tra kết quả
    assert "inventory.html" in driver.current_url
    assert driver.find_element(By.CLASS_NAME, "title").text == "Products"
    
    # Chụp ảnh minh họa
    driver.save_screenshot(os.path.join(SCREENSHOT_DIR, "tc01_login.png"))
    print("\n[PASSED] TC01: Đăng nhập thành công! Ảnh đã lưu vào screenshots/tc01_login.png")


def test_02_login_failure(setup):
    """TC02: Kiểm thử Đăng nhập thất bại"""
    driver = setup
    driver.get("https://www.saucedemo.com/")

    # Điền Username & Password không hợp lệ
    driver.find_element(By.ID, "user-name").send_keys("invalid_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()

    # Kiểm tra thông báo lỗi
    error_element = driver.find_element(By.XPATH, "//h3[@data-test='error']")
    assert error_element.is_displayed()
    assert "Username and password do not match" in error_element.text
    
    # Chụp ảnh minh họa
    driver.save_screenshot(os.path.join(SCREENSHOT_DIR, "tc02_error.png"))
    print("\n[PASSED] TC02: Hiển thị thông báo lỗi chính xác! Ảnh đã lưu vào screenshots/tc02_error.png")


def test_03_add_to_cart(setup):
    """TC03: Thêm một sản phẩm vào giỏ hàng"""
    driver = setup
    driver.get("https://www.saucedemo.com/")

    # Đăng nhập
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Click thêm sản phẩm đầu tiên vào giỏ hàng
    driver.find_element(By.XPATH, "(//button[text()='Add to cart'])[1]").click()

    # Kiểm tra badge giỏ hàng
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "1"
    
    # Chụp ảnh minh họa
    driver.save_screenshot(os.path.join(SCREENSHOT_DIR, "tc03_cart.png"))
    print("\n[PASSED] TC03: Thêm giỏ hàng thành công! Ảnh đã lưu vào screenshots/tc03_cart.png")


def test_04_sort_products(setup):
    """TC04: Sắp xếp sản phẩm theo giá từ Thấp đến Cao"""
    driver = setup
    driver.get("https://www.saucedemo.com/")

    # Đăng nhập
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Chọn Lọc theo giá (Low to High)
    select_element = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    select_element.select_by_value("lohi")

    # Kiểm tra giá sản phẩm đầu tiên
    first_price_text = driver.find_element(By.CLASS_NAME, "inventory_item_price").text
    first_price = float(first_price_text.replace("$", ""))
    assert first_price == 7.99
    
    # Chụp ảnh minh họa
    driver.save_screenshot(os.path.join(SCREENSHOT_DIR, "tc04_sort.png"))
    print("\n[PASSED] TC04: Sắp xếp sản phẩm thành công! Ảnh đã lưu vào screenshots/tc04_sort.png")


def test_05_logout(setup):
    """TC05: Đăng xuất tài khoản"""
    driver = setup
    driver.get("https://www.saucedemo.com/")

    # Đăng nhập
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Mở Menu Sidebar và Click Logout
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    logout_btn = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    )
    logout_btn.click()

    # Kiểm tra đã quay lại trang đăng nhập
    assert driver.find_element(By.ID, "login-button").is_displayed()
    
    # Chụp ảnh minh họa
    driver.save_screenshot(os.path.join(SCREENSHOT_DIR, "tc05_logout.png"))
    print("\n[PASSED] TC05: Đăng xuất thành công! Ảnh đã lưu vào screenshots/tc05_logout.png")