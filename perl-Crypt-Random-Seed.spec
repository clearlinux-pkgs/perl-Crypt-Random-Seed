#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Crypt-Random-Seed
Version  : 0.03
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/D/DA/DANAJ/Crypt-Random-Seed-0.03.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DA/DANAJ/Crypt-Random-Seed-0.03.tar.gz
Summary  : 'Provide strong randomness for seeding'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Crypt-Random-Seed-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Crypt::Random::Seed version 0.03
========================
Crypt::Random::Seed provides a simple interface to get the strongest source
of randomness on the current platform, typically for use in seeding a CSPRNG
such as Math::Random::ISAAC.  It can also be restricted to non-blocking
sources, and has a very simple plug-in method.

%package dev
Summary: dev components for the perl-Crypt-Random-Seed package.
Group: Development
Provides: perl-Crypt-Random-Seed-devel = %{version}-%{release}

%description dev
dev components for the perl-Crypt-Random-Seed package.


%package license
Summary: license components for the perl-Crypt-Random-Seed package.
Group: Default

%description license
license components for the perl-Crypt-Random-Seed package.


%prep
%setup -q -n Crypt-Random-Seed-0.03

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Crypt-Random-Seed
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Crypt-Random-Seed/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Crypt/Random/Seed.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Crypt::Random::Seed.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Crypt-Random-Seed/LICENSE
