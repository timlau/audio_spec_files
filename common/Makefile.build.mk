
ifeq ($(ROOT),)
$(error invalid usage)
endif

SRC_DIR = $(GIT_DIR)/$(PROJECT)
DNF_BUILDDEP_INSTALLED = ${BUILDDIR}/DEPS_INSTALLED
MOCK_REL = fedora-43-x86_64
MOCK_RESULT = /var/lib/mock/${MOCK_REL}/result
COPR_REPO = audio
SUB_MODULES=$(shell sed -n 's/\tpath = //p' $(SRC_DIR)/.gitmodules)

all: srpm

clone:
ifeq (,$(wildcard $(SRC_DIR)))
	@echo "Cloning repository"
	@git clone $(GIT_URL) $(SRC_DIR)
ifdef GIT_TAG
	@echo "--> Checking out git tag : $(GIT_TAG)"
	@cd $(SRC_DIR); git checkout -b release $(GIT_TAG)
else
	@echo "--> No git tag specified, using master branch"
endif	
	@$(MAKE) -s update_submodules
	@echo "Repository cloned into: $(SRC_DIR)"
	@$(MAKE) -s update-gitdate
endif

update_submodules:
	@for module in $(SUB_MODULES); do \
		if [[ ! " $(GIT_EXCLUDE) " =~ " $$module " ]]; then \
			echo "Module: $$module"; \
			cd $(SRC_DIR); git submodule update --init --recursive $$module; \
		fi \
	done

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
ifdef MOCK_REPO
	@mock -r $(MOCK_REL) --rebuild $(BUILDDIR)/SRPMS/$(PROJECT)-$(VERSION)*.src.rpm -a $(MOCK_REPO)
else
	@mock -r $(MOCK_REL) --rebuild $(BUILDDIR)/SRPMS/$(PROJECT)-$(VERSION)*.src.rpm
endif	
	@echo "--> Build RPMs"
	@tree -P *.rpm -I *.src.rpm $(MOCK_RESULT)

mock-files:
	find $(MOCK_RESULT) -name *64.rpm -print -exec rpm -qlp {} \;

mock-provides:
	find $(MOCK_RESULT) -name *64.rpm -print -exec rpm -qp --provides {} \;

mock-requires:
	find $(MOCK_RESULT) -name *64.rpm -print -exec rpm -qp --requires {} \;

mockinst:
	@sudo dnf install $(MOCK_RESULT)/$(PROJECT)*-$(VERSION)*.x86_64.rpm

coprbuild: srpm
	@echo "Building RPM in copr"
	@copr-cli build --nowait $(COPR_REPO) $(BUILDDIR)/SRPMS/$(PROJECT)-$(VERSION)*.src.rpm

clean:
	@rm -rf $(BUILDDIR)

clean-archive:
	@rm -rf $(BUILDDIR)/SOURCES/*

clean-builddep:
	@rm -f $(DNF_BUILDDEP_INSTALLED)

clean-build:
	@rm -rf $(BUILDDIR)/BUILD
	@rm -rf $(BUILDDIR)/RPMS


.PHONY: clean mockinst mockbuild coprbuild test-submodules clone update_submodules copy_pactches update-gitdate
.PHONY:	srpm localbuild mock-files mock-requires mock-provides clean-build clean-builddep clean-archive
