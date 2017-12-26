# EixDiffNotifier
A Notifications Script for upgrades available on Gentoo's Portage System

This script runs the eix-diff utility and looks for Upgrades(indicated in the output as [U]).
On detection of Upgrades available this script will compile a list, compare it with a previously sent list(if one exists)
and then if these are upgrades previously not notified on an email will be sent with the available upgrades.

#Requiremets:
* Python 3.4+
* Gentoo Linux installation
* The app-portage/eix toolkit installed
* A cron entry that runs eix-sync before this script executes
* SMTP availability(using /usr/bin/mail)

#Installation
1. copy the EixNotifier.py and config folder to an appropriate tools location on your linux system. 
2. copy the example.ini to default.ini setting the appropriate settings to your specific configuration. 
   * EmailAddress should be the email address to send the notice to.
   * CacheDir should be the location that the script can use to store cached upgrade lists(previous runs)
   * CacheFile should be updated with whatever you want to call the cachefile.(preserve the %(CacheDir)s/ in order to preserve the CacheDir usage
3. (optional) set a crontab to run after your eix-sync would complete in order for the notifier to parse the changes and notify you.
