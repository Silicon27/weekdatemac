from datetime import datetime
from Foundation import NSObject, NSBundle, NSTimer
from AppKit import NSApplication, NSStatusBar, NSVariableStatusItemLength, NSMenu, NSMenuItem

app = NSApplication.sharedApplication()
app.setActivationPolicy_(2)  # 2 means NSApplicationActivationPolicyProhibited, which hides the app in $

class MenuBarApp(NSObject):
    def applicationDidFinishLaunching_(self, notification):
        # Create the menu bar item
        self.status_bar_item = NSStatusBar.systemStatusBar().statusItemWithLength_(NSVariableStatusItemLength)

        # Create the dropdown menu
        self.menu = NSMenu.alloc().init()
        quit_item = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_("Quit", "terminate:", "")
        self.menu.addItem_(quit_item)
        self.status_bar_item.setMenu_(self.menu)

        # Update the week number on the menu bar
        self.update_week_number()

        # Set a timer to refresh every hour (just in case the day changes)
        self.timer = NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_(
            3600, self, "update_week_number", None, True
        )

    def update_week_number(self):
        # Get the current week number
        week_number = datetime.now().isocalendar()[1]
        self.status_bar_item.button().setTitle_(f"Week {week_number}")


if __name__ == "__main__":
    app = NSApplication.sharedApplication()
    delegate = MenuBarApp.alloc().init()
    app.setDelegate_(delegate)
    app.run()
