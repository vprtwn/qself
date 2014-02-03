## Setting up selfspy on OSX
Install command line tools
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
Start selfspy automatically on login. I prefer configuring selfspy to not track my keystrokes when it starts.
```
curl https://raw.github.com/benzguo/qself/master/com.github.selfspy.plist > ~/Library/LaunchAgents/com.github.selfspy.plist
```
