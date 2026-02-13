%global debug_package %{nil}
%global gitdate git20250222.a74ffd3
%global builddest  redhat-linux-build/{{ name }}_artefacts/Release
%global buildname {{ name }}

Name:           {{ name }}
Version:        {{ version }}
Release:        %autorelease -s %{?gitdate}
Summary:        # TODO: Insert summary here

License:        GPL-3.0-or-later
URL:            https://github.com/{{ github_owner }}/{{ github_project }}

# The source for this package was pulled from upstream's vcs.
# check here : https://github.com/timlau/audio_spec_files/
# for a Makefile that can be used to create the source tarball
Source0:        %{name}-%{version}.tar.gz
# >>>>>>>>> TODO: REMOVE THIS is there is custom CMakeUuserPresets.json
# add a second source with a custom CMakeUuserPresets.json
Source1:        cmake_preset.tar.gz
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

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

# TODO: If a -data is used then comment out this weak or hard requirement
# Recommends: %{name}-data%{?_isa} = %{version}-%{release}
# Requires: %{name}-data%{?_isa} = %{version}-%{release}



%description
# TODO: Insert description here

%package clap
Summary: CLAP plugin of %{name}
# TODO: If a -data is used then comment out this weak or hard requirement
# Recommends: %{name}-data%{?_isa} = %{version}-%{release}
# Requires: %{name}-data%{?_isa} = %{version}-%{release}

%description clap
This package contains %{name} as a CLAP plugin.

%package vst3
Summary: VST3 plugin of %{name}
# TODO: If a -data is used then comment out this weak or hard requirement
# Recommends: %{name}-data%{?_isa} = %{version}-%{release}
# Requires: %{name}-data%{?_isa} = %{version}-%{release}

%description vst3
This package contains %{name} as a VST3 plugin.

%package lv2
Summary: LV2 plugin of %{name}
# TODO: If a -data is used then comment out this weak or hard requirement
# Recommends: %{name}-data%{?_isa} = %{version}-%{release}
# Requires: %{name}-data%{?_isa} = %{version}-%{release}

%description lv2
This package contains %{name} as a LV2 plugin.
# TODO: If a -data is used then comment out this weak or hard requirement
# Recommends: %{name}-data%{?_isa} = %{version}-%{release}
# Requires: %{name}-data%{?_isa} = %{version}-%{release}

# >>>>>>>>> TODO: Uncomment this if a data package is needed
# %package data
# Summary: Data files for %{name}

# %description data
# Datafiles for %{name}
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

%prep
%autosetup
# >>>>>>>>> TODO: REMOVE THIS is there is custom CMakeUuserPresets.json
# unpack the custom CMakeUuserPresets.json in same directory as the primary source
%setup -T -D -a 1
# <<<<<<<<<

%build
%cmake --preset rpmbuild
%cmake_build --preset rpmbuild

%install
# Manual install of plugins into buildroot
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

# >>>>>>>>> TODO: Uncomment this if a data package is needed
# %files data
# %license LICENSE
# %doc README.md
# %{_datadir}/%{name}/
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

%changelog
%autochangelog
