#! /usr/bin/env python

# Install the configuration files, creating a symbolic link to them from our
# home directory. A dotfile is any file in the same directory as this script
# and whose filename ends with 'rc'. A period is affixed to the filenames so
# that they effectively become dotfiles. For example, 'pythonrc' would be
# linked from ~/.pythonrc.

# Inspired by https://github.com/rmm5t/dotfiles/blob/master/install.rb

from __future__ import print_function

import glob
import os
import os.path

dotfiles_dir = os.path.abspath(os.path.dirname(__file__))
home_dir = os.path.expanduser('~')

os.chdir(dotfiles_dir)
for rcfile in glob.iglob('*rc'):
    source = os.path.relpath(rcfile, home_dir)
    link_name = os.path.expanduser('~/.%s' % rcfile)

    if os.path.exists(link_name):
        print("File already exists: %s" % os.path.basename(link_name))
        options = "[s]kip, [o]verwite ? "
        response = raw_input(options).lower()

        if response == 'o':
            os.unlink(link_name)
        else:
            continue

    os.symlink(source, link_name)
    print("`%s' -> `%s'" % (link_name, source))

