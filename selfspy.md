## Setting up selfspy on OSX

If you don't have xcode or command line tools installed, install the command line tools.

```
xcode-select --install
```

Clone the repo

```
git clone git://github.com/gurgeh/selfspy
cd selfspy
```

Install selfspy

```
sudo easy_install -U pyobjc-core
sudo python setup.py install
```

Start selfspy automatically on login.

```
curl https://raw.github.com/benzguo/qself/master/com.github.selfspy.plist > ~/Library/LaunchAgents/com.github.selfspy.plist
```

Try running `/usr/bin/python` and `/usr/local/bin/selfspy`. Edit the selfspy plist in `~/Library/LaunchAgents` if your python or selfspy are located elsewhere.

Log out and log back in. Go to System Preferences > Security & Privacy > Privacy > Accessibility. You should see python in the list of apps – give it accessibility access. You'll have to log out and log in again for selfspy to start tracking keypresses.

Run `selfstats --pactive`, type some stuff, and run `selfstats --pactive` again. If everything is gravy, the keystroke count will have increased. Bravo! You're on your way to quantifying yourself.
