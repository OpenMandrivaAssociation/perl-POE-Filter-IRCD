%define upstream_name	 POE-Filter-IRCD
%define upstream_version 2.44

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	A POE-based parser for the IRC protocol
License:	GPL
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/POE/POE-Filter-IRCD-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(POE)
BuildArch:	noarch

%description
POE::Filter::IRCD is a Perl module that provides a convenient way of parsing
and creating IRC protocol lines.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/POE
%{_mandir}/*/*


%changelog
* Sat Dec 12 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.420.0-1mdv2010.1
+ Revision: 477634
- update to 2.42

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.400.0-1mdv2010.0
+ Revision: 404349
- rebuild using %%perl_convert_version

* Wed May 06 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.40-1mdv2010.0
+ Revision: 372532
- update to new version 2.40

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 2.38-2mdv2009.0
+ Revision: 268703
- rebuild early 2009.0 package (before pixel changes)

* Tue May 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.38-1mdv2009.0
+ Revision: 209331
- update to new version 2.38

* Sun Mar 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.36-1mdv2008.1
+ Revision: 183105
- update to new version 2.36

* Tue Jan 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.35-1mdv2008.1
+ Revision: 152846
- update to new version 2.35

* Wed Dec 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.34-1mdv2008.1
+ Revision: 138048
- update to new version 2.34

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Nov 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.32-1mdv2008.1
+ Revision: 105309
- update to new version 2.32

* Thu Aug 09 2007 Funda Wang <fwang@mandriva.org> 2.31-1mdv2008.0
+ Revision: 60694
- New version 2.31


* Wed Feb 28 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.30-1mdv2007.0
+ Revision: 127192
- new version

* Wed Nov 15 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.2-1mdv2007.1
+ Revision: 84384
- new version
- Import perl-POE-Filter-IRCD

* Fri Sep 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.1-1mdv2007.0
- New version 2.1

* Tue Sep 12 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.0-1mdv2007.0
- New version 2.0

* Wed Sep 06 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.9-1mdv2007.0
- new version
- fix sources URL

* Tue Aug 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.8-1mdv2007.0
- New version 1.8

* Sun May 14 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.7-1mdk
- New release 1.7

* Wed May 10 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.6-1mdk
- New release 1.6

* Thu May 04 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.5-2mdk
- Fix According to perl Policy
	- BuildRequires
	- Source URL

* Thu Dec 22 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.5-1mdk
- New release 1.5

* Wed Dec 14 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.4-1mdk
- New release 1.4
- spec cleanup
- fix directory ownership

* Fri Aug 19 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.2-1mdk
- new version 
- fix sources url for rpmbuildupdate

* Sat Jun 04 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.1-1mdk
- First Mandriva release


