SUBDIRS := $(shell ls plugins/)
# ARCHIVE_EXCLUDE = plugins/dexed/*

all:
	@echo "Nothing to do, use a specific target"

clean:
	@for dir in $(SUBDIRS); do \
		echo "Cleaning plugins/$$dir"; \
		$(MAKE) -s -C plugins/$$dir clean; \
	done

show:
	@for dir in $(SUBDIRS); do \
		printf "\n######## $$dir ########\n\n"; \
		$(MAKE) -s -C plugins/$$dir show; \
	done


TAR_GZ = ./plugins/dexed/build/SOURCES/dexed-0.9.8.tar.gz

test:
	@echo "wildcard : $(wildcard $(TAR_GZ))"
ifeq (,$(wildcard $(TAR_GZ)))
	@echo "Creating archive: $(TAR_GZ)"
else
	@echo "Archive already exists: $(TAR_GZ)"
endif
.PHONY: all clean test