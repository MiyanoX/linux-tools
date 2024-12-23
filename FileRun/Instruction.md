## 创建目录结构

```bash
mkdir -vp cloudreve/{uploads,avatar} \
&& touch cloudreve/conf.ini \
&& touch cloudreve/cloudreve.db
```

## 运行 Docker

```bash
cd ~/cloudreve

docker run -d \
-p 5212:5212 \
--mount type=bind,source=./conf.ini,target=/cloudreve/conf.ini \
--mount type=bind,source=./cloudreve.db,target=/cloudreve/cloudreve.db \
-v ./uploads:/cloudreve/uploads \
-v ./avatar:/cloudreve/avatar \
-v /var/www/files:/var/www/files \
cloudreve/cloudreve:latest
```
