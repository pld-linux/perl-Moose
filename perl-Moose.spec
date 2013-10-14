#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Moose
Summary:	Moose - A postmodern object system for Perl 5
Summary(pl.UTF-8):	Moose - postmodernistyczny system obiektów dla Perla 5
Name:		perl-Moose
Version:	2.1005
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/E/ET/ETHER/%{pdir}-%{version}.tar.gz
# Source0-md5:	8878c5b28ee5312c31983f2de3167db1
URL:		http://www.iinteractive.com/moose/
BuildRequires:	perl-Dist-CheckConflicts >= 0.02
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.42
BuildRequires:	perl-devel >= 1:5.8.3
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Carp) >= 1.22
BuildRequires:	perl-CPAN-Meta-Check >= 0.007
BuildRequires:	perl-Class-Load >= 0.09
BuildRequires:	perl-Class-Load-XS >= 0.01
BuildRequires:	perl-DBM-Deep >= 1.0003
BuildRequires:	perl-Data-OptList >= 0.107
BuildRequires:	perl-DateTime
BuildRequires:	perl-DateTime-Calendar-Mayan
BuildRequires:	perl-DateTime-Format-MySQL >= 0.01
BuildRequires:	perl-Declare-Constraints-Simple
BuildRequires:	perl-Devel-GlobalDestruction
BuildRequires:	perl-Eval-Closure >= 0.04
BuildRequires:	perl-File-Find-Rule
BuildRequires:	perl-IO-String >= 0.01
BuildRequires:	perl-List-MoreUtils >= 0.28
BuildRequires:	perl-Locale-US
BuildRequires:	perl-MRO-Compat >= 0.05
BuildRequires:	perl-Module-Info
BuildRequires:	perl-Module-Refresh >= 0.01
BuildRequires:	perl-Package-DeprecationManager >= 0.11
BuildRequires:	perl-Package-Stash >= 0.32
BuildRequires:	perl-Package-Stash-XS >= 0.24
BuildRequires:	perl-Params-Coerce
BuildRequires:	perl-Params-Util >= 1.00
BuildRequires:	perl-Regexp-Common
BuildRequires:	perl-Scalar-List-Utils >= 1.19
BuildRequires:	perl-Sub-Exporter >= 0.980
BuildRequires:	perl-Sub-Name >= 0.05
BuildRequires:	perl-Task-Weaken
BuildRequires:	perl-Test-CheckDeps >= 0.007
BuildRequires:	perl-Test-Deep
BuildRequires:	perl-Test-Fatal >= 0.001
BuildRequires:	perl-Test-Inline
BuildRequires:	perl-Test-NoTabs
BuildRequires:	perl-Test-Output >= 0.01
BuildRequires:	perl-Test-Pod-Coverage >= 1.04
BuildRequires:	perl-Test-Requires >= 0.05
BuildRequires:	perl-Test-Simple >= 0.94
BuildRequires:	perl-Test-Spelling
BuildRequires:	perl-Try-Tiny >= 0.02
BuildRequires:	perl-URI
BuildRequires:	perl-libwww
%endif
Provides:	perl-Class-MOP = %{version}
Obsoletes:	perl-Class-MOP < %{version}
Conflicts:	perl-Catalyst <= 5.80028
Conflicts:	perl-Devel-REPL <= 1.003008
Conflicts:	perl-Fey <= 0.36
Conflicts:	perl-Fey-ORM <= 0.42
Conflicts:	perl-File-ChangeNotify <= 0.15
Conflicts:	perl-KiokuDB <= 0.51
Conflicts:	perl-Markdent <= 0.16
Conflicts:	perl-MooseX-ABC <= 0.05
Conflicts:	perl-MooseX-Aliases <= 0.08
Conflicts:	perl-MooseX-AlwaysCoerce <= 0.13
Conflicts:	perl-MooseX-AttributeHelpers <= 0.22
Conflicts:	perl-MooseX-AttributeIndexes <= 1.0.0
Conflicts:	perl-MooseX-AttributeInflate <= 0.02
Conflicts:	perl-MooseX-Attribute-Deflator <= 2.1.7
Conflicts:	perl-MooseX-Attribute-Dependent <= 1.1.0
Conflicts:	perl-MooseX-Attribute-Prototype <= 0.10
Conflicts:	perl-MooseX-CascadeClearing <= 0.03
Conflicts:	perl-MooseX-ClassAttribute <= 0.25
Conflicts:	perl-MooseX-Constructor-AllErrors <= 0.012
Conflicts:	perl-MooseX-FollowPBP <= 0.02
Conflicts:	perl-MooseX-HasDefaults <= 0.02
Conflicts:	perl-MooseX-InstanceTracking <= 0.04
Conflicts:	perl-MooseX-LazyRequire <= 0.06
Conflicts:	perl-MooseX-Meta-Attribute-Index <= 0.04
Conflicts:	perl-MooseX-Meta-Attribute-Lvalue <= 0.05
Conflicts:	perl-MooseX-MethodAttributes <= 0.22
Conflicts:	perl-MooseX-NonMoose <= 0.17
Conflicts:	perl-MooseX-POE <= 0.214
Conflicts:	perl-MooseX-Params-Validate <= 0.05
Conflicts:	perl-MooseX-PrivateSetters <= 0.03
Conflicts:	perl-MooseX-Role-Cmd <= 0.06
Conflicts:	perl-MooseX-Role-Parameterized <= 0.23
Conflicts:	perl-MooseX-Role-WithOverloading <= 0.07
Conflicts:	perl-MooseX-Scaffold <= 0.05
Conflicts:	perl-MooseX-SemiAffordanceAccessor <= 0.05
Conflicts:	perl-MooseX-SetOnce <= 0.100473
Conflicts:	perl-MooseX-Singleton <= 0.25
Conflicts:	perl-MooseX-SlurpyConstructor <= 1.1
Conflicts:	perl-MooseX-StrictConstructor <= 0.12
Conflicts:	perl-MooseX-Types <= 0.19
Conflicts:	perl-MooseX-Types-Parameterizable <= 0.05
Conflicts:	perl-MooseX-Types-Signal <= 1.101930
Conflicts:	perl-MooseX-UndefTolerant <= 0.11
Conflicts:	perl-PRANG <= 0.14
Conflicts:	perl-Pod-Elemental <= 0.093280
Conflicts:	perl-Reaction <= 0.002003
Conflicts:	perl-Test-Able <= 0.10
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
%doc Changes README.md TODO
%attr(755,root,root) %{_bindir}/moose-outdated
%{perl_vendorarch}/Class/MOP.pm
%{perl_vendorarch}/Class/MOP
%dir %{perl_vendorlib}/MooseX
%{perl_vendorarch}/Moose.pm
%{perl_vendorarch}/Moose
%{perl_vendorarch}/Test/Moose.pm
%{perl_vendorarch}/metaclass.pm
%{perl_vendorarch}/oose.pm
%dir %{perl_vendorarch}/auto/Moose
%{perl_vendorarch}/auto/Moose/Moose.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Moose/Moose.so
%{_mandir}/man3/Class::MOP*.3pm*
%{_mandir}/man3/Moose*.3pm*
%{_mandir}/man3/Test::Moose.3pm*
%{_mandir}/man3/metaclass.3pm*
%{_mandir}/man3/oose.3pm*
