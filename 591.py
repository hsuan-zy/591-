from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 创建WebDriver实例
driver = webdriver.Chrome()
driver.get("https://www.591.com.tw/")

# 等待弹窗出现并选择基隆市
try:
    wait = WebDriverWait(driver, 10)
    # 等待弹出窗口的基隆市选项出现
    keelung_city_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//dd[contains(text(), '基隆市')]")))
    keelung_city_option.click()  # 点击基隆市选项

    time.sleep(3)  # 等待3秒

    # 等待并点击“租屋”链接
    rent_button = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                         "//a[@href='//rent.591.com.tw' and contains(@class, 'gtm-flag') and @google-data-stat='頭部導航_租屋_租屋']")))
    rent_button.click()  # 点击租屋按钮

    # 等待页面加载完成
    time.sleep(3)  # 页面加载可能需要一些时间


    # 为了代码的可读性和易于维护，我们可以创建一个函数来处理点击操作
    def click_district(district_name):
        xpath = f"//ul[@class='town-list clearfix']/li[contains(text(), '{district_name}')]"
        district_element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        district_element.click()
        time.sleep(1)


    # 点击指定的地区
    click_district('中正區')
    click_district('仁愛區')
    click_district('信義區')
    click_district('安樂區')
    click_district('中山區')

# 等待輸入區域顯示
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "vue-filter-list-input")))

    # 使用XPath定位到第二個輸入框
    price_input = driver.find_element(By.XPATH, "(//div[@class='vue-filter-list-input']//input[@class='filter-custom-input'])[2]")
    price_input.clear()  # 清除輸入框中的現有內容
    price_input.send_keys("8500")  # 輸入期望的價格

    # 定位到關聯的提交按鈕並點擊
    submit_button = driver.find_element(By.XPATH, "//div[@class='vue-filter-list-input']//button[@class='filter-custom-submit']")
    submit_button.click()  # 點擊提交按鈕

    # 定位並點擊“展開選項”按鈕以顯示隱藏的選項
    show_more_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='show-more']/div")))
    show_more_button.click()

    # 等待動畫完成，顯示額外的選項
    time.sleep(3)  # 可以調整這裡的等待時間

    elevator_building_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), '電梯大樓')]")))
    elevator_building_option.click()

    # 現在點擊“床”的選項
    bed_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), '床')]")))
    bed_option.click()

    # 使用XPath定位到“排除頂樓加蓋”選項
    exclude_top_floor_option = driver.find_element(By.XPATH, "//li[contains(text(), '排除頂樓加蓋')]")
    exclude_top_floor_option.click()  # 點擊“排除頂樓加蓋”的選項

    # 定位并点击“最新”选项
    latest_option = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//ul[@class='switch-sort']/li[contains(text(), '最新')]")))
    latest_option.click()

except Exception as e:
    print("Error:", e)

input("Press Enter to quit")  # 这会使程序暂停，直到您按下Enter键
driver.quit()  # 然后关闭浏览器
