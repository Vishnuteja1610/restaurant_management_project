from datetime import datetime, time

def is_restaurant_open():
    now = datetime.now()
    weekday = now.weekday()

    open_time = time(9,0)
    close_time = time(22,0)

    current_time = now.time()
    return open_time <= current_time <=close_time