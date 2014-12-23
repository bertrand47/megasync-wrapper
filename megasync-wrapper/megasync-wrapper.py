#!/usr/bin/env python
import subprocess
import os
import shutil
import stat
import re

mega_bin = '/usr/bin/megasync'

if __name__ == '__main__':

    pid = subprocess.Popen([mega_bin]).pid
    substr = "sni-qt_megasync_{0}".format(pid)

    finished = False
    folder_name = ""

    while not finished:
        for name in os.listdir("/tmp/"):
            if name.startswith(substr):
                folder_name = name
                finished = True

    icons_folder = "/tmp/" + folder_name + "/icons/hicolor/22x22/apps/"
    os.makedirs(icons_folder)

    subst_icons_folder = os.path.dirname(os.path.realpath(__file__)) + '/icons/'
    
    mega_icon = icons_folder + 'megasync_{0}_5e6bbab03e062640f0a3c6c540f119a7.png'.format(pid)
    shutil.copy(subst_icons_folder + 'megasync.png', mega_icon)
    os.chmod(mega_icon, stat.S_IRUSR)
    mega_icon1 = icons_folder + 'megasync_{0}_a8fb04239cb3d37ca409bd8a55eaa7d8.png'.format(pid)
    shutil.copy(subst_icons_folder + 'megasync1.png', mega_icon1)
    os.chmod(mega_icon1, stat.S_IRUSR)
