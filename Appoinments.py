import datetime
import os
import pytz
import json
from google.oauth2 import service_account
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from flask import Flask, request, make_response
from dotenv import load_dotenv


load_dotenv()


calendar_id = os.getenv('Calendar_Id')
service_account_file = 'cyberli-takx-de2049a95968.json'
timezone = 'Africa/Johannesburg'
class AppointmentScheduler:
    def __init__(self, calendar_id=calendar_id, service_account_file=service_account_file, timezone=timezone):
        # Set up Google Calendar API service account credentials
        self.calendar_id = calendar_id
        self.service_account_file = service_account_file
        self.creds = service_account.Credentials.from_service_account_file(
            service_account_file, scopes=['https://www.googleapis.com/auth/calendar'])
        self.calendar_service = build('calendar', 'v3', credentials=self.creds)
        self.timezone = timezone

    def calculate_appointment_time(self, date, time):
        date_time_str = f"{date} {time}"
        date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')
        appointment_start = date_time_obj.astimezone(pytz.timezone(self.timezone))
        appointment_end = appointment_start + datetime.timedelta(hours=1)
        return appointment_start, appointment_end

    def create_calendar_event(self, start_time, end_time, event_name):
        event = {
            'summary': f'{event_name} Appointment',
            'description': event_name,
            'start': {
                'dateTime': start_time.isoformat(),
                'timeZone': self.timezone,
            },
            'end': {
                'dateTime': end_time.isoformat(),
                'timeZone': self.timezone,
            },
        }
        events_result = self.calendar_service.events().list(
            calendarId=self.calendar_id, alwaysIncludeEmail=False, orderBy='updated').execute()
        events = events_result.get('items', [])    
        try:
            for _event in events:
                if event['start'] == _event['start']:
                    raise Exception(f"Found duplicate event: {_event['summary']}")
            event = self.calendar_service.events().insert(calendarId=self.calendar_id, body=event).execute()
        except Exception as e:
            #print(f"An error occurred: {e}")
            raise Exception(f"An error occurred: {e}")
        return event

    def schedule_appointment(self, appointment_type, datetime):
        # Extract the date and time from the datetime string
        time = datetime.split('T')[1][:5]  # Extract the time as 'HH:MM'
        date = datetime.split('T')[0]  # Extract the date as 'YYYY-MM-DD'
        appointment_start, appointment_end = self.calculate_appointment_time(date, time)

        # Check the availability of the time, and make an appointment if there is time on the calendar
        try:
            self.create_calendar_event(appointment_start, appointment_end, appointment_type)
            fulfillment = f"Ok, we can fit you in for {appointment_type} at {appointment_start.strftime('%B %d, %Y at %I:%M %p')}."
        except HttpError as error:
            #print('An error occurred: %s' % error)
            fulfillment = f"An error occurred while scheduling the appointment. Please try again later."
        except Exception as e:
            #print(f'An error occurred: {e}')
            fulfillment = f"Sorry, there is already an event scheduled at {appointment_start.strftime('%B %d, %Y at %I:%M %p')}."

        res = {
            'fulfillmentText': fulfillment
        }
        return res
