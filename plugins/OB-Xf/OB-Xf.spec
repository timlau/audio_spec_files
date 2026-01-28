%global debug_package %{nil}
<<<<<<< HEAD
%global gitdate .git20260128.9cc6a05
=======
%global gitdate .git20260127.721f084
>>>>>>> 1df7e1d (+ rebuilds)
%global builddest redhat-linux-build/obxf_products
%global buildname OB-Xf

Name:           OB-Xf
Version:        0.9.27
Release:        1%{?gitdate}%{?dist}
Summary:        OB-Xf is a Synth based on the legendary Oberheim OB-X. 

License:        GPLv3+
URL:            https://github.com/surge-synthesizer/OB-Xf

# The source for this package was pulled from upstream's vcs.
# check here : https://github.com/timlau/spec_files/tree/master/plpugins/
# for a Makefile that can be used to create the source tarball
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  git
BuildRequires:  gcc-c++
BuildRequires:  pipewire-jack-audio-connection-kit-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
BuildRequires:  pkgconfig(gtk+-x11-3.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  cmake(fmt) 
BuildRequires:  cmake(JUCE) = 8.0.11 

Requires: %{name}-data%{?_isa} = %{version}-%{release}

%description
OB-Xf is a Synth based on the legendary Oberheim OB-X. 
OB-Xf is a continuation of the last open source version of OB-Xd by 2DaT and later discoDSP,
bringing together several efforts going on in the audio space and combining them inside the Surge Synth Team infrastructure.
The synth is currently in a beta phase, with a few features still under development, but the plugin is feature stable and working rather well,
we believe.

%package clap
Summary: CLAP plugin of %{name}
Requires: %{name}-data%{?_isa} = %{version}-%{release}

%description clap
%{description}
This package contains %{name} as a CLAP plugin.

%package vst3
Summary: VST3 plugin of ½´%{name}
Requires: %{name}-data%{?_isa} = %{version}-%{release}

%description vst3
%{description}
This package contains %{name} as a VST3 plugin.

%package lv2
Summary: LV2 plugin of %{name}
Requires: %{name}-data%{?_isa} = %{version}-%{release}

%description lv2
%{description}
This package contains %{name} as a LV2 plugin.

%package data
Summary: patches and themes for %{name}

%description data
%{description}
This package patches and themes for %{name} 

%prep
%autosetup

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DCPM_USE_LOCAL_PACKAGES=ON
%cmake_build --config Release --target obxf-staged

%install
# install plugins and standalone
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_libdir}/vst3
install -d -m 755 %{buildroot}%{_libdir}/lv2
install -d -m 755 %{buildroot}%{_libdir}/clap
cp -R %{builddest}/%{buildname}.vst3 %{buildroot}%{_libdir}/vst3/ 
cp -R %{builddest}/%{buildname}.lv2 %{buildroot}%{_libdir}/lv2/ 
install %{builddest}/%{buildname}.clap %{buildroot}%{_libdir}/clap/
install %{builddest}/%{buildname} %{buildroot}%{_bindir}
# install themes and patches
%cmake_install

%files clap
%license LICENSE
%doc README.md
%{_libdir}/clap/*.clap

%files vst3
%license LICENSE
%doc README.md
%{_libdir}/vst3/*.vst3/*

%files lv2
%license LICENSE
%doc README.md
%{_libdir}/lv2/*.lv2/*

%files data
%license LICENSE
%doc README.md
%{_datadir}/*/OB-Xf/


%files 
%license LICENSE
%doc README.md
%{_bindir}/*


%changelog
* Tue Jan 27 2026 Tim Lauridsen <tla@rasmil.dk> - 0.9.27-1
- Initial package
