#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Moose
Summary:	Moose - A postmodern object system for Perl 5
Summary(pl.UTF-8):	Moose - postmodernistyczny system obiektów dla Perla 5
Name:		perl-Moose
Version:	1.24
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/CPAN/authors/id/D/DR/DROLSKY/%{pdir}-%{version}.tar.gz
# Source0-md5:	1feb512a74fa2215e6b39bd10ecccf58
URL:		http://www.iinteractive.com/moose/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.42
BuildRequires:	perl-devel >= 1:5.8.3
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-MOP >= 1.11
BuildRequires:	perl-DBM-Deep >= 1.0003
BuildRequires:	perl-Data-OptList
BuildRequires:	perl-DateTime
BuildRequires:	perl-DateTime-Calendar-Mayan
BuildRequires:	perl-DateTime-Format-MySQL
BuildRequires:	perl-Declare-Constraints-Simple
BuildRequires:	perl-File-Find-Rule
BuildRequires:	perl-IO-String
BuildRequires:	perl-List-MoreUtils >= 0.12
BuildRequires:	perl-Locale-US
BuildRequires:	perl-Module-Info
BuildRequires:	perl-Module-Refresh
BuildRequires:	perl-Package-DeprecationManager >= 0.10
BuildRequires:	perl-Params-Coerce
BuildRequires:	perl-Params-Util >= 1.00
BuildRequires:	perl-Regexp-Common
BuildRequires:	perl-Scalar-List-Utils >= 1.19
BuildRequires:	perl-Sub-Exporter >= 0.980
BuildRequires:	perl-Sub-Name
BuildRequires:	perl-Task-Weaken
BuildRequires:	perl-Test-Deep
BuildRequires:	perl-Test-Exception >= 0.27
BuildRequires:	perl-Test-Fatal >= 0.001
BuildRequires:	perl-Test-Inline
BuildRequires:	perl-Test-NoTabs
BuildRequires:	perl-Test-Output
BuildRequires:	perl-Test-Pod-Coverage
BuildRequires:	perl-Test-Requires >= 0.05
BuildRequires:	perl-Test-Simple >= 0.88
BuildRequires:	perl-Test-Spelling
BuildRequires:	perl-Try-Tiny >= 0.02
BuildRequires:	perl-URI
BuildRequires:	perl-libwww
%endif
Conflicts:	perl-Catalyst <= 5.80028
Conflicts:	perl-Devel-REPL <= 1.003008
Conflicts:	perl-Fey <= 0.36
Conflicts:	perl-Fey-ORM <= 0.34
Conflicts:	perl-File-ChangeNotify <= 0.15
Conflicts:	perl-KiokuDB <= 0.49
Conflicts:	perl-Markdent <= 0.16
Conflicts:	perl-MooseX-Aliases <= 0.07
Conflicts:	perl-MooseX-AlwaysCoerce <= 0.05
Conflicts:	perl-MooseX-AttributeHelpers <= 0.22
Conflicts:	perl-MooseX-AttributeInflate <= 0.02
Conflicts:	perl-MooseX-Attribute-Prototype <= 0.10
Conflicts:	perl-MooseX-ClassAttribute <= 0.17
Conflicts:	perl-MooseX-FollowPBP <= 0.02
Conflicts:	perl-MooseX-HasDefaults <= 0.02
Conflicts:	perl-MooseX-InstanceTracking <= 0.04
Conflicts:	perl-MooseX-LazyRequire <= 0.05
Conflicts:	perl-MooseX-MethodAttributes <= 0.22
Conflicts:	perl-MooseX-NonMoose <= 0.15
Conflicts:	perl-MooseX-Params-Validate <= 0.05
Conflicts:	perl-MooseX-POE <= 0.205
Conflicts:	perl-MooseX-Role-Cmd <= 0.06
Conflicts:	perl-MooseX-Role-WithOverloading <= 0.07
Conflicts:	perl-MooseX-SemiAffordanceAccessor <= 0.05
Conflicts:	perl-MooseX-Singleton <= 0.24
Conflicts:	perl-MooseX-StrictConstructor <= 0.08
Conflicts:	perl-MooseX-Types <= 0.19
Conflicts:	perl-MooseX-UndefTolerant <= 0.04
Conflicts:	perl-Pod-Elemental <= 0.093280
Conflicts:	perl-namespace-autoclean <= 0.08
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Moose is an extension of the Perl 5 object system.

%description -l pl.UTF-8
Moose to rozszerzenie systemu obiektowego Perla 5.

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
%dir %{perl_vendorlib}/MooseX
%{perl_vendorarch}/Moose.pm
%{perl_vendorarch}/Moose
%{perl_vendorarch}/Test/Moose.pm
%{perl_vendorarch}/oose.pm
%dir %{perl_vendorarch}/auto/Moose
%{perl_vendorarch}/auto/Moose/Moose.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Moose/Moose.so
%{_mandir}/man3/Moose*.3pm*
%{_mandir}/man3/Test::Moose.3pm*
%{_mandir}/man3/oose.3pm*
