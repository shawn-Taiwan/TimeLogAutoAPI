import requests
import json
from datetime import date, timedelta

timelog = 'http://140.124.181.95:30200/api/log/record'

logList = []
userID = "" #Your user ID
today = date.today()
today = today-timedelta(days=7)  #How many days you need to push back to last week or the week you want
while today.weekday() != 0: #Find that week's monday
  today = today-timedelta(days=1)
monday=today.strftime('%Y/%m/%d')
tuesday=(today-timedelta(days=-1)).strftime('%Y/%m/%d')
wendesday=(today-timedelta(days=-2)).strftime('%Y/%m/%d')
thursday=(today-timedelta(days=-3)).strftime('%Y/%m/%d')
friday=(today-timedelta(days=-4)).strftime('%Y/%m/%d')

# API Json templete
# activityTypeName should be same as Active Type
logList.append({
'activityTypeName': 'LabProject',
'activityUnitID': "3ac3fee8-1ad9-49ac-9c77-e5c7dc28be8f",
'description': '',
'startTime': monday+' 10:00',
'endTime': monday+' 12:00',
'title': 'dctrack',
'userID': userID
})
logList.append({
'activityTypeName': 'LabProject',
'activityUnitID': "3ac3fee8-1ad9-49ac-9c77-e5c7dc28be8f",
'description': '',
'startTime': monday+' 14:00',
'endTime': monday+' 18:00',
'title': 'dctrack',
'userID': userID
})
logList.append({
'activityTypeName': 'study group',
'activityUnitID': userID,
'description': '',
'startTime': tuesday+' 10:00',
'endTime': tuesday+' 10:30',
'title': 'study group',
'userID': userID
})
logList.append({
'activityTypeName': 'LabProject',
'activityUnitID': "3ac3fee8-1ad9-49ac-9c77-e5c7dc28be8f",
'description': '',
'startTime': tuesday+' 11:00',
'endTime': tuesday+' 12:00',
'title': 'dctrack',
'userID': userID
})
logList.append({
'activityTypeName': 'LabProject',
'activityUnitID': "3ac3fee8-1ad9-49ac-9c77-e5c7dc28be8f",
'description': '',
'startTime': tuesday+' 14:00',
'endTime': tuesday+' 18:00',
'title': 'dctrack',
'userID': userID
})
logList.append({
'activityTypeName': 'LabProject',
'activityUnitID': "3ac3fee8-1ad9-49ac-9c77-e5c7dc28be8f",
'description': '',
'startTime': wendesday+' 10:00',
'endTime': wendesday+' 12:00',
'title': 'dctrack',
'userID': userID
})
logList.append({
'activityTypeName': 'LabProject',
'activityUnitID': "3ac3fee8-1ad9-49ac-9c77-e5c7dc28be8f",
'description': '',
'startTime': wendesday+' 14:00',
'endTime': wendesday+' 15:00',
'title': 'dctrack',
'userID': userID
})
logList.append({
'activityTypeName': 'LabProject',
'activityUnitID': "3ac3fee8-1ad9-49ac-9c77-e5c7dc28be8f",
'description': '',
'startTime': thursday+' 15:00',
'endTime': thursday+' 18:00',
'title': 'dctrack',
'userID': userID
})
logList.append({
'activityTypeName': 'LabProject',
'activityUnitID': "3ac3fee8-1ad9-49ac-9c77-e5c7dc28be8f",
'description': '',
'startTime': friday+' 10:00',
'endTime': friday+' 12:00',
'title': 'dctrack',
'userID': userID
})
logList.append({
'activityTypeName': 'LabProject',
'activityUnitID': "3ac3fee8-1ad9-49ac-9c77-e5c7dc28be8f",
'description': '',
'startTime': friday+' 14:00',
'endTime': friday+' 15:00',
'title': 'dctrack',
'userID': userID
})

print(monday)

for log in logList :
  # response = requests.options(timelog)
  # print(response.status_code)
  r = requests.post(timelog, data=json.dumps(log), headers={"Content-Type":"application/json"})
  print(r.status_code)
