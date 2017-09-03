# coding:utf8
import codecs
import random
import string




import requests
import re
import pandas as pd
import sys

reload(sys)
sys.setdefaultencoding("utf8")

def cookieGenerator():
    bid = "".join(random.sample(string.ascii_letters + string.digits, 11))
    cookies = {
        'Cookie' : 'bid=%s; ps=y; ue="aukuno@126.com"; dbcl2="65548707:dmtiAByXcfI"'%bid
    }
    return cookies
def save_comments(comments):
        data = pd.DataFrame(comments)
        with open('WarWolf_Comment.csv', 'a+') as csvfile:
            csvfile.write(codecs.BOM_UTF8)
            data.to_csv(csvfile, header=False, index=False, mode='a+')  # 写入csv文件,'a+'是追加模式

# head={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/59.0.3071.109 Chrome/59.0.3071.109 Safari/537.36'}
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"
}



session = requests.Session()
url_first='https://movie.douban.com/subject/26363254/comments?start=0'
html=session.get(url_first, headers=head, cookies=cookieGenerator(), verify=False)


reg=re.compile(r'<a href="(.*?)&amp;.*?class="next">') #下一页
#  <a href="?start=119620&amp;limit=20&amp;sort=new_score&amp;status=P" data-page="" class="next">后页 ></a>

ren=re.compile(r'<span class="votes">(.*?)</span>.*?comment">(.*?)</a>.*?</span>.*?<span.*?class="">(.*?)</a>.*?<span>(.*?)</span>.*?title="(.*?)"></span>.*?title="(.*?)">.*?class=""> (.*?)\n',re.S)  #评论等内容



count = 1
while html.status_code==200:
    comments = re.findall(ren, html.text)
    print pd.DataFrame(comments)
    save_comments(comments)

    postfix = re.findall(reg, html.text)[0]
    url_next = 'https://movie.douban.com/subject/26363254/comments' + postfix
    html=session.get(url_next, cookies=cookieGenerator(), headers=head, verify=False)
    print "This is the %s-th loop loading Comments" %count

    count += 1
    session.cookies.update(html.cookies)


while html.status_code==403:
    print "Sorry Captcha Occurs!"
    raise exit(1)


print "Loading Comments completed!"



