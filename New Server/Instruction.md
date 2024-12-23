### 制作 Live Linux U 盘

在 macOS 上，可以通过以下步骤查看 U 盘的设备路径：

---

### **步骤 1：插入 U 盘**

将 U 盘插入你的 Mac，并确保 macOS 已识别到它。

---

### **步骤 2：查看磁盘列表**

打开终端，然后运行以下命令：

```bash
diskutil list
```

</code></div></div></pre>

这将列出所有已连接的存储设备，包括内部硬盘和外接 U 盘。

示例输出：

/dev/disk0 (internal, physical):
#:                       TYPE NAME                    SIZE       IDENTIFIER
0:      GUID_partition_scheme                        *500.3 GB   disk0
1:                        EFI EFI                     209.7 MB   disk0s1
2:                 Apple_APFS Container disk1         500.1 GB   disk0s2

/dev/disk2 (external, physical):
#:                       TYPE NAME                    SIZE       IDENTIFIER
0:      GUID_partition_scheme                        *16.0 GB    disk2
1:       Microsoft Basic Data UNTITLED               16.0 GB    disk2s1
</code></div></div></pre>

---

### **步骤 3：找到 U 盘的设备路径**

在输出中找到你的 U 盘。例如，上述输出中，`/dev/disk2` 是 U 盘的设备路径。

注意：

* **设备路径** 是 `/dev/disk2`。
* **分区路径** 是 `/dev/disk2s1`，我们不会使用这个路径。

---

### **步骤 4：卸载 U 盘**

在写入 ISO 前，必须卸载 U 盘上的文件系统，但不移除设备本身。

运行以下命令卸载 U 盘（替换 `disk2` 为你的设备路径）：

diskutil unmountDisk /dev/disk2
</code></div></div></pre>

---

### **步骤 5：写入 ISO 文件**

使用 `dd` 将 ISO 写入 U 盘（**注意：确保设备路径正确，操作有破坏性**）：

sudo dd if=/path/to/ubuntu.iso of=/dev/disk2 bs=4M status=progress
</code></div></div></pre>

* **`if=/path/to/ubuntu.iso`**: ISO 文件路径。
* **`of=/dev/disk2`**: U 盘设备路径（不加分区编号，如 `disk2` 而非 `disk2s1`）。
* **`bs=4M`**: 每次写入 4MB 数据，提升速度。
* **`status=progress`**: 显示进度。

---

### **步骤 6：完成写入**

写入完成后，运行以下命令确保 macOS 识别到 U 盘：

diskutil eject /dev/disk2
</code></div></div></pre>

拔出 U 盘，将其插入目标电脑即可用于启动。

---

### **提示**

* 如果不确定设备路径，可以在插入和拔出 U 盘前后分别运行 `diskutil list` 比较输出，确定正确的路径。
* 写入时要格外小心，误操作可能覆盖到系统盘。

sudo mkdir -p /var/www

sudo chown -R tencent:www-data /var/www

sudo rsync -avz --progress /var/www/ tencent@30.61.33.125:/var/www/

## 服务器转移

apache

python conda update env

googlechrome (don't intsall googlechrome!)

crontab

0 0 \* \* 0 /bin/bash -c "source /home/tencent/miniconda3/etc/profile.d/conda.sh && conda activate update && /home/tencent/miniconda3/envs/update/bin/python3 /var/www/files/oitqs/software/update/ubuntu\_update.py >> /var/www/files/oitqs/software/update/log\_file.log 2>&1"
