## Update Software
sudo python update.py

## ssh
ssh tencent@30.61.33.6
pw: tencent

## http
/var/www/files/
http://30.61.33.6/

Software_List：
http://30.61.33.6/Software_List.csv

## 定时任务
sudo crontab -e
0 0 * * * /bin/bash -c "source ~/anaconda3/etc/profile.d/conda.sh && conda activate update && python3 /var/www/files/oitqs/software/update/ubuntu_update.py >> /var/www/files/oitqs/software/update/log_file.log 2>&1"
sudo crontab -l

## 查看日志
tail -f /var/www/files/oitqs/software/update/log_file.log

## nginx
tencent@tencentserver:/etc/nginx/sites-available$ sudo nano default 
tencent@tencentserver:/etc/nginx/sites-available$ sudo systemctl restart nginx

## DHCP problem

从你提供的配置信息来看，你的Ubuntu服务器上的网络接口enp0s31f6配置了两个IPv4地址：30.61.33.6和30.61.33.99。这两个地址都在同一个子网30.61.33.0/24内。

分析配置
主IP地址：30.61.33.6/24是主IP地址，这个地址没有额外的参数，通常是在系统启动时通过静态配置或DHCP自动配置的。

次级动态IP地址：

30.61.33.99/24被标记为secondary dynamic，这意味着它是动态配置的次级IP地址。metric 100表示当存在多个路由选择时，这个IP地址的路由优先级是100。
valid_lft 14177sec和preferred_lft 14177sec表明这个IP地址的有效期限是14177秒，之后如果不续租，这个IP地址将会失效。
可能的配置原因
DHCP配置：这个次级IP地址很可能是通过DHCP自动分配的。有时，网络管理员设置了DHCP服务器以提供多个IP地址给单个网络接口，用于网络管理、负载平衡或其他特定的网络需求。
临时需求：某些应用程序或服务可能临时请求额外的IP地址，用于特定的服务或任务。