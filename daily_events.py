import requests
import datetime
from bs4 import BeautifulSoup

import notice


# 記念日と年間行事を取得
def get_events():
    today = datetime.date.today().strftime('%Y年%m月%d日')

    url = 'https://zatsuneta.com/category/anniversary.html'
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')

    events = soup.select_one(
        "body > "
        "div[id='container'] > "
        "div[id='wrapper'] > "
        "div[id='contents'] > "
        "div[class='article'] > "
        "p > "
        "ul"
    ).text

    message = (
        "\n"
        "{0}の記念日・年中行事\n"
        "{1}\n"
        "引用元 : {2}"
    ).format(today, events, url)

    return message


def main():
    message = get_events()
    notice.notice(message)


if __name__ == '__main__':
    main()
