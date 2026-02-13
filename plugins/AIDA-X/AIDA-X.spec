%global debug_package %{nil}
%global gitdate .git20260127.41eb988
%global builddest redhat-linux-build/bin

Name:           AIDA-X
Version:        1.1.0
Release:        1%{?gitdate}%{?dist}
Summary:        Amp Model Player leveraging

License:        GPL-3.0
URL:            https://github.com/AidaDSP/AIDA-X

# The source for this package was pulled from upstream's vcs.
# check here : https://github.com/timlau/spec_files/tree/master/AIDA-X
# for a Makefile that can be used to create the source tarball
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pipewire-jack-audio-connection-kit-devel
BuildRequires:  pkgconfig(gl)

%description
AIDA-X is an Amp Model Player, allowing it to load models of AI trained music gear, which you can then play through guitar
This package contains the standalone version of AIDA-X.

%package clap
Summary: CLAP plugin of AIDA-X

%description clap
AIDA-X is an Amp Model Player, allowing it to load models of AI trained music gear, which you can then play through guitar
This package contains AIDA-X as a CLAP plugin.

%package vst3
Summary: VST3 plugin of AIDA-X

%description vst3
AIDA-X is an Amp Model Player, allowing it to load models of AI trained music gear, which you can then play through guitar
This package contains AIDA-X as a VST3 plugin.

%package lv2
Summary: LV2 plugin of AIDA-X

%description lv2
AIDA-X is an Amp Model Player, allowing it to load models of AI trained music gear, which you can then play through guitar
This package contains AIDA-X as a LV2 plugin.

%prep
%autosetup -p1 -n %{name}-%{version}


%build
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build

%install
%cmake_install
# put the vst3 and clap files in the correct location
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_libdir}/vst3
install -d -m 755 %{buildroot}%{_libdir}/clap
install -d -m 755 %{buildroot}%{_libdir}/lv2
cp -R %{builddest}/%{name}.vst3 %{buildroot}%{_libdir}/vst3/
cp -R %{builddest}/%{name}.lv2 %{buildroot}%{_libdir}/lv2/
install %{builddest}/%{name}.clap %{buildroot}%{_libdir}/clap/
install %{builddest}/%{name} %{buildroot}%{_bindir}/

%files clap
%license LICENSE
%doc README.md
%{_libdir}/clap/%{name}.clap

%files vst3
%license LICENSE
%doc README.md
%{_libdir}/vst3/%{name}.vst3/*

%files lv2
%license LICENSE
%doc README.md
%{_libdir}/lv2/%{name}.lv2/*

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}


%changelog
* Fri Feb 21 2025 Tim Lauridsen <tla@rasmil.dk> - 1.1.0-1
- version 1.1.0
