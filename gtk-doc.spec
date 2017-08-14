#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gtk-doc
Version  : 1.26
Release  : 15
URL      : https://download.gnome.org/sources/gtk-doc/1.26/gtk-doc-1.26.tar.xz
Source0  : https://download.gnome.org/sources/gtk-doc/1.26/gtk-doc-1.26.tar.xz
Summary  : API documentation generator
Group    : Development/Tools
License  : GFDL-1.1 GPL-2.0
Requires: gtk-doc-bin
Requires: gtk-doc-data
Requires: gtk-doc-doc
Requires: six
BuildRequires : bc
BuildRequires : docbook-utils
BuildRequires : docbook-xml
BuildRequires : itstool
BuildRequires : libxml2-dev
BuildRequires : libxml2-python
BuildRequires : libxslt-bin
BuildRequires : openjade-dev
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : six
BuildRequires : six-python
BuildRequires : vim

%description
GTK+ DocBook Documentation Generator
====================================
GTK-Doc is used to document C code. It is typically used to document the public
API of libraries, such as the GTK+ and GNOME libraries, but it can also be
used to document application code.

%package bin
Summary: bin components for the gtk-doc package.
Group: Binaries
Requires: gtk-doc-data

%description bin
bin components for the gtk-doc package.


%package data
Summary: data components for the gtk-doc package.
Group: Data

%description data
data components for the gtk-doc package.


%package dev
Summary: dev components for the gtk-doc package.
Group: Development
Requires: gtk-doc-bin
Requires: gtk-doc-data
Provides: gtk-doc-devel

%description dev
dev components for the gtk-doc package.


%package doc
Summary: doc components for the gtk-doc package.
Group: Documentation

%description doc
doc components for the gtk-doc package.


%prep
%setup -q -n gtk-doc-1.26

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1502729541
%configure --disable-static --with-xml-catalog=/usr/share/defaults/xml/catalog
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1502729541
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/cmake/GtkDoc/GtkDocConfig.cmake
/usr/lib64/cmake/GtkDoc/GtkDocConfigVersion.cmake
/usr/lib64/cmake/GtkDoc/GtkDocScanGObjWrapper.cmake

%files bin
%defattr(-,root,root,-)
/usr/bin/gtkdoc-check
/usr/bin/gtkdoc-depscan
/usr/bin/gtkdoc-fixxref
/usr/bin/gtkdoc-mkdb
/usr/bin/gtkdoc-mkhtml
/usr/bin/gtkdoc-mkman
/usr/bin/gtkdoc-mkpdf
/usr/bin/gtkdoc-rebase
/usr/bin/gtkdoc-scan
/usr/bin/gtkdoc-scangobj
/usr/bin/gtkdocize

%files data
%defattr(-,root,root,-)
/usr/share/gtk-doc/data/devhelp2.xsd
/usr/share/gtk-doc/data/devhelp2.xsl
/usr/share/gtk-doc/data/gtk-doc.flat.make
/usr/share/gtk-doc/data/gtk-doc.make
/usr/share/gtk-doc/data/gtk-doc.xsl
/usr/share/gtk-doc/data/home.png
/usr/share/gtk-doc/data/left-insensitive.png
/usr/share/gtk-doc/data/left.png
/usr/share/gtk-doc/data/right-insensitive.png
/usr/share/gtk-doc/data/right.png
/usr/share/gtk-doc/data/style.css
/usr/share/gtk-doc/data/up-insensitive.png
/usr/share/gtk-doc/data/up.png
/usr/share/gtk-doc/data/version-greater-or-equal.xsl
/usr/share/gtk-doc/python/gtkdoc/__init__.py
/usr/share/gtk-doc/python/gtkdoc/__init__.pyc
/usr/share/gtk-doc/python/gtkdoc/__init__.pyo
/usr/share/gtk-doc/python/gtkdoc/check.py
/usr/share/gtk-doc/python/gtkdoc/check.pyc
/usr/share/gtk-doc/python/gtkdoc/check.pyo
/usr/share/gtk-doc/python/gtkdoc/common.py
/usr/share/gtk-doc/python/gtkdoc/common.pyc
/usr/share/gtk-doc/python/gtkdoc/common.pyo
/usr/share/gtk-doc/python/gtkdoc/config.py
/usr/share/gtk-doc/python/gtkdoc/config.pyc
/usr/share/gtk-doc/python/gtkdoc/config.pyo
/usr/share/gtk-doc/python/gtkdoc/fixxref.py
/usr/share/gtk-doc/python/gtkdoc/fixxref.pyc
/usr/share/gtk-doc/python/gtkdoc/fixxref.pyo
/usr/share/gtk-doc/python/gtkdoc/md_to_db.py
/usr/share/gtk-doc/python/gtkdoc/md_to_db.pyc
/usr/share/gtk-doc/python/gtkdoc/md_to_db.pyo
/usr/share/gtk-doc/python/gtkdoc/mkdb.py
/usr/share/gtk-doc/python/gtkdoc/mkdb.pyc
/usr/share/gtk-doc/python/gtkdoc/mkdb.pyo
/usr/share/gtk-doc/python/gtkdoc/mkhtml.py
/usr/share/gtk-doc/python/gtkdoc/mkhtml.pyc
/usr/share/gtk-doc/python/gtkdoc/mkhtml.pyo
/usr/share/gtk-doc/python/gtkdoc/mkman.py
/usr/share/gtk-doc/python/gtkdoc/mkman.pyc
/usr/share/gtk-doc/python/gtkdoc/mkman.pyo
/usr/share/gtk-doc/python/gtkdoc/mkpdf.py
/usr/share/gtk-doc/python/gtkdoc/mkpdf.pyc
/usr/share/gtk-doc/python/gtkdoc/mkpdf.pyo
/usr/share/gtk-doc/python/gtkdoc/rebase.py
/usr/share/gtk-doc/python/gtkdoc/rebase.pyc
/usr/share/gtk-doc/python/gtkdoc/rebase.pyo
/usr/share/gtk-doc/python/gtkdoc/scan.py
/usr/share/gtk-doc/python/gtkdoc/scan.pyc
/usr/share/gtk-doc/python/gtkdoc/scan.pyo
/usr/share/gtk-doc/python/gtkdoc/scangobj.py
/usr/share/gtk-doc/python/gtkdoc/scangobj.pyc
/usr/share/gtk-doc/python/gtkdoc/scangobj.pyo

%files dev
%defattr(-,root,root,-)
/usr/lib64/pkgconfig/gtk-doc.pc
/usr/share/aclocal/*.m4

%files doc
%defattr(-,root,root,-)
/usr/share/help/C/gtk-doc-manual/fdl-appendix.xml
/usr/share/help/C/gtk-doc-manual/index.docbook
/usr/share/help/bn_IN/gtk-doc-manual/fdl-appendix.xml
/usr/share/help/bn_IN/gtk-doc-manual/index.docbook
/usr/share/help/cs/gtk-doc-manual/fdl-appendix.xml
/usr/share/help/cs/gtk-doc-manual/index.docbook
/usr/share/help/de/gtk-doc-manual/fdl-appendix.xml
/usr/share/help/de/gtk-doc-manual/index.docbook
/usr/share/help/el/gtk-doc-manual/fdl-appendix.xml
/usr/share/help/el/gtk-doc-manual/index.docbook
/usr/share/help/en_GB/gtk-doc-manual/fdl-appendix.xml
/usr/share/help/en_GB/gtk-doc-manual/index.docbook
/usr/share/help/es/gtk-doc-manual/fdl-appendix.xml
/usr/share/help/es/gtk-doc-manual/index.docbook
/usr/share/help/fr/gtk-doc-manual/fdl-appendix.xml
/usr/share/help/fr/gtk-doc-manual/index.docbook
/usr/share/help/gl/gtk-doc-manual/fdl-appendix.xml
/usr/share/help/gl/gtk-doc-manual/index.docbook
/usr/share/help/gu/gtk-doc-manual/fdl-appendix.xml
/usr/share/help/gu/gtk-doc-manual/index.docbook
/usr/share/help/pt_BR/gtk-doc-manual/fdl-appendix.xml
/usr/share/help/pt_BR/gtk-doc-manual/index.docbook
/usr/share/help/sl/gtk-doc-manual/fdl-appendix.xml
/usr/share/help/sl/gtk-doc-manual/index.docbook
/usr/share/help/sv/gtk-doc-manual/fdl-appendix.xml
/usr/share/help/sv/gtk-doc-manual/index.docbook
/usr/share/help/ta/gtk-doc-manual/fdl-appendix.xml
/usr/share/help/ta/gtk-doc-manual/index.docbook
/usr/share/help/te/gtk-doc-manual/fdl-appendix.xml
/usr/share/help/te/gtk-doc-manual/index.docbook
/usr/share/help/zh_CN/gtk-doc-manual/fdl-appendix.xml
/usr/share/help/zh_CN/gtk-doc-manual/index.docbook
