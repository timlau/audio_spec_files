
ifeq ($(ROOT),)
$(error invalid usage)
endif

VERSION=$(shell awk '/Version:/ { print $$2 }' ${PROJECT}.spec)
CURDIR = ${shell pwd}
BUILDDIR= $(CURDIR)/build
GIT_DIR = ${BUILDDIR}
TAR_GZ = ${BUILDDIR}/SOURCES/$(PROJECT)-$(VERSION).tar.gz


all: srpm
	
archive: clone
ifeq (, $(wildcard $(TAR_GZ)))
	@echo "Creating archive: $(TAR_GZ)"
	@mkdir -p ${BUILDDIR}/SOURCES
	@cd $(SRC_DIR); git ls-files --recurse-submodules | tar caf $(TAR_GZ) --ignore-failed-read --xform s:^:$(PROJECT)-$(VERSION)/: --verbatim-files-from -T-
	@echo "Archive created : $(TAR_GZ)"
	@$(MAKE) -s copy_pactches
endif

show:
	@echo "Project           : $(PROJECT)"
	@echo "Project version   : $(VERSION)"
	@echo "Git URL           : $(GIT_URL)"
	@echo "Current directory : $(CURDIR)"
	@echo "Build directory   : $(BUILDDIR)"
	@echo "Source directory  : $(SRC_DIR)"
	@echo "Tarball           : $(TAR_GZ)"
	@echo "Mock release      : $(MOCK_REL)"
	@echo "Copr repository   : $(COPR_REPO)"
ifdef GIT_TAG
	@echo "Source            : git checkout - Tag: $(GIT_TAG)"
else
	@echo "Source            : git checkout - HEAD"
endif

.PHONY: archive show

include $(ROOT)/Makefile.build.mk
