%global debug_package %{nil}
%global gitdate .git20260127.5a5865a

Name:           neural-amp-modeler
Version:        0.1.9
Release:        1%{?gitdate}%{?dist}
Summary:        LV2 plugin for using neural network machine learning amp models

License:        GPL-3.0
URL:            https://github.com/mikeoliphant/neural-amp-modeler-lv2

# The source for this package was pulled from upstream's vcs.
# check here : https://github.com/timlau/spec_files/tree/master/neural-amp-modeler
# for a Makefile that can be used to create the source tarball
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake


%description
LV2 plugin for using neural network machine learning amp models

%package lv2
Summary:        LV2 plugin for using neural network machine learning amp models

%description lv2
LV2 plugin for using neural network machine learning amp models

%prep
%autosetup -p1 -n %{name}-%{version}


%build
%cmake
%cmake_build

%install
%cmake_install

%files lv2
%license LICENCE.md
%doc README.md
%{_libdir}/lv2/neural_amp_modeler.lv2/*

%changelog
* Fri Feb 21 2025 Tim Lauridsen <tla@rasmil.dk> - 0.1.7-1
- version 0.1.7
