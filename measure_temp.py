import subprocess

import notice


def get_temp():
    temp = subprocess.getoutput('vcgencmd measure_temp').split('=')
    message = "\n現在のRaspberry PiのCPU温度 : "+temp[1].replace('\'', '°')

    return message


def main():
    message = get_temp()
    notice.notice(message)


if __name__ == '__main__':
    main()
