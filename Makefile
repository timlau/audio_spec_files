SUBDIRS = dexed geonkick sfizz AIDA-X neural-amp-modeler dragonfly-reverb

all:
	@echo "Nothing to do, use a specific target"

clean:
	@for dir in $(SUBDIRS); do \
		echo "Cleaning $$dir"; \
		$(MAKE) -s -C $$dir clean; \
	done

show:
	@for dir in $(SUBDIRS); do \
		printf "\n######## $$dir ########\n\n"; \
		$(MAKE) -s -C $$dir show; \
	done

.PHONY: all clean