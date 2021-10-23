import requests
from datetime import datetime

import notice


# 都道府県名からエリアコードを逆引きして天気を取得
def get_weather(area_name='Tokyo'):
    res = requests.get(
        'https://www.jma.go.jp/bosai/common/const/area.json').json()
    key = [k for k, d in res['offices'].items()
           if d['name'] == area_name or d['enName'] == area_name]
    area_code = ''.join(key)

    if area_code == '':
        message = (
            "\n"
            "天気情報を取得することができませんでした。エリア名を再確認してください。\n"
            "例: '大阪府', 'Kyoto'\n"
            "\n"
            "全国の天気予報\n"
            "https://www.jma.go.jp/bosai/forecast/"
        )

        return message

    url = 'https://www.jma.go.jp/bosai/forecast/data/overview_forecast/'+area_code+'.json'
    forecast_data = requests.get(url).json()

    report_time = datetime.fromisoformat(
        forecast_data['reportDatetime']
    ).replace(tzinfo=None)

    message = (
        "\n"
        "{0}\n"
        "{1}\n"
        "{2}\n"
        "\n"
        "{3}発表\n"
        "引用元: {4}\n"
        "\n"
        "全国の天気予報\n"
        "https://www.jma.go.jp/bosai/forecast/"
    ).format(
        forecast_data['publishingOffice'],
        forecast_data['headlineText'],
        forecast_data['text'],
        report_time.strftime('%Y年%m月%d日%H時%M分'),
        url
    ).replace('\u3000', '')

    return message


def main():
    message = get_weather()
    notice.notice(message)


if __name__ == '__main__':
    main()
