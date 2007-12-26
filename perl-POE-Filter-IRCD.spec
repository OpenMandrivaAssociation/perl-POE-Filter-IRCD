%define module	POE-Filter-IRCD
%define name	perl-%{module}
%define version	2.34
%define release	%mkrel 1

Name:		    %{name}
Version:	    %{version}
Release:	    %{release}
Summary:	    A POE-based parser for the IRC protocol
License:	    GPL
Group:		    Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/POE/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:  perl(POE)
BuildArch:	    noarch
Buildroot:	    %{_tmppath}/%{name}-%{version}

%description
POE::Filter::IRCD is a Perl module that provides a convenient way of parsing
and creating IRC protocol lines.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/POE
%_mandir/*/*


