import requests
import json
from datetime import date, timedelta

timelog = 'https://ssl-timelog.csie.ntut.edu.tw/api/log/record'

logList = []
userID = "" #Your user ID
today = date.today()
today = today-timedelta(days=4)  #How many days you need to push back to last week or the day you want
while today.weekday() != 0: #Find that week's monday
  today = today-timedelta(days=1)
monday=today.strftime('%Y/%m/%d')
tuesday=(today-timedelta(days=-1)).strftime('%Y/%m/%d')
wendesday=(today-timedelta(days=-2)).strftime('%Y/%m/%d')
thursday=(today-timedelta(days=-3)).strftime('%Y/%m/%d')
friday=(today-timedelta(days=-4)).strftime('%Y/%m/%d')

#API Json templete
#activityTypeName should be same as Active Type
logList.append({
'activityTypeName': 'LabProject',
'description': '',
'startTime': monday+' 14:00',
'endTime': monday+' 18:00',
'title': 'dctrack',
'userID': userID
})
logList.append({
'activityTypeName': 'study group',
'description': '',
'startTime': tuesday+' 10:00',
'endTime': tuesday+' 10:30',
'title': 'study group',
'userID': userID
})
logList.append({
'activityTypeName': 'LabProject',
'description': '',
'startTime': tuesday+' 14:00',
'endTime': tuesday+' 18:00',
'title': 'dctrack',
'userID': userID
})
logList.append({
'activityTypeName': 'LabProject',
'description': '',
'startTime': wendesday+' 10:00',
'endTime': wendesday+' 12:00',
'title': 'dctrack',
'userID': userID
})
logList.append({
'activityTypeName': 'LabProject',
'description': '',
'startTime': wendesday+' 14:00',
'endTime': wendesday+' 18:00',
'title': 'dctrack',
'userID': userID
})
logList.append({
'activityTypeName': 'LabProject',
'description': '',
'startTime': thursday+' 10:00',
'endTime': thursday+' 12:00',
'title': 'dctrack',
'userID': userID
})
logList.append({
'activityTypeName': 'LabProject',
'description': '',
'startTime': thursday+' 14:00',
'endTime': thursday+' 18:00',
'title': 'dctrack',
'userID': userID
})

print(monday)

for log in logList :
  r = requests.post(timelog, data=json.dumps(log), headers={"Content-Type":"application/json"})
  print(r.status_code)
