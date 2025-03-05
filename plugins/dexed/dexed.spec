%global debug_package %{nil}

# relative directory where the build results is placed
%global builddest redhat-linux-build/Source/Dexed_artefacts

Name:           dexed
Version:        0.9.8
Release:        5%{?dist}
Summary:        Standalone version of Dexed a synth that is closely modeled on the Yamaha DX7

License:        GPLv3
URL:            https://github.com/asb2m10/dexed

# The source for this package was pulled from upstream's vcs.
# chech here : https://github.com/timlau/spec_files/tree/master/dexed
# for a Makefile that can be used to create the source tarball

Source0:        %{name}-%{version}.tar.gz
Patch0:         0001-use-prebuild-juce.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pipewire-jack-audio-connection-kit-devel
BuildRequires:  pkgconfig(alsa) 
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(x11) 
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
BuildRequires:  pkgconfig(gtk+-x11-3.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  cmake(JUCE)

%description
Dexed is a multi platform, multi format plugin synth that is closely modeled on the Yamaha DX7.
Dexed is also a midi cartridge librarian/manager for the DX7.
This package contains the standalone version of Dexed.

%package clap
Summary:	CLAP plugin of Dexed a synth that is closely modeled on the Yamaha DX7

%description clap
Dexed is a multi platform, multi format plugin synth that is closely modeled on the Yamaha DX7.
Dexed is also a midi cartridge librarian/manager for the DX7.
This package contains Dexed as a CLAP plugin.

%package vst3
Summary:	VST3 plugin of Dexed a synth that is closely modeled on the Yamaha DX7

%description vst3
Dexed is a multi platform, multi format plugin synth that is closely modeled on the Yamaha DX7.
Dexed is also a midi cartridge librarian/manager for the DX7.
This package contains Dexed as a VST3 plugin.

%package lv2
Summary:	LV2 plugin of Dexed a synth that is closely modeled on the Yamaha DX7

%description lv2
Dexed is a multi platform, multi format plugin synth that is closely modeled on the Yamaha DX7.
Dexed is also a midi cartridge librarian/manager for the DX7.
This package contains Dexed as a LV2 plugin.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files clap
%doc README.md
%license LICENSE
%{_libdir}/clap/Dexed.clap

%files vst3
%doc README.md
%license LICENSE
%{_libdir}/vst3/Dexed.vst3/*

%files lv2
%doc README.md
%license LICENSE
%{_libdir}/lv2/Dexed.lv2/*

%files
%doc README.md
%license LICENSE
%{_bindir}/Dexed

%changelog
* Wed Mar 05 2025 Tim Lauridsen <tla@rasmil.dk> - 0.9.8-5
- Added LV2 subpackage
- do install code in Cmake
- Add readme & license to sub packages
- Build against pipewire jack
* Fri Feb 21 2025 Tim Lauridsen <tla@rasmil.dk> - 0.9.8-4
- Build with pre-build JUCE
* Fri Feb 21 2025 Tim Lauridsen <tla@rasmil.dk> - 0.9.8-3
- use pkgconfig(jack) as buildrequire
* Thu Feb 20 2025 Tim Lauridsen <tla@rasmil.dk> - 0.9.8-2
- package released version not the git version
* Wed Feb 19 2025 Tim Lauridsen <tla@rasmil.dk> - 0.9.8-1.gite087754
- Initial package
