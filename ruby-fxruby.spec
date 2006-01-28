#
%bcond_without	apidocs # don't generate documentation through rdoc
#
%define		_pnam	FXRuby
# TODO: __ruby  macro should be defined in rpm macros similarly as __perl
%define		__ruby	/usr/bin/ruby
#
Summary:	FXRuby - the Ruby language bindings for the FOX GUI toolkit
Summary(pl):	FXRuby - wi±zania jêzyka Ruby do toolkitu graficznego FOX
Name:		ruby-%{_pnam}
Version:	1.4.4	
Release:	1
License:	LGPL	
Group:		X11/Libraries		
Source0:	http://rubyforge.lauschmusik.de/fxruby/%{_pnam}-%{version}.tar.gz
# Source0-md5:	e92f1e24b04802a532b1ad9de18e5306
Patch0:		%{name}-CFLAGS.patch
URL:		http://rubyforge.org/projects/fxruby/
BuildRequires:	fox >= 1.4
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FXRuby - the Ruby language bindings for the FOX GUI toolkit.

%description -l pl
FXRuby - wi±zania jêzyka Ruby do toolkitu graficznego interfejsu
u¿ytkownika FOX.

%package apidocs
Summary:	API documentation for FXRuby
Summary(pl):	Dokumentacja API biblioteki FXRuby
Group:		Documentation

%description apidocs
API documentation for FXRuby - the Ruby language bindings for the FOX
GUI toolkit.

%description apidocs -l pl
Dokumentacja API biblioteki FXRuby - wi±zañ jêzyka Ruby do toolkitu
graficznego interfejsu u¿ytkownika FOX.

%package examples 
Summary:	Examples for FXRuby
Summary(pl):	Przyk³ady do biblioteki FXRuby
#TODO: new group Development/Languages/Ruby
Group:		Development/Languages

%description examples
Example programs for FXRuby - the Ruby language bindings for the FOX
GUI toolkit.

%description examples -l pl
Przyk³ady do biblioteki FXRuby - wi±zañ jêzyka Ruby do toolkitu
graficznego interfejsu u¿ytkownika FOX.


%prep
%setup -q -n %{_pnam}-%{version}
%patch0 -p1

%build
CC="%{__cc}" \
CXX="%{__cxx}" \
CFLAGS="%{rpmcflags}" \
CXXFLAGS="%{rpmcxxflags}" \
%{__ruby} install.rb config

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
%doc ChangeLog README 
%{ruby_sitelibdir}/fox14
%attr(755,root,root) %{ruby_sitearchdir}/*.so

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc doc rdoc
%endif

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
