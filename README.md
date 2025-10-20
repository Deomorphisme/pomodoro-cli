### **📌 Pomodoro CLI**
**A command-line tool to manage your work sessions using the Pomodoro Technique.**

#### **✨ Features**
- **Customizable Timer**: Set focus and rest durations to fit your workflow.
- **Visual & Audio Notifications**: Clear alerts with terminal colors and sound cues.
- **Graceful Interruption Handling**: Clean exit on `Ctrl+C` (no traceback).
- **Minimalist Interface**: Real-time terminal display with color-coded countdowns (red for the last 10 seconds).
- **Flexible Arguments**: Configure cycles, focus, and rest times via CLI flags (`-c`, `-f`, `-r`).

#### **🛠 Built With**
- **Python**: Lightweight, modular scripts (`pomodoro.py`, `timer.py`).
- **Pygame**: For audio notifications.
- **ANSI Codes**: Terminal formatting and colors.

#### **🚀 Installation**
1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/pomodoro-cli.git
   ```
2. Make the script executable:
   ```bash
   chmod +x pomodoro-cli/pomodoro.py
   ```
3. Create a symlink for global use:
   ```bash
   sudo ln -s /path/to/pomodoro-cli/pomodoro.py /usr/local/bin/pomodoro
   ```
4. Start a session:
   ```bash
   pomodoro -c 4 -f 25 -r 5  # 4 cycles of 25min focus / 5min rest
   ```

#### **📂 Project Structure**
```
pomodoro-cli/
├── pomodoro.py    # Core logic
├── timer.py       # Countdown and sound management
└── songs/         # Audio files for alerts
```

#### **🎯 Why This Project?**
- **Boost Productivity**: Apply the Pomodoro Technique to stay focused.
- **Simplicity**: No GUI—just your terminal.
- **Customization**: Adjust durations to match your workflow.

#### **📋 Requirements**
- Python 3.x
- Pygame (`pip install pygame`)
- ANSI-compatible terminal (most modern terminals).

#### **📜 License**
[MIT](LICENSE) – Free to use, modify, and share!

#### **🤝 Contributing**
Pull requests are welcome! For bugs or suggestions, open an [issue](https://github.com/your-username/pomodoro-cli/issues).

---
**⭐ Star the repo** if you find it useful, and feel free to share feedback!