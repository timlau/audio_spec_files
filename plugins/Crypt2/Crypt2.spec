%global debug_package %{nil}
%global gitdate git20260208.fecd5ef
%global builddest  redhat-linux-build/Crypt2_artefacts
%global buildname Crypt2

Name:           Crypt2
Version:        2.1.0
Release:        %autorelease -s %{?gitdate}
Summary:        Crypt is a software synthesiser plugin designed for creating spacious cold hyper-unisoned synth sounds

License:        GPL-3.0
URL:            https://github.com/vitling/crypt

# The source for this package was pulled from upstream's vcs.
# check here : https://github.com/timlau/spec_files/tree/master/plpugins/
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
BuildRequires:  cmake(JUCE) = 8.0.12


%description
Crypt is a software synthesiser plugin designed for creating spacious cold hyper-unisoned synth sounds; developed by Vitling for the Bow Church project.

%package clap
Summary: CLAP plugin of %{name}

%description clap
%{description}
This package contains %{name} as a CLAP plugin.

%package vst3
Summary: VST3 plugin of %{name}

%description vst3
%{description}
This package contains %{name} as a VST3 plugin.

%package lv2
Summary: LV2 plugin of %{name}

%description lv2
%{description}
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
%license COPYING
%doc README.md
%{_libdir}/clap/*.clap

%files vst3
%license COPYING
%doc README.md
%{_libdir}/vst3/*.vst3/*

%files lv2
%license COPYING
%doc README.md
%{_libdir}/lv2/*.lv2/*

%files
%license COPYING
%doc README.md
%{_bindir}/*

%changelog
%autochangelog
