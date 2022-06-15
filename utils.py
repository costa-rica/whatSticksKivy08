import json;import datetime;from datetime import timedelta;import os, zipfile;
import requests
import time
import pytz
from pytz import timezone
import datetime


base_url = 'https://api.what-sticks-health.com'


def text_size_coef_utility(size):
  if size=='small':
    text_size_coef=.05
    text_size_coef_sm =.03
  elif size=='big':
    text_size_coef=.07
    text_size_coef_sm=.05
  else:
    text_size_coef=.06
    text_size_coef_sm=.04
  return (text_size_coef,text_size_coef_sm)

def add_activity_util(title, note,user_id,user_timezone,date_str,time_str, user_email,login_token):
  print('**** Add activity ****')
  url=base_url + "/add_activity"

  payload={}
  headers={}
  #convert datetime_thing to string
  datetime_thing=datetime.datetime.strptime(date_str+" "+ time_str,'%m/%d/%Y %I:%M %p')
  datetime_thing_str=datetime_thing.strftime('%Y-%m-%dT%H:%M:%S')
  user_tz = timezone(user_timezone)
  datetime_tz_aware=user_tz.localize(datetime_thing)
  timezone_delta=datetime_tz_aware.utcoffset().total_seconds()/60

  payload['datetime_of_activity']=datetime_thing_str
  payload['time_offset']=timezone_delta
  payload["var_activity"]= title
  payload["user_id"]= user_id
  payload["source_name"]= "iPhone"
  payload["note"]= note

  headers['Content-Type']='application/json'
  headers['x-access-token'] = login_token

  # response = requests.request("POST", url, headers=headers,
  #     data=str(json.dumps(payload)))
  # print('api response:::',response.status_code)
  print('payload:',type(payload))
  print(payload)

def current_time_util(user_timezone):
  date_time_obj=datetime.datetime.now()
  date_time_obj_tz_aware=timezone(user_timezone).localize(date_time_obj)
  hour_temp=date_time_obj_tz_aware.strftime("%H")
  hour=hour_temp if hour_temp[0]!='0' else hour_temp[1]
  am_pm='AM' if int(hour)<12 else 'PM'
  hour=hour if int(hour)<13 else str(int(hour)-12)
  minute=date_time_obj_tz_aware.strftime("%M")
  time_thing=f'{hour}:{minute} {am_pm}'
  date_thing=date_time_obj_tz_aware.strftime("%m/%d/%Y")
  date_time_now=(date_thing,time_thing)

  return(date_time_now)



def table_api_util(login_token):

  url_get_activities=base_url + '/kivy_table01'
  headers = {'x-access-token':login_token, 'Content-Type': 'application/json'}
  response = requests.request('GET',url_get_activities, headers=headers)
  print('url_get_activities:::', url_get_activities)
  response_dict = json.loads(response.text)

  print('response_list:::',type(response_dict['content']))
  print('response_list:::', response_dict['content'][0])

  row_data_list=[
    [i[0],convert_datetime(i[1]),i[2], make_date_string(i[1]),h] for h,i in enumerate(response_dict['content'])
    ]
  print('****row_data_list created****')
  print(row_data_list[0:3])
  return row_data_list

def convert_datetime(date_time_str):
    try:
        date_time_obj = datetime.datetime.strptime(date_time_str, '%a, %d %b %Y %H:%M:%S %Z')
    except ValueError:
        # date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%S')
        print("""There is an error converting datetimes in
        scroll_table_data.py or with API call to kivy_table01""")
    # return date_time_obj.strftime("%m/%d/%Y, %H:%M:%S")
    return date_time_obj.strftime("%b%-d '%-y %-I:%M%p")#<------Potential hangup!***************!

def make_date_string(date_time_str):
    date_time_obj = datetime.datetime.strptime(date_time_str, '%a, %d %b %Y %H:%M:%S %Z')
    return date_time_obj.strftime('%Y%m%d')
