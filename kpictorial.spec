Summary:	KDE3 logical game
Summary(pl.UTF-8):	Gra logiczna dla KDE3
Name:		kpictorial
Version:	0.9.1
Release:	5
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	f4c7d7de8bac9ff6432ecbc91ba3478f
Source1:	http://dl.sourceforge.net/sourceforge/%{name}/kpictorial-imglib-29052002.tar.gz
# Source1-md5:	6f8245672e74388cff5cd4ca5e2a6905
URL:		http://members.chello.at/roland.lezuo/kpictorial.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.0.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kpictorial is a little logical game.

%description -l pl.UTF-8
Kpictorial jest niedużą grą logiczną.

%package imglib
Summary:	Kpictorial - set of images
Summary(pl.UTF-8):	Kpictorial - zbiór obrazków
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description imglib
This is a set of images in xbm and xpm format which can be used
together with kpictorial.

%description imglib -l pl.UTF-8
Zbiór obrazków w formacie xbm i xpm, które mogą być użyte z
kpictorial.

%prep
%setup -q

%build
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"

%configure \
	--enable-final \
	--disable-rpath

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir}/kde,%{_datadir}/apps/kpictorial}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT{%{_datadir}/applnk/Games,%{_desktopdir}/kde}/kpictorial.desktop

tar zxvf %{SOURCE1} -C $RPM_BUILD_ROOT%{_datadir}/apps/kpictorial
mv $RPM_BUILD_ROOT%{_datadir}/apps/kpictorial/{kpictorial-imglib,imglib}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/kde/*.desktop
%dir %{_datadir}/apps/kpictorial
%{_datadir}/apps/kpictorial/icons
%{_datadir}/apps/kpictorial/kpictorialui.rc
%{_iconsdir}/hicolor/*/*/*.png

%files imglib
%defattr(644,root,root,755)
%{_datadir}/apps/kpictorial/imglib
