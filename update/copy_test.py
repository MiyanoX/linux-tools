import os
import shutil

# 在最后添加以下代码
print("开始复制文件到目标目录...")

try:
    # 确保目标目录存在
    os.makedirs('/var/www/files/oitqs/software/mac', exist_ok=True)
    os.makedirs('/var/www/files/oitqs/software/win', exist_ok=True)

    # 复制 mac 目录下的文件
    mac_source = './software/mac/'
    mac_dest = '/var/www/files/oitqs/software/mac/'
    for file in os.listdir(mac_source):
        source_path = os.path.join(mac_source, file)
        dest_path = os.path.join(mac_dest, file)
        print(f"正在复制: {source_path} -> {dest_path}")
        shutil.copy2(source_path, dest_path)
        print(f"复制完成: {source_path} -> {dest_path}")

    # 复制 win 目录下的文件
    win_source = './software/win/'
    win_dest = '/var/www/files/oitqs/software/win/'
    for file in os.listdir(win_source):
        source_path = os.path.join(win_source, file)
        dest_path = os.path.join(win_dest, file)
        print(f"正在复制: {source_path} -> {dest_path}")
        shutil.copy2(source_path, dest_path)
        print(f"复制完成: {source_path} -> {dest_path}")
    # 复制 Software_List_v2.csv
    csv_source = './Software_List_v2.csv'
    csv_dest = '/var/www/files/oitqs/Software_List_v2.csv'
    print(f"正在复制: {csv_source} -> {csv_dest}")
    shutil.copy2(csv_source, csv_dest)
    print(f"复制完成: {csv_source} -> {csv_dest}")
    
    print("所有文件复制完成")

except Exception as e:
    print(f"复制文件时出错: {str(e)}")

