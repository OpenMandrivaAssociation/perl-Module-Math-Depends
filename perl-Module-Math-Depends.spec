%define upstream_name    Module-Math-Depends
Name:		perl-%{upstream_name}
Version:	0.02
Release:	7

Summary:	Convenience object for manipulating module dependencies
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Module-Math-Depends
Source0:	https://cpan.metacpan.org/authors/id/A/AD/ADAMK/Module-Math-Depends-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Params::Util)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This is a small convenience module created originally as part of the
Module::Inspector manpage but released seperately, in the hope that people
might find it useful in other contexts.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README LICENSE Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.20.0-2mdv2011.0
+ Revision: 655057
- rebuild for updated spec-helper

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2011.0
+ Revision: 403867
- rebuild using %0.02 Sat Aug 30 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.02-1mdv2009.0
+ Revision: 277636
- import perl-Module-Math-Depends


