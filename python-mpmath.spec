%define module	mpmath

Summary:	Python library for symbolic mathematics
Name:		python-%{module}
Version:	0.19
Release:	1
License:	BSD and MIT
Group:		Development/Python
Url:		http://mpmath.org/
Source0:	https://github.com/fredrik-johansson/%{module}/archive/%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	pkgconfig(python)
BuildRequires:	pythonegg(sphinx)

Suggests:	python-gmpy >= 1.03, python-numpy, python-matplotlib

%description
Mpmath is a pure-Python library for multiprecision floating-point arithmetic.
It provides an extensive set of transcendental functions, unlimited exponent
sizes, complex numbers, interval arithmetic, numerical integration and
differentiation, root-finding, linear algebra, and much more. Almost any
calculation can be performed just as well at 10-digit or 1000-digit precision,
and in many cases mpmath implements asymptotically fast algorithms that scale
well for extremely high precision work. If available, mpmath will (optionally)
use gmpy to speed up high precision operations. 

%files -f FILELIST
%doc CHANGES LICENSE README
%doc demo/

#----------------------------------------------------------------------------

%package doc
Group:		Development/Python
Summary:	Documentation for python-%{module}

%description doc
Documentation for python-%{module}.

%files doc
%{_docdir}/%{module}/

#----------------------------------------------------------------------------

%prep
%setup -q -n %{module}-%{version}

%build
# build doc
pushd doc
%{__python} build.py
popd

%install
%{__python} setup.py install --root=%{buildroot} --record=FILELIST

# remove *.pyc files from FILELIST
sed -i '/\\*.pyc$/d' FILELIST

# install doc
rm -rf doc/build/.buildinfo doc/build/.doctrees
install -dm 0755 %{buildroot}/%{_docdir}/%{module}/
cp -far build/* %{buildroot}/%{_docdir}/%{module}/

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

