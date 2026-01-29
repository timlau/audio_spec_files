
ifeq ($(ROOT),)
$(error invalid usage)
endif

VERSION=$(shell awk '/Version:/ { print $$2 }' ${PROJECT}.spec)
CURDIR = ${shell pwd}
BUILDDIR= $(CURDIR)/build
TAR_GZ = ${BUILDDIR}/SOURCES/v$(VERSION).tar.gz

all: srpm

archive:
ifeq (,$(wildcard $(TAR_GZ)))
	@echo "Creating archive"
	@mkdir -p ${BUILDDIR}/SOURCES
	@spectool -g -S $(PROJECT).spec -C ${BUILDDIR}/SOURCES
	@echo "Archive created : $(TAR_GZ)"
	@$(MAKE) -s copy_pactches
endif
.PHONY: archive

show:
	@echo "Project           : $(PROJECT)"
	@echo "Project version   : $(VERSION)"
	@echo "Current directory : $(CURDIR)"
	@echo "Build directory   : $(BUILDDIR)"
	@echo "Tarball           : $(TAR_GZ)"
	@echo "Mock release      : $(MOCK_REL)"
	@echo "Copr repository   : $(COPR_REPO)"
	@echo "Source            : spectool download"
.PHONY: show

include $(ROOT)/Makefile.build.mk
