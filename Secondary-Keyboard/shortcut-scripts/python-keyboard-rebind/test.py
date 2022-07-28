#!/usr/bin/python3

import subprocess as sp

#output = subprocess.check_output(['grep -A 10 \"Hoksi Technology KB105\" \/proc\/bus\/input\/devices \| grep devices \| awk `{print substr($0,length,1)}`'])
commandl = "~/Programming/development/secondkbd/shortcut-scripts/python-solution/helper.sh"
#commandl = "grep -A 10 '\"Hoksi Technology KB105\"' /proc/bus/input/devices | grep devices | awk '{print substr($0,length,1)}'"
#commandl = "cat /proc/bus/input/devices | grep -v Consumer | grep -A 10 '\"Hoksi Technology KB105\"'| grep devices | awk '{print substr($0,length,1)}'"
#commandl = "cat /proc/bus/input/devices | grep -v (System|Consumer|Keyboard|Mouse) | grep -A 10 '\"Hoksi Technology KB105\"'  | grep devices | awk '{print substr($0,length,1)}'"

output = sp.getoutput(commandl)

inputpath = '/dev/input/event%s' % output

print("%s" % inputpath)
