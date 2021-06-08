FOLDERS = cpp cppinternals gcc gccgo gccint gfortran libgomp libitm libquadmath install gfc-internals libiberty

default: html man xelatexpdf info

.PHONY: html
html:
	for dir in $(FOLDERS); do $(MAKE) -C $$dir html; done

.PHONY: man
man:
	for dir in $(FOLDERS); do $(MAKE) -C $$dir man; done

.PHONY: xelatexpdf
xelatexpdf:
	for dir in $(FOLDERS); do $(MAKE) -C $$dir xelatexpdf; done

.PHONY: info
info:
	for dir in $(FOLDERS); do $(MAKE) -C $$dir info; done

.PHONY: clean
clean:
	for dir in $(FOLDERS); do $(MAKE) -C $$dir clean; done
