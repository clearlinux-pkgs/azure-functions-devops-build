#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : azure-functions-devops-build
Version  : 0.0.22
Release  : 2
URL      : https://files.pythonhosted.org/packages/d5/96/59ca26c8d9985df8a092cf5974e54b6c3e11208833ea1c0163d7fb763c94/azure-functions-devops-build-0.0.22.tar.gz
Source0  : https://files.pythonhosted.org/packages/d5/96/59ca26c8d9985df8a092cf5974e54b6c3e11208833ea1c0163d7fb763c94/azure-functions-devops-build-0.0.22.tar.gz
Summary  : Python package for integrating Azure Functions with Azure DevOps. Specifically made for the Azure CLI
Group    : Development/Tools
License  : MIT
Requires: azure-functions-devops-build-license = %{version}-%{release}
Requires: azure-functions-devops-build-python = %{version}-%{release}
Requires: azure-functions-devops-build-python3 = %{version}-%{release}
Requires: Jinja2
Requires: msrest
BuildRequires : Jinja2
BuildRequires : buildreq-distutils3
BuildRequires : msrest

%description
# Azure Devops Build Manager For Azure Functions
> :construction: The project is currently **work in progress**. Please **do not use in production** as we expect developments over time. :construction:

%package license
Summary: license components for the azure-functions-devops-build package.
Group: Default

%description license
license components for the azure-functions-devops-build package.


%package python
Summary: python components for the azure-functions-devops-build package.
Group: Default
Requires: azure-functions-devops-build-python3 = %{version}-%{release}

%description python
python components for the azure-functions-devops-build package.


%package python3
Summary: python3 components for the azure-functions-devops-build package.
Group: Default
Requires: python3-core
Provides: pypi(azure_functions_devops_build)
Requires: pypi(jinja2)
Requires: pypi(msrest)
Requires: pypi(vsts)

%description python3
python3 components for the azure-functions-devops-build package.


%prep
%setup -q -n azure-functions-devops-build-0.0.22
cd %{_builddir}/azure-functions-devops-build-0.0.22

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588635886
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/azure-functions-devops-build
cp %{_builddir}/azure-functions-devops-build-0.0.22/LICENSE %{buildroot}/usr/share/package-licenses/azure-functions-devops-build/03e1fe6fd0bc6d73c3cd3370d5f0a73c4fcb60d6
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/azure-functions-devops-build/03e1fe6fd0bc6d73c3cd3370d5f0a73c4fcb60d6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
