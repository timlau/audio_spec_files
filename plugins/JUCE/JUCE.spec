%global debug_package %{nil}
%global builddest bin

Name:           JUCE
Version:        8.0.12
Release:        1%{?dist}
Summary:        JUCE is an open-source cross-platform C++ application framework

License:        GPLv3+
URL:            https://github.com/juce-framework/JUCE

Source0:        https://github.com/juce-framework/%{name}/archive/refs/tags/%{version}.tar.gz
Patch0:         fix_cmake_paths.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(alsa) 
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
BuildRequires:  pkgconfig(gtk+-x11-3.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(xcomposite)

%description
JUCE is an open-source cross-platform C++ application framework for creating desktop and mobile applications, including VST, VST3, AU, AUv3, AAX and LV2 audio plug-ins and plug-in hosts.

%package -n lib%{name}-devel
Summary:        JUCE is an open-source cross-platform C++ application framework

%description -n lib%{name}-devel
%{description}

%prep
%autosetup -p1

%build
%cmake 
%cmake_build 

%install
%cmake_install --prefix %{_prefix}

%files -n lib%{name}-devel
%license LICENSE.md
%doc README.md
%{_bindir}/juce*
%{_libdir}/cmake/%{name}/*    
%{_includedir}/%{name}/*


%changelog
* Sat Jan 10 2026 Tim Lauridsen <tla@rasmil.dk> - 8.0.12-1
- Version 8.0.12
- replace patches
* Sun Feb 23 2025 Tim Lauridsen <tla@rasmil.dk> - 8.0.6-1
- Initial package
