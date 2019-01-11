%define module	mpmath

Summary:	Python library for symbolic mathematics
Name:		python-%{module}
Version:	1.1.0
Release:	1
Source0:	https://pypi.io/packages/source/m/mpmath/mpmath-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://mpmath.org
BuildArch:	noarch
Suggests:	python-gmpy >= 1.03, python-numpy, python-matplotlib
BuildRequires:	python
BuildRequires:	python-setuptools
BuildRequires:	python2
BuildRequires:	python2-setuptools
BuildRequires:  python-sphinx

%description
Mpmath is a pure-Python library for multiprecision floating-point arithmetic.
It provides an extensive set of transcendental functions, unlimited exponent
sizes, complex numbers, interval arithmetic, numerical integration and
differentiation, root-finding, linear algebra, and much more. Almost any
calculation can be performed just as well at 10-digit or 1000-digit precision,
and in many cases mpmath implements asymptotically fast algorithms that scale
well for extremely high precision work. If available, mpmath will (optionally)
use gmpy to speed up high precision operations. 

%package -n python2-%module
Suggests:	python2-gmpy >= 1.03, python2-numpy, python2-matplotlib

%prep
%setup -qn %{module}-%{version}
cp -a . %py2dir

%install
PYTHONDONTWRITEBYTECODE= %__%py_install 

pushd %py2dir
PYTHONDONTWRITEBYTECODE= python2 setup.py install --root=%{buildroot}

%files
%doc CHANGES LICENSE
%{py_puresitedir}/*

%files -n python2-%module
%doc CHANGES LICENSE
%py2_puresitedir/*
