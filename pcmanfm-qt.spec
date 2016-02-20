#
# Conditional build:
#
%define		qtver		5.3.1

Summary:	pcmanfm-qt
Name:		pcmanfm-qt
Version:	0.10.0
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	http://downloads.lxqt.org/lxqt/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	9a69dcb7940123e2b17523855ccda6ae
URL:		http://www.lxqt.org/
BuildRequires:	cmake >= 2.8.11
BuildRequires:	glib2-devel
BuildRequires:	libfm-devel >= 1.2.0
BuildRequires:	liblxqt-devel >= 0.10.0
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

%find_lang %{name} --all-name --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pcmanfm-qt
%attr(755,root,root) %ghost %{_libdir}/libfm-qt5.so.2
%attr(755,root,root) %{_libdir}/libfm-qt5.so.2.0.0
%{_desktopdir}/pcmanfm-qt-desktop-pref.desktop
%{_desktopdir}/pcmanfm-qt.desktop
%{_mandir}/man1/pcmanfm-qt.1*
%dir %{_datadir}/libfm-qt
%dir %{_datadir}/libfm-qt/translations
%dir %{_datadir}/pcmanfm-qt
%dir %{_datadir}/pcmanfm-qt/translations

%files devel
%defattr(644,root,root,755)
%{_includedir}/libfm-qt
%{_libdir}/libfm-qt5.so
%{_pkgconfigdir}/libfm-qt5.pc
