# ToolBox

### CheckBook

本项目是一个基于Python语言的简单爬虫。其主要功能是检测图灵社区每天是否有新的图书上架，并将新上架的图书通过邮件的方式通知用户。

邮件相关设定在源代码文件中进行了注释说明。

该程序仅供个人实验所用。

v1版每天只爬取少量网页，切不可过多爬取相关网页。

v2版本的程序更新成post请求的方式获取数据，不再通过爬取页面的方式。

#### 使用方式

##### 需要准备的参数

v1版爬取图灵社区的图书类型网址，发送邮箱的smtp地址、授权码、接受于发送对用的邮箱地址。

v2版采用bark进行通知的方式。因此需要在程序运行的当前文件夹创建`deviceId.json`。内容设置如下：

```json
{
  "ID": ""
}
```

##### 使用

v1版需要安装lxml、BeautifulSoup4、Header依赖，运行`main.py`即可。

![image](https://user-images.githubusercontent.com/19681022/110322711-827d8280-804e-11eb-8c56-0dc19572db5f.png)

v2版只需安装一个额外的第三方包:requests，运行`main.py`即可。

### UnicomTask

本项目是基于[已有项目](https://github.com/srcrs/UnicomTask)进行的二次开发，利用python实现联通手机营业厅自动完成每日任务，领流量、签到获取积分等。去掉了云函数执行，将原本的邮件通知服务从不稳定的公用接口换成自己的邮箱保证运行的稳定性。

#### 功能

* [x] 沃之树领流量、浇水(12M日流量)
* [x] 每日签到(1积分+翻倍4积分+第七天1G流量日包)
* [x] 天天抽奖，每天三次免费机会(随机奖励)
* [x] 游戏中心每日打卡(连续打卡，积分递增至最高7，第七天1G流量日包)
* [x] 游戏中心宝箱100M任务(100M日流量+随机奖励并翻倍)
* [x] 4G流量包看视频、下软件任务(90M+150M七日流量)
* [x] 每日领取100定向积分 
* [x] 积分抽奖，每天最多抽30次(中奖几率渺茫)
* [x] 冬奥积分活动(第1和7天，可领取600定向积分，其余领取300定向积分,有效期至下月底)
* [x] 获取每日1G流量日包(截止日期暂时不知道)
* [x] 邮件、钉钉、Tg、企业微信等推送运行结果
* [x] 自动激活即将过期流量包（到期时间1天内）

#### 使用方式

##### 需要准备的参数

手机号、服务密码、`appId`、发送邮箱的授权码、smtp地址、收件邮箱地址。

其中`appId`的获取:

+ 安卓用户可在文件管理 --> `Unicom/appid` 文件中获取。

+ 苹果用户可抓取客户端登录接口获取。

> `https://m.client.10010.com/mobileService/login.htm`（解绑重新登录，在响应体中）

> `https://m.client.10010.com/mobileService/onLine.htm`（退出客户端重新进入，在请求体中）

> `http://m.client.10010.com/mobileService/customer/getclientconfig.htm?appId=xxx&mobile=yyy`（退出客户端重新进入，xxx就是）

> `https://m.client.10010.com/mobileService/customer/accountListData.htm`（退出客户端重新进入，在请求体中）

其中，后三个链接在安卓也是适用的。

在`Secrets`中的`Name`和`Value`格式如下：

| Name        | Value             |
| ----------- | ----------------- |
| USERS_COVER | config.json中内容 |

将`config.json`中内容复制下来，按照要求填写添加到`Secrets`中，如若选填内容不想配置，需将该行删除。如只想基本功能，无需通知和用积分抽奖，应填写如下内容：

```json
[
    {
        "username": "18566669999",
        "password": "123456",
        "appId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
]
```

注意`json`格式，最后一个要删掉逗号。建议在填写之前，使用[json校验工具](https://www.bejson.com/)进行校验。

注意：不要将个人信息填写到仓库`config.json`文件中（不要动这个文件就没事），以免泄露。

多账号，参考[关于多账号的使用方式](https://github.com/srcrs/UnicomTask/discussions/16)

![](https://draw-static.vercel.app/UnicomTask/将参数填到Secrets中.gif)

##### 使用

使用`pip3 install -r requirement.txt`安装依赖。执行`main.py`即可。

### Alfred-BaseConversion
进制转换的Alfred Workflow
