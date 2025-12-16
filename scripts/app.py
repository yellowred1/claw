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

browser = Chromium(co)
page= browser.latest_tab
page.get('https://eu-central-1.run.claw.cloud/signin')
print('---'*50)
print(page.ele('.css-1xigfyl').text)
time.sleep(5)
# 2. 点击 GitHub
page.ele('.chakra-button css-1ggp06u').click()
time.sleep(5)
print('---'*50)
print(page.ele('.authentication ').text)
print('---'*50)
