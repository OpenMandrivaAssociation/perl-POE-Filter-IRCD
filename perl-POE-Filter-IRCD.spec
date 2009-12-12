%define upstream_name	 POE-Filter-IRCD
%define upstream_version 2.42

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	A POE-based parser for the IRC protocol
License:	GPL
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/POE/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:  perl(POE)
BuildArch:	    noarch
Buildroot:	    %{_tmppath}/%{name}-%{version}-%{release}

%description
POE::Filter::IRCD is a Perl module that provides a convenient way of parsing
and creating IRC protocol lines.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
