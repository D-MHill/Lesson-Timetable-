lessons = [

    # MONDAY
    {"day": "Monday", "time": "09:15", "subject": "Maths"},
    {"day": "Monday", "time": "10:00", "subject": "Biology"},
    {"day": "Monday", "time": "10:45", "subject": "Break"},
    {"day": "Monday", "time": "11:00", "subject": "English"},
    {"day": "Monday", "time": "11:45", "subject": "History"},
    {"day": "Monday", "time": "12:30", "subject": "Lunch"},
    {"day": "Monday", "time": "13:30", "subject": "Spanish"},
    {"day": "Monday", "time": "14:15", "subject": "Computing"},

    # TUESDAY
    {"day": "Tuesday", "time": "09:15", "subject": "English"},
    {"day": "Tuesday", "time": "10:00", "subject": "Maths"},
    {"day": "Tuesday", "time": "10:45", "subject": "Break"},
    {"day": "Tuesday", "time": "11:00", "subject": "Geography"},
    {"day": "Tuesday", "time": "11:45", "subject": "Art"},
    {"day": "Tuesday", "time": "12:30", "subject": "Lunch"},
    {"day": "Tuesday", "time": "13:30", "subject": "Food Technology"},
    {"day": "Tuesday", "time": "14:15", "subject": "DT"},

    # WEDNESDAY
    {"day": "Wednesday", "time": "09:15", "subject": "Maths"},
    {"day": "Wednesday", "time": "10:00", "subject": "English"},
    {"day": "Wednesday", "time": "10:45", "subject": "Break"},
    {"day": "Wednesday", "time": "11:00", "subject": "Biology"},
    {"day": "Wednesday", "time": "11:45", "subject": "Computing"},
    {"day": "Wednesday", "time": "12:30", "subject": "Lunch"},
    {"day": "Wednesday", "time": "13:30", "subject": "Geography"},
    {"day": "Wednesday", "time": "14:15", "subject": "History"},

    # THURSDAY
    {"day": "Thursday", "time": "09:15", "subject": "English"},
    {"day": "Thursday", "time": "10:00", "subject": "Maths"},
    {"day": "Thursday", "time": "10:45", "subject": "Break"},
    {"day": "Thursday", "time": "11:00", "subject": "Spanish"},
    {"day": "Thursday", "time": "11:45", "subject": "Art"},
    {"day": "Thursday", "time": "12:30", "subject": "Lunch"},
    {"day": "Thursday", "time": "13:30", "subject": "DT"},
    {"day": "Thursday", "time": "14:15", "subject": "Food Technology"},

    # FRIDAY
    {"day": "Friday", "time": "09:15", "subject": "Maths"},
    {"day": "Friday", "time": "10:00", "subject": "English"},
    {"day": "Friday", "time": "10:45", "subject": "Break"},
    {"day": "Friday", "time": "11:00", "subject": "Biology"},
    {"day": "Friday", "time": "11:45", "subject": "Computing"},
    {"day": "Friday", "time": "12:30", "subject": "Lunch"},
    {"day": "Friday", "time": "13:30", "subject": "Geography"},
    {"day": "Friday", "time": "14:15", "subject": "Spanish"}
]

day = input("What day would you like to see? ")

for lesson in lessons:
    if day.lower() == lesson["day"].lower():
        print(lesson["time"], "-", lesson["subject"])