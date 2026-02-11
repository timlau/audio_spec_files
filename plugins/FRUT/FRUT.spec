%global debug_package %{nil}
%global gitdate git20250222.a74ffd3
%global builddest  redhat-linux-build/FRUT_artefacts/Release
%global buildname FRUT

Name:           FRUT
Version:        0.1.0
Release:        %autorelease -s %{?gitdate}
Summary:        Tool to convert Juce projucer projects in Cmake

License:        GPLv3+
URL:            https://github.com/timlau/FRUT

# The source for this package was pulled from upstream's vcs.
# check here : https://github.com/timlau/audio_spec_files/
# for a Makefile that can be used to create the source tarball
Source0:        %{name}-%{version}.tar.gz

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
# BuildRequires:  cmake(juce) = 8.0.11

%description
%{name} is a tool to convert Juce projucer projects in Cmake.
This package only contains the Juce2Cmake tool, not the reproducer CMake files.

%prep
%autosetup

%build
%cmake -G Ninja -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_BINDIR=%{buildroot}%{_bindir}
%cmake_build --target Jucer2CMake

%install
%cmake_build --target Jucer2CMake/install
#Nothing to do here, the cmake install step will put the binary in the right place

%files
%license LICENSE
%doc README.rst
%{_bindir}/*

%changelog
%autochangelog
