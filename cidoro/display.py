from pystyle import Colorate, Colors, Center
import shutil, random, os, threading
import subprocess

alarm_file = os.path.join(os.path.dirname(__file__), "alarm.mp3")

def tocar_alarme():
    try:
        subprocess.run([
            "ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet", alarm_file
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"Erro ao tocar alarme: {e}")

def play_alarm_for_5s_display():
    thread = threading.Thread(target=tocar_alarme, daemon=True)
    thread.start()

def play_alarm_now():
    tocar_alarme()

logotipo = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠻⣶⡆⠀⠿⠀⣶⠒⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣴⠾⠛⢹⣶⡤⢶⣿⡟⠶⠦⠄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣶⣤⣤⣤⣤⣴⠂⠸⠋⢀⣄⡉⠓⠀⠲⣶⣾⣿⣷⣄⠀⠀⠀⠀
⠀⠀⠀⢀⣾⡿⠋⠁⣠⣤⣿⡟⢀⣠⣾⣿⣿⣿⣷⣶⣤⣼⣿⣿⣿⣿⣆⠀⠀⠀
⠀⠀⠀⣾⡟⠀⣰⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀
⠀⠀⢸⡿⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
⠀⠀⢸⡇⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
⠀⠀⢸⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀
⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀
⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

logo = """
    █████████   ███      █████                            
  ███░░░░░███ ░░░      ░░███                             
 ███     ░░░  ████   ███████   ██████  ████████   ██████ 
░███         ░░███  ███░░███  ███░░███░░███░░███ ███░░███
░███          ░███ ░███ ░███ ░███ ░███ ░███ ░░░ ░███ ░███
░░███     ███ ░███ ░███ ░███ ░███ ░███ ░███     ░███ ░███
 ░░█████████  █████░░████████░░██████  █████    ░░██████ 
  ░░░░░░░░░  ░░░░░  ░░░░░░░░  ░░░░░░  ░░░░░      ░░░░░░  
"""

baarco = '''
                   ~.                       
            Ya...___|__..ab.     .   .  
             Y88b   |88b  y88b   (   )  
              Y88b  :88b  :88b   `.oo'   
              :888  |888  |888  ( (`-'   
     .---.    d88P  ;88P  ;88P   `.`.    
    / .-._)  d8P-"""|"""'-Y8P      `.`.  
   ( (`._) .-.  .-. |.-.  .-.  .-.   ) ) 
    \ `---( O )( O )( O )( O )( O )-' /  
     `.    `-'  `-'  `-'  `-'  `-'  .' cidoro.
       `---------------------------'
'''

def random_banners():
    return random.choice([logotipo, logo, baarco])

def random_phrase():
    frases = [
        "     Discipline is the key.",
        "      Welcome to Cidoro.",
        "         TOMATOEEEE",
        " Your pomodor time, in your time."
    ]
    return random.choice(frases)

intro = f"""
{logotipo}
{random_phrase()}
"""

def center(text):
    width = shutil.get_terminal_size((80, 20)).columns
    return text.center(width)

def show_logo(theme):
    os.system("clear")
    color = get_color_for_theme(theme)
    print(Colorate.Horizontal(color, Center.XCenter(logo)))
    print('\n')

def random_logo(theme):
    os.system("clear")
    color = get_color_for_theme(theme)
    print(Colorate.Horizontal(color, Center.XCenter(random_banners())))
    print('\n')

def get_color_for_theme(theme):
    if theme == "Dracula":
        return Colors.purple_to_blue
    elif theme == "Solarized":
        return Colors.red_to_yellow
    elif theme == "Clean":
        return Colors.green_to_black
    else:
        return Colors.cyan_to_blue

def print_timer(timer_str, label, cycle, theme, paused):
    color = Colors.green_to_black if theme=="Clean" else (
        Colors.blue_to_green if int(timer_str[:2])>3 else Colors.green_to_yellow)
    print("\n"*3)
    print(Colorate.Horizontal(color, Center.XCenter(f"{timer_str} - {label} | Cycle number: {cycle}")))
    print(Center.XCenter(f"Press space to pause/resume, q to quit"))
    if paused:
        print(Center.XCenter("\n▶"))
    else:
        print(Center.XCenter("\n⏸"))

class display:
    gi = "\033[3;90m"
    black = "\033[0;30m"
    red = "\033[0;31m"
    bred = "\033[1;31m"
    green = "\033[0;32m"
    bgreen = "\033[1;32m"
    yellow = "\033[0;33m"
    byellow = "\033[1;33m"
    blue = "\033[0;34m"
    bblue = "\033[1;34m"
    purple = "\033[0;35m"
    bpurple = "\033[1;35m"
    cyan = "\033[0;36m"
    bcyan = "\033[1;36m"
    white = "\033[0m"
    bwhite = "\033[1;37m"
    lwhite = "\033[5;37m"
    iwhite = "\033[3;1;37m"

bwhite = display.bwhite
byellow = display.byellow
yellow = display.yellow
white = display.white
red = display.red
green = display.green
bred = display.bred
bgreen = display.bgreen
bblue = display.bblue
blue = display.blue
purple = display.purple
bpurple = display.bpurple
cyan = display.cyan
bcyan = display.bcyan
gi = display.gi
lwhite = display.lwhite
iwhite = display.iwhite
