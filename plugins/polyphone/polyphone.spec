%global debug_package %{nil}
%global builddest bin

Name:           polyphone
Version:        2.5.1
Release:        1%{?dist}
Summary:        Polyphone is a multiplatform and open-source soundfont editor for creating musical instruments.

License:        GPLv3
URL:            https://github.com/davy7125/polyphone

Source0:        https://github.com/davy7125/polyphone/archive/refs/tags/%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  pipewire-jack-audio-connection-kit-devel
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(rtmidi)
BuildRequires:  stk-devel
BuildRequires:  pkgconfig(qcustomplot-qt5)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(sndfile)

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
%qmake_qt5 polyphone.pro DEFINES+=USE_LOCAL_QCUSTOMPLOT DEFINES+=USE_LOCAL_RTMIDI 
make -j$(nproc)

%install
%make_install

%files 
%license LICENSE
%doc README.md
%{_bindir}/*


%changelog
* Fri Feb 28 2025 Tim Lauridsen <tla@rasmil.dk> - 2.5.1-1
- Initial package

qt5-default libqt5svg5-dev portaudio19-dev librtmidi-dev libstk0-dev libqcustomplot-dev libvorbis-dev libogg-dev libssl-dev libflac-dev
