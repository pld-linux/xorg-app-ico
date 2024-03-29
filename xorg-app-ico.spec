Summary:	ico application - animate an icosahedron or other polyhedron
Summary(pl.UTF-8):	Aplikacja ico - animowanie dwudziestościanu lub innego wielościanu
Name:		xorg-app-ico
Version:	1.0.6
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/ico-%{version}.tar.xz
# Source0-md5:	0c5a669eb1930fd3fcf50978c8ac4ff3
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel >= 0.99.1
BuildRequires:	xorg-proto-xproto-devel >= 7.0.22
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ico displays a wire-frame rotating polyhedron, with hidden lines
removed, or a solid-fill polyhedron with hidden faces removed. There
are a number of different polyhedra available; adding a new polyhedron
to the program is quite simple.

%description -l pl.UTF-8
ico wyświetla obracający się model drutowy dwudziestościanu bez
ukrytych krawędzi lub wypełniony wielościan bez niewidocznych ścian.
Dostępnych jest wiele różnych wielościanów; dodanie do programu nowego
wielościanu jest dość proste.

%prep
%setup -q -n ico-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/ico
%{_mandir}/man1/ico.1*
