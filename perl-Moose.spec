#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Moose
Summary:	Moose - A postmodern object system for Perl 5
#Summary(pl.UTF-8):	
Name:		perl-Moose
Version:	0.43
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/S/ST/STEVAN/Moose-0.43.tar.gz
# Source0-md5:	0f61233715b97485a06f640d4d888a85
URL:		http://www.iinteractive.com/moose/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Class::MOP) >= 0.55
BuildRequires:	perl(Sub::Exporter) >= 0.972
BuildRequires:	perl-Sub-Name >= 0.02
BuildRequires:	perl(Test::LongString)
BuildRequires:	perl-Test-Exception >= 0.21
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Moose is an extension of the Perl 5 object system.

# %description -l pl.UTF-8
# TODO

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
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/Moose/
%{perl_vendorlib}/Test/*.pm
%{_mandir}/man3/*
