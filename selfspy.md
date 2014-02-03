## Setting up selfspy on OSX
Install command line tools
```
xcode-select --install
```
Clone selfspy
```
git clone git://github.com/gurgeh/selfspy
cd selfspy
```
Install
```
sudo easy_install -U pyobjc-core
sudo python setup.py install
```
Start selfspy automatically on login
```
curl https://raw.github.com/benzguo/qself/master/com.github.selfspy.plist > ~/Library/LaunchAgents/com.github.selfspy.plist
```
You may have to adjust this plist to point to your python location.
