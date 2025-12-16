import os
import time

from DrissionPage import Chromium, ChromiumOptions
co = ChromiumOptions()
co.headless(True)
co.set_argument("--headless=new")
co.set_argument("--blink-settings=imagesEnabled=true")
# 额外添加Linux下的浏览器优化参数
co.set_argument("--no-sandbox")
co.set_argument("--disable-dev-shm-usage")
# 可选：设置窗口大小（非无头模式下更友好）
co.set_argument("--window-size=1280,720")
# co.set_browser_path('/opt/google/chrome/google-chrome')

browser = Chromium(co)
page= browser.latest_tab
page.get('https://eu-central-1.run.claw.cloud/signin')
print(page.ele('.css-1xigfyl').text)
time.sleep(5)
# 2. 点击 GitHub
page.ele('.chakra-button css-1ggp06u').click()
time.sleep(5)
print(page.ele('.authentication').text)
