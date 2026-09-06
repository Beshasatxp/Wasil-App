[app]
title = Wasil
package.name = wasil
package.domain = com.wasil.netoptimizer
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf
version = 1.0.0

# python3 & kivy master: kivy master fixes NDK25 OpenGL header mismatch (documented kivy issue)
requirements = python3,kivy==master

orientation = portrait
fullscreen = 0

android.permissions = INTERNET, ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
