#!/usr/bin/env bash

echo -e "\e[1;32m
    █████████   ███      █████                            
  ███░░░░░███ ░░░      ░░███                             
 ███     ░░░  ████   ███████   ██████  ████████   ██████ 
░███         ░░███  ███░░███  ███░░███░░███░░███ ███░░███
░███          ░███ ░███ ░███ ░███ ░███ ░███ ░░░ ░███ ░███
░░███     ███ ░███ ░███ ░███ ░███ ░███ ░███     ░███ ░███
 ░░█████████  █████░░████████░░██████  █████    ░░██████ 
  ░░░░░░░░░  ░░░░░  ░░░░░░░░  ░░░░░░  ░░░░░      ░░░░░░  
\e[0m"

echo -e "\e[1;36mWelcome to Cidoro installation script! 🍅\e[0m"

if ! command -v python3 &> /dev/null; then
    echo -e "\e[1;31mPython3 not found. Installing...\e[0m"
    sudo apt update && sudo apt install python3 -y
fi


if ! command -v ffplay &> /dev/null; then
    echo -e "\e[1;33m⚠️ 'ffplay' not found. Required for alarm playback.\e[0m"
    echo -e "\e[1;33mInstalling via ffmpeg package...\e[0m"
    sudo apt update && sudo apt install ffmpeg -y
fi


echo -e "\e[1;33mCreating virtual environment: cidoro_env...\e[0m"
python3 -m venv cidoro_env


source cidoro_env/bin/activate


pip install --upgrade pip


echo -e "\e[1;33mInstalling Cidoro and dependencies (editable mode)...\e[0m"
pip install -e .


pip install pystyle InquirerPy terminaltexteffects

deactivate

echo -e "\n\e[1;32m✅ Installation complete!\e[0m"
echo -e "To start, activate env:\n  \e[1;36msource cidoro_env/bin/activate\e[0m"
echo -e "Then run:\n  \e[1;36mcidoro\e[0m"
echo -e "\n\e[1;35mHappy productivity! 🍅\e[0m"
