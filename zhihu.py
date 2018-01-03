import os
import platform
from splinter import Browser
from selenium import webdriver
from utils import log
import config


class Model():
    """
    基类, 用来显示类的信息
    """

    def __repr__(self):
        name = self.__class__.__name__
        properties = ('{}=({})'.format(k, v) for k, v in self.__dict__.items())
        s = '\n<{} \n  {}>'.format(name, '\n  '.join(properties))
        return s


class Article(Model):
    """
    存储关注者的回答或文章
    """

    def __init__(self):
        self.author = ''
        self.title = ''
        self.upvote = 0
        self.quote = ''
        self.answer_url = ''


def add_chrome_webdriver():
    """
    将环境变量加入电脑
    """
    print(platform.system())
    if platform.system() == 'Windows':
        working_path = os.getcwd()
        library = 'library'
        path = os.path.join(working_path, library)
        os.environ["PATH"] += '{}{}{}'.format(os.pathsep, path, os.pathsep)
        print(os.environ['PATH'])


def find_website():
    """
    爬取知乎首页内容
    """
    chrome_options = webdriver.ChromeOptions()
    # config 中存放的是私人资料， profile 变量为 chrome 浏览器 'chrome://version/' 中的个人资料路径（需去除末尾的'\Default'，并防止'\'转义)
    chrome_options.add_argument("user-data-dir={}".format(config.profile))
    with Browser('chrome', options=chrome_options) as browser:
        url = "https://www.zhihu.com"
        browser.visit(url)
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        found = False
        while not found:
            found = browser.is_text_present('5 天前')
            if found:
                article_divs = browser.find_by_css('.TopstoryItem')
                total = 0
                good = 0
                for div in article_divs:
                    # 获取每个 div 右上角的内容，如果为广告则略过
                    article_type = div.find_by_css('.TopstoryItem-rightButton').text
                    total += 1
                    if article_type == '广告':
                        continue
                    # 获取每个 div 的 Feed-title class 内容，其中若有 AuthorInfo class，
                    # 则说明是关注者发布文章或回答问题，而不是点赞
                    elif div.find_by_css('.Feed-title').first.find_by_css('.AuthorInfo') != []:
                        a = Article()
                        author = div.find_by_css('.Feed-title').first.find_by_css('.AuthorInfo-head').text
                        title = div.find_by_css('.ContentItem-title').text
                        answer_url = div.find_by_css('.ContentItem-title').first.find_by_tag('a').first['href']
                        quote = div.find_by_css('.CopyrightRichText-richText').first.text
                        upvote = div.find_by_css('.ContentItem-actions').first.find_by_tag('button').first.text
                        a.author = author
                        a.title = title
                        a.answer_url = answer_url
                        a.quote = quote
                        a.upvote = upvote
                        good += 1
                        log(a)
                log('拿到了最近5天的个人动态')
                log('总计筛选了 {} 条信息'.format(total))
                log('共有 {} 条合格信息'.format(good))
                break
            else:
                browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')


def main():
    add_chrome_webdriver()
    find_website()


if __name__ == '__main__':
    main()
