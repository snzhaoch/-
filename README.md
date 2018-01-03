知乎与豆瓣爬虫
===========================
## 注意
运行 zhihu.py 前需要在 spider 文件夹下创建 config.py 文件，并在文件中设定 profile 变量，
profile 变量是字符串，值为 chrome 浏览器 'chrome://version/' 地址中的个人资料路径（需去除末尾的'\Default'，并防止'\'转义)
------------------------------------------------
## 爬虫简介/演示
    * douban
        * 分页爬取豆瓣电影 top250
        * 对数据进行清洗
        * 将爬取内容缓存到本地
        * 代码规范，易于完成任务变更

        ![image](https://github.com/snzhaoch/demo/blob/master/spider/douban.gif)

    * zhihu
        * 完成知乎 cookie 验证
        * 爬取内容
            * 地址：知乎主页
            * 对象：个人关注用户回答的问题，或发表的文章（点赞分享不算）
            * 时间：近五日

        ![image](https://github.com/snzhaoch/demo/blob/master/spider/zhihu.gif)
