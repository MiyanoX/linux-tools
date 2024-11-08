import os
import time
import shutil
import zipfile
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


# 指定ChromeDriver的路径
chrome_driver_path = 'AutoAppDownloader/chromedriver-mac-arm64/chromedriver'  # 请替换为实际的路径

# 设置下载目录
download_folder = os.path.abspath('AutoAppDownloader/installers')
print("Download folder is set to:", download_folder)
if not os.path.exists(download_folder):
  os.makedirs(download_folder)


# # 配置Chrome选项
# options = webdriver.ChromeOptions()
# prefs = {
#     'download.default_directory': os.path.abspath(download_folder),
#     "profile.default_content_settings.popups": 0,
#     "download.prompt_for_download": False,
#     "safebrowsing.enabled": False,  # 禁用安全浏览检查
#     "download_restrictions": 0,
#     "safebrowsing.disable_download_protection": True,  # 禁用下载保护
#     'profile.default_content_setting_values.automatic_downloads': 1,  # 允许自动下载
# }
# options.add_experimental_option("prefs", prefs)
# options.add_argument("--safebrowsing-disable-download-protection")

# # 创建Chrome浏览器实例
# service = Service(chrome_driver_path)
# driver = webdriver.Chrome(service=service, options=options)


from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

# 创建Firefox配置文件
profile = FirefoxProfile()

# 打印下载目录，进行调试
print("Current working directory:", os.getcwd())



# 配置下载目录和行为
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.dir", download_folder)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream,application/pdf,application/x-msdownload")  # 根据需要调整MIME类型
profile.set_preference("pdfjs.disabled", True)  # 禁用内置PDF查看器
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.panel.shown", False)
profile.set_preference("browser.download.useDownloadDir", True)
profile.set_preference("browser.download.viewableInternally.enabledTypes", "")  # 禁用所有内部查看器

# 禁用安全检查
profile.set_preference("browser.safebrowsing.downloads.enabled", False)

# 使用Firefox代替Chrome
firefox_options = FirefoxOptions()
firefox_options.profile = profile

driver = webdriver.Firefox(service=FirefoxService('AutoAppDownloader/firefoxdriver/geckodriver'), options=firefox_options)

'''
windows app download
1. WeCom
2. WeChat
3. Slack
4. VooV
5. AcrobatReader
6. 7-Zip
7. Chrome
'''
def win_7_chrome():
  
    url = 'https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7BA26FB3A3-F8BB-11CE-D91F-BB647E14D7ED%7D%26lang%3Den%26browser%3D4%26usagestats%3D0%26appname%3DGoogle%2520Chrome%26needsadmin%3Dtrue%26ap%3Dx64-stable-statsdef_0%26brand%3DGCGW/dl/chrome/install/googlechromestandaloneenterprise64.msi'

    response = requests.get(url)
    with open('AutoAppDownloader/installers/googlechromestandaloneenterprise64.msi', 'wb') as file:
        file.write(response.content)

    # 重命名文件
    destination_msi = os.path.join(download_folder, "GoogleChromeStandaloneEnterprise64.msi")
    new_file_folder =os.path.join(download_folder, "win")
    
    if not os.path.exists(new_file_folder):
      print(1)
      os.makedirs(new_file_folder)
      
    new_file_name = os.path.join(new_file_folder, "GoogleChrome_win_All.msi")
    os.rename(destination_msi, new_file_name)
    print(f"文件已重命名为: {new_file_name}")
    print("下载过程完成。文件保存在文件夹:", new_file_folder)
    
    
    
'''
mac app download
1. WeCom Apple
2. WeCom Intel
3. WeChat
4. Slack
5. Chrome
6. VooV Apple
7. VooV Intel
'''

def mac_5_chrome():
    url = 'https://dl.google.com/dl/chrome/mac/universal/stable/gcea/googlechrome.dmg'

    response = requests.get(url)
    with open('AutoAppDownloader/installers/googlechrome.dmg', 'wb') as file:
        file.write(response.content)

    # 重命名文件
    destination_file = os.path.join(download_folder, 'googlechrome.dmg')
    new_file_folder =os.path.join(download_folder, "mac")
    
    if not os.path.exists(new_file_folder):
      os.makedirs(new_file_folder)
      
    new_file_name = os.path.join(new_file_folder, "GoogleChrome_mac_All.dmg")

    os.rename(destination_file, new_file_name)
    print(f"文件已重命名为: {new_file_name}")
    print("下载过程完成。文件保存在文件夹:", new_file_folder)

try:
    win_7_chrome()
    mac_5_chrome()

finally:
    # 关闭浏览器
    driver.quit()

