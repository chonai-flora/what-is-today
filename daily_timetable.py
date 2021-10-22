import csv
from datetime import datetime

import notice


def get_timetable():
    weekday = datetime.now().weekday()
    file_name = open('data/timetable.csv', 'r')
    timetable = list(csv.reader(file_name))

    if weekday > 4:
        return "\n今日は休暇です"

    message = "\n今日の時間割\n"+"\n".join(timetable[weekday])
    return message


def main():
    message = get_timetable()
    notice.notice(message)


if __name__ == '__main__':
    main()
