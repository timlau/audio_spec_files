    include(GNUInstallDirs)
    # Install the standalone application
    if(TARGET ${PROJECT_NAME}_Standalone)
        install(TARGETS ${PROJECT_NAME}_Standalone DESTINATION ${CMAKE_INSTALL_BINDIR})
    endif()

    # Install the native Juce plugins
    foreach(format VST3 LV2)
        if(TARGET ${PROJECT_NAME}_${format})
            get_target_property(output ${PROJECT_NAME}_${format} JUCE_PLUGIN_ARTEFACT_FILE)
            install(DIRECTORY ${output} DESTINATION ${CMAKE_INSTALL_LIBDIR}/$<LOWER_CASE:${format}>)
        endif()
    endforeach()

    # Install the CLAP plugin
    if(TARGET ${PROJECT_NAME}_CLAP)
        install(TARGETS ${PROJECT_NAME}_CLAP DESTINATION ${CMAKE_INSTALL_LIBDIR}/clap)
    endif()
