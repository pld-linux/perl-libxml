%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	libxml-perl
Summary:	libxml Perl module
Summary(cs):	Modul libxml pro Perl
Summary(da):	Perlmodul libxml
Summary(de):	libxml Perl Modul
Summary(es):	M�dulo de Perl libxml
Summary(fr):	Module Perl libxml
Summary(it):	Modulo di Perl libxml
Summary(ja):	libxml Perl �⥸�塼��
Summary(ko):	libxml �� ����
Summary(no):	Perlmodul libxml
Summary(pl):	Modu� Perla libxml
Summary(pt):	M�dulo de Perl libxml
Summary(pt_BR):	M�dulo Perl libxml
Summary(ru):	������ ��� Perl libxml
Summary(sv):	libxml Perlmodul
Summary(uk):	������ ��� Perl libxml
Summary(zh_CN):	libxml Perl ģ��
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
libxml-perl to zestaw mniejszych perlowych modu��w, skrypt�w i
dokument�w do pracy z XML w Perlu. Dzia�a w po��czeniu z XML::Parser,
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
