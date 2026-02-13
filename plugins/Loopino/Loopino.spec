%global debug_package %{nil}
%global buildname loopino

Name:           Loopino
Version:        0.9.6
Release:        %autorelease
Summary:        Loopino is a lightweight audio sampler

License:        BSD-3-Clause
URL:            https://github.com/brummer10/Loopino

# The source for this package was pulled from upstream's vcs.
# check here : https://github.com/timlau/audio_spec_files/
# for a Makefile that can be used to create the source tarball
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  pipewire-jack-audio-connection-kit-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  pkgconfig(sndfile)

%description
Loopino is a lightweight audio sampler. It allows you to load, trim, and loop audio files with precision,
making it ideal for crafting seamless sample loops. With a clean, minimal interface,
Loopino fits perfectly into any audio workflow — whether for sound design,
live performance, or creative sampling experiments

%package clap
Summary:        CLAP plugin of %{name}

%description clap
Loopino is a lightweight audio sampler. It allows you to load, trim, and loop audio files with precision,
making it ideal for crafting seamless sample loops. With a clean, minimal interface,
Loopino fits perfectly into any audio workflow — whether for sound design,
live performance, or creative sampling experiments


%prep
%autosetup -p1 -n %{name}-%{version}


%build
%make_build
%make_build clap

%install
# Manual install of plugins into buildroot
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_libdir}/clap
install bin/%{buildname}.clap %{buildroot}%{_libdir}/clap/%{name}.clap
install bin/%{buildname} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%files clap
%license LICENSE
%doc README.md
%{_libdir}/clap/%{name}.clap

%changelog
%autochangelog
