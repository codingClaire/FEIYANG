
selenium官方文档
https://seleniumhq.github.io/selenium/docs/api/py/api.html

对所有公众号开放在图文消息中插入全平台已群发文章链接
https://mp.weixin.qq.com/s/67sk-uKz9Ct4niT-f4u1KA

2018-10-19

1.在Anaconda官网下载GUI安装包，安装常用模块
文档：
http://docs.anaconda.com/anaconda/user-guide/getting-started/
下载配置Anaconda

2.下载ChromeDriver
 1)国内镜像网站下载 注意要下载和chrome浏览器匹配的chromedriver
 2)将exe文件移动到chrome的application目录
 3）打开高级系统设置-->高级-->环境变量 在path中添加刚才的目录
 
3 代码：
import selenium
from selenium import webdriver
driver=webdriver.Chrome()
即可打开Chrome浏览器