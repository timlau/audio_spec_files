%global debug_package %{nil}
%global gitdate .git20260127.a74ffd3
%global builddest bin

Name:           dragonfly-reverb

Version:        3.2.10
Release:        1%{?gitdate}%{?dist}
Summary:        A set of free reverb effects for audio

License:        GPLv3
URL:            https://github.com/michaelwillis/dragonfly-reverb

# The source for this package was pulled from upstream's vcs.
# check here : https://github.com/timlau/spec_files/tree/master/drangonfly-reverb
# for a Makefile that can be used to create the source tarball
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pipewire-jack-audio-connection-kit-devel
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(x11) 
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrender)


%description
Dragonfly Reverb is a bundle of free audio effects for Linux, MacOS, and Windows. The reverb algorithms are based on the original Freeverb. The DR-1 algorithm is based on the Schroeder/Moorer reverb. The DR-2 algorithm is based on the original Freeverb algorithm. The DR-3 algorithm is a unique reverb algorithm developed by Michael Willis.

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
# fix symlinks
ln -s -r --force common/AbstractUI.* plugins/dragonfly-plate-reverb/
ln -s -r --force common/AbstractUI.* plugins/dragonfly-hall-reverb/
ln -s -r --force common/AbstractUI.* plugins/dragonfly-room-reverb/
ln -s -r --force common/AbstractUI.* plugins/dragonfly-early-reflections/
ln -s -r --force dpf/dgl/src/pugl.cpp dpf/dgl/src/pugl.mm

%build
%make_build

%install
# put the vst3 and clap files in the correct location
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_libdir}/vst3
install -d -m 755 %{buildroot}%{_libdir}/clap
install -d -m 755 %{buildroot}%{_libdir}/lv2
cp -R %{builddest}/Dragonfly*.vst3 %{buildroot}%{_libdir}/vst3/ 
cp -R %{builddest}/Dragonfly*.lv2 %{buildroot}%{_libdir}/lv2/ 
install %{builddest}/Dragonfly*.clap %{buildroot}%{_libdir}/clap/
install %{builddest}/DragonflyHallReverb %{buildroot}%{_bindir}/
install %{builddest}/DragonflyPlateReverb %{buildroot}%{_bindir}/
install %{builddest}/DragonflyRoomReverb %{buildroot}%{_bindir}/
install %{builddest}/DragonflyEarlyReflections %{buildroot}%{_bindir}/

%files clap
%license LICENSE
%doc README.md
%{_libdir}/clap/Dragonfly*.clap

%files vst3
%license LICENSE
%doc README.md
%{_libdir}/vst3/Dragonfly*.vst3/*

%files lv2
%license LICENSE
%doc README.md
%{_libdir}/lv2/Dragonfly*.lv2/*

%files 
%license LICENSE
%doc README.md
%{_bindir}/DragonflyHallReverb
%{_bindir}/DragonflyPlateReverb
%{_bindir}/DragonflyRoomReverb
%{_bindir}/DragonflyEarlyReflections


%changelog
* Sat Feb 22 2025 Tim Lauridsen <tla@rasmil.dk> - 3.2.10-1
- version 3.2.10
- Initial package
