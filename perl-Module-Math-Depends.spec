%define realname   Module-Math-Depends
%define version    0.02
%define release    %mkrel 1

Name:          perl-%{realname}
Version:       %{version}
Release:       %{release}
License:       GPL or Artistic
Group:         Development/Perl
Summary:       Convenience object for manipulating module dependencies
Source:        http://www.cpan.org/modules/by-module/Module/%{realname}-%{version}.tar.gz
Url:           http://search.cpan.org/dist/%{realname}
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Carp)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Params::Util)
BuildRequires: perl(Test::More)

BuildArch:     noarch

%description
This is a small convenience module created originally as part of the
Module::Inspector manpage but released seperately, in the hope that people
might find it useful in other contexts.

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README LICENSE Changes
%{_mandir}/man3/*
%perl_vendorlib/*
