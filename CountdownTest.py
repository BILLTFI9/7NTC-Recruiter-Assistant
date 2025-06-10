import threading
import time

_timer_running = False
def _countdown_thread_function(duration_seconds):
    global _timer_running
    temp_seconds = duration_seconds
    while temp_seconds >= 0 and _timer_running:
        mins, secs = divmod(temp_seconds, 60)
        time_str = "   {:02d}:{:02d}".format(mins, secs)
        print(time_str, end="\r")
        time.sleep(1)
        temp_seconds -= 1
    print("\nTimer finished!")
    _timer_running = False

def start_non_blocking_timer(duration_seconds):
    global _timer_running
    if not _timer_running:
        _timer_running = True
        timer_thread = threading.Thread(target=_countdown_thread_function, args=(duration_seconds,))
        timer_thread.daemon = True
        timer_thread.start()
