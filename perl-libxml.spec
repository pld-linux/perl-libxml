#
# Conditional build:
# _with_tests - perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	libxml-perl
Summary:	Collection of Perl modules for working with XML
Summary(pl):	Kolekcja modu³ów Perla do pracy z XML
Name:		perl-libxml
Version:	0.07
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
URL:		http://bitsko.slc.ut.us/libxml-perl/
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-XML-Parser >= 2.19
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	perl-libxml-perl

%define		_noautoreqdep	'perl(UNIVERSAL)'

%description
libxml-perl is a collection of smaller Perl modules, scripts, and
documents for working with XML in Perl. libxml-perl software works in
combination with XML::Parser, PerlSAX, XML::DOM, XML::Grove and
others.

%description -l pl
libxml-perl to zestaw mniejszych perlowych modu³ów, skryptów i
dokumentów do pracy z XML w Perlu. Dzia³a w po³±czeniu z XML::Parser,
PerlSAX, XML::DOM, XML::Grove i innymi.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Change*
%{perl_sitelib}/Data/Grove.pm
%{perl_sitelib}/Data/Grove
%{perl_sitelib}/XML/*.pm
%{perl_sitelib}/XML/Handler/*.pm
%{perl_sitelib}/XML/Parser/*.pm
%{perl_sitelib}/XML/PatAct
%{_mandir}/man3/*
