%global debug_package %{nil}
%global gitdate .git20250222.a74ffd3
%global builddest  redhat-linux-build/{{ name }}_artefacts
%global buildname {{ name }}

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

# Basic build requirements for a JUCE based plugin
BuildRequires:  cmake
BuildRequires:  git
BuildRequires:  gcc-c++
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

%build
%cmake 
%cmake_build

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
