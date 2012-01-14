#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Package
%define		pnam	DeprecationManager
%include	/usr/lib/rpm/macros.perl
Summary:	Package::DeprecationManager - manage deprecation warnings for your distribution
Summary(pl.UTF-8):	Package::DeprecationManager - zarządzanie ostrzeżeniami o przestarzałych elementach
Name:		perl-Package-DeprecationManager
Version:	0.11
Release:	1
License:	Artistic 2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DR/DROLSKY/Package-DeprecationManager-%{version}.tar.gz
# Source0-md5:	d09664839b730997c591a5c891a2972b
URL:		http://search.cpan.org/dist/Package-DeprecationManager/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-List-MoreUtils
BuildRequires:	perl-Params-Util
BuildRequires:	perl-Sub-Install
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-Requires
BuildRequires:	perl-Test-Simple >= 0.88
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows you to manage a set of deprecations for one or more
modules.

%description -l pl.UTF-8
Ten moduł pozwala na zarządzanie zbiorem przestarzałych elementów dla
jednego lub większej liczby modułów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Package/DeprecationManager.pm
%{_mandir}/man3/Package::DeprecationManager.3pm*
