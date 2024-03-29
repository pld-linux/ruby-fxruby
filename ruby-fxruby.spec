# Conditional build:
%bcond_without	apidocs # don't generate documentation through rdoc
#
%define		__ruby	/usr/bin/ruby
%define		_pnam	FXRuby
#
Summary:	FXRuby - the Ruby language bindings for the FOX GUI toolkit
Summary(pl.UTF-8):	FXRuby - wiązania języka Ruby do toolkitu graficznego FOX
Name:		ruby-%{_pnam}
Version:	1.6.16
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://rubyforge.lauschmusik.de/fxruby/%{_pnam}-%{version}.tar.gz
# Source0-md5:	2eeef754f565b820d73ac39f6492ea4c
Patch0:		%{name}-CFLAGS.patch
URL:		http://www.fxruby.org/
BuildRequires:	fox >= 1.6
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
BuildRequires:	fxscintilla-devel >= 1.71
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FXRuby - the Ruby language bindings for the FOX GUI toolkit.

%description -l pl.UTF-8
FXRuby - wiązania języka Ruby do toolkitu graficznego interfejsu
użytkownika FOX.

%package apidocs
Summary:	API documentation for FXRuby
Summary(pl.UTF-8):	Dokumentacja API biblioteki FXRuby
Group:		Documentation

%description apidocs
API documentation for FXRuby - the Ruby language bindings for the FOX
GUI toolkit.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki FXRuby - wiązań języka Ruby do toolkitu
graficznego interfejsu użytkownika FOX.

%package examples
Summary:	Examples for FXRuby
Summary(pl.UTF-8):	Przykłady do biblioteki FXRuby
#TODO: new group Development/Languages/Ruby
Group:		Development/Languages

%description examples
Example programs for FXRuby - the Ruby language bindings for the FOX
GUI toolkit.

%description examples -l pl.UTF-8
Przykłady do biblioteki FXRuby - wiązań języka Ruby do toolkitu
graficznego interfejsu użytkownika FOX.


%prep
%setup -q -n %{_pnam}-%{version}
#patch0 -p1

%build
CC="%{__cc}" \
CXX="%{__cxx}" \
CFLAGS="%{rpmcflags}" \
CXXFLAGS="%{rpmcxxflags}" \
%{__ruby} install.rb config -- \
	--with-fox-include=/usr/include/fox-1.6 \
	--with-fox-lib="%{_libdir}" \
	--with-fxscintilla-include=/usr/include \
	--with-fxscintilla-lib="%{_libdir}"

CC="%{__cc}" \
CXX="%{__cxx}" \
CFLAGS="%{rpmcflags}" \
CXXFLAGS="%{rpmcxxflags}" \
%{__ruby} install.rb setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__ruby} install.rb install --prefix=$RPM_BUILD_ROOT

%{?with_apidocs:rdoc --op rdoc rdoc-sources}
cp -R examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{ruby_sitelibdir}/fox16
%attr(755,root,root) %{ruby_sitearchdir}/*.so

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc doc rdoc
%endif

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
