import pygetwindow as gw
import time
import threading

# Work Applications (lowercase)
Work_Apps = ['pycharm', 'brave', 'excel', 'word', 'vscode']

stop_flag = False

def get_active_window():
    try:
        window = gw.getActiveWindow()
        if window:
            return window.title.lower()
    except Exception as e:
        print('Error:', e)
    return 'unknown'

def is_work_app(active_window):
    return any(app in active_window for app in Work_Apps) if active_window else False

def monitor_work_time():
    global stop_flag
    work_time = 0
    start_time = None

    print("Work Hours Monitor Started... Type 'stop' to end.\n")

    while not stop_flag:
        active_window = get_active_window()
        if is_work_app(active_window):
            if start_time is None:
                start_time = time.time()
        else:
            if start_time:
                work_time += time.time() - start_time
                start_time = None

        print(f"Total Work Time: {round(work_time / 60, 2)} minutes", end="\r")
        time.sleep(10)

    if start_time:
        work_time += time.time() - start_time

    total_minutes = round(work_time / 60, 2)
    hours = int(total_minutes // 60)
    minutes = int(total_minutes % 60)
    print("\n\nMonitoring Stopped.")
    print(f"Total Work Time: {hours} hour(s) and {minutes} minute(s) ({total_minutes} minutes)")

# Run monitor in a separate thread
monitor_thread = threading.Thread(target=monitor_work_time)
monitor_thread.start()

# Wait for user input to stop
while True:
    user_input = input("Type 'stop' to end: ").strip().lower()
    if user_input == 'stop':
        stop_flag = True
        monitor_thread.join()
        break
