
ifeq ($(ROOT),)
$(error invalid usage)
endif

SRC_DIR = $(GIT_DIR)/$(PROJECT)
DNF_BUILDDEP_INSTALLED = ${BUILDDIR}/DEPS_INSTALLED
MOCK_REL = fedora-43-x86_64
MOCK_RESULT = /var/lib/mock/${MOCK_REL}/result
COPR_REPO = audio
SUB_MODULES=$(shell sed -n 's/\tpath = //p' $(SRC_DIR)/.gitmodules)
NAME = $(shell git config --get user.name)
EMAIL = $(shell git config --get user.email)
PACKAGER = $(NAME) <$(EMAIL)>
RPMBUILD_OPTS = --define '_topdir $(BUILDDIR)' --define 'packager $(PACKAGER)'
CMAKE_GZ = ${BUILDDIR}/SOURCES/cmake_preset.tar.gz

all: srpm

clone:
ifeq (,$(wildcard $(SRC_DIR)))
	@echo "--> Cloning repository : $(GIT_URL)"
	@git clone $(GIT_URL) $(SRC_DIR)
ifdef GIT_BRANCH
	@echo "--> Checkout branch: $(GIT_BRANCH)"
	@cd $(SRC_DIR); git checkout $(GIT_BRANCH)
else
ifdef GIT_TAG
	@echo "--> Checking out git tag : $(GIT_TAG)"
	@cd $(SRC_DIR); git checkout -b release $(GIT_TAG)
else
	@echo "--> No git tag specified, using master branch"
endif
endif
ifneq ($(SKIP_SUBMODULES),true)
	@$(MAKE) -s update_submodules
else
	@echo "--> Skipping submodule update as per configuration"
endif
	@echo "Repository cloned into: $(SRC_DIR)"
	@$(MAKE) -s update-gitdate
endif
.PHONY: clone

update_submodules:
	@for module in $(SUB_MODULES); do \
		if [[ ! " $(GIT_EXCLUDE) " =~ " $$module " ]]; then \
			echo "Module: $$module"; \
			cd $(SRC_DIR); git submodule update --init --recursive $$module; \
		fi \
	done
.PHONY: update_submodules

copy_pactches:
ifneq (,$(wildcard $(CURDIR)/*.patch))
	@echo "--> Copying patches"
	@echo $(wildcard $(CURDIR)/*.patch)
	@cp $(CURDIR)/*.patch ${BUILDDIR}/SOURCES
endif
.PHONY: copy_patches

copy_cmake_preset:
ifneq (,$(wildcard $(CURDIR)/CMakeUserPresets.json))
	@echo "--> Adding CMakeUserPresets.json to $(CMAKE_GZ)"
	@cd $(CURDIR) && echo CMakeUserPresets.json | tar caf $(CMAKE_GZ) --ignore-failed-read --verbatim-files-from -T-
endif
.PHONY: copy_cmake_preset

update-gitdate:
	$(eval GITDATE := .git$(shell date +%Y%m%d).$(shell git -C $(SRC_DIR) rev-parse --short HEAD))
	@echo "Updating spec file with git date : $(GITDATE)"
	@sed -i -e "s/\.git[0-9]*\.[0-9a-f]*/$(GITDATE)/" $(PROJECT).spec
.PHONY: update-gitdate

srpm: archive
	@echo "Building SRPM"
	@rm -rf $(BUILDDIR)/SRPMS
	rpmbuild $(RPMBUILD_OPTS) -bs $(PROJECT).spec
.PHONY: srpm

localbuild: srpm
	@echo "Building RPM locally"
ifeq (,$(wildcard $(DNF_BUILDDEP_INSTALLED)))
	@sudo dnf builddep -y ${PROJECT}.spec
	@touch $(DNF_BUILDDEP_INSTALLED)
endif
	@rpmbuild $(RPMBUILD_OPTS) -ba ${PROJECT}.spec
	@$(MAKE) -s show-rpms
.PHONY: localbuild

show-rpms:
	@echo "--> Build RPMs"
	@tree -P *.rpm -I *.src.rpm $(BUILDDIR)/RPMS
.PHONY: show-rpms

mockbuild: srpm
	@echo "Building RPM in mock"
ifdef MOCK_REPO
	@mock -r $(MOCK_REL) --rebuild $(BUILDDIR)/SRPMS/$(PROJECT)-$(VERSION)*.src.rpm -a $(MOCK_REPO) --enable-network
else
	@mock -r $(MOCK_REL) --rebuild $(BUILDDIR)/SRPMS/$(PROJECT)-$(VERSION)*.src.rpm --enable-network
endif
	@echo "--> Build RPMs"
	@tree -P *.rpm -I *.src.rpm $(MOCK_RESULT)
.PHONY: mockbuild

mock-files:
	find $(MOCK_RESULT) -name *64.rpm -print -exec rpm -qlp {} \;
.PHONY: mock-files

mock-provides:
	find $(MOCK_RESULT) -name *64.rpm -print -exec rpm -qp --provides {} \;
.PHONY: mock-provides

mock-requires:
	find $(MOCK_RESULT) -name *64.rpm -print -exec rpm -qp --requires {} \;
.PHONY: mock-requires

mockinst:
	@sudo dnf install $(MOCK_RESULT)/$(PROJECT)*-$(VERSION)*.x86_64.rpm
.PHONY: mockinst

coprbuild: srpm
	@echo "Building RPM in copr"
	@copr-cli build --nowait $(COPR_REPO) $(BUILDDIR)/SRPMS/$(PROJECT)-$(VERSION)*.src.rpm
.PHONY: coprbuild

clean: clean-archive clean-build
	@rm -rf $(SRC_DIR)
.PHONY: clean

clean-archive:
	@rm -rf $(BUILDDIR)/SOURCES/*
.PHONY: clean-archive

clean-builddep:
	@rm -f $(DNF_BUILDDEP_INSTALLED)
.PHONY: clean-builddep

clean-build:
	@rm -rf $(BUILDDIR)/BUILD
	@rm -rf $(BUILDDIR)/RPMS
	@rm -rf $(BUILDDIR)/SRPMS

.PHONY: cleam-build
