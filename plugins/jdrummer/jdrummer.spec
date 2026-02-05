%global debug_package %{nil}
%global gitdate .git20260205.221da0c
%global builddest  redhat-linux-build/jdrummer_artefacts/Release
%global buildname jdrummer

Name:           jdrummer
Version:        1.0.0
Release:        %autorelease%{?gitdate}%{?dist}
Summary:        Soundfont-based drum kit, comprehensive groove library, composition tool, and intelligent Groove Matcher

License:        GPLv3+
URL:            https://github.com/timlau/jdrummer

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
BuildRequires:  cmake(juce) = 8.0.11



%description
JDrummer features Soundfont-based drum kits, a comprehensive groove library with tempo-synced playback,
a composition tool, and an intelligent Groove Matcher that analyzes audio to find matching drum patterns.

%package clap
Summary: CLAP plugin of %{name}

%description clap
JDrummer features Soundfont-based drum kits, a comprehensive groove library with tempo-synced playback,
a composition tool, and an intelligent Groove Matcher that analyzes audio to find matching drum patterns.
This package contains %{name} as a CLAP plugin.

%package vst3
Summary: VST3 plugin of %{name}

%description vst3
JDrummer features Soundfont-based drum kits, a comprehensive groove library with tempo-synced playback,
a composition tool, and an intelligent Groove Matcher that analyzes audio to find matching drum patterns.
This package contains %{name} as a VST3 plugin.

%package lv2
Summary: LV2 plugin of %{name}

%description lv2
JDrummer features Soundfont-based drum kits, a comprehensive groove library with tempo-synced playback,
a composition tool, and an intelligent Groove Matcher that analyzes audio to find matching drum patterns.
This package contains %{name} as a LV2 plugin.

%package data
Summary: Soundfonts and Groves for %{name}

%description data
JDrummer features Soundfont-based drum kits, a comprehensive groove library with tempo-synced playback,
a composition tool, and an intelligent Groove Matcher that analyzes audio to find matching drum patterns.
Soundfonts and Groves for %{name}

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
