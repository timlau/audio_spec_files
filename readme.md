## RPM spec files and Makefile's to build audio applications & plugins for Fedora 40 & Later

Build packages are available in the [timlau/audio](https://copr.fedorainfracloud.org/coprs/timlau/audio/) Fedora Copr Repository

## Applications/Plugins

#### Sfizz

Sfizz is a musical sampler, available as LV2 and VST plugins for musicians,

#### Dexed
A synth that is closely modeled on the Yamaha DX7

#### Geonkick
Geonkick is a synthesizer that can synthesize elements of percussion. The most basic examples are: kicks, snares, hit-hats, shakers, claps.

#### Neural Amp Modeler 
LV2 plugin implementation Neural Amp Modeler

#### AIDA-X
AIDA-X is an Amp Model Player, allowing it to load models of AI trained music gear, which you can then play through guitar

#### Dragonfly Reverb
Dragonfly Reverb is a bundle of free audio effects for Linux, MacOS, and Windows. The reverb algorithms are based on the original Freeverb. The DR-1 algorithm is based on the Schroeder/Moorer reverb. The DR-2 algorithm is based on the original Freeverb algorithm. The DR-3 algorithm is a unique reverb algorithm developed by Michael Willis.

#### JUCE
JUCE is an open-source cross-platform C++ application framework for creating desktop and mobile applications, including VST, VST3, AU, AUv3, AAX and LV2 audio plug-ins and plug-in hosts.
This package is used to build application there is using the JUCE framework, so the package don't need to have the whole JUCE source and build it every time.
a very basic dummy plugin made with JUCE is located [Here](https://github.com/timlau/juce-test)

#### Polyphone
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

#### YK Chorus
A chorus effect inspired by the one found in certain well-known Japanese vintage analog synthesizers (Juno 60)


## Install from timlau/audio copr

### enable copr repo in Fedora 40+
```bash
sudo dnf copr enable timlau/audio 
```

#### Install sfizz audio plugins (vst3 or lv2)

```bash
sudo dnf install sfizz-vst3
sudo dnf install sfizz-lv2
```

#### Install Dexed (clap or vst3 or standalone)
```bash
sudo dnf install dexed-clap
sudo dnf install dexed-vst3
sudo dnf install dexed

```

#### Install Geonkick (lv2 or standalone)
```bash
sudo dnf install geonkick
sudo dnf install geonkick-lv2
```

#### Install Neural Amp Modeler  (lv2)
```bash
sudo dnf install neural-amp-modeler-lv2
```
#### Install AIDA-X (clap or vst3 or lv2 or standalone)
```bash
sudo dnf install AIDA-X-clap
sudo dnf install AIDA-X-vst3
sudo dnf install AIDA-X-lv2
sudo dnf install AIDA-X
```

#### Install dragonfly-reverb  (clap or vst3 or lv2  or standalone)
```bash
sudo dnf install dragonfly-reverb-clap
sudo dnf install dragonfly-reverb-vst3
sudo dnf install dragonfly-reverb-lv2
sudo dnf install dragonfly-reverb
```

#### Install JUCE
```bash
sudo dnf install libJUCE-devel
```

#### Install polyphone
```bash
sudo dnf install polyphone
```

#### Install ykchorus  (clap or vst3 or lv2  or standalone)
```bash
sudo dnf install ykchorus-clap
sudo dnf install ykchorus-vst3
sudo dnf install ykchorus-lv2
sudo dnf install ykchorus
```

## Make targets
Each application/plugin subdirectory contains a Makefile with the following target

#### Clonning the upstream source git repo
```bash
make clone
```

#### Making an source archive (will clone if needed)
```bash
make archive
```

#### Making an source src.rpm (will make archive if needed)
```bash
make srpm
```

#### Building on localsystem (will build a new .src.rpm)
will install build requirements defined in .spec before build
```bash
make localbuild
```

#### Building in local mock (will build a new .src.rpm)
```bash
make mockbuild
```

#### Building in Fedora Copr  (will build a new .src.rpm)
```bash
make coprbuild
```