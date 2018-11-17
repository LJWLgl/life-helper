## life-helper是一个基于python开发的生活助手插件
插件所依赖的API接口是由[聚合数据](https://www.juhe.cn/)提供

### 功能
1. 微信精选
2. 笑话大全
3. 查询邮编
4. 查询ip地址
5. 查询号码归属地
6. 查新闻

### 使用
- 微信精选  
输入`life wx`，会展现微信精选文章列表（点击`enter`可调具体网页）
- 笑话大全  
输入`life joke`，会展现笑话列表（`cmd` + `enter`可复制笑话内容）
- 查询邮编  
输入`life yb [县名或区民]`，会查询到该县或该区的邮编，如`life yb 浦东新区`
- 查询ip地址  
输入`life ip [ip地址]`，会查询该IP所在地理位置，如果是国内ip，运营商信息也会一并返回，如`life ip 34.54.43.32`
- 查询号码归属地
输入`life gsd [手机号]`，会查询到该手机号的归属地信息
- 查新闻
输入`life news [新闻类别]`，会查到最新新闻，可选的新闻类别有：  
    - top（头条）
    - shehui（社会）
    - guonei（国内）
    - yule（娱乐）
    - tiyu（体育）
    - junshi（军事）
    - keji（科技）
    - caijing（财经）
    - shishang（时尚）
### 配置
注意：本插件大部分接口是依赖聚合数据的接口，但是普通会员调用api次数有限制（100 times/day）,
为了不影响大家的正常使用，建议大家可以自己申请[聚合数据](https://www.juhe.cn/)的账号，申请账号成功后，可以申请以下几个应用：
- 手机号码归属地
- 邮编查询
- IP地址
- 新闻头条
- 笑话大全
- 微信精选  

申请成功后可以在[个人中心](https://www.juhe.cn/myData)看到appkey，拿到appkey后，输入`life config`可以看到不同应用appkey，然后替换成自己的就好。
![](http://tc.ganzhiqiang.wang/1542467793.png?imageMogr2/thumbnail/!70p)


### 示例图
![](http://tc.ganzhiqiang.wang/111.gif?imageMogr2/thumbnail/!70p)

