[app]
# (str) Title of your application
title = Wasil

# (str) Package name
package.name = wasil

# (str) Package domain (needed for android packaging)
package.domain = com.wasil.netoptimizer

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (process only files with these extensions)
source.include_exts = py,png,jpg,kv,atlas,ttf

# (str) Application versioning
version = 1.0.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = hostpython3==3.11.5,python3==3.11.5,kivy,certifi,chardet,filetype,idna,requests,six,urllib3

# (str) Supported orientations (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API required.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (list) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Android logcat filters to use
android.allow_backup = True

# (bool) Accept SDK license automatically
android.accept_sdk_license = True

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = ignore, 1 = warn)
warn_on_root = 1

