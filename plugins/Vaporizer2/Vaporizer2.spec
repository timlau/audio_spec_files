%global debug_package %{nil}
%global gitdate git20260203.f0b1a21
%global builddest  redhat-linux-build/Vaporizer2_artefacts/Release
%global buildname Vaporizer2

Name:           Vaporizer2
Version:        3.5.0
Release:        %autorelease -s %{?gitdate}
Summary:        Vaporizer2 is a hybrid wavetable additive / subtractive synthesizer / sampler workstation.

License:        GPL-3.0 AND GPL-2.0
URL:            https://github.com/VASTDynamics/Vaporizer2

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
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  cmake(juce) = 8.0.11

Requires: %{name}-data%{?_isa} = %{version}-%{release}

%description
Vaporizer2 is a hybrid wavetable additive / subtractive synthesizer / sampler workstation.
Vaporizer2 comes with a groundbreaking wavetable editor with a vast number of editing possibilities including
frequency shift, smooth, clean, bend and bloat for single-cycles, parts of single-cycles or even whole wavetables.
Featuring an easy-to use wavetable draw mode with smooth Bezier curves and snap to grid function.


%package clap
Summary: CLAP plugin of %{name}
Requires: %{name}-data%{?_isa} = %{version}-%{release}

%description clap
Vaporizer2 is a hybrid wavetable additive / subtractive synthesizer / sampler workstation.
Vaporizer2 comes with a groundbreaking wavetable editor with a vast number of editing possibilities including
frequency shift, smooth, clean, bend and bloat for single-cycles, parts of single-cycles or even whole wavetables.
Featuring an easy-to use wavetable draw mode with smooth Bezier curves and snap to grid function.
This package contains %{name} as a CLAP plugin.

%package vst3
Summary: VST3 plugin of %{name}
Requires: %{name}-data%{?_isa} = %{version}-%{release}

%description vst3
Vaporizer2 is a hybrid wavetable additive / subtractive synthesizer / sampler workstation.
Vaporizer2 comes with a groundbreaking wavetable editor with a vast number of editing possibilities including
frequency shift, smooth, clean, bend and bloat for single-cycles, parts of single-cycles or even whole wavetables.
Featuring an easy-to use wavetable draw mode with smooth Bezier curves and snap to grid function.
This package contains %{name} as a VST3 plugin.

%package lv2
Summary: LV2 plugin of %{name}
Requires: %{name}-data%{?_isa} = %{version}-%{release}

%description lv2
Vaporizer2 is a hybrid wavetable additive / subtractive synthesizer / sampler workstation.
Vaporizer2 comes with a groundbreaking wavetable editor with a vast number of editing possibilities including
frequency shift, smooth, clean, bend and bloat for single-cycles, parts of single-cycles or even whole wavetables.
Featuring an easy-to use wavetable draw mode with smooth Bezier curves and snap to grid function.
This package contains %{name} as a LV2 plugin.

%package data
Summary: patches for %{name}

%description data
Vaporizer2 is a hybrid wavetable additive / subtractive synthesizer / sampler workstation.
Vaporizer2 comes with a groundbreaking wavetable editor with a vast number of editing possibilities including
frequency shift, smooth, clean, bend and bloat for single-cycles, parts of single-cycles or even whole wavetables.
Featuring an easy-to use wavetable draw mode with smooth Bezier curves and snap to grid function.
This package contains patches for %{name}

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

%files
%license LICENSE
%doc README.md
%{_bindir}/*

%files data
%license LICENSE
%doc README.md
%{_datadir}/%{name}/

%changelog
%autochangelog
