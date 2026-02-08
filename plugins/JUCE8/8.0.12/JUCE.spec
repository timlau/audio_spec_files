%global debug_package %{nil}
%global builddest bin
%global libname JUCE8_0_12-devel

Name:           JUCE
Version:        8.0.12
Release:        %autorelease%{?dist}
Summary:        JUCE is an open-source cross-platform C++ application framework

License:        GPLv3+
URL:            https://github.com/juce-framework/JUCE

Source0:        https://github.com/juce-framework/JUCE/archive/refs/tags/%{version}.tar.gz
# add a second source with a custom CMakeUuserPresets.json
Source1:        cmake_preset.tar.gz
Patch0:         fix_cmake_paths.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
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

%package -n %{libname}
Summary:        JUCE is an open-source cross-platform C++ application framework

%description -n %{libname}
%{description}

%prep
%autosetup -p1
# unpack the custom CMakeUuserPresets.json in same directory as the primary source
%setup -T -D -a 1

%build
%cmake --preset=rpmbuild -DJUCE_INSTALL_DESTINATION=%{_libdir}/cmake/%{name}-%{version} -DJUCE_MODULE_PATH=%{_includedir}/%{name}-%{version}/modules -DJUCE_TOOL_INSTALL_DIR=%{_libexecdir}/%{name}-%{version}
%cmake_build --preset=rpmbuild

%install
%cmake_install --prefix %{_prefix}

%files -n  %{libname}
%license LICENSE.md
%doc README.md
%{_libdir}/cmake/%{name}-%{version}/
%{_includedir}/%{name}-%{version}/
%{_libexecdir}/%{name}-%{version}/

%changelog
%autochangelog
