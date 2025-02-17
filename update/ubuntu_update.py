import pandas as pd
print(pd.__version__)
import os
from tqdm import tqdm
import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time
import tempfile
import shutil
import json
import socket
import re

def get_local_ip():
    try:
        # 创建一个 UDP 套接字，不实际发送数据
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # 使用外部地址确保可以访问
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address
    except Exception as e:
        return f"Error: {e}"
    
print("Local IP Address:", get_local_ip())


def update_server_ip():
    """更新 Software_List_v2.csv 中的服务器IP地址"""
    try:
        # 使用之前定义的get_local_ip()函数获取实际可用的IP
        local_ip = get_local_ip()
        if not local_ip or local_ip.startswith('Error:'):
            print(f"获取本地IP失败: {local_ip}")
            return False
            
        csv_path = '/var/www/files/oitqs/software/update/Software_List_v2.csv'
        # 首先读取文件内容
        with open(csv_path, 'r') as file:
            content = file.read()
            
        # 查找当前URL中的IP地址
        ip_pattern = r'http://(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/'
        match = re.search(ip_pattern, content)
        if not match:
            print("在CSV文件中未找到IP地址")
            return False
            
        current_ip = match.group(1)
        
        # 如果IP相同，无需更新
        if current_ip == local_ip:
            print(f"当前IP ({current_ip}) 无需更新")
            return True
            
        # 更新文件内容
        new_content = content.replace(f'http://{current_ip}/', f'http://{local_ip}/')
        
        # 写入更新后的内容
        with open(csv_path, 'w') as file:
            file.write(new_content)
            
        print(f"已将服务器IP从 {current_ip} 更新为 {local_ip}")
        
        # 同时更新目标目录的文件
        target_path = '/var/www/files/oitqs/Software_List_v2.csv'
        with open(target_path, 'w') as file:
            file.write(new_content)
            
        print(f"已同步更新 {target_path}")
        return True
        
    except Exception as e:
        print(f"更新服务器IP时出错: {str(e)}")
        return False
    
# 更新服务器IP
update_server_ip()

class ProgressCallback:
    def __init__(self, filename, filesize):
        self.pbar = tqdm(total=filesize, unit='B', unit_scale=True, desc=filename)
    
    def __call__(self, transferred, remaining):
        self.pbar.update(transferred - self.pbar.n)
    
    def close(self):
        self.pbar.close()
        
# 定义一个函数来处理文件名和版本号的拼接
def append_version(filename, version):
    name, ext = os.path.splitext(filename)
    new_filename = f"{name}_{version}{ext}"
    return new_filename
  
# 从网页获取软件最新版本信息
def get_latest_version_from_web(url):
    try:
        print(f"正在获取最新版本: {url}")
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        # 这里需要根据实际网页结构编写解析逻辑
        # 示例：version = soup.find('div', class_='version').text.strip()
        # print(soup)
        version = soup.find('div', class_='version').text.strip()
        print(f"获取最新版本: {version}")
        return version
    except Exception as e:
        print(f"获取最新版本时出错: {str(e)}")
        return None
      

def extract_version_from_filename(filename):
    """从文件名中提取版本号"""
    try:
        # 对于 WeCom_4.1.30.6008.exe 这样的格式
        parts = filename.split('_')
        if len(parts) > 1:
            version = parts[1].split('.exe')[0]  # 获取 4.1.30.6008
            return version
    except Exception as e:
        print(f"提取版本号时出错: {str(e)}")
    return None
  
def get_filename_from_url(url):
    if '7-zip' in url:
        # 找到 filename%3D 后的文件名部分
        filename_start = url.find('filename%3D') + len('filename%3D')
        filename_end = url.find('&', filename_start)
        if filename_end == -1:
            filename = url[filename_start:]
        else:
            filename = url[filename_start:filename_end]
        # URL解码
        return unquote(filename)
    
    return url.split('/')[-1]
  

def get_real_download_url(url):
    """使用 Selenium 获取真实下载链接"""
    driver = None
    try:
        temp_dir = tempfile.mkdtemp()
        
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument(f'--user-data-dir={temp_dir}')
        chrome_options.add_argument('--disable-dev-shm-usage')
        
        # 设置 Windows 的 User-Agent
        windows_ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        chrome_options.add_argument(f'user-agent={windows_ua}')
        
        # 设置 Windows 平台
        chrome_options.add_argument('--platform=Windows')
        chrome_options.add_experimental_option('prefs', {
            'profile.default_content_settings.plugins': 1,
            'profile.content_settings.plugin_whitelist.adobe-flash-player': 1,
            'profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player': 1,
            'intl.accept_languages': 'en-US,en'
        })
        
        # 启用性能日志记录
        chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        
        service = webdriver.ChromeService()
        driver = webdriver.Chrome(options=chrome_options, service=service)
        
        # Chrome Enterprise Windows 版本特殊处理
        if 'chromeenterprise.google' in url and 'WIN64_MSI' in url:
            # Chrome Enterprise Windows 版本的直接下载链接
            direct_url = "https://dl.google.com/dl/chrome/install/GoogleChromeStandaloneEnterprise64.msi"
            print(f"找到 Chrome Enterprise Windows 下载链接: {direct_url}")
            return direct_url
            
        driver.get(url)
        time.sleep(5)  # 等待页面加载
        
        # 获取所有网络请求
        logs = driver.get_log('performance')
        download_url = None
        
        for entry in logs:
            try:
                log = json.loads(entry['message'])['message']
                if ('Network.requestWillBeSent' in log['method'] or 
                    'Network.responseReceived' in log['method']):
                    if 'params' in log and 'request' in log['params']:
                        url = log['params']['request'].get('url', '')
                    elif 'params' in log and 'response' in log['params']:
                        url = log['params']['response'].get('url', '')
                    else:
                        continue
                        
                    if url.endswith(('.dmg', '.exe')):
                        print(f"找到下载链接: {url}")
                        download_url = url
                        break
            except Exception as e:
                continue
        
        return download_url
            
    except Exception as e:
        print(f"获取下载链接时出错: {str(e)}")
        return None
    
    finally:
        try:
            if driver:
                # 强制结束 Chrome 进程
                driver.service.process.kill()
                
                # 清理临时文件
                if temp_dir and os.path.exists(temp_dir):
                    shutil.rmtree(temp_dir, ignore_errors=True)
                
                # 查找并结束所有相关的 Chrome 进程
                if os.name == 'nt':  # Windows
                    os.system('taskkill /f /im chrome.exe')
                    os.system('taskkill /f /im chromedriver.exe')
                else:  # Linux/Mac
                    os.system('pkill -f chrome')
                    os.system('pkill -f chromedriver')
        except:
            pass


def download_file(index, url, save_path, platform):
    """
    下载文件并显示进度条
    Args:
        url: 下载链接
        save_path: 保存路径（包含文件名）
    """
    try:
        # 如果是 VooV Meeting or Chrome or Adobe 的下载页面
        if 'voovmeeting' in url or 'chrome' in url or 'adobe' in url:
            real_url = get_real_download_url(url)
            if real_url:
                url = real_url
            else:
                raise Exception("无法获取真实下载链接")
        
        # 其余下载代码保持不变
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, stream=True, headers=headers, allow_redirects=True)
        response.raise_for_status()
                
        # 从最终 URL 中获取文件名
        final_url = response.url
        print(f"final_url: {final_url}")
        filename = get_filename_from_url(final_url)  # 获取 URL 最后一部分作为文件名
        
        # 提取版本号
        version = extract_version_from_filename(filename)
        if version:
            print(f"检测到版本号: {version}")
            # 这里可以更新 CSV 中的版本信息
            
        # save_path = os.path.join(os.path.dirname(save_path), filename)
        
        total_size = int(response.headers.get('content-length', 0))

        # 使用tqdm显示下载进度
        with open(save_path, 'wb') as f:
            with tqdm(total=total_size, unit='B', unit_scale=True, desc=os.path.basename(save_path)) as pbar:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        pbar.update(len(chunk))
        print(f"文件下载完成: {save_path}")
        
        # 更新成功修改 version_control csv 文件的 origin_name
        version_control_change = pd.read_csv('/var/www/files/oitqs/software/update/version_control.csv')
        version_control_change.loc[index, 'origin_name'] = filename
        version_control_change.loc[index, 'update_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        version_control_change.to_csv('/var/www/files/oitqs/software/update/version_control.csv', index=False)
        
        print(f"url: {url}")
        print(f"platform: {platform}")
        if ('meeting' in url) and (platform == 'mac'):
            # 去掉 .dmg 扩展名
            filename_without_ext = os.path.splitext(filename)[0]
            print(f"更新 Software_List_v2.csv 文件的 volumn_name: {filename_without_ext}")
            software_list_change = pd.read_csv('/var/www/files/oitqs/software/update/Software_List_v2.csv')
            software_list_change.loc[index, 'volumn_name'] = filename_without_ext
            software_list_change.to_csv('/var/www/files/oitqs/software/update/Software_List_v2.csv', index=False, lineterminator='\n')
            file_data = open('/var/www/files/oitqs/software/update/Software_List_v2.csv', 'rb').read()
            open('/var/www/files/oitqs/software/update/Software_List_v2.csv', 'wb').write(file_data[:-2])
        
        return True
    except Exception as e:
        print(f"下载文件时出错: {str(e)}")
        return False

# Load the version_control list
version_control = pd.read_csv('/var/www/files/oitqs/software/update/version_control.csv')

# 在上传文件之前，先更新最新版本信息
# for _, row in software_list.iterrows():
#     url = row.get('website')  # 需要在 CSV 中添加此列
#     if url and row['filename'] == '7-Zip_win_All.exe':
#         latest_version = get_latest_version_from_web(url)
#         print(f"最新版本: {latest_version}")
#         if latest_version:
#             software_list.loc[_, 'latest version'] = latest_version
        
# 根据 download_url 的参数，获取最新的版本
for index, row in version_control.iterrows():
    download_url = row.get('download_url')
    print(f"filename: {row['filename']}")
    if download_url:
      
        # 确保目标文件夹存在
        save_dir = os.path.join('/var/www/files/oitqs/software/update/software/', row['platform'])
        os.makedirs(save_dir, exist_ok=True)
        # 构建保存路径
        save_path = os.path.join(save_dir, row['filename'])
        print(f"开始下载: {download_url}")
        print(f"保存到: {save_path}")
        download_file(index,download_url, save_path, row['platform'])
        
# 处理 ioa 文件
print("开始处理 ioa 文件...")
for index, row in version_control.iterrows():
    if 'ioa' in row['filename'].lower():
        source_dir = '/var/www/files/oitqs/software/update/software/ioa/'
        target_platform_dir = f"/var/www/files/oitqs/software/update/software/{row['platform']}"
        
        # 确保目标目录存在
        os.makedirs(target_platform_dir, exist_ok=True)
        
        # 根据平台选择文件扩展名
        file_extension = '.pkg' if row['platform'] == 'mac' else '.exe'
        
        # 在源目录中查找对应扩展名的文件
        try:
            for file in os.listdir(source_dir):
                if file.endswith(file_extension):
                    source_path = os.path.join(source_dir, file)
                    target_path = os.path.join(target_platform_dir, row['filename'])
                    
                    print(f"复制文件: {source_path} -> {target_path}")
                    shutil.copy2(source_path, target_path)
                    print(f"成功复制 ioa 文件到 {row['platform']} 目录")
                    
                    # 更新成功修改 version_control csv 文件的 origin_name
                    version_control_change = pd.read_csv('/var/www/files/oitqs/software/update/version_control.csv')
                    version_control_change.loc[index, 'origin_name'] = file
                    version_control_change.loc[index, 'update_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    version_control_change.to_csv('/var/www/files/oitqs/software/update/version_control.csv', index=False)
                    
                    break
            else:
                print(f"在 {source_dir} 中未找到 {file_extension} 文件")
        except Exception as e:
            print(f"处理 ioa 文件时出错: {str(e)}")

# 在最后添加以下代码
print("开始复制文件到目标目录...")

try:
    # 确保目标目录存在
    os.makedirs('/var/www/files/oitqs/software/mac', exist_ok=True)
    os.makedirs('/var/www/files/oitqs/software/win', exist_ok=True)

    # 复制 mac 目录下的文件
    mac_source = '/var/www/files/oitqs/software/update/software/mac/'
    mac_dest = '/var/www/files/oitqs/software/mac/'
    for file in os.listdir(mac_source):
        source_path = os.path.join(mac_source, file)
        dest_path = os.path.join(mac_dest, file)
        print(f"正在复制: {source_path} -> {dest_path}")
        shutil.copy2(source_path, dest_path)
        print(f"复制完成: {source_path} -> {dest_path}")

    # 复制 win 目录下的文件
    win_source = '/var/www/files/oitqs/software/update/software/win/'
    win_dest = '/var/www/files/oitqs/software/win/'
    for file in os.listdir(win_source):
        source_path = os.path.join(win_source, file)
        dest_path = os.path.join(win_dest, file)
        print(f"正在复制: {source_path} -> {dest_path}")
        shutil.copy2(source_path, dest_path)
        print(f"复制完成: {source_path} -> {dest_path}")

    # 复制 Software_List_v2.csv
    csv_source = '/var/www/files/oitqs/software/update/Software_List_v2.csv'
    csv_dest = '/var/www/files/oitqs/Software_List_v2.csv'
    print(f"正在复制: {csv_source} -> {csv_dest}")
    shutil.copy2(csv_source, csv_dest)
    print(f"复制完成: {csv_source} -> {csv_dest}")
    
    print("所有文件复制完成")

except Exception as e:
    print(f"复制文件时出错: {str(e)}")
    
# 添加完成时间显示
print(f"\n任务完成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
