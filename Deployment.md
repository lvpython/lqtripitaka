# Linux/Mac/Windos 用 Docker 部署项目步骤
目前注册腾讯云可以免费领取一个月的服务器使用权限，亲测以下教程在腾讯云部署成功。

### 1.Docker安装
Linux(CenOS 7)：
```bash
yum install -y docker
systemctl start docker
chkconfig docker on
```
Windows :
- Windows 10 以下推荐使用 Docker Toolbox
Toolbox的介绍和帮助：mirrors.aliyun.com/help/docker-toolbox
Windows系统的安装文件目录：http://mirrors.aliyun.com/docker-toolbox/windows/docker-toolbox/
- Windows 10 以上推荐使用 Docker for Windows
Windows系统的安装文件目录：http://mirrors.aliyun.com/docker-toolbox/windows/docker-for-windows/

Mac :
- 10.10.3 以下推荐使用 Docker Toolbox
Toolbox的介绍和帮助：mirrors.aliyun.com/help/docker-toolbox
Mac系统的安装文件目录：http://mirrors.aliyun.com/docker-toolbox/mac/docker-toolbox/
- 10.10.3以上推荐使用 Docker for Mac
Mac系统的安装文件目录：http://mirrors.aliyun.com/docker-toolbox/mac/docker-for-mac/

[镜像加速方法](https://www.daocloud.io/mirror#accelerator-doc)


### 2.Dcoker-compose安装

|docker-compose |docker-engine |CentOS    |
|:-------------:|:------------:|:--------:|
|1.7.0          |1.9.1-        |7.0       |
|1.6.2          |1.9.1-        |7.0       |
|1.5.2          |1.7.1-        |6.7       |

```bash
yum install -y python-pip
pip install -U docker-compose

# Win/ Mac 用户从这里开始执行
git clone https://github.com/kangqiao/lqtripitaka.git
cd lqtripitaka
# 查看 docker-compose 是否已安装
docker-compose -v
```


### 3.修改配置文件
1. 修改 `conf/nginx/tripitaka_nginx.conf` 中的 IP 和域名，默认都是 `127.0.0.1`，IP 和域名请改成你自己服务器的 IP 和 自己的域名。
2. `settings.py` 中 `DATABASES` 配置要和 `docker-compose.yml`里的数据库配置保持一致（可以不做修改使用默认值），其中 HOST 为 `mysql`。


### 4.启动项目
```bash
docker-compose up -d
```

### 5.同步数据库
```bash
docker-compose run web_tripitaka /usr/local/bin/python manage.py makemigrations
docker-compose run web_tripitaka /usr/local/bin/python manage.py migrate
```

### 6.收集样式
```bash
docker-compose run web_tripitaka /usr/local/bin/python manage.py collectstatic
```

### 7. 导入初始数据
```
docker-compose run web_tripitaka  python manage.py loaddata data.json
```

打开浏览器 `127.0.0.1` 或者打开你自己配置的域名 or IP，就能预览项目了。

### 9.最后
- 你可以手动导入你自己的数据到数据库
- 你也可以用 Docker 作为本地的开发环境，这个时候应使用应修改 `manage.py`, 使用 `settingsdev.py` 而不是 `settings.py`
- 登录 admin 后台时前，别忘了先创建超级用户
```bash
docker-compose run lq_tripitaka python manage.py createsuperuser
Username (leave blank to use 'root'): admin
Email address: admin@126.com
Password: admin
Password (again): admin
Superuser created successfully.
```
### 写在最后

#### 遇到的问题
###### centos 6 中安装docker
```
yum install https://get.docker.com/rpm/1.7.1/centos-6/RPMS/x86_64/docker-engine-1.7.1-1.el6.x86_64.rpm
# centos 6 中 docker-compose 需要安装1.5.2版本
pip3 install docker-compose==1.5.2
```
###### [docker参考文档](https://yeasy.gitbooks.io/docker_practice/content/introduction/)

#### docker常用命令
```
# 停止所有的容器运行
docker stop $(docker ps -q)
# 删除所有的容器
docker rm $(docker ps -a -q)
# 删除所有的镜像
docker rmi $(docker images -q)
```
