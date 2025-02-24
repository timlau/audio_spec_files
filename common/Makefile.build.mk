
ifeq ($(ROOT),)
$(error invalid usage)
endif

VERSION=$(shell awk '/Version:/ { print $$2 }' ${PROJECT}.spec)
CURDIR = ${shell pwd}
BUILDDIR= $(CURDIR)/build
SRC_DIR = $(GIT_DIR)/$(PROJECT)
TAR_GZ = ${BUILDDIR}/SOURCES/$(PROJECT)-$(VERSION).tar.gz

DNF_BUILDDEP_INSTALLED = ${BUILDDIR}/DEPS_INSTALLED
MOCK_REL = fedora-41-x86_64
MOCK_RESULT = /var/lib/mock/${MOCK_REL}/result
COPR_REPO = audio

all: srpm

clone:
ifeq (,$(wildcard $(SRC_DIR)))
	@echo "Cloning repository"
	@git clone $(GIT_URL) $(SRC_DIR)
ifdef GIT_TAG
	@echo "--> Checking out git tag : $(GIT_TAG)"
	@cd $(SRC_DIR); git checkout -b release $(GIT_TAG); git submodule update --init --recursive
else
	@echo "--> No git tag specified, using master branch"
	@cd $(SRC_DIR); git submodule update --init --recursive
endif	
	@echo "Repository cloned : $(SRC_DIR)"
	@$(MAKE) -s update-gitdate
endif

copy_pactches:
ifneq (,$(wildcard $(CURDIR)/*.patch))
	@echo "--> Copying patches"
	@echo $(wildcard $(CURDIR)/*.patch)
	@cp $(CURDIR)/*.patch ${BUILDDIR}/SOURCES
endif

update-gitdate:
	$(eval GITDATE := .git$(shell date +%Y%m%d).$(shell git -C $(SRC_DIR) rev-parse --short HEAD))
	@echo "Updating spec file with git date : $(GITDATE)"
	@sed -i -e "s/\.git[0-9]*\.[0-9a-f]*/$(GITDATE)/" $(PROJECT).spec

srpm: archive
	@echo "Building SRPM"
	@rm -rf $(BUILDDIR)/SRPMS
	@rpmbuild --define '_topdir $(BUILDDIR)' -bs $(PROJECT).spec


localbuild: srpm
	@echo "Building RPM locally"
ifeq (,$(wildcard $(DNF_BUILDDEP_INSTALLED)))
	@sudo dnf builddep -y ${PROJECT}.spec
	@touch $(DNF_BUILDDEP_INSTALLED)
endif	
	@rpmbuild --define "_topdir $(BUILDDIR)" -ba ${PROJECT}.spec
	@echo "--> Build RPMs"
	@tree -P *.rpm -I *.src.rpm $(BUILDDIR)/RPMS	

mockbuild: srpm
	@echo "Building RPM in mock"
	@mock -r $(MOCK_REL) --rebuild $(BUILDDIR)/SRPMS/$(PROJECT)-$(VERSION)*.src.rpm
	@echo "--> Build RPMs"
	@tree -P *.rpm -I *.src.rpm $(MOCK_RESULT)

mockinst:
	@sudo dnf install $(MOCK_RESULT)/$(PROJECT)*-$(VERSION)*.x86_64.rpm

coprbuild: srpm
	@echo "Building RPM in copr"
	@copr-cli build --nowait $(COPR_REPO) $(BUILDDIR)/SRPMS/$(PROJECT)-$(VERSION)*.src.rpm

clean:
	@rm -rf $(BUILDDIR)

clean-archive:
	@rm -rf $(BUILDDIR)/SOURCES/*


.PHONY: clean mockinst mockbuild coprbuild 
