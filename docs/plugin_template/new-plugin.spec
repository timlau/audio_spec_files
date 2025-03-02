%global debug_package %{nil}
%global gitdate .git20250222.a74ffd3
%global builddest bin

Name:           {{ name }}
Version:        {{ version }}
Release:        1%{?gitdate}%{?dist}
Summary:        

License:        GPLv3+
URL:            https://github.com/{{ github_owner }}/{{ github_project }}

# The source for this package was pulled from upstream's vcs.
# check here : https://github.com/timlau/spec_files/tree/master/plpugins/
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

%build
%cmake 
%cmake_build

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


%changelog
* {{ changelog_date }} Tim Lauridsen <tla@rasmil.dk> - {{ version }}-1
- Initial package