
Introduction to :command:`gcov-tool`

.. man begin DESCRIPTION 

:command:`gcov-tool` is an offline tool to process gcc's gcda profile files.

Current gcov-tool supports the following functionalities:

* merge two sets of profiles with weights.

  * read one set of profile and rewrite profile contents. One can scale or
  normalize the count values.

Examples of the use cases for this tool are:

* Collect the profiles for different set of inputs, and use this tool to merge
  them. One can specify the weight to factor in the relative importance of
  each input.

  * Rewrite the profile after removing a subset of the gcda files, while maintaining
  the consistency of the summary and the histogram.

  * It can also be used to debug or libgcov code as the tools shares the majority
  code as the runtime library.

Note that for the merging operation, this profile generated offline may
contain slight different values from the online merged profile. Here are
a list of typical differences:

* histogram difference: This offline tool recomputes the histogram after merging
  the counters. The resulting histogram, therefore, is precise. The online
  merging does not have this capability - the histogram is merged from two
  histograms and the result is an approximation.

  * summary checksum difference: Summary checksum uses a CRC32 operation. The value
  depends on the link list order of gcov-info objects. This order is different in
  gcov-tool from that in the online merge. It's expected to have different
  summary checksums. It does not really matter as the compiler does not use this
  checksum anywhere.

  * value profile counter values difference: Some counter values for value profile
  are runtime dependent, like heap addresses. It's normal to see some difference
  in these kind of counters.

.. man end 

