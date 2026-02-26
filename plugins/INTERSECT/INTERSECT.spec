%global debug_package %{nil}
%global gitdate git20250222.a74ffd3
%global builddest  redhat-linux-build/INTERSECT_artefacts/Release
%global buildname Intersect

Name:           INTERSECT
Version:        0.8.13
Release:        %autorelease -s %{?gitdate}
Summary:        A nondestructive, time-stretching, and intersecting sample slicer.

License:        GPL-3.0-or-later AND MIT AND MPL-2.0
URL:            https://github.com/timlau/INTERSECT

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
A nondestructive, time-stretching, and intersecting sample slicer plugin with independent per-slice parameter control.
multiple time/pitch algorithms, and MIDI-triggered slice playback.

%package clap
Summary: CLAP plugin of %{name}

%description clap
A nondestructive, time-stretching, and intersecting sample slicer plugin with independent per-slice parameter control.
multiple time/pitch algorithms, and MIDI-triggered slice playback.
This package contains %{name} as a CLAP plugin.

%package vst3
Summary: VST3 plugin of %{name}

%description vst3
A nondestructive, time-stretching, and intersecting sample slicer plugin with independent per-slice parameter control.
multiple time/pitch algorithms, and MIDI-triggered slice playback.
This package contains %{name} as a VST3 plugin.

%package lv2
Summary: LV2 plugin of %{name}

%description lv2
A nondestructive, time-stretching, and intersecting sample slicer plugin with independent per-slice parameter control.
multiple time/pitch algorithms, and MIDI-triggered slice playback.
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

%files
%license LICENSE
%doc README.md
%{_bindir}/*

%changelog
%autochangelog
