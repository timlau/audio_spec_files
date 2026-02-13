%global debug_package %{nil}
%global toolchain clang
%global gitdate git20250222.a74ffd3
%global builddest  redhat-linux-build/ZLSplitter_artefacts/Release
%global buildname "ZL Splitter"

Name:           ZLSplitter
Version:        0.2.1
Release:        %autorelease -s %{?gitdate}
Summary:        ZLSplitter is a equalizer plugin.

License:        AGPL-3.0-or-later
URL:            https://github.com/ZL-Audio/ZLSplitter

# The source for this package was pulled from upstream's vcs.
# check here : https://github.com/timlau/audio_spec_files/
# for a Makefile that can be used to create the source tarball
Source0:        %{name}-%{version}.tar.gz
# add a second source with a custom CMakeUuserPresets.json
Source1:        cmake_preset.tar.gz

# Basic build requirements for a JUCE based plugin
BuildRequires:  cmake
BuildRequires:  git
BuildRequires:  clang
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
ZL Splitter is a splitter plugin.

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
install -d -m 755 %{buildroot}%{_libdir}/vst3
install -d -m 755 %{buildroot}%{_libdir}/lv2
cp -R %{builddest}/VST3/%{buildname}.vst3 %{buildroot}%{_libdir}/vst3/
cp -R %{builddest}/LV2/%{buildname}.lv2 %{buildroot}%{_libdir}/lv2/

%files vst3
%license LICENSE.md
%doc README.md
%{_libdir}/vst3/*.vst3/*

%files lv2
%license LICENSE.md
%doc README.md
%{_libdir}/lv2/*.lv2/*

%changelog
%autochangelog
