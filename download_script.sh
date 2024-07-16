#!/bin/bash

# 定义下载目录
DOWNLOAD_DIR="/var/www/files/oitqs/software"

# 确保下载目录存在
mkdir -p "$DOWNLOAD_DIR"

# 从CSV文件中读取下载链接并下载
while IFS=, read -r platform location display_name volumn_name app_name chip_type params checksum search_name icon profile download_link
do  
    # 清理URL，移除可能的非打印字符
    location=$(echo "$location" | tr -d '\r')
    download_link=$(echo "$download_link" | tr -d '\r')
    
    # 跳过空的下载链接
    if [ -z "$download_link" ]; then
        echo "No download link for $display_name. Skipping..."
        continue
    fi
    
    # 获取文件原始扩展名
    EXTENSION="${download_link##*.}"

    # 定义下载文件的名称
    FILENAME="${display_name}_${platform}_${chip_type}.${EXTENSION}"
    TARGET_PATH="$DOWNLOAD_DIR/$platform/$FILENAME"

    # 确保下载目录存在
    mkdir -p "$DOWNLOAD_DIR/$platform"

    # 检查文件是否已存在并与远程文件相同
    if [ -f "$TARGET_PATH" ]; then
        wget -O "$TARGET_PATH.tmp" "$download_link"
        if cmp -s "$TARGET_PATH" "$TARGET_PATH.tmp"; then
            echo "$FILENAME is already up to date. Skipping download."
            rm "$TARGET_PATH.tmp"
            continue
        else
            mv "$TARGET_PATH.tmp" "$TARGET_PATH"
        fi
    else
        echo "Downloading $display_name as $FILENAME..."
        wget -O "$TARGET_PATH" "$download_link"
    fi

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
