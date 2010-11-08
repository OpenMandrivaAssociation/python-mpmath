%define module	mpmath
%define name	python-%{module}
%define version	0.14
%define release	%mkrel 2

Summary:	Python library for symbolic mathematics
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://mpmath.googlecode.com/files/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://mpmath.googlecode.com/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: 	python-numpy
Suggests:	python-gmpy >= 1.03, python-pyglet
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python-sphinx


%description
Mpmath is a pure-Python library for multiprecision floating-point arithmetic.
It provides an extensive set of transcendental functions, unlimited exponent
sizes, complex numbers, interval arithmetic, numerical integration and
differentiation, root-finding, linear algebra, and much more. Almost any
calculation can be performed just as well at 10-digit or 1000-digit precision,
and in many cases mpmath implements asymptotically fast algorithms that scale
well for extremely high precision work. If available, mpmath will (optionally)
use gmpy to speed up high precision operations. 

%package	doc
Group:		Development/Other
Summary:	Documentation for python-%{name}

%description	doc
Documentation for python-%{name}.

%prep
%setup -q -n %{module}-%{version}

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot} --record=FILELIST

pushd doc
    %__python build.py
    mkdir -p %{buildroot}/%{_docdir}/%{module}
    cp -far build/* %{buildroot}/%{_docdir}/%{module}
popd

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%py_puresitedir/*

%files		doc
%defattr(-,root,root)
%dir %{_docdir}/%{module}
%{_docdir}/%{module}/*
