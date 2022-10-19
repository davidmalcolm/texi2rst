FOLDERS = cpp cppinternals gcc gccgo gccint gfortran libgomp libitm libquadmath install gfc-internals libiberty demo gdc gm2
MAKEOPTS = SPHINXOPTS="-j auto"

default: html man latexpdf info epub

.PHONY: html
html:
	for dir in $(FOLDERS); do $(MAKE) -C $$dir html $(MAKEOPTS); done

.PHONY: man
man:
	for dir in $(FOLDERS); do $(MAKE) -C $$dir man $(MAKEOPTS); done

.PHONY: latexpdf
latexpdf:
	for dir in $(FOLDERS); do $(MAKE) -C $$dir latexpdf $(MAKEOPTS); done

.PHONY: info
info:
	for dir in $(FOLDERS); do $(MAKE) -C $$dir info $(MAKEOPTS); done

.PHONY: epub
epub:
	for dir in $(FOLDERS); do $(MAKE) -C $$dir epub $(MAKEOPTS); done

.PHONY: linkcheck
linkcheck:
	for dir in $(FOLDERS); do $(MAKE) -C $$dir linkcheck $(MAKEOPTS); done

.PHONY: clean
clean:
	for dir in $(FOLDERS); do $(MAKE) -C $$dir clean $(MAKEOPTS); done
