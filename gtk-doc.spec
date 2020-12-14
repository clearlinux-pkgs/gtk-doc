#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gtk-doc
Version  : 1.33.1
Release  : 43
URL      : https://download.gnome.org/sources/gtk-doc/1.33/gtk-doc-1.33.1.tar.xz
Source0  : https://download.gnome.org/sources/gtk-doc/1.33/gtk-doc-1.33.1.tar.xz
Summary  : API documentation generator
Group    : Development/Tools
License  : GFDL-1.1 GPL-2.0
Requires: gtk-doc-bin = %{version}-%{release}
Requires: gtk-doc-data = %{version}-%{release}
Requires: gtk-doc-license = %{version}-%{release}
Requires: Pygments
Requires: libxslt
Requires: six
Requires: source-highlight
BuildRequires : Pygments
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : docbook-utils
BuildRequires : docbook-xml
BuildRequires : libxml2-dev
BuildRequires : libxml2-python
BuildRequires : libxslt
BuildRequires : libxslt-bin
BuildRequires : openjade-dev
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : six
BuildRequires : source-highlight
Patch1: noversion.patch

%description
GTK+ DocBook Documentation Generator
====================================
GTK-Doc is used to document C code. It is typically used to document the public
API of libraries, such as the GTK+ and GNOME libraries, but it can also be
used to document application code.

%package bin
Summary: bin components for the gtk-doc package.
Group: Binaries
Requires: gtk-doc-data = %{version}-%{release}
Requires: gtk-doc-license = %{version}-%{release}

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
Requires: gtk-doc-bin = %{version}-%{release}
Requires: gtk-doc-data = %{version}-%{release}
Provides: gtk-doc-devel = %{version}-%{release}
Requires: gtk-doc = %{version}-%{release}

%description dev
dev components for the gtk-doc package.


%package doc
Summary: doc components for the gtk-doc package.
Group: Documentation

%description doc
doc components for the gtk-doc package.


%package license
Summary: license components for the gtk-doc package.
Group: Default

%description license
license components for the gtk-doc package.


%prep
%setup -q -n gtk-doc-1.33.1
cd %{_builddir}/gtk-doc-1.33.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1606164429
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static --with-xml-catalog=/usr/share/defaults/xml/catalog PYTHON=/usr/bin/python3
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1606164429
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gtk-doc
cp %{_builddir}/gtk-doc-1.33.1/COPYING %{buildroot}/usr/share/package-licenses/gtk-doc/dfac199a7539a404407098a2541b9482279f690d
cp %{_builddir}/gtk-doc-1.33.1/COPYING-DOCS %{buildroot}/usr/share/package-licenses/gtk-doc/5e7b36dfb18c7b8002bb9c41f87b65d280abd2ae
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gtkdoc-check
/usr/bin/gtkdoc-depscan
/usr/bin/gtkdoc-fixxref
/usr/bin/gtkdoc-mkdb
/usr/bin/gtkdoc-mkhtml
/usr/bin/gtkdoc-mkhtml2
/usr/bin/gtkdoc-mkman
/usr/bin/gtkdoc-mkpdf
/usr/bin/gtkdoc-rebase
/usr/bin/gtkdoc-scan
/usr/bin/gtkdoc-scangobj
/usr/bin/gtkdocize

%files data
%defattr(-,root,root,-)
/usr/share/cmake/*
/usr/share/gtk-doc/data/devhelp2.xsd
/usr/share/gtk-doc/data/devhelp2.xsl
/usr/share/gtk-doc/data/gtk-doc.flat.make
/usr/share/gtk-doc/data/gtk-doc.make
/usr/share/gtk-doc/data/gtk-doc.no-xslt-flat.make
/usr/share/gtk-doc/data/gtk-doc.no-xslt.make
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
/usr/share/gtk-doc/python/gtkdoc/check.py
/usr/share/gtk-doc/python/gtkdoc/common.py
/usr/share/gtk-doc/python/gtkdoc/config.py
/usr/share/gtk-doc/python/gtkdoc/config_data.py
/usr/share/gtk-doc/python/gtkdoc/fixxref.py
/usr/share/gtk-doc/python/gtkdoc/highlight.py
/usr/share/gtk-doc/python/gtkdoc/md_to_db.py
/usr/share/gtk-doc/python/gtkdoc/mkdb.py
/usr/share/gtk-doc/python/gtkdoc/mkhtml.py
/usr/share/gtk-doc/python/gtkdoc/mkhtml2.py
/usr/share/gtk-doc/python/gtkdoc/mkman.py
/usr/share/gtk-doc/python/gtkdoc/mkpdf.py
/usr/share/gtk-doc/python/gtkdoc/rebase.py
/usr/share/gtk-doc/python/gtkdoc/scan.py
/usr/share/gtk-doc/python/gtkdoc/scangobj.py

%files dev
%defattr(-,root,root,-)
/usr/lib64/pkgconfig/gtk-doc.pc
/usr/share/aclocal/*.m4

%files doc
%defattr(0644,root,root,0755)
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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gtk-doc/5e7b36dfb18c7b8002bb9c41f87b65d280abd2ae
/usr/share/package-licenses/gtk-doc/dfac199a7539a404407098a2541b9482279f690d
