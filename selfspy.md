## Getting started with selfspy on OSX

If you don't have xcode or command line tools installed, install them.

```
xcode-select --install
```

Clone the selfspy repo.

```
git clone git://github.com/gurgeh/selfspy
cd selfspy
```

Install selfspy.

```
sudo easy_install -U pyobjc-core
sudo python setup.py install
```

Run selfspy. You'll have to enter a password to encrypt your keypresses. When prompted, save your password in your keychain so selfspy can start without authenticating on login.

Start selfspy automatically on login.

```
curl https://raw.github.com/benzguo/qself/master/com.github.selfspy.plist > ~/Library/LaunchAgents/com.github.selfspy.plist
```

If your python and selfspy binaries are located elsewhere, you should edit `~/Library/LaunchAgents/com.github.selfspy.plist`. If you're not sure, try running `/usr/bin/python` and `/usr/local/bin/selfspy`.

To start the daemon, log out and log back in. Go to System Preferences > Security & Privacy > Privacy > Accessibility. You should see python – give it accessibility access. You'll have to log out and log in again for selfspy to start tracking keypresses.

Run `selfstats --pactive`, type some stuff, and run `selfstats --pactive` again. If everything is gravy, you'll see your keystroke count increase.

## Some interesting commands

"What sites have I visited today, and for how long?"

```
selfstats --process 'Google Chrome' --clock 00:00 --tactive
```

This will list all window titles from processes matching 'Google Chrome', starting at 12am today and sorted by time active.

"What does my email usage look like today?"

```
selfstats --title 'Venmo Mail' --process 'Google Chrome' --clock 00:00 --tactive
```

This is the same command above with an additional `--title` argument, which we can use to filter by window title.
