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


def job_mapper(job):
    switcher = {
        'r': 1,
        's': 1.2,
        'm': 1.5
    }
    return switcher.get(job)


def amount_calculator(hours, day, job):
    day_type = day_mapper(day)
    has_worked_additionaly = hours > 8
    additional_hours = has_worked_additionaly * (hours - 8)
    partial_hours = not has_worked_additionaly * (additional_hours > 0) * hours

    sum = 0
    sum += (day_type in 'reg') * partial_hours * 30
    sum += (day_type in 'reg') * (has_worked_additionaly * 8 * 30 + additional_hours * 35)

    sum += (day_type in 'end') * partial_hours * 42
    sum += (day_type in 'end') * (has_worked_additionaly * 8 * 42 + additional_hours * 49)

    return sum * job_mapper(job)


print('Menu: \n r: Regular \n s: Supervison \n m: Manager')
job = str(input())
print('Enter work day:')
day = str(input())
print('Enter work hours:')
work_hours = int(input())
print(amount_calculator(work_hours, day, job))
