#!/usr/bin/env python3
# Copyright 2009-2017 BHG HTTP://bw.org/

import platform

print('This is python version %s' % platform.python_version())          # python v2, deprecated!

print('This is python version {}'.format(platform.python_version()))    # python v3
print(f'This is python version {platform.python_version()}')            # python v3.6 and up
