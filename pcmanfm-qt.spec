#
# Conditional build:
#
%define		qtver		5.3.1

Summary:	pcmanfm-qt
Name:		pcmanfm-qt
Version:	0.8.0
Release:	0.2
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	5d86e2ec63463e615c21b812397785ae
URL:		http://www.lxqt.org/
BuildRequires:	cmake >= 2.8.11
BuildRequires:	glib2-devel
BuildRequires:	libfm-devel >= 1.2.0
BuildRequires:	liblxqt-devel >= 0.8.0
BuildRequires:	libqtxdg-devel >= 1.0.0
BuildRequires:	menu-cache-devel >= 0.4.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz-devel
Requires:	lxqt-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pcmanfm-qt

%package devel
Summary:	pcmanfm-qt - header files and development documentation
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do pcmanfm-qt
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core-devel >= %{qtver}
Requires:	Qt5Gui-devel >= %{qtver}
Requires:	Qt5Xml-devel >= %{qtver}

%description devel
This package contains header files and development documentation for
pcmanfm-qt.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe i dokumentację potrzebną przy
pisaniu własnych programów wykorzystujących pcmanfm-qt.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DUSE_QT5=ON \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

cd $RPM_BUILD_ROOT%{_libdir}
ln -sf libfm-qt.so.0.0.0 libfm-qt.so.0
cd -

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pcmanfm-qt
%ghost %{_libdir}/libfm-qt5.so.1
%ghost %{_libdir}/libfm-qt.so.0
%attr(755,root,root) %{_libdir}/libfm-qt5.so.*.*.*
%{_desktopdir}/pcmanfm-qt-desktop-pref.desktop
%{_desktopdir}/pcmanfm-qt.desktop
%{_datadir}/man/man1/pcmanfm-qt.1.gz
%dir %{_datadir}/libfm-qt
%dir %{_datadir}/libfm-qt/translations
%{_datadir}/libfm-qt/translations/libfm-qt_template.qm
%dir %{_datadir}/pcmanfm-qt
%dir %{_datadir}/pcmanfm-qt/translations
%{_datadir}/pcmanfm-qt/translations/pcmanfm-qt_template.qm
%lang(pt) %{_datadir}/libfm-qt/translations/libfm-qt_pt.qm
%lang(zh_TW) %{_datadir}/libfm-qt/translations/libfm-qt_zh_TW.qm
%lang(cs_CZ) %{_datadir}/libfm-qt/translations/libfm-qt_cs_CZ.qm
#%lang(lt_LT) %{_datadir}/libfm-qt/translations/libfm-qt_lt_LT.qm
%lang(pt) %{_datadir}/pcmanfm-qt/translations/pcmanfm-qt_pt.qm
%lang(cs_CZ) %{_datadir}/pcmanfm-qt/translations/pcmanfm-qt_cs_CZ.qm
#%lang(lt_LT) %{_datadir}/pcmanfm-qt/translations/pcmanfm-qt_lt_LT.qm
%lang(fr) %{_datadir}/libfm-qt/translations/libfm-qt_template-fr.qm
#%lang(lg) %{_datadir}/libfm-qt/translations/libfm-qt_template-gl.qm
%lang(it) %{_datadir}/libfm-qt/translations/libfm-qt_template-it.qm
%lang(zh_TW) %{_datadir}/pcmanfm-qt/translations/pcmanfm-qt_zh_TW.qm
%lang(fr) %{_datadir}/pcmanfm-qt/translations/pcmanfm-qt_template-fr.qm
#%lang(gl) %{_datadir}/pcmanfm-qt/translations/pcmanfm-qt_template-gl.qm
%lang(it) %{_datadir}/pcmanfm-qt/translations/pcmanfm-qt_template-it.qm

%files devel
%defattr(644,root,root,755)
%{_includedir}/libfm-qt
%{_libdir}/libfm-qt5.so
%{_pkgconfigdir}/libfm-qt5.pc



