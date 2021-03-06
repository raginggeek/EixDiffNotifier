#!/usr/bin/env python
import subprocess
import re
import os.path
import datetime
from configparser import ConfigParser,ExtendedInterpolation
from UtilFunctions import get_script_path

basepath = get_script_path()
if __name__ == "__main__":
    configFile = basepath + '/config/default.ini'
    config = ConfigParser(interpolation=ExtendedInterpolation())
    config.read(configFile)
    targetAddress = None
    upgradeCache = None
    if 'Notifier' in config:
        targetAddress = config['Notifier']['EmailAddress']
        upgradeCache = config['Notifier']['CacheFile']
    currentDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    subjectLine = "Gentoo Upgrade List for " + currentDate
    oldlist = ""

    eixdiff = subprocess.run(['eix-diff'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    upgradePattern = re.compile('^\[U\]')
    upgrades = []
    for diffline in eixdiff.splitlines():
        if upgradePattern.match(diffline):
            upgrades.append(diffline)
    if len(upgrades) > 0:
        upgradeList = upgrades[0]
        upgradeList += """
{}
        """.format("\n".join(upgrades[1:]))
        if os.path.isfile(upgradeCache):
            with open(upgradeCache) as readList:
                oldlist = readList.read()
        if oldlist != upgradeList:
            fh = open(upgradeCache, "w")
            fh.write(upgradeList)
            fh.close()
            cmd = "/usr/bin/mail -s \"" + subjectLine + "\" "
            cmd += targetAddress + " < " + upgradeCache
            subprocess.run(cmd, shell=True)
