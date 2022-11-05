from datetime import datetime, date


users = [{'name': 'John', 'birthday': date(1978, 11, 5)},
         {'name': 'Marta', 'birthday': date(1990, 11, 6)},
         {'name': 'Bill', 'birthday': date(2000, 11, 7)},
         {'name': 'Michael', 'birthday': date(1959, 11, 8)},
         {'name': 'Fredd', 'birthday': date(1978, 11, 9)},
         {'name': 'Austin', 'birthday': date(1978, 11, 10)},
         {'name': 'Lisa', 'birthday': date(1978, 11, 11)}]

def get_birthdays_per_week(users: dict, current_date=datetime.now().date()):
    week_days = {'Monday': [],
                'Tuesday': [],
                'Wednesday': [],
                'Thursday': [],
                'Friday': []}
    for user in users:
        if 0 <= user['birthday'].day - current_date.day <= 7:
            brth_date = date(current_date.year, user['birthday'].month, user['birthday'].day)
            if brth_date.strftime('%A') not in ('Sunday', 'Saturday'):
                brth_day = brth_date.strftime('%A')
            else: brth_day = 'Monday'
            week_days[brth_day].append(user['name'])
    for day, user in zip(week_days.keys(), week_days.values()):
        us = ', '.join(i for i in user)
        if us:
            print(day+':', us)

def main():
    get_birthdays_per_week(users)      
            
if __name__ == '__main__':
    main()