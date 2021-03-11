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
