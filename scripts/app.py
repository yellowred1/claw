import os
import time

from DrissionPage import Chromium, ChromiumOptions
co = ChromiumOptions()
co.headless(True)
co.set_argument("--headless=new")
co.set_argument("--blink-settings=imagesEnabled=true")
co.set_argument("--no-sandbox")
co.set_argument("--disable-dev-shm-usage")
co.set_argument("--window-size=1280,720")

GH_USERNAME=''
GH_PASSWORD=''

browser = Chromium(co)
page= browser.latest_tab
page.get('https://eu-central-1.run.claw.cloud/signin')
print(page.ele('.chakra-button css-1ggp06u').text)
print(page.wait.ele_displayed('.chakra-button css-1ggp06u'))
page.ele('.chakra-button css-1ggp06u').click()
if 'github.com/login' in page.url:
    # print(page.ele('.authentication ').text)
    print(page.wait.ele_displayed('.form-control  js-login-field'))
    page.ele('.form-control  js-login-field').input(GH_USERNAME)
    page.ele('.form-control form-control js-password-field').input(GH_PASSWORD)
    page.ele('.btn btn-primary btn-block js-sign-in-button').click()
    time.sleep(5)
    if 'github.com/sessions/verified-device' in page.url:
        print('github需要验证码')
        print(page.ele('.Box mt-3 color-bg-subtle').text)
        page.ele('.form-control input-block js-verification-code-input-auto-submit').clear().input(input('请输入验证码:'))
else:
    print('github登入成功')


browser.quit()
