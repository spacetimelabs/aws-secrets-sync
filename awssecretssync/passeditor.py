#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

PASS_CONTENT_FILE = os.path.expanduser('~/.passeditor.content')


def editor():
    target_file = sys.argv[1]
    if os.path.isfile(PASS_CONTENT_FILE):
        pass_file = open(target_file, 'w')
        pass_file.write(open(PASS_CONTENT_FILE, 'r').read())
        pass_file.close()


if __name__ == '__main__':
    editor()
