#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	libxml-perl
Summary:	Collection of Perl modules for working with XML
Summary(pl):	Kolekcja modu³ów Perla do pracy z XML-em
Name:		perl-libxml
Version:	0.07
Release:	11
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	a79c6da708e5906fec84ea611fa4b41e
URL:		http://bitsko.slc.ut.us/libxml-perl/
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	perl-XML-Parser >= 2.19
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
Obsoletes:	perl-libxml-perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	'perl(UNIVERSAL)'

%description
libxml-perl is a collection of smaller Perl modules, scripts, and
documents for working with XML in Perl. libxml-perl software works in
combination with XML::Parser, PerlSAX, XML::DOM, XML::Grove and
others.

%description -l pl
libxml-perl to zestaw mniejszych perlowych modu³ów, skryptów i
dokumentów do pracy z XML-em w Perlu. Dzia³a w po³±czeniu z
XML::Parser, PerlSAX, XML::DOM, XML::Grove i innymi.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Change*
%{perl_vendorlib}/Data/Grove.pm
%{perl_vendorlib}/Data/Grove
%{perl_vendorlib}/XML/*.pm
%{perl_vendorlib}/XML/Handler/*.pm
%{perl_vendorlib}/XML/Parser/*.pm
%{perl_vendorlib}/XML/PatAct
%{_mandir}/man3/*
