import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

link = 'https://api.weekify.ru/api/calendar/get_week'
headers = {
    'Authorization': os.getenv("TOKEN")
}
data = {
    
}

response = requests.post(link, headers=headers, data=data)
response_data = json.loads(response.text)

print(response.text)

# Перебираем дни
for day in response_data["days"]:
    date = day["date"]
    date_marker = day["date_marker"]
    
    print(f"Date: {date}, Date Marker: {date_marker}")

    # Перебираем занятия в каждом дне
    for lesson in day["lessons"]:
        lesson_id = lesson["id"]
        student = lesson.get("student", "N/A")
        start_time = lesson.get("start_time", "N/A")
        end_time = lesson.get("end_time", "N/A")
        
        print(f"Lesson ID: {lesson_id}, Student: {student}, Start Time: {start_time}, End Time: {end_time}")

# Доступ к next_date и prev_date
next_date = response_data["next_date"]
prev_date = response_data["prev_date"]
print(f"Next Date: {next_date}, Previous Date: {prev_date}")
