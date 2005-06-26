Summary:	Access Point Hunter
Summary(pl):	Access Point Hunter - wyszukiwacz punktów dostêpowych
Name:		aphunter
Version:	1
Release:	0.1
License:	GPL ?
Group:		Networking/Utilities
Source0:	http://www.math.ucla.edu/~jimc/%{name}.tgz
# Source0-md5:	993075e53e2e682a54b9ee327f4b0647
URL:		http://www.math.ucla.edu/~jimc/
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Access Point Hunter can find and automatically connect to whatever
wireless network is within range. It can be used for site surveys,
writing the results in a file.

%description -l pl
Access Point Hunter potrafi znale¼æ i automatycznie po³±czyæ z dowoln±
sieci± bezprzewodow± w zasiêgu. Mo¿e byæ u¿ywany do inspekcji,
zapisuj±c wyniki w pliku.

%prep
%setup -q -c

%build
sed -i -e 's#/usr/local/bin/perl#/usr/bin/perl#' %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install %{name} $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
