#
# Conditional build:
#
%define		qtver		4.8.5

Summary:	pcmanfm-qt
Name:		pcmanfm-qt
Version:	0.7.0
Release:	0.1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	http://lxqt.org/downloads/lxqt/0.7.0/%{name}-%{version}.tar.xz
# Source0-md5:	f054167fc989d1c1ecfdd302f9142192
URL:		http://www.lxqt.org/
BuildRequires:	cmake >= 2.8.3
BuildRequires:	glib2-devel
BuildRequires:	libfm-devel >= 1.2.0
BuildRequires:	liblxqt-devel >= 0.7.0
BuildRequires:	libqtxdg-devel >= 0.5.3
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
Requires:	QtCore-devel >= %{qtver}
Requires:	QtGui-devel >= %{qtver}
Requires:	QtXml-devel >= %{qtver}

%description devel
This package contains header files and development documentation for
pcmanfm-qt.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe i dokumentację potrzebną przy
pisaniu własnych programów wykorzystujących pcmanfm-qt.

%prep
%setup -q -c %{name}-%{version}

%build
install -d build
cd build
%cmake \
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
%ghost %{_libdir}/libfm-qt.so.0
%attr(755,root,root) %{_libdir}/libfm-qt.so.*.*.*
%{_desktopdir}/pcmanfm-qt-desktop-pref.desktop
%{_desktopdir}/pcmanfm-qt.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/libfm-qt
%{_libdir}/libfm-qt.so
%{_pkgconfigdir}/libfm-qt.pc
