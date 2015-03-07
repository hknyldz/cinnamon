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
    shelltools.system("sed -i -e 's:import PAM:import pam:' files/usr/lib/cinnamon-settings/modules/cs_user.py")
    shelltools.system("sed -i 's:/usr/bin/python :/usr/bin/python :' files/usr/bin/cinnamon-menu-editor")
    #shelltools.system("sed -i 's/RequiredComponents=\(.*\)$/RequiredComponents=\1polkit-gnome-authentication-agent-1;/' files/usr/share/cinnamon-session/sessions/cinnamon*.sessio")
    shelltools.system("sed -i 's:import PAM:import pam:' files/usr/lib/cinnamon-settings/modules/cs_user.py")
    shelltools.system("find -type f | xargs sed -i 's@^#!.*python2$@#!/usr/bin/python@'")
    shelltools.system("sed -i 's:import PAM:import pam:' files/usr/lib/cinnamon-settings/modules/cs_user.py")
    shelltools.system("sed -i -e 's|/usr/bin/cinnamon-control-center|/usr/lib/cinnamon-control-center-1/panels|' files/usr/bin/cinnamon-settings")
    #shelltools.system("sed -i -e 's/gksu/pkexec/' files/usr/bin/cinnamon-settings-users")
    shelltools.system("./autogen.sh")
    autotools.autoreconf()
    autotools.configure("--prefix=/usr \
			 --sysconfdir=/etc \
			 --libexecdir=/usr/lib/cinnamon \
			 --localstatedir=/var \
			 --disable-static \
			 --disable-schemas-compile \
		         --disable-schemas-install \
		         --enable-compile-warnings=yes ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #pisitools.insinto("/usr/lib/girepository-1.0", "usr/lib/cinnamon/*.typelib")
    shelltools.makedirs("/usr/share/locale/")

    pisitools.dodoc("README", "AUTHORS")