# What Week Is It?

What week is it? This is a simple Python script that tells you what week of the year it is.

This is the MacOS implementation of the script.

## Setup
First, clone and navigate to the repository:
```bash
git clone https://github.com/Silicon27/weekdatemac
cd weekdatemac/weekdatemac
```

Then install the dependencies:
```bash
pip3 install pyobjc
```

Move it to `~/Library/LaunchAgents/`
```bash
mv com.weeknumber.plist ~/Library/LaunchAgents/
```

Then you can add it to your Launch Agent with `launchctl` and run it:
```bash
launchctl unload ~/Library/LaunchAgents/com.weeknumber.plist && \
launchctl load ~/Library/LaunchAgents/com.weeknumber.plist
```

And that's it! You should see the week number in your menu bar.

An example would look like this: 
![Week Date Mac](/demo.png)
