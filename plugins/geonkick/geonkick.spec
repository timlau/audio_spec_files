%global debug_package %{nil}

Name:           geonkick
Version:        3.5.2
Release:        1%{?dist}
Summary:        Geonkick - a free software percussion synthesizer

License:        GPL-3.0-or-later
URL:            https://github.com/Geonkick-Synthesizer/geonkick/
Source0:        https://github.com/Geonkick-Synthesizer/geonkick/archive/refs/tags/v%{version}.tar.gz
Patch0:         0001-no-arguments-for-geonkick_midi_channels_number.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(RapidJSON)
BuildRequires:  pkgconfig(lv2)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  desktop-file-utils


%description
Geonkick is a synthesizer that can synthesize elements of percussion. The most basic examples are: kicks, snares, hit-hats, shakers, claps.

%package lv2
Summary:        Geonkick LV2 plugin
# the presets are in the main package, but will work without them
Recommends:     %{name} = %{version}-%{release}

%description lv2
Geonkick is a synthesizer that can synthesize elements of percussion. The most basic examples are: kicks, snares, hit-hats, shakers, claps.

%prep
%autosetup -p1 -n %{name}-%{version}


%build
%cmake -DGKICK_STANDALONE=ON
%cmake_build

%install
%cmake_install
# remove unneeded redkite devel files
rm -rf %{buildroot}/usr/include/redkite/*
rm -rf %{buildroot}/usr/bin/rkpng2c
rm -rf %{buildroot}/usr/lib/libredkite.a

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}*.png
%{_datadir}/icons/hicolor/*/apps/%{name}*.svg
%{_datadir}/mime/packages/%{name}.xml

%files lv2
%license LICENSE
%doc README.md
%{_libdir}/lv2/geonkick*.lv2/*

%changelog
* Thu Feb 20 2025 Tim Lauridsen <tla@rasmil.dk> - 3.5.2-1
- version 3.5.2
- added lv2 plugin in subpackage
* Tue Apr 27 2021 Tim Lauridsen <tla@rasmil.dk> - 2.8.0-1
- Initial SPEC
