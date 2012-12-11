%define module	mpmath

Summary:	Python library for symbolic mathematics
Name:		python-%{module}
Version:	0.17
Release:	2
Source0:	http://mpmath.googlecode.com/files/%{module}-all-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://mpmath.googlecode.com/
BuildArch:	noarch
Suggests:	python-gmpy >= 1.03, python-numpy, python-matplotlib
BuildRequires:	python
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

%package	doc
Group:		Development/Python
Summary:	Documentation for python-%{name}

%description	doc
Documentation for python-%{name}.

%prep
%setup -q -n %{module}-all-%{version}

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} 

pushd doc
%__python build.py
%__rm -rf build/.buildinfo build/.doctrees
mkdir -p %{buildroot}/%{_docdir}/%{module}
cp -far build/* %{buildroot}/%{_docdir}/%{module}
popd

%files
%doc CHANGES LICENSE README
%py_puresitedir/*

%files doc
%defattr(-,root,root)
%{_docdir}/%{module}/



%changelog
* Wed Feb 02 2011 Lev Givon <lev@mandriva.org> 0.17-1mdv2011.0
+ Revision: 634920
- Update to 0.17.

* Tue Nov 09 2010 Lev Givon <lev@mandriva.org> 0.16-1mdv2011.0
+ Revision: 595135
- Update to 0.16.

* Mon Nov 08 2010 Funda Wang <fwang@mandriva.org> 0.14-2mdv2011.0
+ Revision: 594960
- update file list
- rebuild for py 2.7

* Sat Feb 06 2010 Frederik Himpe <fhimpe@mandriva.org> 0.14-1mdv2010.1
+ Revision: 501447
- update to new version 0.14

* Fri Sep 18 2009 Paulo Andrade <pcpa@mandriva.com.br> 0.13-1mdv2010.0
+ Revision: 444223
- Initial import of python-mpmath 0.13.
- python-mpmath

