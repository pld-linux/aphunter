Summary:	TODO
Name:		aphunter
Version:	1
Release:	0.1
License:	GPL ?
Group:		Networking/Utilities
Source0:	http://www.math.ucla.edu/~jimc/%{name}.tgz
# Source0-md5:	993075e53e2e682a54b9ee327f4b0647
URL:		http://www.math.ucla.edu/~jimc/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TODO

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
