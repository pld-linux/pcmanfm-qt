#
# Conditional build:
#
%define		qtver		6.6.0

Summary:	LXQt file manager - PCManFM
Summary(pl.UTF-8):	Manager plików dla LXQt - PCManFM
Name:		pcmanfm-qt
Version:	2.3.0
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	https://github.com/lxqt/pcmanfm-qt/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	cf8e4780a53203377be779d3c7112391
URL:		http://www.lxqt.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.18.0
BuildRequires:	kp6-layer-shell-qt-devel >= 6.0.0
BuildRequires:	libfm-qt-devel >= 2.3.0
BuildRequires:	lxqt-build-tools >= 2.3.0
BuildRequires:	qt6-linguist >= %{qtver}
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PCManFM-Qt is a Qt-based file manager which uses GLib for file
management. It was started as the Qt port of PCManFM, the file manager
of LXDE.

PCManFM-Qt is used by LXQt for handling the desktop. Nevertheless, it
can also be used independently of LXQt and under any desktop
environment.

%description -l pl.UTF-8
PCManFM-Qt to menedżer plików oparty na Qt, który wykorzystuje
bibliotekę GLib do zarządzania plikami. Powstał jako port Qt PCManFM,
menedżera plików LXDE.

PCManFM-Qt jest używany przez LXQt do obsługi pulpitu. Niemniej
jednak, może być również używany niezależnie od LXQt i w dowolnym
środowisku graficznym.

%package devel
Summary:	PCManFM-Qt - header files and development documentation
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do PCManFM-Qt
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt6Core-devel >= %{qtver}
Requires:	Qt6DBus-devel >= %{qtver}
Requires:	Qt6Gui-devel >= %{qtver}
Requires:	Qt6Widgets-devel >= %{qtver}

%description devel
This package contains header files and development documentation for
pcmanfm-qt.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe i dokumentację potrzebną przy
pisaniu własnych programów wykorzystujących pcmanfm-qt.

%prep
%setup -q

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pcmanfm-qt
%{_desktopdir}/pcmanfm-qt-desktop-pref.desktop
%{_desktopdir}/pcmanfm-qt.desktop
%{_mandir}/man1/pcmanfm-qt.1*
/etc/xdg/autostart/lxqt-desktop.desktop
%{_iconsdir}/hicolor/scalable/apps/pcmanfm-qt.svg
%dir %{_datadir}/pcmanfm-qt
%dir %{_datadir}/pcmanfm-qt/lxqt
# required for the lang files
%dir %{_datadir}/pcmanfm-qt/translations
%{_datadir}/pcmanfm-qt/lxqt/settings.conf
