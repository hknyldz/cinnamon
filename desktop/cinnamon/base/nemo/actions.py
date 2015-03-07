#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

Workdir="linuxmint-nemo-/*/"

def setup():
  
    shelltools.system("find -type f | xargs sed -i 's@^#!.*python2$@#!/usr/bin/python@'")
    shelltools.system("sed -i 's/^Name\(.*\)=.*/Name\1=Nemo/' data/nemo.desktop.in.in")
    shelltools.system("sed -i -e '/AC_SUBST(DISABLE_DEPRECATED_CFLAGS)/d' configure.in")
    shelltools.system("./autogen.sh")
    autotools.configure("--prefix=/usr \
			 --sysconfdir=/etc \
			 --localstatedir=/var \
			 --disable-static \
			 --libexecdir=/usr/lib/nemo \
			 --disable-update-mimedb \
			 --disable-tracker \
			 --disable-gtk-doc-html \
			 --disable-schemas-compile")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodir("/usr/share/nemo/themes/Adwaita-Nemo/gtk-3.0/apps/")

    pisitools.dodoc("README", "AUTHORS")