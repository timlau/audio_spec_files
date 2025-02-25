# /usr/bin/python

import argparse

dep_map = {
    "libasound2-dev": "pkgconfig(alsa)",
    "libjack-jackd2-dev": "pipewire-jack-audio-connection-kit-devel",
    "libfreetype-dev": "pkgconfig(freetype2)",
    "libfontconfig1-dev": "pkgconfig(fontconfig)",
    "libx11-dev": "pkgconfig(x11)",
    "libxcursor-dev": "pkgconfig(xcursor)",
    "libxext-dev": "pkgconfig(xext)",
    "libxinerama-dev": "pkgconfig(xinerama)",
    "libxrandr-dev": "pkgconfig(xrandr)",
    "libxrender-dev": "pkgconfig(xrender)",
    "libwebkit2gtk-4.0-dev": "pkgconfig(webkit2gtk-4.0)",
    "libwebkit2gtk-4.1-dev": "pkgconfig(webkit2gtk-4.1)",
    "libglu1-mesa-dev": "pkgconfig(gl)",
    "mesa-common-dev": "pkgconfig(gl)",
    "libxcomposite-dev": "pkgconfig(xcomposite)",
    "ladspa-sdk": "ladspa-devel",
    "libx11-xcb-dev": "pkgconfig(xcb)",
    "libxcb-util-dev": "pkgconfig(xcb-util)",
    "libxcb-cursor-dev": "pkgconfig(xcb-cursor)",
    "libxcb-xkb-dev": "pkgconfig(xkb)",
    "libxcb-keysyms1-dev": "pkgconfig(xcb-keysyms)",
    "libxkbcommon-dev": "pkgconfig(xkbcommon)",
    "libxkbcommon-x11-dev": "pkgconfig(xkbcommon-x11)",
    "libcairo2-dev": "pkgconfig(cairo)",
    "libgtkmm-3.0-dev": "pkgconfig(gtkmm-3.0)",
    "libsqlite3-dev": "pkgconfig(sqlite3)",
    "qt5-default": "pkgconfig(Qt5)",
    "libqt5svg5-dev": "pkgconfig(Qt5Svg)",
    "portaudio19-dev": "pkgconfig(portaudio-2.0)",
    "librtmidi-dev": "pkgconfig(pkgconfig(rtmidi))",
    "libstk0-dev": "stk-devel",
    "libqcustomplot-dev": "pkgconfig(qcustomplot-qt5)",
    "libvorbis-dev": "pkgconfig(vorbis)",
    "libogg-dev": "pkgconfig(ogg)",
    "libssl-dev": "pkgconfig(libssl)",
    "libflac-dev": "pkgconfig(flac)",
}


def markdown():
    header = """
### Mapping common used ubuntu build deps to fedora deps.

Best practice in Fedora packages is to use the **pkgconfig(dependcy)** format to define build requirements

#### Example

```
BuildRequires:  pkgconfig(alsa)
```

### Mappings

| ubuntu build deps      | Fedora BuildRequire:                          |
| -----------------------| ----------------------------------------------|"""
    print(header)
    for dep in dep_map:
        fed_dep = dep_map[dep]
        print(f"| {dep:22} | {fed_dep:45} |")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--notfound", action="store_true")
    parser.add_argument("--format", action="store_true")
    parser.add_argument("--markdown", action="store_true")
    parser.add_argument("deps", nargs="*", default=[])
    args = parser.parse_args()
    found = 0
    notfound = 0
    if args.markdown:
        markdown()
    else:
        for dep in args.deps:
            if dep in dep_map:
                found += 1
                if not args.notfound:
                    print(f"BuildRequires:  {dep_map[dep]}")
            else:
                notfound += 1
                if args.notfound:
                    if args.format:
                        print(f'"{dep}":"pkgconfig()",')
                    else:
                        print(dep)
                else:
                    print(f"{dep} not found")
        print(f"Found: {found} Missing: {notfound}")


if __name__ == "__main__":
    main()
