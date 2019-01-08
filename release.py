#!/usr/bin/env python

"""
This Python script is used to package up and create the releases for aud.

This involves:
* Removing any __pycache__ and .pyc files
* Making a zip bundle out of each plugin and copying the aud library inside that bundle

This file is purposefully not called package.py because I may want to make it a rez package
at a later point in time
"""
from __future__ import print_function

import os
import logging
import shutil
logging.basicConfig()

logger = logging.getLogger('aud_release')
logger.setLevel(logging.DEBUG)

ROOT = os.path.dirname(os.path.abspath(__file__))
PLUGINS = os.path.join(ROOT, 'plugins')


def make_clean_release_dir():
    release_dir = os.path.join(ROOT, 'release')
    if os.path.exists(release_dir):
        logger.warning('Deleting release directory: %s', release_dir)
        shutil.rmtree(release_dir)

    logger.info('Making release directory: %s', release_dir)
    os.mkdir(release_dir)

    return release_dir


def make_plugin_release(path, release):
    if not os.path.exists(release):
        os.mkdir(release)

    for root, dirs, files in os.walk(path, followlinks=True):
        for d in dirs:
            if '__' in d:
                continue
            dpath = os.path.join(root, d)
            target = dpath.replace(path, release)
            if not os.path.exists(target):
                os.mkdir(target)

        for f in files:
            if '__' in root:
                continue
            if f.endswith('.pyc'):
                continue

            fpath = os.path.join(root, f)
            target = fpath.replace(path, release)

            shutil.copy(fpath, target, follow_symlinks=True)


def zip_plugin(plugin_release):
    shutil.make_archive(plugin_release, 'zip', plugin_release)


def main():
    release = make_clean_release_dir()
    for plugin in os.listdir(PLUGINS):
        path = os.path.join(PLUGINS, plugin)
        if not os.path.isdir(path):
            continue

        plugin_release = os.path.join(release, plugin)

        make_plugin_release(path, plugin_release)
        zip_plugin(plugin_release)


if __name__ == '__main__':
    main()