#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%define		pdir	XML
%define		pnam	libxml-perl
Summary:	Collection of Perl modules for working with XML
Summary(pl.UTF-8):	Kolekcja modułów Perla do pracy z XML-em
Name:		perl-libxml
Version:	0.08
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/XML/%{pnam}-%{version}.tar.gz
# Source0-md5:	0ed5fbdda53d1301ddaed88db10503bb
URL:		http://search.cpan.org/dist/libxml-perl/
BuildRequires:	perl-XML-Parser >= 2.19
BuildRequires:	perl-devel >= 1:5.8.0
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

%description -l pl.UTF-8
libxml-perl to zestaw mniejszych perlowych modułów, skryptów i
dokumentów do pracy z XML-em w Perlu. Działa w połączeniu z
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
%{perl_vendorlib}/XML/ESISParser.pm
%{perl_vendorlib}/XML/Perl2SAX.pm
%{perl_vendorlib}/XML/SAX2Perl.pm
%{perl_vendorlib}/XML/Handler/CanonXMLWriter.pm
%{perl_vendorlib}/XML/Handler/Sample.pm
%{perl_vendorlib}/XML/Handler/Subs.pm
%{perl_vendorlib}/XML/Handler/XMLWriter.pm
%{perl_vendorlib}/XML/Parser/PerlSAX.pm
%{perl_vendorlib}/XML/PatAct
%{_mandir}/man3/Data::Grove*.3pm*
%{_mandir}/man3/XML::ESISParser.3pm*
%{_mandir}/man3/XML::Handler::*.3pm*
%{_mandir}/man3/XML::Parser::PerlSAX.3pm*
%{_mandir}/man3/XML::PatAct::*.3pm*
%{_mandir}/man3/XML::Perl2SAX.3pm*
%{_mandir}/man3/XML::SAX2Perl.3pm*
