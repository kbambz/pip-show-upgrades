#!/usr/bin/env python

# Originally based on:
# http://code.activestate.com/recipes/577708-check-for-package-updates-on-pypi-works-best-in-pi/

import xmlrpclib
import pip


PYPI_URL = 'https://pypi.python.org/pypi'


def get_upgrade_cmd(package, version):
    return 'pip install --upgrade {package}=={version}'.format(package=package, version=version)


def main():
    upgrade_cmds = []
    pypi = xmlrpclib.ServerProxy(PYPI_URL)
    for dist in pip.get_installed_distributions():
        name = dist.project_name
        available = pypi.package_releases(name, True)
        if not available:
            name = name.capitalize()
            available = pypi.package_releases(name)
        if not available and '-' in name:
            name = name.replace('-', '_')
            available = pypi.package_releases(name)
        if not available and '_' in name:
            name = name.lower()
            available = pypi.package_releases(name)
        if not available:
            msg = 'no releases at pypi'
        elif available[0] != dist.version:
            dists = [available[0]]
            upgrade_cmds.append(get_upgrade_cmd(name, available[0]))
            i = 1
            while (('b' in available[i - 1] or 'a' in available[i - 1]) and
                   i < len(available) and available[i] != dist.version):
                # might be a beta; print the one below it, too
                dists.append(available[i])
                upgrade_cmds.append(get_upgrade_cmd(name, available[i]))
                i += 1
            msg = '{} available'.format(', '.join(dists))
        else:
            msg = 'up to date'
        pkg_info = '{dist.project_name} {dist.version}'.format(dist=dist)
        print('{pkg_info:40} {msg}'.format(pkg_info=pkg_info, msg=msg))

    if upgrade_cmds:
        print('')
        for cmd in upgrade_cmds:
            print(cmd)


if __name__ == '__main__':
    main()
