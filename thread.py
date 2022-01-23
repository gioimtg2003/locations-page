import random
import time
from selenium import webdriver
from threading import Thread
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

file = open("diachi.txt", "r", encoding='utf-8')


class web:
    """
    Class web
    """

    def runfirefox(self):
        """
        Khởi động trình duyệt firefox
        """
        self.driver = webdriver.Firefox()

    def loginfacebook(self, user, password):
        """
        Đăng nhập facebook
        """
        print("Loading")
        self.driver.get("https://facebook.com")

        self.driver.implicitly_wait(30)
        # wait time find element

        tk = self.driver.find_element_by_id('email')
        tk.send_keys(user)
        # Enter email

        self.driver.implicitly_wait(30)
        # wait time find element

        mk = self.driver.find_element_by_id('pass')
        mk.send_keys(password)
        # Enter password
        time.sleep(0)
        mk.send_keys(Keys.ENTER)
        # login success
        print(" Login thành công")
        time.sleep(5)

    def set_window(self):
        """
        Cài đặt khung cửa sổ
        """

        self.driver.set_window_size(900, 600)

    def Url_business(self, Url):
        """
        Nhập Url business locations
        """
        self.driver.get(Url)

    def start_auto(self):
        """
        Bắt đầu tự động bước 1
        """
        self.driver.implicitly_wait(30)
        # wait time find element
        self.driver.find_element_by_class_name('_43rm').click()
        # click on addstore

        self.driver.implicitly_wait(30)
        # wait time find element
        self.driver.execute_script(
            'document.querySelector("body > div._10._d2i.uiLayer._4-hy._3qw > div._59s7._9l2g > div > div > div > div > div > div > div._4iyh._2pia._2pi4 > span._4iyi > div > div:nth-child(2) > button > div > div").click()')
        # Next

        self.driver.implicitly_wait(30)
        # wait time find element
        self.driver.find_element_by_css_selector(
            'input[value="ADD_MANUALLY"]').click()
        # click button add manually

        self.driver.implicitly_wait(30)
        # wait time find element

        tiep = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "div._4iyh._2pia._2pi4 span._4iyi div div button._271k._271m._1qjd._7tvm._7tv3._7tv4[style='max-width: 100%; letter-spacing: normal; color: rgb(255, 255, 255); font-size: 14px; font-weight: bold; font-family: Roboto, Arial, sans-serif; line-height: 36px; text-align: center; background-color: rgb(24, 119, 242); border-color: rgb(24, 119, 242); height: 36px; padding-left: 16px; padding-right: 16px; border-radius: 6px; border-width: 0px;']")))
        tiep.click()
        # Next

    def input_address1(self):
        """
        Nhập địa chỉ thứ nhất
        """
        print("Đang nhập địa chỉ thứ nhất")

        self.driver.implicitly_wait(30)
        # wait time find element
        self.driver.find_element_by_xpath(
            '/html/body/div[3]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[4]/div/div[2]/span/input').send_keys('huhu')

        print("Đã nhập thành công địa chỉ thứ nhất")

    def input_address2(self):
        """
        Nhập địa chỉ thứ hai
        """
        print("Đang nhập địa chỉ thứ hai")
        address = file.readline()
        self.driver.implicitly_wait(30)
        # wait time find element
        address_2 = self.driver.find_element_by_xpath(
            '/html/body/div[3]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[5]/span/span/label/input').send_keys(address)
        # click
        time.sleep(1)
        self.driver.implicitly_wait(30)
        # wait time find element
        click_address2 = self.driver.find_element_by_xpath(
            '/html/body/div[3]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[5]/span/span/label/input')
        click_address2.click()
        self.driver.implicitly_wait(30)
        # wait time find element
        enter_address2 = self.driver.find_element_by_xpath(
            '/html/body/div[3]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[5]/span/span/label/input')
        # Enter get address
        time.sleep(1)
        enter_address2.send_keys(Keys.ENTER)
        # Enter address success
        print(f"Nhập thành công địa chỉ: {address}")

    def input_zipcode(self):
        """
        Nhập zipcode...
        """
        print("Đang nhập zipcode")
        zipcode = int(random.randint(33333, 99999))
        self.driver.implicitly_wait(30)
        # wait time find element

        zip_code = self.driver.find_element_by_xpath(
            '/html/body/div[3]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[6]/div/div[2]/span/input')
        zip_code.send_keys(zipcode)
        # Enter zipcode
        print(f"Nhập thành công zipcode: {zipcode}")

    def input_phonenumber(self):
        """
        Nhập số điện thoại
        """
        print("Đang nhập số điện thoại")
        self.driver.implicitly_wait(30)
        # wait time find element
        phonenumber_1 = str(random.randint(3333, 9999))
        phonenumber_2 = "038475" + phonenumber_1
        # Enter phonenumber
        phonenumber = self.driver.find_element_by_xpath(
            '/html/body/div[3]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[7]/div/div[2]/span/input')
        phonenumber.send_keys(phonenumber_2)
        print(f"Đã nhập thành công số điện thoại: {phonenumber_2}")

    def input_danhmuc(self):
        """
        Nhập danh mục..
        """
        print("Nhập danh mục")
        self.driver.execute_script(
            'document.querySelector("body > div._10._d2i.uiLayer._4-hy._3qw > div._59s7._9l2g > div > div > div > div > div > div > div._jmh").scrollBy(0,1000)')
        self.driver.implicitly_wait(30)
        # wait time find element
        danhmuc1 = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(
            By.CSS_SELECTOR, "div._3zzo._58-2.clearfix._3zzo span._58ak._3ct8 input._58al[style='letter-spacing: normal; font-family: Roboto, Arial, sans-serif; color: rgba(0, 0, 0, 0.85); font-size: 14px; line-height: 18px; width: 70px;']"))

        danhmuc1.click()
        danhmuc2 = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(
            By.CSS_SELECTOR, "div._3zzo._58-2.clearfix._3zzo span._58ak._3ct8 input._58al[style='letter-spacing: normal; font-family: Roboto, Arial, sans-serif; color: rgba(0, 0, 0, 0.85); font-size: 14px; line-height: 18px; width: 70px;']"))
        danhmuc2.send_keys(Keys.ENTER)

    def the_end(self):
        """
        Nút kết thúc
        """
        self.driver.implicitly_wait(30)
        # wait time find element
        Theend = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "span._4iyi div div button._271k._271m._1qjd._7tvm._7tv3._7tv4[style='max-width: 100%; letter-spacing: normal; color: rgb(255, 255, 255); font-size: 14px; font-weight: bold; font-family: Roboto, Arial, sans-serif; line-height: 36px; text-align: center; background-color: rgb(24, 119, 242); border-color: rgb(24, 119, 242); height: 36px; padding-left: 16px; padding-right: 16px; border-radius: 6px; border-width: 0px;']")))
        try:
            Theend.click()
        except:
            self.driver.refresh()
            
        time.sleep(7)
        self.driver.refresh()


soluong = int(input("Nhập số trang để chạy: "))
user = str(input("Nhập tài khoản facebook : "))
password = str(input("Nhập mật khẩu : "))
threads = []

def func(number):
    url = str(input(f"Nhập url {number+1}: "))
    run_tool = web()
    run_tool.runfirefox()
    run_tool.set_window()
    run_tool.loginfacebook(user=user, password=password)
    run_tool.Url_business(Url= url)
    for i in range(21):
        print(f"Bắt đầu luồng {number+1}------->")
        run_tool.start_auto()
        print(f"Luồng {number+1}")
        run_tool.input_address1()
        print(f"Luồng {number+1}")
        run_tool.input_address2()
        print(f"Luồng {number+1}")
        run_tool.input_zipcode()
        print(f"Luồng {number+1}")
        run_tool.input_phonenumber()
        run_tool.the_end()
        deplay = int(random.randint(15,20))
        print(f"Luồng {number+1} đã xong lần thứ {i}")
        print(f"Thời gian nghỉ: {deplay}")
        time.sleep(deplay)
        


for number in range(soluong):

    t = Thread(target=func, args={number},)

    time.sleep(2)
    t.start()
    threads.append


for t in threads:
    t.join()



# for i in range(thread):

#     numberaccount = int(input("Nhập số nick facebook muốn chạy: "))
#     user = str(input("Nhập tài khoản facebook: "))
#     password = str(input("Nhập mật khẩu facebook: "))
#     urlpage = str(input("Nhập URL của page locations: "))
