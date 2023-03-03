def secondsToText(secs):
    days = secs // 86400
    hours = (secs - days * 86400) // 3600
    minutes = (secs - days * 86400 - hours * 3600) // 60
    seconds = secs - days * 86400 - hours * 3600 - minutes * 60
    result = ("{} days, ".format(days) if days else "") + \
             ("{} hours, ".format(hours) if hours else "") + \
             ("{} minutes, ".format(minutes) if minutes else "") + \
             ("{} seconds, ".format(seconds) if seconds else "")
    print(result)

sec = int(input('Input seconds: '))
secondsToText(sec)