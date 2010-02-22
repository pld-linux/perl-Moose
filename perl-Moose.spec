#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Moose
Summary:	Moose - A postmodern object system for Perl 5
Summary(pl.UTF-8):	Moose - postmodernistyczny system obiektów dla Perla 5
Name:		perl-Moose
Version:	0.98
Release:	2
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/CPAN/authors/id/D/DR/DROLSKY/%{pdir}-%{version}.tar.gz
# Source0-md5:	c040bde14d843ea09a0d138b25642f42
URL:		http://www.iinteractive.com/moose/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(DBM::Deep) >= 1.0003
BuildRequires:	perl(DateTime)
BuildRequires:	perl(DateTime::Calendar::Mayan)
BuildRequires:	perl(DateTime::Format::MySQL)
BuildRequires:	perl(Declare::Constraints::Simple)
BuildRequires:	perl(HTTP::Headers)
BuildRequires:	perl(Locale::US)
BuildRequires:	perl(Module::Refresh)
BuildRequires:	perl(Params::Coerce)
BuildRequires:	perl(Regexp::Common)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::Output)
BuildRequires:	perl(Try::Tiny) >= 0.02
BuildRequires:	perl(URI)
BuildRequires:	perl-Class-MOP >= 0.98
BuildRequires:	perl-Data-OptList
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.42
BuildRequires:	perl-List-MoreUtils >= 0.12
BuildRequires:	perl-Sub-Exporter >= 0.980
BuildRequires:	perl-Sub-Name
BuildRequires:	perl-Task-Weaken
BuildRequires:	perl-Test-Exception >= 0.27
BuildRequires:	perl-Test-Simple >= 0.77
%endif
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
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/MooseX

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/MooseX/
%{perl_vendorarch}/*.pm
%{perl_vendorarch}/%{pdir}
%{perl_vendorarch}/Test/*.pm
%dir %{perl_vendorarch}/auto/%{pdir}
%attr(755,root,root) %{perl_vendorarch}/auto/%{pdir}/*.so
%{_mandir}/man3/Moose*.3pm*
%{_mandir}/man3/Test::Moose.3pm*
%{_mandir}/man3/oose.3pm*
