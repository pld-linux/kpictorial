Summary:	KDE3 logical game
Summary(pl):	Gra logiczna dla KDE3
Name:		kpictorial
Version:	0.9.1
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://telia.dl.sourceforge.net/sourceforge/kpictorial/%{name}-%{version}.tar.gz
Source1:	http://telia.dl.sourceforge.net/sourceforge/kpictorial/kpictorial-imglib-29052002.tar.gz
URL:		http://members.chello.at/roland.lezuo/kpictorial.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.0
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define         _htmldir        /usr/share/doc/kde/HTML

%description
Kpictorial is a little logical game. 

%description -l pl
Kpictorial jest niedu�� gr� logiczn�.

%package imglib
Summary:	Kpictorial - set of images
Summary(pl):	Kpictorial - zbi�r obrazk�w
Group:		X11/Applications
Requires:	%{name}

%description imglib
This is a set of images in xbm and xpm format which can be used together with kpictorial.

%description imglib -l pl
Zbi�r obrazk�w w formacie xbm i xpm, kt�re mog� by� u�yte z kpictorial.

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"

%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_applnkdir}/Games/Board
mv $RPM_BUILD_ROOT%{_applnkdir}/{Games,Games/Board}/kpictorial.desktop
install -d $RPM_BUILD_ROOT%{_datadir}/apps/kpictorial
tar zxvf %{SOURCE1} -C $RPM_BUILD_ROOT%{_datadir}/apps/kpictorial
mv $RPM_BUILD_ROOT%{_datadir}/apps/kpictorial/{kpictorial-imglib,imglib}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Games/Board/*
%{_datadir}/apps/kpictorial/kpictorialui.rc
%{_datadir}/apps/kpictorial/icons
%{_pixmapsdir}/*/*/*/*
%{_docdir}/kde/HTML/en/kpictorial

%files imglib
%{_datadir}/apps/kpictorial/imglib
