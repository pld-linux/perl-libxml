%include	/usr/lib/rpm/macros.perl
Summary:	Perl libxml module
Summary(pl):	Modu³ perla libxml
Name:		perl-libxml
Version:	0.07
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/libxml-perl-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libxml-perl is a collection of smaller Perl modules, scripts, and
documents for working with XML in Perl. libxml-perl software
works in combination with XML::Parser, PerlSAX, XML::DOM,
XML::Grove and others.

%description -l pl
libxml-perl to zestaw mniejszych perlowych modu³ów, skryptów i
dokumentów do pracy z XML w Perlu. Dzia³a w po³±czeniu z XML::Parser,
PerlSAX, XML::DOM, XML::Grove i innymi.

%prep
%setup -q -n libxml-perl-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README Change*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Data/Grove.pm
%{perl_sitelib}/Data/Grove
%{perl_sitelib}/XML
%{_mandir}/man3/*
