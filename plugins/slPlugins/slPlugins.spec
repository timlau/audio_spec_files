%global debug_package %{nil}
%global gitdate .git20260206.912f766
%global buildname slPlugins

Name:           slPlugins
Version:        1.1.0
Release:        %autorelease%{?gitdate}%{?dist}
Summary:        Various audio Plugins from SocaLabs.com
License:        GPLv3+
URL:            https://github.com/FigBug/slPlugins

# The source for this package was pulled from upstream's vcs.
# check here : https://github.com/timlau/audio_spec_files/
# for a Makefile that can be used to create the source tarball
Source0:        %{name}-%{version}.tar.gz
# add a second source with a custom CMakeUuserPresets.json
Source1:        cmake_preset.tar.gz

# Basic build requirements for a JUCE based plugin
BuildRequires:  cmake
BuildRequires:  git
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pipewire-jack-audio-connection-kit-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
BuildRequires:  pkgconfig(gtk+-x11-3.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  cmake(juce) = 8.0.12

%description
This package contains various audio plugins from SocaLabs.com. The following plugins are included:
- ABTester
- AddInvert
- ChannelMute
- CompensatedDelay
- Compressor
- Crossfeed
- Delay
- Expander
- Gate
- GraphicEQ
- HugeGain
- Limiter
- Maths
- MidiLooper
- Oscilloscope
- PitchTrack
- SFX8
- SampleDelay
- SimpleVerb
- SpectrumAnalyzer
- StereoEnhancer
- StereoProcessor
- ToneGenerator
- WaveLooper
- XYScope

%package clap
Summary: CLAP plugin of %{name}

%description clap
This package contains %{name} as a CLAP plugin.

%package vst3
Summary: VST3 plugin of %{name}

%description vst3
This package contains %{name} as a VST3 plugin.

%package lv2
Summary: LV2 plugin of %{name}

%description lv2
This package contains %{name} as a LV2 plugin.

%prep
%autosetup
# unpack the custom CMakeUuserPresets.json in same directory as the primary source
%setup -T -D -a 1

%build
%cmake --preset rpmbuild
%cmake_build --preset rpmbuild

%install
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

%changelog
%autochangelog
