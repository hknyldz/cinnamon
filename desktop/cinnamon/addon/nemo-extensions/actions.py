#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("find -type f | xargs sed -i 's@^#!.*python2$@#!usr/bin/python@'")
    shelltools.system("sed -i '/AM_GNU_GETTEXT/d' nemo-preview/configure.ac")
    shelltools.cd("nemo-fileroller")
    autotools.autoreconf("-fi")
    autotools.configure("--prefix=/usr --sysconfdir=/etc --localstatedir=/var --libexecdir=/usr/lib/%s \
			 --disable-static")
    shelltools.cd("../nemo-seahorse")
    autotools.autoreconf("-fi")
    autotools.configure("--prefix=/usr --sysconfdir=/etc --localstatedir=/var --libexecdir=/usr/lib/%s \
			 --disable-static")
    shelltools.cd("../nemo-share")
    autotools.autoreconf("-fi")
    autotools.configure("--prefix=/usr --sysconfdir=/etc --localstatedir=/var --libexecdir=/usr/lib/%s \
			 --disable-static")
    shelltools.cd("../nemo-preview")
    autotools.autoreconf("-fi")
    autotools.configure("--prefix=/usr --sysconfdir=/etc --localstatedir=/var --libexecdir=/usr/lib/%s \
			 --disable-static")
    shelltools.cd("../nemo-python")
    autotools.autoreconf("-fi")
    autotools.configure("--prefix=/usr --sysconfdir=/etc --localstatedir=/var --libexecdir=/usr/lib/%s \
			 --disable-static")
    
def build():
    shelltools.cd("nemo-fileroller")
    autotools.make()
    shelltools.cd("../nemo-seahorse")
    autotools.make()
    shelltools.cd("../nemo-share")
    autotools.make()
    shelltools.cd("../nemo-preview")
    autotools.make()
    shelltools.cd("../nemo-python")
    autotools.make()

def install():
    shelltools.cd("nemo-fileroller")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../nemo-seahorse")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../nemo-share")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../nemo-preview")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../nemo-python")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.dodoc("COPYING", "AUTHORS")