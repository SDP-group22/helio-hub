def valid_ip(ip):
    octets = ip.split('.')
    if len(octets) != 4:
        return False
    for x in octets:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True


def valid_day(day):
    if day == 'Monday':
        return True
    if day == 'Tuesday':
        return True
    if day == 'Wednesday':
        return True
    if day == 'Thursday':
        return True
    if day == 'Friday':
        return True
    if day == 'Saturday':
        return True
    if day == 'Sunday':
        return True
    else:
        return False


def day_number_to_day_name(day_number):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return days[day_number]


def is_later(time1, time2):
    hour1, minute1 = time1.split(':')
    hour2, minute2 = time2.split(':')

    if hour1 > hour2:
        return True
    if hour2 > hour1:
        return False
    if minute1 > minute2:
        return True
    else:
        return False


def get_sec(time_str):
    h, m = time_str.split(':')
    return int(h) * 3600 + int(m) * 60
