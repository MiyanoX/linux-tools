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
ssh tencent@30.61.33.71
pw: tencent

