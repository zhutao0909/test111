import requests
import time
import streamlit as st

headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
  'referer': 'http://movie.mtime.com/'
}

def get_comments(page_index):
    params = {
        "tt": "{}".format(int(time.time() * 1000)),
        "movieId": "209164",
        "pageIndex": "{}".format(page_index),
        "pageSize": "50",
        "orderType": "2"
    }

    res = requests.get(
        'http://front-gateway.mtime.com/library/movie/comment.api',
        params=params,
        headers=headers)

    comment_list = res.json()['data']['list']
    for i in comment_list:
        st.write("用户：", i['nickname'])
        st.write("打分：", i['rating'])
        st.write("评论：", i['content'])

    # 暂停一下，防止爬取太快被封
    time.sleep(1)

st.title("电影评论爬取")
page_index = st.number_input("请输入要爬取的评论页数（1-4）：", min_value=1, max_value=4, value=1)
if st.button("开始爬取"):
    get_comments(page_index)
