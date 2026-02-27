# Check list for JUCE based plugin packaging

## Fork the github repository

## Improve CMakeLists.txt file

### Use CPM for dependency management

Copy the `template/cmake/cmake` directory into your project.

add the following lines to your `CMakeLists.txt` file:

```
# Fetch JUCE from GitHub
include(cmake/CPM.cmake)
CPMAddPackage("gh:/juce-framework/JUCE#8.0.12")
  
```
### Add clap support

add the following lines to your `CMakeLists.txt` file, bellow the other CPMAddPackage above

```cmake
CPMAddPackage("gh:/free-audio/clap-juce-extensions#main")
```
and these lines after the `juce_add_plugin` command

```cmake
clap_juce_extensions_plugin(TARGET ${PROJECT_NAME}
        CLAP_ID "x.y.z"
        CLAP_FEATURES instrument "virtual synth")
  
```
Update the CLAP_ID and CLAP_FEATURES

### Add lv2 support

use the following lines in `CMakeLists.txt` to setup lv2 plugin on Linux

```cmake
set(LV2_URI "http://")

# ==================== Setup plugin types to build =======================
set(AUDIO_FORMATS AU VST3 Standalone)

# Build LV2 only on Linux
if(LINUX)
    list(APPEND AUDIO_FORMATS LV2)
endif()


juce_add_plugin (${PROJECT_NAME}
         ..
				 FORMATS ${AUDIO_FORMATS}
				 ..	
				 LV2URI ${LV2_URI})
)

```
Update the LV2_URI to the homepage of the project

### Add cmake install support

Use the following lines in `CMakeLists.txt` to setup `cmake install` support 


```cmake
# ==================== Installation of plugins (Linux) =======================
if(LINUX)
    include(cmake/LinuxInstall.cmake)
endif()

```


### Other changes
```cmake

# Enable compile commands export for IDEs
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Copy plugins after build option
option(COPY_AFTER_BUILD "Copy JUCE Plugins after built" OFF)

juce_add_plugin (${PROJECT_NAME}
        ...
				 COPY_PLUGIN_AFTER_BUILD ${COPY_AFTER_BUILD}
				...
)

```
