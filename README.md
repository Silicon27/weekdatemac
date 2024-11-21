# What Week Is It?

What week is it? This is a simple Python script that tells you what week of the year it is.

This is the MacOS implementation of the script.

## Setup
First, clone and navigate to the repository:
```bash
git clone https://github.com/Silicon27/weekdatemac
cd weekdatemac
```

Make it executable:
```bash
chmod +x run_week_menu_bar.sh
```

Move it to `~/Library/LaunchAgents/`
```bash
mv com.weekmenubar.plist ~/Library/LaunchAgents/
```

Then you can add it to your Launch Agent with `launchctl` and run it:
```bash
launchctl load ~/Library/LaunchAgents/com.weekmenubar.plist
launchctl list | grep com.weekmenubar
```

