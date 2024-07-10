## Next Cloud
sudo -i
nano /var/lib/docker/volumes/nextcloud-docker_nextcloud/_data/config/config.php

'trusted_domains' =>
  array (
    0 => 'localhost',
    1 => 'existing-domain.com',
    2 => 'new-domain.com',  // 添加新的域名
  ),


## ssh
ssh tencent@30.61.33.99
pw: tencent

## http
/var/www/files
http://30.61.33.99/files



## location

Downloading WeCom as WeCom_win_All.exe...
--2024-07-10 06:44:10--  https://dldir1.qq.com/wework/work_weixin/WeCom_4.1.26.6014.exe
Resolving dldir1.qq.com (dldir1.qq.com)... 113.201.154.200, 122.188.38.140, 122.188.38.225, ...
Connecting to dldir1.qq.com (dldir1.qq.com)|113.201.154.200|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 488752464 (466M) [application/octet-stream]
Saving to: ‘~/installer/win/WeCom_win_All.exe’

~/installer/win/WeCom_win_All.exe     100%[=======================================================================>] 466.11M  3.27MB/s    in 2m 23s  

2024-07-10 06:46:34 (3.26 MB/s) - ‘~/installer/win/WeCom_win_All.exe’ saved [488752464/488752464]

WeCom downloaded successfully.
Downloading WeChat as WeChat_win_All.exe...
--2024-07-10 06:46:34--  https://dldir1.qq.com/weixin/Windows/WeChatSetup.exe
Resolving dldir1.qq.com (dldir1.qq.com)... 112.64.213.175, 122.188.38.225, 122.188.38.140
Connecting to dldir1.qq.com (dldir1.qq.com)|112.64.213.175|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 257062168 (245M) [application/octet-stream]
Saving to: ‘~/installer/win/WeChat_win_All.exe’

~/installer/win/WeChat_win_All.exe    100%[=======================================================================>] 245.15M  3.06MB/s    in 82s     

2024-07-10 06:47:59 (2.97 MB/s) - ‘~/installer/win/WeChat_win_All.exe’ saved [257062168/257062168]

WeChat downloaded successfully.
Downloading Slack as Slack_win_All.exe...
--2024-07-10 06:47:59--  https://downloads.slack-edge.com/desktop-releases/windows/x64/4.38.127/SlackSetup.exe
Resolving downloads.slack-edge.com (downloads.slack-edge.com)... 3.165.39.26, 3.165.39.9, 3.165.39.103, ...
Connecting to downloads.slack-edge.com (downloads.slack-edge.com)|3.165.39.26|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 119711024 (114M) [application/octet-stream]
Saving to: ‘~/installer/win/Slack_win_All.exe’

~/installer/win/Slack_win_All.exe     100%[=======================================================================>] 114.17M  5.29MB/s    in 28s     

2024-07-10 06:48:28 (4.06 MB/s) - ‘~/installer/win/Slack_win_All.exe’ saved [119711024/119711024]

Slack downloaded successfully.
Downloading VooV Meeting as VooV Meeting_win_All.exe...
--2024-07-10 06:48:28--  https://updatecdn.meeting.qq.com/cos/cb3c7bda5205119bd5f4fc9fcc30294e/VooVMeeting_1410000197_3.23.0.510.publish.exe
Resolving updatecdn.meeting.qq.com (updatecdn.meeting.qq.com)... 43.132.83.184, 43.132.83.98, 43.132.83.119, ...
Connecting to updatecdn.meeting.qq.com (updatecdn.meeting.qq.com)|43.132.83.184|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 217647448 (208M) [application/x-msdownload]
Saving to: ‘~/installer/win/VooV Meeting_win_All.exe’

~/installer/win/VooV Meeting_win_All. 100%[=======================================================================>] 207.56M  4.99MB/s    in 41s     

2024-07-10 06:49:10 (5.04 MB/s) - ‘~/installer/win/VooV Meeting_win_All.exe’ saved [217647448/217647448]

VooV Meeting downloaded successfully.
Downloading Acrobat Reader as Acrobat Reader_win_All.exe...
--2024-07-10 06:49:10--  https://ardownload2.adobe.com/pub/adobe/reader/win/AcrobatDC/2300820421/AcroRdrDC2300820421_en_US.exe
Resolving ardownload2.adobe.com (ardownload2.adobe.com)... 23.54.60.171, 2600:140b:1c00:385::11e2, 2600:140b:1c00:382::11e2
Connecting to ardownload2.adobe.com (ardownload2.adobe.com)|23.54.60.171|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 292904408 (279M) [application/octet-stream]
Saving to: ‘~/installer/win/Acrobat Reader_win_All.exe’

~/installer/win/Acrobat Reader_win_Al 100%[=======================================================================>] 279.33M  19.9MB/s    in 15s     

2024-07-10 06:49:25 (18.1 MB/s) - ‘~/installer/win/Acrobat Reader_win_All.exe’ saved [292904408/292904408]

Acrobat Reader downloaded successfully.
Downloading 7-Zip as 7-Zip_win_All.exe...
--2024-07-10 06:49:25--  https://www.7-zip.org/a/7z2201-x64.exe
Resolving www.7-zip.org (www.7-zip.org)... 49.12.202.237
Connecting to www.7-zip.org (www.7-zip.org)|49.12.202.237|:443... connected.
HTTP request sent, awaiting response... 302 Moved Temporarily
Location: https://github.com/ip7z/7zip/releases/download/22.01/7z2201-x64.exe [following]
--2024-07-10 06:49:27--  https://github.com/ip7z/7zip/releases/download/22.01/7z2201-x64.exe
Resolving github.com (github.com)... 20.27.177.113
Connecting to github.com (github.com)|20.27.177.113|:443... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://objects.githubusercontent.com/github-production-release-asset-2e65be/466446150/38bbff3d-4eab-407d-8e7d-d04a43f2729e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=releaseassetproduction%2F20240710%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240710T064927Z&X-Amz-Expires=300&X-Amz-Signature=db22d6e491dae03e64aa1b2fd2d943e817cc2b9f185b1eb19034ad10fb47a5fa&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=466446150&response-content-disposition=attachment%3B%20filename%3D7z2201-x64.exe&response-content-type=application%2Foctet-stream [following]
--2024-07-10 06:49:27--  https://objects.githubusercontent.com/github-production-release-asset-2e65be/466446150/38bbff3d-4eab-407d-8e7d-d04a43f2729e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=releaseassetproduction%2F20240710%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240710T064927Z&X-Amz-Expires=300&X-Amz-Signature=db22d6e491dae03e64aa1b2fd2d943e817cc2b9f185b1eb19034ad10fb47a5fa&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=466446150&response-content-disposition=attachment%3B%20filename%3D7z2201-x64.exe&response-content-type=application%2Foctet-stream
Resolving objects.githubusercontent.com (objects.githubusercontent.com)... 185.199.109.133, 185.199.110.133, 185.199.111.133, ...
Connecting to objects.githubusercontent.com (objects.githubusercontent.com)|185.199.109.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1575742 (1.5M) [application/octet-stream]
Saving to: ‘~/installer/win/7-Zip_win_All.exe’

~/installer/win/7-Zip_win_All.exe     100%[=======================================================================>]   1.50M  --.-KB/s    in 0.02s   

2024-07-10 06:49:28 (62.4 MB/s) - ‘~/installer/win/7-Zip_win_All.exe’ saved [1575742/1575742]

7-Zip downloaded successfully.
Downloading Google Chrome as Google Chrome_win_All.msi...
--2024-07-10 06:49:28--  https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B1C8FC26D-70C3-3491-26C6-A97477C16269%7D%26lang%3Den%26browser%3D0%26usagestats%3D0%26appname%3DGoogle%2520Chrome%26needsadmin%3Dtrue%26ap%3Dx64-stable-statsdef_0%26brand%3DGCEA/dl/chrome/install/googlechromestandaloneenterprise64.msi
Resolving dl.google.com (dl.google.com)... 172.217.26.238, 2404:6800:4004:801::200e
Connecting to dl.google.com (dl.google.com)|172.217.26.238|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 119250944 (114M) [application/octet-stream]
Saving to: ‘~/installer/win/Google Chrome_win_All.msi’

~/installer/win/Google Chrome_win_All 100%[=======================================================================>] 113.73M  22.9MB/s    in 5.0s    

2024-07-10 06:49:33 (22.9 MB/s) - ‘~/installer/win/Google Chrome_win_All.msi’ saved [119250944/119250944]

Google Chrome downloaded successfully.
Downloading ioav5 as ioav5_win_All.exe...
--2024-07-10 06:49:33--  http://windows/standard/ioav5_setup5.4.19.188.exe
Resolving windows (windows)... failed: Temporary failure in name resolution.
wget: unable to resolve host address ‘windows’
Failed to download ioav5. Check the URL and network connection.
Downloading Office365 as Office365_win_All.zip...
--2024-07-10 06:49:33--  http://windows/standard/office365_2308.zip
Resolving windows (windows)... failed: Temporary failure in name resolution.
wget: unable to resolve host address ‘windows’
Failed to download Office365. Check the URL and network connection.
Downloading WeCom as WeCom_mac_Apple.dmg...
--2024-07-10 06:49:33--  https://dldir1.qq.com/foxmail/wecom-mac/updatebzl/WeCom_4.1.26.99469_Apple.dmg
Resolving dldir1.qq.com (dldir1.qq.com)... 122.188.38.225, 122.188.38.140, 112.64.213.175
Connecting to dldir1.qq.com (dldir1.qq.com)|122.188.38.225|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 547103375 (522M) [application/octet-stream]
Saving to: ‘~/installer/mac/WeCom_mac_Apple.dmg’

~/installer/mac/WeCom_mac_Apple.dmg   100%[=======================================================================>] 521.76M  7.29MB/s    in 74s     

2024-07-10 06:50:47 (7.10 MB/s) - ‘~/installer/mac/WeCom_mac_Apple.dmg’ saved [547103375/547103375]

WeCom downloaded successfully.
Downloading WeCom as WeCom_mac_Intel.dmg...
--2024-07-10 06:50:47--  https://dldir1.qq.com/foxmail/wecom-mac/updatebzl/WeCom_4.1.26.90928_Intel.dmg
Resolving dldir1.qq.com (dldir1.qq.com)... 122.188.38.140, 122.188.38.225, 112.64.213.175
Connecting to dldir1.qq.com (dldir1.qq.com)|122.188.38.140|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 576036003 (549M) [application/octet-stream]
Saving to: ‘~/installer/mac/WeCom_mac_Intel.dmg’

~/installer/mac/WeCom_mac_Intel.dmg   100%[=======================================================================>] 549.35M  19.2MB/s    in 28s     

2024-07-10 06:51:16 (19.8 MB/s) - ‘~/installer/mac/WeCom_mac_Intel.dmg’ saved [576036003/576036003]

WeCom downloaded successfully.
Downloading WeChat as WeChat_mac_All.dmg...
--2024-07-10 06:51:16--  https://dldir1.qq.com/weixin/mac/WeChatMac.dmg
Resolving dldir1.qq.com (dldir1.qq.com)... 122.188.38.225, 112.64.213.175, 122.188.38.140
Connecting to dldir1.qq.com (dldir1.qq.com)|122.188.38.225|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 368769513 (352M) [application/octet-stream]
Saving to: ‘~/installer/mac/WeChat_mac_All.dmg’

~/installer/mac/WeChat_mac_All.dmg    100%[=======================================================================>] 351.69M  22.5MB/s    in 16s     

2024-07-10 06:51:33 (21.3 MB/s) - ‘~/installer/mac/WeChat_mac_All.dmg’ saved [368769513/368769513]

WeChat downloaded successfully.
Downloading Slack as Slack_mac_All.dmg...
--2024-07-10 06:51:33--  https://downloads.slack-edge.com/desktop-releases/mac/universal/4.38.125/Slack-4.38.125-macOS.dmg
Resolving downloads.slack-edge.com (downloads.slack-edge.com)... 3.165.39.26, 3.165.39.52, 3.165.39.103, ...
Connecting to downloads.slack-edge.com (downloads.slack-edge.com)|3.165.39.26|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 175414223 (167M) [application/octet-stream]
Saving to: ‘~/installer/mac/Slack_mac_All.dmg’

~/installer/mac/Slack_mac_All.dmg     100%[=======================================================================>] 167.29M  16.0MB/s    in 11s     

2024-07-10 06:51:45 (14.9 MB/s) - ‘~/installer/mac/Slack_mac_All.dmg’ saved [175414223/175414223]

Slack downloaded successfully.
Downloading google chrome as google chrome_mac_All.dmg...
--2024-07-10 06:51:45--  https://dl.google.com/dl/chrome/mac/universal/stable/gcea/googlechrome.dmg
Resolving dl.google.com (dl.google.com)... 172.217.26.238, 2404:6800:4004:801::200e
Connecting to dl.google.com (dl.google.com)|172.217.26.238|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 204194468 (195M) [application/x-apple-diskimage]
Saving to: ‘~/installer/mac/google chrome_mac_All.dmg’

~/installer/mac/google chrome_mac_All 100%[=======================================================================>] 194.73M  16.9MB/s    in 11s     

2024-07-10 06:51:56 (17.5 MB/s) - ‘~/installer/mac/google chrome_mac_All.dmg’ saved [204194468/204194468]

google chrome downloaded successfully.
Downloading VooV Meeting as VooV Meeting_mac_Intel.dmg...
--2024-07-10 06:51:56--  https://updatecdn.meeting.qq.com/cos/07a3712ac6022d03441baacbe87c53f2/VooVMeeting_1410000198_3.23.1.510.publish.x86_64.dmg
Resolving updatecdn.meeting.qq.com (updatecdn.meeting.qq.com)... 43.132.85.167, 43.132.85.236, 43.175.16.103, ...
Connecting to updatecdn.meeting.qq.com (updatecdn.meeting.qq.com)|43.132.85.167|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 194517680 (186M) [application/x-apple-diskimage]
Saving to: ‘~/installer/mac/VooV Meeting_mac_Intel.dmg’

~/installer/mac/VooV Meeting_mac_Inte 100%[=======================================================================>] 185.51M  5.11MB/s    in 37s     

2024-07-10 06:52:39 (5.01 MB/s) - ‘~/installer/mac/VooV Meeting_mac_Intel.dmg’ saved [194517680/194517680]

VooV Meeting downloaded successfully.
Downloading VooV Meeting as VooV Meeting_mac_Apple.dmg...
--2024-07-10 06:52:39--  https://updatecdn.meeting.qq.com/cos/577b1e710cdac11aaef996c61e2184cd/VooVMeeting_1410000198_3.23.1.510.publish.arm64.dmg
Resolving updatecdn.meeting.qq.com (updatecdn.meeting.qq.com)... 43.175.16.103, 43.132.83.119, 43.132.85.92, ...
Connecting to updatecdn.meeting.qq.com (updatecdn.meeting.qq.com)|43.175.16.103|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 177609838 (169M) [application/x-apple-diskimage]
Saving to: ‘~/installer/mac/VooV Meeting_mac_Apple.dmg’

~/installer/mac/VooV Meeting_mac_Appl 100%[=======================================================================>] 169.38M  5.03MB/s    in 34s     

2024-07-10 06:53:13 (4.99 MB/s) - ‘~/installer/mac/VooV Meeting_mac_Apple.dmg’ saved [177609838/177609838]

VooV Meeting downloaded successfully.
Downloading ioav5 as ioav5_mac_Apple.pkg...
--2024-07-10 06:53:13--  http://mac/standard/ioav5_setup5.4.12.126.pkg
Resolving mac (mac)... failed: Temporary failure in name resolution.
wget: unable to resolve host address ‘mac’
Failed to download ioav5. Check the URL and network connection.
Downloading ioav5 as ioav5_mac_Intel.pkg...
--2024-07-10 06:53:13--  http://mac/standard/ioav5_setup5.4.12.126.pkg
Resolving mac (mac)... failed: Temporary failure in name resolution.
wget: unable to resolve host address ‘mac’
Failed to download ioav5. Check the URL and network connection.
All downloads are complete.

