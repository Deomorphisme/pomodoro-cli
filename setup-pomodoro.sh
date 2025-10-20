#!/bin/bash


# Define paths
PROJECT_DIR=$(pwd)
SCRIPT_NAME_1="pomodoro.py"
SCRIPT_NAME_2="timer.py"
LINK_NAME_1="pomodoro"
LINK_NAME_2="timer"

# 1. Make the script executable
echo "Making $SCRIPT_NAME_1 and $SCRIPT_NAME_2 executable..."
chmod u+x "$PROJECT_DIR/$SCRIPT_NAME_1" "$PROJECT_DIR/$SCRIPT_NAME_2" # modify if you want to be more permissive

# 2. Add project directory to PYTHONPATH (temporarily for this session)
echo "Adding $PROJECT_DIR to PYTHONPATH..."
export PYTHONPATH="$PROJECT_DIR:$PYTHONPATH"

# 3. Create a symlink in /usr/local/bin
echo "Creating symlink for $LINK_NAME_1 and $LINK_NAME_2 in /usr/local/bin..."
sudo ln -sf "$PROJECT_DIR/$SCRIPT_NAME_1" "/usr/local/bin/$LINK_NAME_1"
sudo ln -sf "$PROJECT_DIR/$SCRIPT_NAME_2" "/usr/local/bin/$LINK_NAME_2"

# 4. Verify the command works
echo "Testing the commands..."
if command -v "$LINK_NAME_1" &> /dev/null; then
    echo "Success! You can now run '$LINK_NAME_1' from anywhere."
else
    echo "Failed to create the command. Check paths and permissions."
fi

if command -v "$LINK_NAME_2" &> /dev/null; then
    echo "Success! You can now run '$LINK_NAME_2' from anywhere."
else
    echo "Failed to create the command. Check paths and permissions."
fi

# 5. Copy the alarm sound to /usr/share/sounds/freedesktop/stereo/
sudo cp "songs/timer-terminer.mp3" "/usr/share/sounds/freedesktop/stereo/timer-terminer.mp3"
echo "Successfully added timer-terminer.mp3 to /usr/share/sounds/freedesktop/stereo"

# 5. Instructions for permanent PYTHONPATH (optional)
echo ""
echo "To make PYTHONPATH permanent, add this line to your ~/.bashrc or ~/.zshrc:"
echo "export PYTHONPATH=\"$PROJECT_DIR:\$PYTHONPATH\""
echo "Then run: source ~/.bashrc (or source ~/.zshrc)"
