# 🍅 Cidoro

Minimalist CLI Pomodoro timer built for focus, discipline and productivity.

![Cidoro Logo](assets/logo.png)


---

## 📌 What is it?

**Cidoro** is a Pomodoro timer running entirely in your terminal.  
Designed for developers, students and anyone who wants to track deep work, with customizable themes, sound alarm and progress logging.

---

## ⚙️ Technologies

- **Python 3** (≥3.7)
- **InquirerPy** – beautiful CLI menus
- **Pystyle** – colorful terminal output
- **FFmpeg (ffplay)** – sound alarm playback
- **JSON** – session logs

---

## 🧪 Tested on

- Ubuntu 22.04 LTS
- Debian-based distributions

*(should work on any system with Python 3 and ffplay)*

---

## 🚀 Installation

Clone this repository:

```bash
git clone https://github.com/yourusername/cidoro.git
cd cidoro
```

Make the installer executable and run:

```bash
chmod +x install.sh
./install.sh
```

This will:

- Create a virtual environment (```cidoro_env```)
- Install dependencies
- Install Cidoro in editable mode (```pip install -e .```)
- Check and install ffplay if missing

---

## 🍅 Usage

Activate the environment:

```bash
source cidoro_env/bin/activate
```

Run:

```bash
cidoro
```

From there, explore the menu to:

- Start pomodoro sessions
- View saved progress
- Change themes and configs

---

## 📁 Project structure

```
cidoro/
 ├── cli.py           # CLI menus
 ├── utils.py         # Core pomodoro logic
 ├── display.py       # Visuals, banners, colors
 ├── alarm.mp3        # Sound alarm
 ├── themes.txt       # Saved theme (auto-generated)
 ├── progress.json    # Saved sessions (auto-generated)
assets/
 ├── logo.png         # Screenshot
pyproject.toml        # Build & install config
install.sh            # Installer script
README.md
LICENSE
```

---

## 📄 License

This project is licensed under the MIT License.  
Feel free to use, modify, and distribute.

---

## 👤 Author & Contact

Instagram: pedrodevoted  
Discord: thedevoted

---

