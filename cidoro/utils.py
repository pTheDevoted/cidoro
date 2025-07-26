import time
import os
import sys
import json
from . import display
from .display import play_alarm_for_5s_display
from pystyle import Center

BASE_DIR = os.path.dirname(__file__)
progress_file = os.path.join(BASE_DIR, "progress.json")


def getch(timeout=None):
    import tty, termios, select
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        if timeout is None:
            ch = sys.stdin.read(1)
        else:
            rlist, _, _ = select.select([sys.stdin], [], [], timeout)
            ch = sys.stdin.read(1) if rlist else None
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
    return ch


def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02}h:{minutes:02}m:{secs:02}s"


def run_classic_pomodoro(theme, work_min, break_min, long_break_min, save_progress):
    cycle = 1
    total_work_time = 0
    total_break_time = 0
    start_time = time.strftime("%Y-%m-%d %H:%M:%S")

    while True:
        elapsed, quit_flag = run_pomodoro(work_min * 60, "Work", cycle, theme)
        if not quit_flag:
            play_alarm_for_5s_display()
        total_work_time += elapsed
        if quit_flag:
            break

        if cycle % 4 == 0:
            input(Center.XCenter(f'\n{display.white}Nice bro! press enter to start long break.'))
            elapsed, quit_flag = run_pomodoro(long_break_min * 60, "Long Break", cycle, theme)
        else:
            input(Center.XCenter(f'\n{display.white}Nice bro! press enter to start break.'))
            elapsed, quit_flag = run_pomodoro(break_min * 60, "Break", cycle, theme)
        if not quit_flag:
            play_alarm_for_5s_display()
        total_break_time += elapsed
        if quit_flag:
            break

        input(Center.XCenter(f'\n{display.white}Nice bro! press enter to start next cycle.'))
        cycle += 1

    end_time = time.strftime("%Y-%m-%d %H:%M:%S")

    os.system("clear")
    print(Center.XCenter(f"\n\n\n⌛ {display.bwhite}Gross study time{display.white} {display.lwhite}(work+break){display.white}: {format_time(total_work_time+total_break_time)}"))
    print(Center.XCenter(f"⌛ {display.bwhite}Net study time{display.white} {display.lwhite}(work){display.white}: {format_time(total_work_time)}"))
    input(Center.XCenter("\nPress enter to menu."))

    if save_progress:
        data = {
            "start_time": start_time,
            "end_time": end_time,
            "gross_time": total_work_time + total_break_time,
            "net_time": total_work_time,
            "cycles": cycle - 1,  # ciclo real concluído
            "config": {"work_min": work_min, "break_min": break_min, "long_break_min": long_break_min}
        }
        try:
            if os.path.exists(progress_file):
                with open(progress_file, "r") as f:
                    all_data = json.load(f)
            else:
                all_data = []
        except Exception as e:
            print(f"Erro ao ler progress.json: {e}")
            all_data = []

        all_data.append(data)
        try:
            with open(progress_file, "w") as f:
                json.dump(all_data, f, indent=4)
        except Exception as e:
            print(f"Erro ao salvar progress.json: {e}")


def run_pomodoro(duration, label, cycle, theme):
    paused = False
    pause_start = None
    elapsed_pause = 0
    start = time.time()
    while True:
        now = time.time()
        elapsed = (pause_start if paused else now) - start - elapsed_pause
        left = max(0, duration - int(elapsed))

        if left <= 0:
            play_alarm_for_5s_display()
            return duration, False

        mins, secs = divmod(left, 60)
        timer_str = f"{mins:02}:{secs:02}"
        os.system("clear")
        display.print_timer(timer_str, label, cycle, theme, paused)

        ch = getch(timeout=1)
        if ch == ' ':
            if not paused:
                paused = True
                pause_start = time.time()
            else:
                paused = False
                elapsed_pause += time.time() - pause_start
        elif ch in ('q', 'Q'):
            elapsed_total = int(time.time() - start - elapsed_pause)
            return elapsed_total, True
