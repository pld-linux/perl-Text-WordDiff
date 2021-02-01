#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Text
%define		pnam	WordDiff
Summary:	Track changes between documents
Name:		perl-Text-WordDiff
Version:	0.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Text/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2a9db19fbb99a5520d2e8281eee6c750
# generic URL, check or change before uncommenting
#URL:		https://metacpan.org/release/Text-WordDiff
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Algorithm-Diff >= 1.19
BuildRequires:	perl-HTML-Parser
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a variation on the lovely Text::Diff module. Rather
than generating traditional line-oriented diffs, however, it generates
word-oriented diffs. This can be useful for tracking changes in
narrative documents or documents with very long lines.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Text/*.pm
%{perl_vendorlib}/Text/WordDiff
%{_mandir}/man3/Text::WordDiff*
%{_examplesdir}/%{name}-%{version}
