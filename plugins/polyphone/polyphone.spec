%global debug_package %{nil}
%global builddest sources
%global app_id io.polyphone.polyphone

Name:           polyphone
Version:        2.5.1
Release:        1%{?dist}
Summary:        Polyphone is a multi-platform and open-source soundfont editor for creating musical instruments.

License:        GPLv3
URL:            https://github.com/davy7125/polyphone

Source0:        https://github.com/davy7125/polyphone/archive/refs/tags/%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  pipewire-jack-audio-connection-kit-devel
BuildRequires:  pkgconfig(Qt6)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  qt6-linguist
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(rtmidi)
BuildRequires:  stk-devel
BuildRequires:  pkgconfig(qcustomplot-qt6)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  desktop-file-utils

%description
Polyphone is a multiplatform and open-source soundfont editor for creating musical instruments.

* editing of sf2, sf3, sfz and sfArk file formats
* compatible with Jack and ASIO audio servers
* built-in synthesizer, controlled by a virtual keyboard or MIDI signals
* automatic recognition of root keys
* automatic loop of samples
* simultaneous editing of parameters
* specific tools for musical instrument creation
* recorder to keep a trace of what is played in a .wav file
* soundfont browser connected to the online repository

%prep
%autosetup

%build
cd sources
%qmake_qt6 polyphone.pro DEFINES+=USE_LOCAL_QCUSTOMPLOT DEFINES+=USE_LOCAL_RTMIDI 
make -j$(nproc)

%install
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_datadir}/applications
install -d -m 755 %{buildroot}%{_datadir}/mime/packages
install -d -m 755 %{buildroot}%{_datadir}/icons
install -d -m 755 %{buildroot}%{_metainfodir}
install -d -m 755 %{buildroot}%{_mandir}/man1
install %{builddest}/bin/%{name} %{buildroot}%{_bindir}/
install %{builddest}/contrib/%{app_id}.metainfo.xml %{buildroot}%{_metainfodir}/
install %{builddest}/contrib/man/man1/%{name}.1 %{buildroot}%{_mandir}/man1/
install %{builddest}/contrib/%{name}.xml %{buildroot}%{_datadir}/mime/packages/
install %{builddest}/contrib/%{name}.png %{buildroot}%{_datadir}/icons/
desktop-file-install \
--dir=%{buildroot}%{_datadir}/applications \
%{builddest}/contrib/%{app_id}.desktop

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml

%files 
%license LICENSE.txt
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/icons/%{name}.png
%{_mandir}/man1/%{name}.1*
%{_metainfodir}/%{app_id}.metainfo.xml
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/%{name}*.png


# /usr/share/doc/polyphone
# /usr/share/doc/polyphone/changelog
# /usr/share/doc/polyphone/polyphone.1



%changelog
* Fri Feb 28 2025 Tim Lauridsen <tla@rasmil.dk> - 2.5.1-1
- Initial package
