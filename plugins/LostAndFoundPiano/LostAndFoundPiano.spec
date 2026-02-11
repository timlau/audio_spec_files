%global debug_package %{nil}
%global gitdate git20260131.d85adc3
%global builddest  redhat-linux-build/LostAndFoundPiano_artefacts
%global buildname LostAndFoundPiano

Name:           LostAndFoundPiano
Version:        1.0.0
Release:        %autorelease -s %{?gitdate}
Summary:        A virtual instrument of the classic mda Piano and mda EPiano.

License:        GPLv3+
URL:            https://github.com/timlau/lost-and-found-piano

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
Lost N' Found Piano, a virtual instrument plug-in that
combines updated versions of the classic mda Piano and mda EPiano VSTs
and gives them a new coat of paint.

%package clap
Summary: CLAP plugin of %{name}

%description clap
%{description}
This package contains %{name} as a CLAP plugin.

%package vst3
Summary: VST3 plugin of ½´%{name}

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
# install -d -m 755 %{buildroot}%{_bindir}
# install -d -m 755 %{buildroot}%{_libdir}/vst3
# install -d -m 755 %{buildroot}%{_libdir}/lv2
# install -d -m 755 %{buildroot}%{_libdir}/clap
# cp -R %{builddest}/VST3/%{buildname}.vst3 %{buildroot}%{_libdir}/vst3/
# cp -R %{builddest}/LV2/%{buildname}.lv2 %{buildroot}%{_libdir}/lv2/
# install %{builddest}/CLAP/%{buildname}.clap %{buildroot}%{_libdir}/clap/
# install %{builddest}/Standalone/%{buildname} %{buildroot}%{_bindir}
%cmake_install

%files clap
%license LICENSE.txt
%doc README.md
%{_libdir}/clap/*.clap

%files vst3
%license LICENSE.txt
%doc README.md
%{_libdir}/vst3/*.vst3/*

%files lv2
%license LICENSE.txt
%doc README.md
%{_libdir}/lv2/*.lv2/*

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/*


%changelog
%autochangelog
