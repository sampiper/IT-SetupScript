#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# -*- coding: utf-8 -*-

import os
import json
import urllib
import urllib2
import subprocess
import shlex

name = ''
email = ''
assettag = ''


# Check if Xcode Command Line Tools are installed
if os.system('xcode-select -p') != 0:
  print "Installing XCode Tools"
  os.system('xcode-select --install')
  print "**************************************************************"
  print "Install the XCode Command Line Tools and run this script again"
  print "**************************************************************"
  exit()


# Sudo: Spectacle, ZSH, OSX Settings
print "\n\nWelcome to the Mac Setup Script by TAB\n"

# Basic Info
while name == '':
  name = raw_input("What's your name and surname?\n").strip()

#while email == '' or '@' not in email:
#  email = raw_input("What's your email?\n").strip()
  
while assettag ==  '' or 'TABLT' not in assettag:
  assettag = raw_input("Please enter the asset tag on the bottom of the laptop.\n").strip()


def show_notification(text):
  os.system('osascript -e \'display notification "'+ text +'" with title "Mac Setup"\' > /dev/null')
  
urllib.urlretrieve("https://raw.githubusercontent.com/sampiper/macos-create-user/master/create-user.sh", "create-user.sh")
os.system('chmod 744')
subprocess.call(shlex.split('sudo ./create-user.sh name Welcome2tab! test)



print "Hi %s!" % name
print "You'll be asked for your password at a few points in the process"
print "*************************************"
print "Setting up your Mac..."
print "*************************************"


# Set computer name info (as done via System Preferences → Sharing)
os.system('sudo scutil --set ComputerName ' + assettag + '-' + name.replace(' ', ''))
os.system('sudo scutil --set HostName ' + assettag + '-' + name.replace(' ', ''))
os.system('sudo scutil --set LocalHostName ' + assettag + '-' + name.replace(' ', '')) # Doesn't support spaces
os.system('sudo defaults write /Library/Preferences/SystemConfiguration/com.apple.smb.server NetBIOSName -string ' + assettag + '-' + name.replace(' ', ''))

show_notification("Laptop name: " + assettag + '-' + name.replace(' ', ''))

# Install Brew & Brew Cask
print "Installing Brew & Brew Cask"
os.system('touch ~/.bash_profile')
os.system('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')
os.system('brew tap caskroom/cask')
os.system('brew tap homebrew/services')
os.system('brew tap caskroom/versions')
os.system('brew tap caskroom/fonts')
os.system('brew update && brew upgrade && brew cleanup && brew cask cleanup')

#Installing Mas
print "Installing Mas"
os.system('brew install mas')

#Installing Appstore Apps
os.system('mas install 409183694')  # Keynote
os.system('mas upgrade')  # Update all appstore apps

# OSX Tweaks & Essentials
print "Installing Quicklook Helpers"
os.system('brew cask install qlcolorcode qlmarkdown quicklook-csv quicklook-json webpquicklook suspicious-package epubquicklook qlstephen qlprettypatch font-hack qlvideo')

# Installing third party apps
print "Installing Essential Apps"
os.system('brew cask install spotify slack zoomus google-backup-and-sync')

#Random OSX Settings
print "Tweaking OSX Settings"

# Check for software updates daily
os.system('defaults write com.apple.SoftwareUpdate ScheduleFrequency -int 1')
# Require password immediately after sleep or screen saver begins
os.system('defaults write com.apple.screensaver askForPassword -int 1')
os.system('defaults write com.apple.screensaver askForPasswordDelay -int 0')
# Show the ~/Library folder
os.system('chflags nohidden ~/Library')
# Prevent Time Machine from prompting to use new hard drives as backup volume
os.system('defaults write com.apple.TimeMachine DoNotOfferNewDisksForBackup -bool true')

# Make Google Chrome the default browser
os.system('open -a "Google Chrome" --args --make-default-browser')

# Clean Up
os.system('brew cleanup && brew cask cleanup')

show_notification("All done! Enjoy your new macOS Thank you for joining Solstice ^^!")






