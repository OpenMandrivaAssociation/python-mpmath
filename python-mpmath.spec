%define module	mpmath

Summary:	Python library for symbolic mathematics
Name:		python-%{module}
Version:	1.1.0
Release:	1
Source0:	http://mpmath.org/files/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://mpmath.org
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python-setuptools
BuildRequires:  python-sphinx

Recommends: python-gmpy
Recommends: python-numpy
Recommends: python-matplotlib

%description
Mpmath is a pure-Python library for multiprecision floating-point arithmetic.
It provides an extensive set of transcendental functions, unlimited exponent
sizes, complex numbers, interval arithmetic, numerical integration and
differentiation, root-finding, linear algebra, and much more. Almost any
calculation can be performed just as well at 10-digit or 1000-digit precision,
and in many cases mpmath implements asymptotically fast algorithms that scale
well for extremely high precision work. If available, mpmath will (optionally)
use gmpy to speed up high precision operations. 


%prep
%setup -qn %{module}-%{version}

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} 

%files
%doc CHANGES LICENSE
%py_puresitedir/*
