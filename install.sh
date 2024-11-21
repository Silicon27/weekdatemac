#!/bin/bash

# Ensure the correct directory
cd "$(dirname "$0")" || exit 1

# Make the script executable (if not already done by pip)
chmod +x run_week_menu_bar.sh

# Move the plist to LaunchAgents folder
mv com.weekmenubar.plist ~/Library/LaunchAgents/

# Load the plist with launchctl
launchctl unload ~/Library/LaunchAgents/com.weekmenubar.plist && \
launchctl load ~/Library/LaunchAgents/com.weekmenubar.plist

echo "Installation complete! The week number should now appear in your menu bar."
