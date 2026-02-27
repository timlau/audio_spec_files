
# Enable compile commands export for IDEs
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Copy plugins after build option
option(COPY_AFTER_BUILD "Copy JUCE Plugins after built" OFF)

# Fetch JUCE from GitHub
include(cmake/CPM.cmake)
CPMAddPackage("gh:/juce-framework/JUCE#8.0.11")
CPMAddPackage("gh:/free-audio/clap-juce-extensions#main")

set(LV2_URI "http://")

# ==================== Setup plugin types to build =======================
set(AUDIO_FORMATS AU VST3 Standalone)

# Build LV2 only on Linux
if(UNIX AND NOT APPLE)
    list(APPEND AUDIO_FORMATS LV2)
endif()


juce_add_plugin (${PROJECT_NAME}
				 FORMATS ${AUDIO_FORMATS}
				 COPY_PLUGIN_AFTER_BUILD ${COPY_AFTER_BUILD}
				 LV2URI ${LV2_URI})

# ==================== CLAP =======================
clap_juce_extensions_plugin(TARGET ${PROJECT_NAME}
        CLAP_ID "x.y.z"
        CLAP_FEATURES instrument "virtual synth")

# ==================== Installation of plugins (Linux) =======================
if(UNIX AND NOT APPLE)
    include(cmake/LinuxInstall.cmake)
endif(UNIX AND NOT APPLE)
