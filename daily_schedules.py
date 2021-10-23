from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import notice


def get_schedules():

    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    ID = 'XXXXXXXXXX'

    TIME_DIFF = datetime.timedelta(hours=9)

    today = datetime.date.today()

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('data/token.pickle'):
        with open('data/token.pickle', 'rb') as token:
            creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'data/credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('data/token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        timefrom = datetime.datetime.strptime(
            today.strftime('%Y/%m/%d'), '%Y/%m/%d'
        ).isoformat()+'Z'
        timeto = (datetime.datetime.strptime(
            today.strftime('%Y/%m/%d'), '%Y/%m/%d'
        )+datetime.timedelta(days=1)).isoformat()+'Z'
        events_result = service.events().list(calendarId=ID,
                                              timeMin=timefrom,
                                              timeMax=timeto,
                                              singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            message = f"\n{today.strftime('%m月%d日')}の予定はありません"
            return message

        message = f"\n{today.strftime('%m月%d日')}の予定\n\n"
        for event in events:
            start = datetime.datetime.strptime(
                event['start']['dateTime'], '%Y-%m-%dT%H:%M:%SZ') + TIME_DIFF

            if start.strftime('%Y/%m/%d') == today.strftime('%Y/%m/%d'):
                message += f"{start.strftime('%H:%M ')}{event['summary']}\n"

        return message

    return "\nカレンダーにアクセスできませんでした"


def main():
    message = get_schedules()
    notice.notice(message)


if __name__ == '__main__':
    main()
