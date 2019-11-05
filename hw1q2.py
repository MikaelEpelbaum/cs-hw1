print('Menu: \n r: Regular \n s: Supervison \n m: Manager')
job = str(input())
print('Enter work day:')
day = str(input())
print('Enter work hours:')
hours = int(input())

calculator = job_mapper(job) *


def job_mapper(job):
    switcher = {
        'r': 1,
        's': 1.2,
        'm': 1.5
    }
    return switcher.get(job)

def day_mapper(day):
    switcher = {
        'sun': 'reg',
        'mon': 'reg',
        'tue': 'reg',
        'wed': 'reg',
        'thu': 'reg',
        'fri': 'end',
        'sat': 'end'
    }
    return switcher.get(day)

def reg_hours_mapper(hours):
    switcher = {
        8: 30,
        9: 35
    }
    return switcher.get(hours)

def end_hours_mapper(hours):
    switcher = {
        8: 42,
        9: 49
    }
    return switcher.get(hours)