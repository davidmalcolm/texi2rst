
Actual Bugs We Havent Fixed Yet
*******************************

* The ``fixincludes`` script interacts badly with automounters; if the
  directory of system header files is automounted, it tends to be
  unmounted while ``fixincludes`` is running.  This would seem to be a
  bug in the automounter.  We dont know any good way to work around it.

