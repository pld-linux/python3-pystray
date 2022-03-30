#
# Conditional build:
%bcond_without	doc	# API documentation
%bcond_with	tests	# unit tests, wants dbus and X11

%define		module	pystray
Summary:	This library allows you to create a system tray icon
Name:		python3-%{module}
Version:	0.17.3
Release:	4
License:	LGPLv3+
Group:		Libraries/Python
Source0:	https://github.com/moses-palmer/pystray/archive/v%{version}/%{module}-%{version}.tar.gz
# Source0-md5:	089154b1ff9c5d33b42510c18edf7cf2
URL:		https://github.com/moses-palmer/pystray
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg-3
%endif
Requires:	dbus
Requires:	gtk+3
Requires:	libappindicator-gtk3
Requires:	python3-modules >= 1:3.2
Requires:	python3-pillow
Requires:	python3-six
Requires:	python3-Xlib
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library allows you to create a system tray icon.

%package apidocs
Summary:	API documentation for Python %{module} module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona %{module}
Group:		Documentation

%description apidocs
API documentation for Python %{module} module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona %{module}.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build %{?with_tests:test}

%if %{with doc}
sphinx-build-3 docs docs/html
rm -rf docs/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst README.rst
%dir %{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}/*.py
%{py3_sitescriptdir}/%{module}/__pycache__
%dir %{py3_sitescriptdir}/%{module}/_util
%{py3_sitescriptdir}/%{module}/_util/*.py
%{py3_sitescriptdir}/%{module}/_util/__pycache__
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/html/*
%endif
