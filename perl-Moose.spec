#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Moose
Summary:	Moose - A postmodern object system for Perl 5
Summary(pl.UTF-8):	Moose - postmodernistyczny system obiektów dla Perla 5
Name:		perl-Moose
Version:	0.54
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/S/ST/STEVAN/%{pdir}-%{version}.tar.gz
# Source0-md5:	53b5cddeb1e287b29f87966c9ad3e433
URL:		http://www.iinteractive.com/moose/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-MOP >= 0.59
BuildRequires:	perl-Scalar-List-Utils >= 1.18
BuildRequires:	perl-Sub-Exporter >= 0.972
BuildRequires:	perl-Test-Exception >= 0.21
BuildRequires:	perl-Test-LongString
BuildRequires:	perl-Test-Simple >= 0.62
%endif
Requires:	perl-Class-MOP >= 0.59
Requires:	perl-Scalar-List-Utils >= 1.18
Requires:	perl-Sub-Exporter >= 0.972
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Moose is an extension of the Perl 5 object system.

%description -l pl.UTF-8
Moose to rozszerzenie systemu obiektowego Perla 5

%prep
%setup -q -n %{pdir}-%{version}

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
%doc Changes README
%{perl_vendorlib}/Moose.pm
%{perl_vendorlib}/oose.pm
%{perl_vendorlib}/Moose
%{perl_vendorlib}/Test/Moose.pm
%{_mandir}/man3/Moose*.3pm*
%{_mandir}/man3/Test::Moose.3pm*
%{_mandir}/man3/oose.3pm*
