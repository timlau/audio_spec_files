%global debug_package %{nil}
%global gitdate git20260211.5e0be2e

Name:           sfizz
Version:        1.2.3
Release:        %autorelease -s %{?gitdate}
Summary:        Sampler plugin and library for SFZ instruments

License:        BSD-2-Clause
URL:            https://github.com/sfztools/sfizz-ui

# The source for this package was pulled from upstream's vcs.
# chech here : https://github.com/timlau/spec_files/tree/master/sfizz
# for a Makefile that can be used to create the source tarball

Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(pangocairo)


%description
Sfizz is a musical sampler, available as LV2 and VST plugins for musicians,
and a library for developers.

%package vst3
Summary:   Sfizz VST3 plugin

%description vst3
Sfizz VST3 Plugins

%package lv2
Summary:   sfizz LV2 plugin

%description lv2
Sfizz LV2 Plugins

%package pd
Summary:   Sfizz puredata (pd) plugin

%description pd
Sfizz puredata (pd) plugin

%prep
%setup

%build
%cmake -DPLUGIN_PUREDATA=ON -DSFIZZ_SHARED=OFF -DSFIZZ_JACK=OFF -DSFIZZ_RENDER=OFF -DENABLE_LTO=OFF -DLV2_PLUGIN_INSTALL_DIR=%{_libdir}/lv2 -DVST3_PLUGIN_INSTALL_DIR=%{_libdir}/vst3 -DPD_PLUGIN_INSTALL_DIR=%{_libdir}/pd/extra -DBUILD_SHARED_LIBS=OFF -DCMAKE_CXX_STANDARD=17 .
%cmake_build

%install
%cmake_install

%files vst3
%doc README.md
%license LICENSE
%dir %{_libdir}/vst3/sfizz.vst3
%{_libdir}/vst3/sfizz.vst3/*

%files lv2
%doc README.md
%license LICENSE
%dir %{_libdir}/lv2/sfizz.lv2
%{_libdir}/lv2/sfizz.lv2/*

%files pd
%doc README.md
%license LICENSE
%dir %{_libdir}/pd/extra/sfizz
%{_libdir}/pd/extra/sfizz/*

%changelog
%autochangelog
