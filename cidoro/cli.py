import sys
import os
import shutil, time, json
from InquirerPy import prompt
from pystyle import Colorate, Colors, Center
from . import utils, display
from terminaltexteffects.effects.effect_beams import Beams

# Variáveis globais
BASE_DIR = os.path.dirname(__file__)
progress_file = os.path.join(BASE_DIR, "progress.json")
themes_file = os.path.join(BASE_DIR, "themes.txt")
default_theme = "Default"
current_theme = default_theme

def center(text):
    width = shutil.get_terminal_size((80, 20)).columns
    return text.center(width)

def read_theme():
    if os.path.exists(themes_file):
        with open(themes_file, "r") as f:
            return f.read().strip()
    return default_theme

def write_theme(theme):
    with open(themes_file, "w") as f:
        f.write(theme)

def get_prompt_style(theme):
    if theme == "Dracula":
        return {"question": "fg:#bd93f9", "answer": "fg:#ff79c6", "pointer": "fg:#bd93f9"}
    elif theme == "Solarized":
        return {"question": "fg:#f39c12", "answer": "fg:#e67e22", "pointer": "fg:#f39c12"}
    elif theme == "Clean":
        return {"question": "fg:#888888", "answer": "fg:#aaaaaa", "pointer": "fg:#888888"}
    else:
        return {"question": "fg:#00aaff", "answer": "fg:#00ffaa", "pointer": "fg:#00aaff"}

def themes_menu():
    global current_theme
    themes = ["Default", "Solarized", "Dracula", "Clean"]
    questions = [{
        "type": "checkbox",
        "message": center("Select a theme (only one)"),
        "name": "themes",
        "choices": [{"name": t, "value": t} for t in themes],
        "default": [current_theme],
    }]
    answer = prompt(questions, style=get_prompt_style(current_theme))
    selected = answer["themes"]
    if selected:
        current_theme = selected[0]
        write_theme(current_theme)
        print(center(f"Selected theme: {current_theme}"))
    else:
        print(center("No theme selected. Keeping current theme."))
    input(center("Press Enter to return"))

def appearance_menu():
    while True:
        display.show_logo(current_theme)
        questions = [{
            "type": "list",
            "name": "appearance",
            "message": center("1. Appearance menu"),
            "choices": [center("1. Themes"), center("2. Return to config")]
        }]
        choice = prompt(questions, style=get_prompt_style(current_theme))["appearance"].strip()
        if choice.startswith("1. Themes"): themes_menu()
        elif choice.startswith("2. Return"): return

def config_menu():
    while True:
        display.show_logo(current_theme)
        questions = [{
            "type": "list",
            "name": "config",
            "message": center("Config menu"),
            "choices": [center("1. Appearance"), center("2. Info"), center("3. Return to menu")]
        }]
        choice = prompt(questions, style=get_prompt_style(current_theme))["config"].strip()
        if choice.startswith("1. Appearance"): appearance_menu()
        elif choice.startswith("2. Info"):
            display.random_logo(current_theme)
            print(Center.XCenter(f"""
{display.bwhite}What is Cidoro?{display.white}

Cidoro is a minimalist CLI Pomodoro timer written in Python,
built for focus, discipline, and tracking deep work or study sessions.

• Version: 0.1.0
• Language: Python 3
• Modular architecture: CLI menus (cli), logic (utils), and visual UI (display)
• Data persistence: logs sessions to JSON (cycles, durations, config)
• Theme system: switch between multiple CLI color themes
• Configurable via [pyproject.toml], easily installed with pip
• Built-in alarm system: plays sound at the end of work and break sessions
• Editable install for instant development: `pip install -e .`
• Terminal effects using InquirerPy and Pystyle

Perfect for developers who value clean code, fast feedback, and a beautiful terminal experience.

🔗 GitHub: https://github.com/pTheDevoted/cidoro
"""))
            input(Center.XCenter(f"\nPress {display.iwhite}enter{display.white} to return"))
        elif choice.startswith("3. Return"): return

def run_menu():
    effect = Beams(display.intro)
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)
    time.sleep(1.5)

    while True:
        display.show_logo(current_theme)
        questions = [{
            "type": "list",
            "name": "option",
            "message": center("Select an option"),
            "choices": [
                center("1. Start Pomodoro"),
                center("2. View progress"),
                center("3. Config"),
                center("4. Exit")
            ]
        }]
        choice = prompt(questions, style=get_prompt_style(current_theme))["option"].strip()

        if choice.startswith("1. Start Pomodoro"):
            display.random_logo(current_theme)
            print(Center.XCenter(f"""
{display.bwhite}In the first place:{display.white}
• Pomodoro Technique in classic format: how it works
• Work in focused blocks of 25 minutes (“pomodoros”).
• After each block, take a short break (about 5 minutes).
• After 4 pomodoros, take a longer break (15–30 minutes).
• Helps with focus, productivity, and reducing stress while studying or working.

Here, you can fully customize your Pomodoro timer to your needs, using the default format (recommended) or modifying it to suit your preferences.

When you start, press the {display.iwhite}space bar{display.white} to pause/resume the timer and {display.iwhite}q{display.white} to end the session.

After finishing, you'll receive your
gross and net study time — gross time is the 
total time you spent studying, including breaks; 
net time is the time you actually focused, excluding breaks."""))
            input(Center.XCenter(f"\nPress {display.iwhite}enter{display.white} to configure"))
            qs = [
                {"type": "input", "name": "work", "message": center("Work minutes:"), "validate": lambda x: x.isdigit()},
                {"type": "input", "name": "break", "message": center("Short break minutes:"), "validate": lambda x: x.isdigit()},
                {"type": "input", "name": "long", "message": center("Long break minutes:"), "validate": lambda x: x.isdigit()},
                {"type": "confirm", "name": "save", "message": center("Save this session?"), "default": True}
            ]
            ans = prompt(qs, style=get_prompt_style(current_theme))
            utils.run_classic_pomodoro(current_theme, int(ans["work"]), int(ans["break"]), int(ans["long"]), ans["save"])

        elif choice.startswith("2. View progress"):
            display.random_logo(current_theme)
            if os.path.exists(progress_file):
                with open(progress_file, "r") as f:
                    data = json.load(f)
                if data:
                    for sess in data:
                        gross = utils.format_time(sess['gross_time'])
                        net = utils.format_time(sess['net_time'])
                        cfg = sess["config"]
                        print(f"\n- Started: {sess['start_time']} {display.bcyan}|{display.white} Ended: {sess['end_time']}")
                        print(f"- Gross: {display.bwhite}{gross}{display.white} {display.bcyan}|{display.white} Net: {display.bwhite}{net}{display.white} {display.bcyan}|{display.white} Cycles: {display.bwhite}{sess['cycles']}{display.white}")
                        print(f" ⚙️  Config: work={cfg['work_min']}m break={cfg['break_min']}m long={cfg['long_break_min']}m")
                        print("\n" + "-"*30)
                    ch = input(center(f"\nPress {display.iwhite}enter{display.white} to return, or {display.iwhite}c{display.white} to clear all: "))
                    if ch.lower() == 'c':
                        os.remove(progress_file)
                        print(center("Progress cleared."))
                        input(center("Press enter to return."))
                else:
                    print(center("No saved sessions."))
                    input(center("Press enter to return"))
            else:
                print(center("No saved sessions."))
                input(center("Press enter to return"))

        elif choice.startswith("3. Config"): config_menu()
        elif choice.startswith("4. Exit"):
            print(center("Until next time!"))
            sys.exit()

def main():
    try:
        global current_theme
        current_theme = read_theme()
        run_menu()
    except KeyboardInterrupt:
        print("\n\n\033[1;31mExiting... Session terminated by user (Ctrl+C).\033[0m\n")
        sys.exit(0)
    except EOFError:
        print("\n\n\033[1;31mExiting... Terminal input terminated (EOF).\033[0m\n")
        sys.exit(0)

if __name__ == "__main__":
    main()
