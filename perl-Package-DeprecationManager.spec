#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Package
%define		pnam	DeprecationManager
Summary:	Package::DeprecationManager - manage deprecation warnings for your distribution
Summary(pl.UTF-8):	Package::DeprecationManager - zarządzanie ostrzeżeniami o przestarzałych elementach
Name:		perl-Package-DeprecationManager
Version:	0.17
Release:	2
License:	Artistic v2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Package/Package-DeprecationManager-%{version}.tar.gz
# Source0-md5:	7b46e92aaae3047ede3c67c1714ab88e
URL:		https://metacpan.org/release/Package-DeprecationManager
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.30
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Params-Util
BuildRequires:	perl-Scalar-List-Utils >= 1.33
BuildRequires:	perl-Sub-Install
BuildRequires:	perl-Sub-Name
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-Requires
BuildRequires:	perl-Test-Simple >= 0.96
BuildRequires:	perl-Test-Warnings
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
%doc Changes
%{perl_vendorlib}/Package/DeprecationManager.pm
%{_mandir}/man3/Package::DeprecationManager.3pm*
