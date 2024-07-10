#!/bin/bash

# 定义下载目录
DOWNLOAD_DIR="~/installer"

# 确保下载目录存在
mkdir -p "$DOWNLOAD_DIR"

# 从CSV文件中读取下载链接并下载
while IFS=, read -r platform location display_name volumn_name app_name chip_type params checksum search_name icon profile download_link
do
    # 获取文件原始扩展名
    EXTENSION="${download_link##*.}"

    # 定义下载文件的名称
    FILENAME="${display_name}_${platform}_${chip_type}.${EXTENSION}"

    # 确保下载目录存在
    mkdir -p "$DOWNLOAD_DIR/$platform"

    echo "Downloading $display_name as $FILENAME..."
    wget -O "$DOWNLOAD_DIR/$platform/$FILENAME" "$download_link"
    
    # 检查 wget 命令是否成功
    if [ $? -ne 0 ]; then
        echo "Failed to download $display_name. Check the URL and network connection."
        # 可选：记录错误到一个日志文件
        echo "$(date): Failed to download $display_name from $download_link" >> download_errors.log
    else
        echo "$display_name downloaded successfully."
    fi
done < <(tail -n +2 ./Software_List.csv)

echo "All downloads are complete."
