import csv
from datetime import datetime

import notice


def get_timetable():
    weekday = datetime.now().weekday()
    file_name = open('data/timetable.csv', 'r')
    timetable_file = list(csv.reader(file_name))

    if weekday > 4:
        return "\n今日は休暇です"

    timetable = ["{0}限 : {1}".format(
        i+1, (timetable_file[weekday][i])) for i in range(5)]
    message = "\n今日の時間割\n"+"\n".join(timetable)
    return message


def main():
    message = get_timetable()
    notice.notice(message)


if __name__ == '__main__':
    main()
