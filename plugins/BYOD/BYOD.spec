%global debug_package %{nil}
%global gitdate git20260201.1cf22b6
%global builddest redhat-linux-build/BYOD_artefacts/Release
%global buildname BYOD

Name:           BYOD
Version:        1.3.1
Release:        %autorelease -s %{?gitdate}
Summary:        BYOD is a guitar effects plugin with a customisable signal chain

License:        GPL-3.0-or-later
URL:            https://github.com/Chowdhury-DSP/BYOD

# The source for this package was pulled from upstream's vcs.
# check here : https://github.com/timlau/audio_spec_files/
# for a Makefile that can be used to create the source tarball
Source0:        %{name}-%{version}.tar.gz
# >>>>>>>>> REMOVE THIS is there is custom CMakeUuserPresets.json
# add a second source with a custom CMakeUuserPresets.json
Source1:        cmake_preset.tar.gz
# <<<<<<<<<

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



%description
BYOD is a guitar effects plugin with a customisable signal chain that allows users to create their own guitar distortion effects.
The plugin contains a wide variety of distortion effects from analog modelled circuits to purely digital creations,
along with some musical tone-shaping filters, and a handful of other useful signal processors.

%package clap
Summary: CLAP plugin of %{name}

%description clap
BYOD is a guitar effects plugin with a customisable signal chain that allows users to create their own guitar distortion effects.
The plugin contains a wide variety of distortion effects from analog modelled circuits to purely digital creations,
along with some musical tone-shaping filters, and a handful of other useful signal processors.
This package contains %{name} as a CLAP plugin.

%package vst3
Summary: VST3 plugin of ½´%{name}

%description vst3
BYOD is a guitar effects plugin with a customisable signal chain that allows users to create their own guitar distortion effects.
The plugin contains a wide variety of distortion effects from analog modelled circuits to purely digital creations,
along with some musical tone-shaping filters, and a handful of other useful signal processors.
This package contains %{name} as a VST3 plugin.

%package lv2
Summary: LV2 plugin of %{name}

%description lv2
BYOD is a guitar effects plugin with a customisable signal chain that allows users to create their own guitar distortion effects.
The plugin contains a wide variety of distortion effects from analog modelled circuits to purely digital creations,
along with some musical tone-shaping filters, and a handful of other useful signal processors.
This package contains %{name} as a LV2 plugin.

%prep
%autosetup
# >>>>>>>>> REMOVE THIS is there is custom CMakeUuserPresets.json
# unpack the custom CMakeUuserPresets.json in same directory as the primary source
%setup -T -D -a 1
# <<<<<<<<<

%build
%cmake --preset rpmbuild
%cmake_build --preset rpmbuild

%install
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_libdir}/vst3
install -d -m 755 %{buildroot}%{_libdir}/lv2
install -d -m 755 %{buildroot}%{_libdir}/clap
cp -R %{builddest}/VST3/%{buildname}.vst3 %{buildroot}%{_libdir}/vst3/
cp -R %{builddest}/LV2/%{buildname}.lv2 %{buildroot}%{_libdir}/lv2/
install %{builddest}/CLAP/%{buildname}.clap %{buildroot}%{_libdir}/clap/
install %{builddest}/Standalone/%{buildname} %{buildroot}%{_bindir}

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
