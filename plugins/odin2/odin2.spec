%global debug_package %{nil}
%global gitdate .git20250302.c8d3861f
%global builddest redhat-linux-build/Odin2_artefacts/Release/
%global buildname Odin2


Name:           odin2
Version:        2.3.4
Release:        1%{?gitdate}%{?dist}
Summary:        Odin 2 is a 24-voice polyphonic powerhouse

License:        GPLv3+
URL:            https://github.com/TheWaveWarden/odin2

# The source for this package was pulled from upstream's vcs.
# check here : https://github.com/timlau/spec_files/tree/master/plpugins/
# for a Makefile that can be used to create the source tarball
Source0:        %{name}-%{version}.tar.gz
Patch0:         0001-use-prebuild-juce.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pipewire-jack-audio-connection-kit-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  cmake(JUCE)


%description
Odin 2 is a 24-voice polyphonic powerhouse that will transport you from your studio straight to Valhalla.
Whether you're after earth-shattering basses, soaring leads, or otherworldly FX, Odin 2 delivers it all.
Harness the classic warmth of analog waveforms — or draw custom ones. 
High-quality emulations of legendary analog filters, like the Moog Ladder, the Korg 35 and many more let you shape your sound. 
Finish it off with five onboard FX or dive into endless modulation possibilities. 
There’s a whole world to explore in Odin 2.

# %package clap
# Summary: CLAP plugin of %{name}

# %description clap
# %{description}
# This package contains AIDA-X as a CLAP plugin.

%package vst3
Summary: VST3 plugin of ½´%{name}

%description vst3
%{description}
This package contains AIDA-X as a VST3 plugin.

%package lv2
Summary: LV2 plugin of %{name}

%description lv2
%{description}
This package contains %{name} as a LV2 plugin.

%prep
%autosetup -p1

%build
%cmake -D CMAKE_BUILD_TYPE=Release
%cmake_build --config Release -j1

%install
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_libdir}/vst3
install -d -m 755 %{buildroot}%{_libdir}/lv2
cp -R %{builddest}/VST3/%{buildname}.vst3 %{buildroot}%{_libdir}/vst3/ 
cp -R %{builddest}/LV2/%{buildname}.lv2 %{buildroot}%{_libdir}/lv2/ 
install %{builddest}/Standalone/%{buildname} %{buildroot}%{_bindir}/

# %files clap
# %license LICENSE
# %doc README.md
# %{_libdir}/clap/*.clap

%files vst3
%license LICENSE
%doc README.md
%{_libdir}/vst3/*.vst3/*

%files lv2
%license LICENSE
%doc README.md
%{_libdir}/lv2/*.lv2/*

%files 
%license LICENSE
%doc README.md
%{_bindir}/*


%changelog
* Sun Mar 02 2025 Tim Lauridsen <tla@rasmil.dk> - 2.3.4-1
- Initial package