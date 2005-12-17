#
%bcond_without	apidocs # don't generate documentation through rdoc
#
%define		_pnam	FXRuby
# TODO: __ruby  macro should be defined in rpm macros similarly as __perl
%define		__ruby	/usr/bin/ruby
#
Summary:	FXRuby - the Ruby language bindings for the FOX GUI toolkit
Name:		ruby-%{_pnam}
Version:	1.4.3	
Release:	0.1
License:	LGPL	
Group:		X11/Libraries		
Source0:	http://rubyforge.lauschmusik.de/fxruby/%{_pnam}-%{version}.tar.gz
# Source0-md5:	54598609033449180963aa38a28dd2ff
Patch0:		%{name}-CFLAGS.patch
URL:		http://rubyforge.org/projects/fxruby/
BuildRequires:	fox >= 1.4
BuildRequires:	rpmbuild(macros) >= 1.272
BuildRequires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FXRuby - the Ruby language bindings for the FOX GUI toolkit.

%package apidocs
Summary:	API documentation for FXRuby
Group:		Documentation

%description apidocs
API documentation for FXRuby - the Ruby language bindings for the FOX
GUI toolkit.

%package examples 
Summary:	API documentation for FXRuby
#TODO: new group Development/Languages/Ruby
Group:		Development/Languages

%description examples
Example programs for FXRuby - the Ruby language bindings for the FOX
GUI toolkit.

%prep
%setup -q -n %{_pnam}-%{version}
%patch0 -p1

%build
CC="%{__cc}" CXX="%{__cxx}" CFLAGS="%{rpmcflags}" CXXFLAGS="%{rpmcxxflags}" %{__ruby} install.rb config
CC="%{__cc}" CXX="%{__cxx}" CFLAGS="%{rpmcflags}" CXXFLAGS="%{rpmcxxflags}" %{__ruby} install.rb setup

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__ruby} install.rb install --prefix=$RPM_BUILD_ROOT

%{?with_apidocs:rdoc --op rdoc rdoc-sources}
# TODO: learn about rdoc
#%%{?with_apidocs:rdoc --ri --op rdoc rdoc-sources}
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
