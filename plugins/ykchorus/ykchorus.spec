%global debug_package %{nil}
%global gitdate .git20250301.ee0e362
%global builddest bin

Name:           ykchorus
Version:        0.2.4
Release:        2%{?gitdate}%{?dist}
Summary:        A chorus effect

License:        GPLv2
URL:            https://github.com/SpotlightKid/ykchorus
# The source for this package was pulled from upstream's vcs.
# check here : https://github.com/timlau/spec_files/tree/master/plpugins/
# for a Makefile that can be used to create the source tarball
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  patch
BuildRequires:  pipewire-jack-audio-connection-kit-devel
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(x11) 
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrender)


%description
A chorus effect inspired by the one found in certain well-known Japanese vintage analog synthesizers

%package clap
Summary: CLAP plugin of %{name}

%description clap
%{description}
This package contains AIDA-X as a CLAP plugin.

%package vst3
Summary: VST3 plugin of ½´%{name}

%description vst3
%{description}
This package contains AIDA-X as a VST3 plugin.

%package lv2
Summary: LV2 plugin of %{name}

%description lv2
%{description}
This package contains %{name} as a LV2 plugin.

%prep
%autosetup
ln -s -r --force dpf/dgl/src/pugl.cpp dpf/dgl/src/pugl.mm

%build
%make_build BUILD_VST2=false BUILD_LADSPA=false

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir} BUILD_VST2=false BUILD_LADSPA=false

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
%{_bindir}/%{name}

%changelog
* Mon Mar 3 2025 Tim Lauridsen <tla@rasmil.dk> - 0.2.4-2
- don't build VST2 & LADSPA
* Sat Mar 1 2025 Tim Lauridsen <tla@rasmil.dk> - 0.2.4-1
- Initial package
