%global debug_package %{nil}
%global gitdate git20260129.c7bd6ae0
%global builddest redhat-linux-build/Odin2_artefacts/Release/
%global buildname Odin2

Name:           odin2
Version:        2.4.1
Release:        %autorelease -s %{?gitdate}
Summary:        Odin 2 is a 24-voice polyphonic powerhouse

License:        GPLv3+
URL:            https://github.com/TheWaveWarden/odin2

# The source for this package was pulled from upstream's vcs.
# check here : https://github.com/timlau/spec_files/tree/master/plpugins/
# for a Makefile that can be used to create the source tarball
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  git
BuildRequires:  pipewire-jack-audio-connection-kit-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  cmake(JUCE) = 8.0.11


%description
Odin 2 is a 24-voice polyphonic powerhouse that will transport you from your studio straight to Valhalla.
Whether you're after earth-shattering basses, soaring leads, or otherworldly FX, Odin 2 delivers it all.
Harness the classic warmth of analog waveforms — or draw custom ones.
High-quality emulations of legendary analog filters, like the Moog Ladder, the Korg 35 and many more let you shape your sound.
Finish it off with five onboard FX or dive into endless modulation possibilities.
There’s a whole world to explore in Odin 2.

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

%package clap
Summary: clap plugin of %{name}

%description clap
%{description}
This package contains %{name} as a clap plugin.

%prep
%autosetup -p1

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DODIN2_COPY_PLUGIN_AFTER_BUILD=FALSE  -DCPM_USE_LOCAL_PACKAGES=ON
%cmake_build --config Release

%install
%cmake_install

%files vst3
%license LICENSE
%doc README.md
%{_libdir}/vst3/%{buildname}.vst3/

%files lv2
%license LICENSE
%doc README.md
%{_libdir}/lv2/%{buildname}.lv2/

%files clap
%license LICENSE
%doc README.md
%{_libdir}/clap/%{buildname}.clap

%files
%license LICENSE
%doc README.md
%{_bindir}/%{buildname}

%changelog
%autochangelog
