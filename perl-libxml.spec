%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	libxml-perl
Summary:	libxml Perl module
Summary(cs):	Modul libxml pro Perl
Summary(da):	Perlmodul libxml
Summary(de):	libxml Perl Modul
Summary(es):	Módulo de Perl libxml
Summary(fr):	Module Perl libxml
Summary(it):	Modulo di Perl libxml
Summary(ja):	libxml Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	libxml ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul libxml
Summary(pl):	Modu³ Perla libxml
Summary(pt):	Módulo de Perl libxml
Summary(pt_BR):	Módulo Perl libxml
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl libxml
Summary(sv):	libxml Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl libxml
Summary(zh_CN):	libxml Perl Ä£¿é
Name:		perl-libxml
Version:	0.07
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-XML-Parser >= 2.19
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	perl-libxml-perl

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
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

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
%{perl_sitelib}/XML/*
%{_mandir}/man3/*
