.. _option-summary:

Option Summary
**************

Here is a summary of all the options, grouped by type.  Explanations are
in the following sections.

*Overall Options*
  See :ref:`Options Controlling the Kind of Output <overall-options>`.

  :option:`-c`  :option:`-S`  :option:`-E`  :option:`-o` ``file``  :option:`-no-canonical-prefixes`  
  :option:`-pipe`  :option:`-pass-exit-codes`  
  :option:`-x` ``language``  :option:`-v`  :option:`-###`  :option:`--help`[=``class``[,...]]  :option:`--target-help`  
  :option:`--version` :option:`-wrapper` @``file`` :option:`-fplugin=```file`` :option:`-fplugin-arg-```name``=``arg``  
  :option:`-fdump-ada-spec`[:option:`-slim`] :option:`-fada-spec-parent=```unit`` :option:`-fdump-go-spec=```file``

*C Language Options*
  See :ref:`Options Controlling C Dialect <c-dialect-options>`.

  :option:`-ansi`  :option:`-std=```standard``  :option:`-fgnu89-inline` 
  :option:`-aux-info` ``filename`` :option:`-fallow-parameterless-variadic-functions` 
  :option:`-fno-asm`  :option:`-fno-builtin`  :option:`-fno-builtin-```function`` 
  :option:`-fhosted`  :option:`-ffreestanding` :option:`-fopenacc` :option:`-fopenmp` :option:`-fopenmp-simd` 
  :option:`-fms-extensions` :option:`-fplan9-extensions` :option:`-trigraphs` :option:`-traditional` :option:`-traditional-cpp` 
  :option:`-fallow-single-precision`  :option:`-fcond-mismatch` :option:`-flax-vector-conversions` 
  :option:`-fsigned-bitfields`  :option:`-fsigned-char` 
  :option:`-funsigned-bitfields`  :option:`-funsigned-char`

*C++ Language Options*
  See :ref:`Options Controlling C++ Dialect <c++-dialect-options>`.

  :option:`-fabi-version=```n``  :option:`-fno-access-control`  :option:`-fcheck-new` 
  :option:`-fconstexpr-depth=```n``  :option:`-ffriend-injection` 
  :option:`-fno-elide-constructors` 
  :option:`-fno-enforce-eh-specs` 
  :option:`-ffor-scope`  :option:`-fno-for-scope`  :option:`-fno-gnu-keywords` 
  :option:`-fno-implicit-templates` 
  :option:`-fno-implicit-inline-templates` 
  :option:`-fno-implement-inlines`  :option:`-fms-extensions` 
  :option:`-fno-nonansi-builtins`  :option:`-fnothrow-opt`  :option:`-fno-operator-names` 
  :option:`-fno-optional-diags`  :option:`-fpermissive` 
  :option:`-fno-pretty-templates` 
  :option:`-frepo`  :option:`-fno-rtti` :option:`-fsized-deallocation` 
  :option:`-fstats`  :option:`-ftemplate-backtrace-limit=```n`` 
  :option:`-ftemplate-depth=```n`` 
  :option:`-fno-threadsafe-statics`  :option:`-fuse-cxa-atexit` 
  :option:`-fno-weak`  :option:`-nostdinc++` 
  :option:`-fvisibility-inlines-hidden` 
  :option:`-fvtable-verify=`[std|preinit|none] 
  :option:`-fvtv-counts` :option:`-fvtv-debug` 
  :option:`-fvisibility-ms-compat` 
  :option:`-fext-numeric-literals` 
  :option:`-Wabi=```n``  :option:`-Wabi-tag`  :option:`-Wconversion-null`  :option:`-Wctor-dtor-privacy` 
  :option:`-Wdelete-non-virtual-dtor` :option:`-Wliteral-suffix` :option:`-Wnarrowing` 
  :option:`-Wnoexcept` :option:`-Wnon-virtual-dtor`  :option:`-Wreorder` 
  :option:`-Weffc++`  :option:`-Wstrict-null-sentinel` 
  :option:`-Wno-non-template-friend`  :option:`-Wold-style-cast` 
  :option:`-Woverloaded-virtual`  :option:`-Wno-pmf-conversions` 
  :option:`-Wsign-promo`

*Objective-C and Objective-C++ Language Options*
  See :ref:`Options Controlling
  Objective-C and Objective-C++ Dialects <objective-c-and-objective-c++-dialect-options>`.

  :option:`-fconstant-string-class=```class:option:`-name``` 
  :option:`-fgnu-runtime`  :option:`-fnext-runtime` 
  :option:`-fno-nil-receivers` 
  :option:`-fobjc-abi-version=```n`` 
  :option:`-fobjc-call-cxx-cdtors` 
  :option:`-fobjc-direct-dispatch` 
  :option:`-fobjc-exceptions` 
  :option:`-fobjc-gc` 
  :option:`-fobjc-nilcheck` 
  :option:`-fobjc-std=objc1` 
  :option:`-fno-local-ivars` 
  :option:`-fivar-visibility=`[public|protected|private|package] 
  :option:`-freplace-objc-classes` 
  :option:`-fzero-link` 
  :option:`-gen-decls` 
  :option:`-Wassign-intercept` 
  :option:`-Wno-protocol`  :option:`-Wselector` 
  :option:`-Wstrict-selector-match` 
  :option:`-Wundeclared-selector`

*Language Independent Options*
  See :ref:`Options to Control Diagnostic Messages Formatting <language-independent-options>`.

  :option:`-fmessage-length=```n``  
  :option:`-fdiagnostics-show-location=`[once|every:option:`-line`]  
  :option:`-fdiagnostics-color=`[auto|never|always]  
  :option:`-fno-diagnostics-show-option` :option:`-fno-diagnostics-show-caret`

*Warning Options*
  See :ref:`Options to Request or Suppress Warnings <warning-options>`.

  :option:`-fsyntax-only`  :option:`-fmax-errors=```n``  :option:`-Wpedantic` 
  :option:`-pedantic-errors` 
  :option:`-w`  :option:`-Wextra`  :option:`-Wall`  :option:`-Waddress`  :option:`-Waggregate-return`  
  :option:`-Waggressive-loop-optimizations` :option:`-Warray-bounds` :option:`-Warray-bounds=```n`` 
  :option:`-Wbool-compare` 
  :option:`-Wno-attributes` :option:`-Wno-builtin-macro-redefined` 
  :option:`-Wc90-c99-compat` :option:`-Wc99-c11-compat` 
  :option:`-Wc++-compat` :option:`-Wc++11-compat` :option:`-Wc++14-compat` :option:`-Wcast-align`  :option:`-Wcast-qual`  
  :option:`-Wchar-subscripts` :option:`-Wclobbered`  :option:`-Wcomment` :option:`-Wconditionally-supported`  
  :option:`-Wconversion` :option:`-Wcoverage-mismatch` :option:`-Wdate-time` :option:`-Wdelete-incomplete` :option:`-Wno-cpp`  
  :option:`-Wno-deprecated` :option:`-Wno-deprecated-declarations` :option:`-Wno-designated-init` 
  :option:`-Wdisabled-optimization` 
  :option:`-Wno-discarded-qualifiers` :option:`-Wno-discarded-array-qualifiers` 
  :option:`-Wno-div-by-zero` :option:`-Wdouble-promotion` :option:`-Wempty-body`  :option:`-Wenum-compare` 
  :option:`-Wno-endif-labels` :option:`-Werror`  :option:`-Werror=*` 
  :option:`-Wfatal-errors`  :option:`-Wfloat-equal`  :option:`-Wformat`  :option:`-Wformat=2` 
  :option:`-Wno-format-contains-nul` :option:`-Wno-format-extra-args` :option:`-Wformat-nonliteral` 
  :option:`-Wformat-security`  :option:`-Wformat-signedness`  :option:`-Wformat-y2k` 
  :option:`-Wframe-larger-than=```len`` :option:`-Wno-free-nonheap-object` :option:`-Wjump-misses-init` 
  :option:`-Wignored-qualifiers`  :option:`-Wincompatible-pointer-types` 
  :option:`-Wimplicit`  :option:`-Wimplicit-function-declaration`  :option:`-Wimplicit-int` 
  :option:`-Winit-self`  :option:`-Winline`  :option:`-Wno-int-conversion` 
  :option:`-Wno-int-to-pointer-cast` :option:`-Wno-invalid-offsetof` 
  :option:`-Winvalid-pch` :option:`-Wlarger-than=```len``  :option:`-Wunsafe-loop-optimizations` 
  :option:`-Wlogical-op` :option:`-Wlogical-not-parentheses` :option:`-Wlong-long` 
  :option:`-Wmain` :option:`-Wmaybe-uninitialized` :option:`-Wmemset-transposed-args` :option:`-Wmissing-braces` 
  :option:`-Wmissing-field-initializers` :option:`-Wmissing-include-dirs` 
  :option:`-Wno-multichar`  :option:`-Wnonnull`  :option:`-Wnormalized=`[none|id|nfc|nfkc] 
  :option:`-Wodr`  :option:`-Wno-overflow`  :option:`-Wopenmp-simd` 
  :option:`-Woverride-init-side-effects` 
  :option:`-Woverlength-strings`  :option:`-Wpacked`  :option:`-Wpacked-bitfield-compat`  :option:`-Wpadded` 
  :option:`-Wparentheses`  :option:`-Wpedantic-ms-format` :option:`-Wno-pedantic-ms-format` 
  :option:`-Wpointer-arith`  :option:`-Wno-pointer-to-int-cast` 
  :option:`-Wredundant-decls`  :option:`-Wno-return-local-addr` 
  :option:`-Wreturn-type`  :option:`-Wsequence-point`  :option:`-Wshadow`  :option:`-Wno-shadow-ivar` 
  :option:`-Wshift-count-negative` :option:`-Wshift-count-overflow` :option:`-Wshift-negative-value` 
  :option:`-Wsign-compare`  :option:`-Wsign-conversion` :option:`-Wfloat-conversion` 
  :option:`-Wsizeof-pointer-memaccess`  :option:`-Wsizeof-array-argument` 
  :option:`-Wstack-protector` :option:`-Wstack-usage=```len`` :option:`-Wstrict-aliasing` 
  :option:`-Wstrict-aliasing=n`  :option:`-Wstrict-overflow` :option:`-Wstrict-overflow=```n`` 
  :option:`-Wsuggest-attribute=`[pure|const|noreturn|format] 
  :option:`-Wsuggest-final-types`  :option:`-Wsuggest-final-methods` :option:`-Wsuggest-override` 
  :option:`-Wmissing-format-attribute` 
  :option:`-Wswitch`  :option:`-Wswitch-default`  :option:`-Wswitch-enum` :option:`-Wswitch-bool` :option:`-Wsync-nand` 
  :option:`-Wsystem-headers`  :option:`-Wtrampolines`  :option:`-Wtrigraphs`  :option:`-Wtype-limits`  :option:`-Wundef` 
  :option:`-Wuninitialized`  :option:`-Wunknown-pragmas`  :option:`-Wno-pragmas` 
  :option:`-Wunsuffixed-float-constants`  :option:`-Wunused`  :option:`-Wunused-function` 
  :option:`-Wunused-label`  :option:`-Wunused-local-typedefs` :option:`-Wunused-parameter` 
  :option:`-Wno-unused-result` :option:`-Wunused-value`  :option:`-Wunused-variable` 
  :option:`-Wunused-but-set-parameter` :option:`-Wunused-but-set-variable` 
  :option:`-Wuseless-cast` :option:`-Wvariadic-macros` :option:`-Wvector-operation-performance` 
  :option:`-Wvla` :option:`-Wvolatile-register-var`  :option:`-Wwrite-strings` 
  :option:`-Wzero-as-null-pointer-constant`

*C and Objective-C-only Warning Options*
  :option:`-Wbad-function-cast`  :option:`-Wmissing-declarations` 
  :option:`-Wmissing-parameter-type`  :option:`-Wmissing-prototypes`  :option:`-Wnested-externs` 
  :option:`-Wold-style-declaration`  :option:`-Wold-style-definition` 
  :option:`-Wstrict-prototypes`  :option:`-Wtraditional`  :option:`-Wtraditional-conversion` 
  :option:`-Wdeclaration-after-statement` :option:`-Wpointer-sign`

*Debugging Options*
  See :ref:`Options for Debugging Your Program or GCC <debugging-options>`.

  :option:`-d```letters``  :option:`-dumpspecs`  :option:`-dumpmachine`  :option:`-dumpversion` 
  :option:`-fsanitize=```style`` :option:`-fsanitize-recover` :option:`-fsanitize-recover=```style`` 
  :option:`-fasan-shadow-offset=```number`` :option:`-fsanitize-sections=```s1,s2,...`` 
  :option:`-fsanitize-undefined-trap-on-error` 
  :option:`-fcheck-pointer-bounds` :option:`-fchkp-check-incomplete-type` 
  :option:`-fchkp-first-field-has-own-bounds` :option:`-fchkp-narrow-bounds` 
  :option:`-fchkp-narrow-to-innermost-array` :option:`-fchkp-optimize` 
  :option:`-fchkp-use-fast-string-functions` :option:`-fchkp-use-nochk-string-functions` 
  :option:`-fchkp-use-static-bounds` :option:`-fchkp-use-static-const-bounds` 
  :option:`-fchkp-treat-zero-dynamic-size-as-infinite` :option:`-fchkp-check-read` 
  :option:`-fchkp-check-read` :option:`-fchkp-check-write` :option:`-fchkp-store-bounds` 
  :option:`-fchkp-instrument-calls` :option:`-fchkp-instrument-marked-only` 
  :option:`-fchkp-use-wrappers` 
  :option:`-fdbg-cnt-list` :option:`-fdbg-cnt=```counter:option:`-value-list``` 
  :option:`-fdisable-ipa-```pass_name`` 
  :option:`-fdisable-rtl-```pass_name`` 
  :option:`-fdisable-rtl-```pass:option:`-name```=``range:option:`-list``` 
  :option:`-fdisable-tree-```pass_name`` 
  :option:`-fdisable-tree-```pass:option:`-name```=``range:option:`-list``` 
  :option:`-fdump-noaddr` :option:`-fdump-unnumbered` :option:`-fdump-unnumbered-links` 
  :option:`-fdump-translation-unit`[-``n``] 
  :option:`-fdump-class-hierarchy`[-``n``] 
  :option:`-fdump-ipa-all` :option:`-fdump-ipa-cgraph` :option:`-fdump-ipa-inline` 
  :option:`-fdump-passes` 
  :option:`-fdump-statistics` 
  :option:`-fdump-tree-all` 
  :option:`-fdump-tree-original`[-``n``]  
  :option:`-fdump-tree-optimized`[-``n``] 
  :option:`-fdump-tree-cfg` :option:`-fdump-tree-alias` 
  :option:`-fdump-tree-ch` 
  :option:`-fdump-tree-ssa`[-``n``] :option:`-fdump-tree-pre`[-``n``] 
  :option:`-fdump-tree-ccp`[-``n``] :option:`-fdump-tree-dce`[-``n``] 
  :option:`-fdump-tree-gimple`[:option:`-raw`] 
  :option:`-fdump-tree-dom`[-``n``] 
  :option:`-fdump-tree-dse`[-``n``] 
  :option:`-fdump-tree-phiprop`[-``n``] 
  :option:`-fdump-tree-phiopt`[-``n``] 
  :option:`-fdump-tree-forwprop`[-``n``] 
  :option:`-fdump-tree-copyrename`[-``n``] 
  :option:`-fdump-tree-nrv` :option:`-fdump-tree-vect` 
  :option:`-fdump-tree-sink` 
  :option:`-fdump-tree-sra`[-``n``] 
  :option:`-fdump-tree-forwprop`[-``n``] 
  :option:`-fdump-tree-fre`[-``n``] 
  :option:`-fdump-tree-vtable-verify` 
  :option:`-fdump-tree-vrp`[-``n``] 
  :option:`-fdump-tree-storeccp`[-``n``] 
  :option:`-fdump-final-insns=```file`` 
  :option:`-fcompare-debug`[=``opts``]  :option:`-fcompare-debug-second` 
  :option:`-feliminate-dwarf2-dups` :option:`-fno-eliminate-unused-debug-types` 
  :option:`-feliminate-unused-debug-symbols` :option:`-femit-class-debug-always` 
  :option:`-fenable-```kind``-``pass`` 
  :option:`-fenable-```kind``-``pass``=``range:option:`-list``` 
  :option:`-fdebug-types-section` :option:`-fmem-report-wpa` 
  :option:`-fmem-report` :option:`-fpre-ipa-mem-report` :option:`-fpost-ipa-mem-report` :option:`-fprofile-arcs` 
  :option:`-fopt-info` 
  :option:`-fopt-info-```options``[=``file``] 
  :option:`-frandom-seed=```number`` :option:`-fsched-verbose=```n`` 
  :option:`-fsel-sched-verbose` :option:`-fsel-sched-dump-cfg` :option:`-fsel-sched-pipelining-verbose` 
  :option:`-fstack-usage`  :option:`-ftest-coverage`  :option:`-ftime-report` :option:`-fvar-tracking` 
  :option:`-fvar-tracking-assignments`  :option:`-fvar-tracking-assignments-toggle` 
  :option:`-g`  :option:`-g```level``  :option:`-gtoggle`  :option:`-gcoff`  :option:`-gdwarf-```version`` 
  :option:`-ggdb`  :option:`-grecord-gcc-switches`  :option:`-gno-record-gcc-switches` 
  :option:`-gstabs`  :option:`-gstabs+`  :option:`-gstrict-dwarf`  :option:`-gno-strict-dwarf` 
  :option:`-gvms`  :option:`-gxcoff`  :option:`-gxcoff+` :option:`-gz`[=``type``] 
  :option:`-fno-merge-debug-strings` :option:`-fno-dwarf2-cfi-asm` 
  :option:`-fdebug-prefix-map=```old``=``new`` 
  :option:`-femit-struct-debug-baseonly` :option:`-femit-struct-debug-reduced` 
  :option:`-femit-struct-debug-detailed`[=``spec:option:`-list```] 
  :option:`-p`  :option:`-pg`  :option:`-print-file-name=```library``  :option:`-print-libgcc-file-name` 
  :option:`-print-multi-directory`  :option:`-print-multi-lib`  :option:`-print-multi-os-directory` 
  :option:`-print-prog-name=```program``  :option:`-print-search-dirs`  :option:`-Q` 
  :option:`-print-sysroot` :option:`-print-sysroot-headers-suffix` 
  :option:`-save-temps` :option:`-save-temps=cwd` :option:`-save-temps=obj` :option:`-time`[=``file``]

*Optimization Options*
  See :ref:`Options that Control Optimization <optimize-options>`.

  :option:`-faggressive-loop-optimizations` :option:`-falign-functions[=```n``] 
  :option:`-falign-jumps[=```n``] 
  :option:`-falign-labels[=```n``] :option:`-falign-loops[=```n``] 
  :option:`-fassociative-math` :option:`-fauto-profile` :option:`-fauto-profile[=```path``] 
  :option:`-fauto-inc-dec` :option:`-fbranch-probabilities` 
  :option:`-fbranch-target-load-optimize` :option:`-fbranch-target-load-optimize2` 
  :option:`-fbtr-bb-exclusive` :option:`-fcaller-saves` 
  :option:`-fcheck-data-deps` :option:`-fcombine-stack-adjustments` :option:`-fconserve-stack` 
  :option:`-fcompare-elim` :option:`-fcprop-registers` :option:`-fcrossjumping` 
  :option:`-fcse-follow-jumps` :option:`-fcse-skip-blocks` :option:`-fcx-fortran-rules` 
  :option:`-fcx-limited-range` 
  :option:`-fdata-sections` :option:`-fdce` :option:`-fdelayed-branch` 
  :option:`-fdelete-null-pointer-checks` :option:`-fdevirtualize` :option:`-fdevirtualize-speculatively` 
  :option:`-fdevirtualize-at-ltrans` :option:`-fdse` 
  :option:`-fearly-inlining` :option:`-fipa-sra` :option:`-fexpensive-optimizations` :option:`-ffat-lto-objects` 
  :option:`-ffast-math` :option:`-ffinite-math-only` :option:`-ffloat-store` :option:`-fexcess-precision=```style`` 
  :option:`-fforward-propagate` :option:`-ffp-contract=```style`` :option:`-ffunction-sections` 
  :option:`-fgcse` :option:`-fgcse-after-reload` :option:`-fgcse-las` :option:`-fgcse-lm` :option:`-fgraphite-identity` 
  :option:`-fgcse-sm` :option:`-fhoist-adjacent-loads` :option:`-fif-conversion` 
  :option:`-fif-conversion2` :option:`-findirect-inlining` 
  :option:`-finline-functions` :option:`-finline-functions-called-once` :option:`-finline-limit=```n`` 
  :option:`-finline-small-functions` :option:`-fipa-cp` :option:`-fipa-cp-clone` :option:`-fipa-cp-alignment` 
  :option:`-fipa-pta` :option:`-fipa-profile` :option:`-fipa-pure-const` :option:`-fipa-reference` :option:`-fipa-icf` 
  :option:`-fira-algorithm=```algorithm`` 
  :option:`-fira-region=```region`` :option:`-fira-hoist-pressure` 
  :option:`-fira-loop-pressure` :option:`-fno-ira-share-save-slots` 
  :option:`-fno-ira-share-spill-slots` :option:`-fira-verbose=```n`` 
  :option:`-fisolate-erroneous-paths-dereference` :option:`-fisolate-erroneous-paths-attribute` 
  :option:`-fivopts` :option:`-fkeep-inline-functions` :option:`-fkeep-static-consts` 
  :option:`-flive-range-shrinkage` 
  :option:`-floop-block` :option:`-floop-interchange` :option:`-floop-strip-mine` 
  :option:`-floop-unroll-and-jam` :option:`-floop-nest-optimize` 
  :option:`-floop-parallelize-all` :option:`-flra-remat` :option:`-flto` :option:`-flto-compression-level` 
  :option:`-flto-partition=```alg`` :option:`-flto-report` :option:`-flto-report-wpa` :option:`-fmerge-all-constants` 
  :option:`-fmerge-constants` :option:`-fmodulo-sched` :option:`-fmodulo-sched-allow-regmoves` 
  :option:`-fmove-loop-invariants` :option:`-fno-branch-count-reg` 
  :option:`-fno-defer-pop` :option:`-fno-function-cse` :option:`-fno-guess-branch-probability` 
  :option:`-fno-inline` :option:`-fno-math-errno` :option:`-fno-peephole` :option:`-fno-peephole2` 
  :option:`-fno-sched-interblock` :option:`-fno-sched-spec` :option:`-fno-signed-zeros` 
  :option:`-fno-toplevel-reorder` :option:`-fno-trapping-math` :option:`-fno-zero-initialized-in-bss` 
  :option:`-fomit-frame-pointer` :option:`-foptimize-sibling-calls` 
  :option:`-fpartial-inlining` :option:`-fpeel-loops` :option:`-fpredictive-commoning` 
  :option:`-fprefetch-loop-arrays` :option:`-fprofile-report` 
  :option:`-fprofile-correction` :option:`-fprofile-dir=```path`` :option:`-fprofile-generate` 
  :option:`-fprofile-generate=```path`` 
  :option:`-fprofile-use` :option:`-fprofile-use=```path`` :option:`-fprofile-values` 
  :option:`-fprofile-reorder-functions` 
  :option:`-freciprocal-math` :option:`-free` :option:`-frename-registers` :option:`-freorder-blocks` 
  :option:`-freorder-blocks-and-partition` :option:`-freorder-functions` 
  :option:`-frerun-cse-after-loop` :option:`-freschedule-modulo-scheduled-loops` 
  :option:`-frounding-math` :option:`-fsched2-use-superblocks` :option:`-fsched-pressure` 
  :option:`-fsched-spec-load` :option:`-fsched-spec-load-dangerous` 
  :option:`-fsched-stalled-insns-dep[=```n``] :option:`-fsched-stalled-insns[=```n``] 
  :option:`-fsched-group-heuristic` :option:`-fsched-critical-path-heuristic` 
  :option:`-fsched-spec-insn-heuristic` :option:`-fsched-rank-heuristic` 
  :option:`-fsched-last-insn-heuristic` :option:`-fsched-dep-count-heuristic` 
  :option:`-fschedule-fusion` 
  :option:`-fschedule-insns` :option:`-fschedule-insns2` :option:`-fsection-anchors` 
  :option:`-fselective-scheduling` :option:`-fselective-scheduling2` 
  :option:`-fsel-sched-pipelining` :option:`-fsel-sched-pipelining-outer-loops` 
  :option:`-fsemantic-interposition` 
  :option:`-fshrink-wrap` :option:`-fsignaling-nans` :option:`-fsingle-precision-constant` 
  :option:`-fsplit-ivs-in-unroller` :option:`-fsplit-wide-types` :option:`-fssa-phiopt` 
  :option:`-fstack-protector` :option:`-fstack-protector-all` :option:`-fstack-protector-strong` 
  :option:`-fstack-protector-explicit` :option:`-fstdarg-opt` :option:`-fstrict-aliasing` 
  :option:`-fstrict-overflow` :option:`-fthread-jumps` :option:`-ftracer` :option:`-ftree-bit-ccp` 
  :option:`-ftree-builtin-call-dce` :option:`-ftree-ccp` :option:`-ftree-ch` 
  :option:`-ftree-coalesce-inline-vars` :option:`-ftree-coalesce-vars` :option:`-ftree-copy-prop` 
  :option:`-ftree-copyrename` :option:`-ftree-dce` :option:`-ftree-dominator-opts` :option:`-ftree-dse` 
  :option:`-ftree-forwprop` :option:`-ftree-fre` :option:`-ftree-loop-if-convert` 
  :option:`-ftree-loop-if-convert-stores` :option:`-ftree-loop-im` 
  :option:`-ftree-phiprop` :option:`-ftree-loop-distribution` :option:`-ftree-loop-distribute-patterns` 
  :option:`-ftree-loop-ivcanon` :option:`-ftree-loop-linear` :option:`-ftree-loop-optimize` 
  :option:`-ftree-loop-vectorize` 
  :option:`-ftree-parallelize-loops=```n`` :option:`-ftree-pre` :option:`-ftree-partial-pre` :option:`-ftree-pta` 
  :option:`-ftree-reassoc` :option:`-ftree-sink` :option:`-ftree-slsr` :option:`-ftree-sra` 
  :option:`-ftree-switch-conversion` :option:`-ftree-tail-merge` :option:`-ftree-ter` 
  :option:`-ftree-vectorize` :option:`-ftree-vrp` 
  :option:`-funit-at-a-time` :option:`-funroll-all-loops` :option:`-funroll-loops` 
  :option:`-funsafe-loop-optimizations` :option:`-funsafe-math-optimizations` :option:`-funswitch-loops` 
  :option:`-fipa-ra` :option:`-fvariable-expansion-in-unroller` :option:`-fvect-cost-model` :option:`-fvpt` 
  :option:`-fweb` :option:`-fwhole-program` :option:`-fwpa` :option:`-fuse-linker-plugin` 
  :option:`--param` ``name``=``value``
  :option:`-O`  :option:`-O0`  :option:`-O1`  :option:`-O2`  :option:`-O3`  :option:`-Os` :option:`-Ofast` :option:`-Og`

*Preprocessor Options*
  See :ref:`Options Controlling the Preprocessor <preprocessor-options>`.

  :option:`-A```question``=``answer`` 
  :option:`-A-```question``[=``answer``] 
  :option:`-C`  :option:`-dD`  :option:`-dI`  :option:`-dM`  :option:`-dN` 
  :option:`-D```macro``[=``defn``]  :option:`-E`  :option:`-H` 
  :option:`-idirafter` ``dir`` 
  :option:`-include` ``file``  :option:`-imacros` ``file`` 
  :option:`-iprefix` ``file``  :option:`-iwithprefix` ``dir`` 
  :option:`-iwithprefixbefore` ``dir``  :option:`-isystem` ``dir`` 
  :option:`-imultilib` ``dir`` :option:`-isysroot` ``dir`` 
  :option:`-M`  :option:`-MM`  :option:`-MF`  :option:`-MG`  :option:`-MP`  :option:`-MQ`  :option:`-MT`  :option:`-nostdinc`  
  :option:`-P`  :option:`-fdebug-cpp` :option:`-ftrack-macro-expansion` :option:`-fworking-directory` 
  :option:`-remap` :option:`-trigraphs`  :option:`-undef`  :option:`-U```macro``  
  :option:`-Wp,```option`` :option:`-Xpreprocessor` ``option`` :option:`-no-integrated-cpp`

*Assembler Option*
  See :ref:`Passing Options to the Assembler <assembler-options>`.

  :option:`-Wa,```option``  :option:`-Xassembler` ``option``

*Linker Options*
  See :ref:`Options for Linking <link-options>`.

  .. code-block:: c++

    ``object-file-name``  -fuse-ld=``linker`` -l``library`` 
    -nostartfiles  -nodefaultlibs  -nostdlib -pie -rdynamic 
    -s  -static -static-libgcc -static-libstdc++ 
    -static-libasan -static-libtsan -static-liblsan -static-libubsan 
    -static-libmpx -static-libmpxwrappers 
    -shared -shared-libgcc  -symbolic 
    -T ``script``  -Wl,``option``  -Xlinker ``option`` 
    -u ``symbol`` -z ``keyword``

*Directory Options*
  See :ref:`Options for Directory Search <directory-options>`.

  :option:`-B```prefix`` :option:`-I```dir`` :option:`-iplugindir=```dir`` 
  :option:`-iquote```dir`` :option:`-L```dir`` :option:`-specs=```file`` :option:`-I-` 
  :option:`--sysroot=```dir`` :option:`--no-sysroot-suffix`

*Machine Dependent Options*
  See :ref:`Hardware Models and Configurations <submodel-options>`.

  .. This list is ordered alphanumerically by subsection name.

  .. Try and put the significant identifier (CPU or system) first,

  .. so users have a clue at guessing where the ones they want will be.

  *AArch64 Options*

  :option:`-mabi=```name``  :option:`-mbig-endian`  :option:`-mlittle-endian` 
  :option:`-mgeneral-regs-only` 
  :option:`-mcmodel=tiny`  :option:`-mcmodel=small`  :option:`-mcmodel=large` 
  :option:`-mstrict-align` 
  :option:`-momit-leaf-frame-pointer`  :option:`-mno-omit-leaf-frame-pointer` 
  :option:`-mtls-dialect=desc`  :option:`-mtls-dialect=traditional` 
  :option:`-mfix-cortex-a53-835769`  :option:`-mno-fix-cortex-a53-835769` 
  :option:`-mfix-cortex-a53-843419`  :option:`-mno-fix-cortex-a53-843419` 
  :option:`-march=```name``  :option:`-mcpu=```name``  :option:`-mtune=```name``
  *Adapteva Epiphany Options*

  :option:`-mhalf-reg-file` :option:`-mprefer-short-insn-regs` 
  :option:`-mbranch-cost=```num`` :option:`-mcmove` :option:`-mnops=```num`` :option:`-msoft-cmpsf` 
  :option:`-msplit-lohi` :option:`-mpost-inc` :option:`-mpost-modify` :option:`-mstack-offset=```num`` 
  :option:`-mround-nearest` :option:`-mlong-calls` :option:`-mshort-calls` :option:`-msmall16` 
  :option:`-mfp-mode=```mode`` :option:`-mvect-double` :option:`-max-vect-align=```num`` 
  :option:`-msplit-vecmove-early` :option:`-m1reg-```reg``
  *ARC Options*

  :option:`-mbarrel-shifter` 
  :option:`-mcpu=```cpu`` :option:`-mA6` :option:`-mARC600` :option:`-mA7` :option:`-mARC700` 
  :option:`-mdpfp` :option:`-mdpfp-compact` :option:`-mdpfp-fast` :option:`-mno-dpfp-lrsr` 
  :option:`-mea` :option:`-mno-mpy` :option:`-mmul32x16` :option:`-mmul64` 
  :option:`-mnorm` :option:`-mspfp` :option:`-mspfp-compact` :option:`-mspfp-fast` :option:`-msimd` :option:`-msoft-float` :option:`-mswap` 
  :option:`-mcrc` :option:`-mdsp-packa` :option:`-mdvbf` :option:`-mlock` :option:`-mmac-d16` :option:`-mmac-24` :option:`-mrtsc` :option:`-mswape` 
  :option:`-mtelephony` :option:`-mxy` :option:`-misize` :option:`-mannotate-align` :option:`-marclinux` :option:`-marclinux_prof` 
  :option:`-mepilogue-cfi` :option:`-mlong-calls` :option:`-mmedium-calls` :option:`-msdata` 
  :option:`-mucb-mcount` :option:`-mvolatile-cache` 
  :option:`-malign-call` :option:`-mauto-modify-reg` :option:`-mbbit-peephole` :option:`-mno-brcc` 
  :option:`-mcase-vector-pcrel` :option:`-mcompact-casesi` :option:`-mno-cond-exec` :option:`-mearly-cbranchsi` 
  :option:`-mexpand-adddi` :option:`-mindexed-loads` :option:`-mlra` :option:`-mlra-priority-none` 
  :option:`-mlra-priority-compact` mlra:option:`-priority-noncompact` :option:`-mno-millicode` 
  :option:`-mmixed-code` :option:`-mq-class` :option:`-mRcq` :option:`-mRcw` :option:`-msize-level=```level`` 
  :option:`-mtune=```cpu`` :option:`-mmultcost=```num`` :option:`-munalign-prob-threshold=```probability``
  *ARM Options*

  :option:`-mapcs-frame`  :option:`-mno-apcs-frame` 
  :option:`-mabi=```name`` 
  :option:`-mapcs-stack-check`  :option:`-mno-apcs-stack-check` 
  :option:`-mapcs-float`  :option:`-mno-apcs-float` 
  :option:`-mapcs-reentrant`  :option:`-mno-apcs-reentrant` 
  :option:`-msched-prolog`  :option:`-mno-sched-prolog` 
  :option:`-mlittle-endian`  :option:`-mbig-endian` 
  :option:`-mfloat-abi=```name`` 
  :option:`-mfp16-format=```name``
  :option:`-mthumb-interwork`  :option:`-mno-thumb-interwork` 
  :option:`-mcpu=```name``  :option:`-march=```name``  :option:`-mfpu=```name``  
  :option:`-mtune=```name`` :option:`-mprint-tune-info` 
  :option:`-mstructure-size-boundary=```n`` 
  :option:`-mabort-on-noreturn` 
  :option:`-mlong-calls`  :option:`-mno-long-calls` 
  :option:`-msingle-pic-base`  :option:`-mno-single-pic-base` 
  :option:`-mpic-register=```reg`` 
  :option:`-mnop-fun-dllimport` 
  :option:`-mpoke-function-name` 
  :option:`-mthumb`  :option:`-marm` 
  :option:`-mtpcs-frame`  :option:`-mtpcs-leaf-frame` 
  :option:`-mcaller-super-interworking`  :option:`-mcallee-super-interworking` 
  :option:`-mtp=```name`` :option:`-mtls-dialect=```dialect`` 
  :option:`-mword-relocations` 
  :option:`-mfix-cortex-m3-ldrd` 
  :option:`-munaligned-access` 
  :option:`-mneon-for-64bits` 
  :option:`-mslow-flash-data` 
  :option:`-masm-syntax-unified` 
  :option:`-mrestrict-it`
  *AVR Options*

  :option:`-mmcu=```mcu`` :option:`-maccumulate-args` :option:`-mbranch-cost=```cost`` 
  :option:`-mcall-prologues` :option:`-mint8` :option:`-mn_flash=```size`` :option:`-mno-interrupts` 
  :option:`-mrelax` :option:`-mrmw` :option:`-mstrict-X` :option:`-mtiny-stack` :option:`-nodevicelib` :option:`-Waddr-space-convert`
  *Blackfin Options*

  :option:`-mcpu=```cpu``[-``sirevision``] 
  :option:`-msim` :option:`-momit-leaf-frame-pointer`  :option:`-mno-omit-leaf-frame-pointer` 
  :option:`-mspecld-anomaly`  :option:`-mno-specld-anomaly`  :option:`-mcsync-anomaly`  :option:`-mno-csync-anomaly` 
  :option:`-mlow-64k` :option:`-mno-low64k`  :option:`-mstack-check-l1`  :option:`-mid-shared-library` 
  :option:`-mno-id-shared-library`  :option:`-mshared-library-id=```n`` 
  :option:`-mleaf-id-shared-library`  :option:`-mno-leaf-id-shared-library` 
  :option:`-msep-data`  :option:`-mno-sep-data`  :option:`-mlong-calls`  :option:`-mno-long-calls` 
  :option:`-mfast-fp` :option:`-minline-plt` :option:`-mmulticore`  :option:`-mcorea`  :option:`-mcoreb`  :option:`-msdram` 
  :option:`-micplb`
  *C6X Options*

  :option:`-mbig-endian`  :option:`-mlittle-endian` :option:`-march=```cpu`` 
  :option:`-msim` :option:`-msdata=```sdata:option:`-type```
  *CRIS Options*

  :option:`-mcpu=```cpu``  :option:`-march=```cpu``  :option:`-mtune=```cpu`` 
  :option:`-mmax-stack-frame=```n``  :option:`-melinux-stacksize=```n`` 
  :option:`-metrax4`  :option:`-metrax100`  :option:`-mpdebug`  :option:`-mcc-init`  :option:`-mno-side-effects` 
  :option:`-mstack-align`  :option:`-mdata-align`  :option:`-mconst-align` 
  :option:`-m32-bit`  :option:`-m16-bit`  :option:`-m8-bit`  :option:`-mno-prologue-epilogue`  :option:`-mno-gotplt` 
  :option:`-melf`  :option:`-maout`  :option:`-melinux`  :option:`-mlinux`  :option:`-sim`  :option:`-sim2` 
  :option:`-mmul-bug-workaround`  :option:`-mno-mul-bug-workaround`
  *CR16 Options*

  :option:`-mmac` 
  :option:`-mcr16cplus` :option:`-mcr16c` 
  :option:`-msim` :option:`-mint32` :option:`-mbit-ops`
  :option:`-mdata-model=```model``
  *Darwin Options*

  :option:`-all_load`  :option:`-allowable_client`  :option:`-arch`  :option:`-arch_errors_fatal` 
  :option:`-arch_only`  :option:`-bind_at_load`  :option:`-bundle`  :option:`-bundle_loader` 
  :option:`-client_name`  :option:`-compatibility_version`  :option:`-current_version` 
  :option:`-dead_strip` 
  :option:`-dependency-file`  :option:`-dylib_file`  :option:`-dylinker_install_name` 
  :option:`-dynamic`  :option:`-dynamiclib`  :option:`-exported_symbols_list` 
  :option:`-filelist`  :option:`-flat_namespace`  :option:`-force_cpusubtype_ALL` 
  :option:`-force_flat_namespace`  :option:`-headerpad_max_install_names` 
  :option:`-iframework` 
  :option:`-image_base`  :option:`-init`  :option:`-install_name`  :option:`-keep_private_externs` 
  :option:`-multi_module`  :option:`-multiply_defined`  :option:`-multiply_defined_unused` 
  :option:`-noall_load`   :option:`-no_dead_strip_inits_and_terms` 
  :option:`-nofixprebinding` :option:`-nomultidefs`  :option:`-noprebind`  :option:`-noseglinkedit` 
  :option:`-pagezero_size`  :option:`-prebind`  :option:`-prebind_all_twolevel_modules` 
  :option:`-private_bundle`  :option:`-read_only_relocs`  :option:`-sectalign` 
  :option:`-sectobjectsymbols`  :option:`-whyload`  :option:`-seg1addr` 
  :option:`-sectcreate`  :option:`-sectobjectsymbols`  :option:`-sectorder` 
  :option:`-segaddr` :option:`-segs_read_only_addr` :option:`-segs_read_write_addr` 
  :option:`-seg_addr_table`  :option:`-seg_addr_table_filename`  :option:`-seglinkedit` 
  :option:`-segprot`  :option:`-segs_read_only_addr`  :option:`-segs_read_write_addr` 
  :option:`-single_module`  :option:`-static`  :option:`-sub_library`  :option:`-sub_umbrella` 
  :option:`-twolevel_namespace`  :option:`-umbrella`  :option:`-undefined` 
  :option:`-unexported_symbols_list`  :option:`-weak_reference_mismatches` 
  :option:`-whatsloaded` :option:`-F` :option:`-gused` :option:`-gfull` :option:`-mmacosx-version-min=```version`` 
  :option:`-mkernel` :option:`-mone-byte-bool`
  *DEC Alpha Options*

  :option:`-mno-fp-regs`  :option:`-msoft-float` 
  :option:`-mieee`  :option:`-mieee-with-inexact`  :option:`-mieee-conformant` 
  :option:`-mfp-trap-mode=```mode``  :option:`-mfp-rounding-mode=```mode`` 
  :option:`-mtrap-precision=```mode``  :option:`-mbuild-constants` 
  :option:`-mcpu=```cpu:option:`-type```  :option:`-mtune=```cpu:option:`-type``` 
  :option:`-mbwx`  :option:`-mmax`  :option:`-mfix`  :option:`-mcix` 
  :option:`-mfloat-vax`  :option:`-mfloat-ieee` 
  :option:`-mexplicit-relocs`  :option:`-msmall-data`  :option:`-mlarge-data` 
  :option:`-msmall-text`  :option:`-mlarge-text` 
  :option:`-mmemory-latency=```time``
  *FR30 Options*

  :option:`-msmall-model` :option:`-mno-lsim`
  *FRV Options*

  :option:`-mgpr-32`  :option:`-mgpr-64`  :option:`-mfpr-32`  :option:`-mfpr-64` 
  :option:`-mhard-float`  :option:`-msoft-float` 
  :option:`-malloc-cc`  :option:`-mfixed-cc`  :option:`-mdword`  :option:`-mno-dword` 
  :option:`-mdouble`  :option:`-mno-double` 
  :option:`-mmedia`  :option:`-mno-media`  :option:`-mmuladd`  :option:`-mno-muladd` 
  :option:`-mfdpic`  :option:`-minline-plt` :option:`-mgprel-ro`  :option:`-multilib-library-pic` 
  :option:`-mlinked-fp`  :option:`-mlong-calls`  :option:`-malign-labels` 
  :option:`-mlibrary-pic`  :option:`-macc-4`  :option:`-macc-8` 
  :option:`-mpack`  :option:`-mno-pack`  :option:`-mno-eflags`  :option:`-mcond-move`  :option:`-mno-cond-move` 
  :option:`-moptimize-membar` :option:`-mno-optimize-membar` 
  :option:`-mscc`  :option:`-mno-scc`  :option:`-mcond-exec`  :option:`-mno-cond-exec` 
  :option:`-mvliw-branch`  :option:`-mno-vliw-branch` 
  :option:`-mmulti-cond-exec`  :option:`-mno-multi-cond-exec`  :option:`-mnested-cond-exec` 
  :option:`-mno-nested-cond-exec`  :option:`-mtomcat-stats` 
  :option:`-mTLS` :option:`-mtls` 
  :option:`-mcpu=```cpu``
  *GNU/Linux Options*

  :option:`-mglibc` :option:`-muclibc` :option:`-mmusl` :option:`-mbionic` :option:`-mandroid` 
  :option:`-tno-android-cc` :option:`-tno-android-ld`
  *H8/300 Options*

  :option:`-mrelax`  :option:`-mh`  :option:`-ms`  :option:`-mn`  :option:`-mexr` :option:`-mno-exr`  :option:`-mint32`  :option:`-malign-300`
  *HPPA Options*

  :option:`-march=```architecture:option:`-type``` 
  :option:`-mdisable-fpregs`  :option:`-mdisable-indexing` 
  :option:`-mfast-indirect-calls`  :option:`-mgas`  :option:`-mgnu-ld`   :option:`-mhp-ld` 
  :option:`-mfixed-range=```register:option:`-range``` 
  :option:`-mjump-in-delay` :option:`-mlinker-opt` :option:`-mlong-calls` 
  :option:`-mlong-load-store`  :option:`-mno-disable-fpregs` 
  :option:`-mno-disable-indexing`  :option:`-mno-fast-indirect-calls`  :option:`-mno-gas` 
  :option:`-mno-jump-in-delay`  :option:`-mno-long-load-store` 
  :option:`-mno-portable-runtime`  :option:`-mno-soft-float` 
  :option:`-mno-space-regs`  :option:`-msoft-float`  :option:`-mpa-risc-1-0` 
  :option:`-mpa-risc-1-1`  :option:`-mpa-risc-2-0`  :option:`-mportable-runtime` 
  :option:`-mschedule=```cpu:option:`-type```  :option:`-mspace-regs`  :option:`-msio`  :option:`-mwsio` 
  :option:`-munix=```unix:option:`-std```  :option:`-nolibdld`  :option:`-static`  :option:`-threads`
  *IA-64 Options*

  :option:`-mbig-endian`  :option:`-mlittle-endian`  :option:`-mgnu-as`  :option:`-mgnu-ld`  :option:`-mno-pic` 
  :option:`-mvolatile-asm-stop`  :option:`-mregister-names`  :option:`-msdata` :option:`-mno-sdata` 
  :option:`-mconstant-gp`  :option:`-mauto-pic`  :option:`-mfused-madd` 
  :option:`-minline-float-divide-min-latency` 
  :option:`-minline-float-divide-max-throughput` 
  :option:`-mno-inline-float-divide` 
  :option:`-minline-int-divide-min-latency` 
  :option:`-minline-int-divide-max-throughput`  
  :option:`-mno-inline-int-divide` 
  :option:`-minline-sqrt-min-latency` :option:`-minline-sqrt-max-throughput` 
  :option:`-mno-inline-sqrt` 
  :option:`-mdwarf2-asm` :option:`-mearly-stop-bits` 
  :option:`-mfixed-range=```register:option:`-range``` :option:`-mtls-size=```tls:option:`-size``` 
  :option:`-mtune=```cpu:option:`-type``` :option:`-milp32` :option:`-mlp64` 
  :option:`-msched-br-data-spec` :option:`-msched-ar-data-spec` :option:`-msched-control-spec` 
  :option:`-msched-br-in-data-spec` :option:`-msched-ar-in-data-spec` :option:`-msched-in-control-spec` 
  :option:`-msched-spec-ldc` :option:`-msched-spec-control-ldc` 
  :option:`-msched-prefer-non-data-spec-insns` :option:`-msched-prefer-non-control-spec-insns` 
  :option:`-msched-stop-bits-after-every-cycle` :option:`-msched-count-spec-in-critical-path` 
  :option:`-msel-sched-dont-check-control-spec` :option:`-msched-fp-mem-deps-zero-cost` 
  :option:`-msched-max-memory-insns-hard-limit` :option:`-msched-max-memory-insns=```max:option:`-insns```
  *LM32 Options*

  :option:`-mbarrel-shift-enabled` :option:`-mdivide-enabled` :option:`-mmultiply-enabled` 
  :option:`-msign-extend-enabled` :option:`-muser-enabled`
  *M32R/D Options*

  :option:`-m32r2` :option:`-m32rx` :option:`-m32r` 
  :option:`-mdebug` 
  :option:`-malign-loops` :option:`-mno-align-loops` 
  :option:`-missue-rate=```number`` 
  :option:`-mbranch-cost=```number`` 
  :option:`-mmodel=```code:option:`-size-model-type``` 
  :option:`-msdata=```sdata:option:`-type``` 
  :option:`-mno-flush-func` :option:`-mflush-func=```name`` 
  :option:`-mno-flush-trap` :option:`-mflush-trap=```number`` 
  :option:`-G` ``num``
  *M32C Options*

  :option:`-mcpu=```cpu`` :option:`-msim` :option:`-memregs=```number``
  *M680x0 Options*

  :option:`-march=```arch``  :option:`-mcpu=```cpu``  :option:`-mtune=```tune`` 
  :option:`-m68000`  :option:`-m68020`  :option:`-m68020-40`  :option:`-m68020-60`  :option:`-m68030`  :option:`-m68040` 
  :option:`-m68060`  :option:`-mcpu32`  :option:`-m5200`  :option:`-m5206e`  :option:`-m528x`  :option:`-m5307`  :option:`-m5407` 
  :option:`-mcfv4e`  :option:`-mbitfield`  :option:`-mno-bitfield`  :option:`-mc68000`  :option:`-mc68020` 
  :option:`-mnobitfield`  :option:`-mrtd`  :option:`-mno-rtd`  :option:`-mdiv`  :option:`-mno-div`  :option:`-mshort` 
  :option:`-mno-short`  :option:`-mhard-float`  :option:`-m68881`  :option:`-msoft-float`  :option:`-mpcrel` 
  :option:`-malign-int`  :option:`-mstrict-align`  :option:`-msep-data`  :option:`-mno-sep-data` 
  :option:`-mshared-library-id=n`  :option:`-mid-shared-library`  :option:`-mno-id-shared-library` 
  :option:`-mxgot` :option:`-mno-xgot`
  *MCore Options*

  :option:`-mhardlit`  :option:`-mno-hardlit`  :option:`-mdiv`  :option:`-mno-div`  :option:`-mrelax-immediates` 
  :option:`-mno-relax-immediates`  :option:`-mwide-bitfields`  :option:`-mno-wide-bitfields` 
  :option:`-m4byte-functions`  :option:`-mno-4byte-functions`  :option:`-mcallgraph-data` 
  :option:`-mno-callgraph-data`  :option:`-mslow-bytes`  :option:`-mno-slow-bytes`  :option:`-mno-lsim` 
  :option:`-mlittle-endian`  :option:`-mbig-endian`  :option:`-m210`  :option:`-m340`  :option:`-mstack-increment`
  *MeP Options*

  :option:`-mabsdiff` :option:`-mall-opts` :option:`-maverage` :option:`-mbased=```n`` :option:`-mbitops` 
  :option:`-mc=```n`` :option:`-mclip` :option:`-mconfig=```name`` :option:`-mcop` :option:`-mcop32` :option:`-mcop64` :option:`-mivc2` 
  :option:`-mdc` :option:`-mdiv` :option:`-meb` :option:`-mel` :option:`-mio-volatile` :option:`-ml` :option:`-mleadz` :option:`-mm` :option:`-mminmax` 
  :option:`-mmult` :option:`-mno-opts` :option:`-mrepeat` :option:`-ms` :option:`-msatur` :option:`-msdram` :option:`-msim` :option:`-msimnovec` :option:`-mtf` 
  :option:`-mtiny=```n``
  *MicroBlaze Options*

  :option:`-msoft-float` :option:`-mhard-float` :option:`-msmall-divides` :option:`-mcpu=```cpu`` 
  :option:`-mmemcpy` :option:`-mxl-soft-mul` :option:`-mxl-soft-div` :option:`-mxl-barrel-shift` 
  :option:`-mxl-pattern-compare` :option:`-mxl-stack-check` :option:`-mxl-gp-opt` :option:`-mno-clearbss` 
  :option:`-mxl-multiply-high` :option:`-mxl-float-convert` :option:`-mxl-float-sqrt` 
  :option:`-mbig-endian` :option:`-mlittle-endian` :option:`-mxl-reorder` :option:`-mxl-mode-```app:option:`-model```
  *MIPS Options*

  :option:`-EL`  :option:`-EB`  :option:`-march=```arch``  :option:`-mtune=```arch`` 
  :option:`-mips1`  :option:`-mips2`  :option:`-mips3`  :option:`-mips4`  :option:`-mips32`  :option:`-mips32r2`  :option:`-mips32r3`  :option:`-mips32r5` 
  :option:`-mips32r6`  :option:`-mips64`  :option:`-mips64r2`  :option:`-mips64r3`  :option:`-mips64r5`  :option:`-mips64r6` 
  :option:`-mips16`  :option:`-mno-mips16`  :option:`-mflip-mips16` 
  :option:`-minterlink-compressed` :option:`-mno-interlink-compressed` 
  :option:`-minterlink-mips16`  :option:`-mno-interlink-mips16` 
  :option:`-mabi=```abi``  :option:`-mabicalls`  :option:`-mno-abicalls` 
  :option:`-mshared`  :option:`-mno-shared`  :option:`-mplt`  :option:`-mno-plt`  :option:`-mxgot`  :option:`-mno-xgot` 
  :option:`-mgp32`  :option:`-mgp64`  :option:`-mfp32`  :option:`-mfpxx`  :option:`-mfp64`  :option:`-mhard-float`  :option:`-msoft-float` 
  :option:`-mno-float`  :option:`-msingle-float`  :option:`-mdouble-float` 
  :option:`-modd-spreg` :option:`-mno-odd-spreg` 
  :option:`-mabs=```mode``  :option:`-mnan=```encoding`` 
  :option:`-mdsp`  :option:`-mno-dsp`  :option:`-mdspr2`  :option:`-mno-dspr2` 
  :option:`-mmcu` :option:`-mmno-mcu` 
  :option:`-meva` :option:`-mno-eva` 
  :option:`-mvirt` :option:`-mno-virt` 
  :option:`-mxpa` :option:`-mno-xpa` 
  :option:`-mmicromips` :option:`-mno-micromips` 
  :option:`-mfpu=```fpu:option:`-type``` 
  :option:`-msmartmips`  :option:`-mno-smartmips` 
  :option:`-mpaired-single`  :option:`-mno-paired-single`  :option:`-mdmx`  :option:`-mno-mdmx` 
  :option:`-mips3d`  :option:`-mno-mips3d`  :option:`-mmt`  :option:`-mno-mt`  :option:`-mllsc`  :option:`-mno-llsc` 
  :option:`-mlong64`  :option:`-mlong32`  :option:`-msym32`  :option:`-mno-sym32` 
  :option:`-G```num``  :option:`-mlocal-sdata`  :option:`-mno-local-sdata` 
  :option:`-mextern-sdata`  :option:`-mno-extern-sdata`  :option:`-mgpopt`  :option:`-mno-gopt` 
  :option:`-membedded-data`  :option:`-mno-embedded-data` 
  :option:`-muninit-const-in-rodata`  :option:`-mno-uninit-const-in-rodata` 
  :option:`-mcode-readable=```setting`` 
  :option:`-msplit-addresses`  :option:`-mno-split-addresses` 
  :option:`-mexplicit-relocs`  :option:`-mno-explicit-relocs` 
  :option:`-mcheck-zero-division`  :option:`-mno-check-zero-division` 
  :option:`-mdivide-traps`  :option:`-mdivide-breaks` 
  :option:`-mmemcpy`  :option:`-mno-memcpy`  :option:`-mlong-calls`  :option:`-mno-long-calls` 
  :option:`-mmad` :option:`-mno-mad` :option:`-mimadd` :option:`-mno-imadd` :option:`-mfused-madd`  :option:`-mno-fused-madd`  :option:`-nocpp` 
  :option:`-mfix-24k` :option:`-mno-fix-24k` 
  :option:`-mfix-r4000`  :option:`-mno-fix-r4000`  :option:`-mfix-r4400`  :option:`-mno-fix-r4400` 
  :option:`-mfix-r10000` :option:`-mno-fix-r10000`  :option:`-mfix-rm7000` :option:`-mno-fix-rm7000` 
  :option:`-mfix-vr4120`  :option:`-mno-fix-vr4120` 
  :option:`-mfix-vr4130`  :option:`-mno-fix-vr4130`  :option:`-mfix-sb1`  :option:`-mno-fix-sb1` 
  :option:`-mflush-func=```func``  :option:`-mno-flush-func` 
  :option:`-mbranch-cost=```num``  :option:`-mbranch-likely`  :option:`-mno-branch-likely` 
  :option:`-mfp-exceptions` :option:`-mno-fp-exceptions` 
  :option:`-mvr4130-align` :option:`-mno-vr4130-align` :option:`-msynci` :option:`-mno-synci` 
  :option:`-mrelax-pic-calls` :option:`-mno-relax-pic-calls` :option:`-mmcount-ra-address`
  *MMIX Options*

  :option:`-mlibfuncs`  :option:`-mno-libfuncs`  :option:`-mepsilon`  :option:`-mno-epsilon`  :option:`-mabi=gnu` 
  :option:`-mabi=mmixware`  :option:`-mzero-extend`  :option:`-mknuthdiv`  :option:`-mtoplevel-symbols` 
  :option:`-melf`  :option:`-mbranch-predict`  :option:`-mno-branch-predict`  :option:`-mbase-addresses` 
  :option:`-mno-base-addresses`  :option:`-msingle-exit`  :option:`-mno-single-exit`
  *MN10300 Options*

  :option:`-mmult-bug`  :option:`-mno-mult-bug` 
  :option:`-mno-am33` :option:`-mam33` :option:`-mam33-2` :option:`-mam34` 
  :option:`-mtune=```cpu:option:`-type``` 
  :option:`-mreturn-pointer-on-d0` 
  :option:`-mno-crt0`  :option:`-mrelax` :option:`-mliw` :option:`-msetlb`
  *Moxie Options*

  :option:`-meb` :option:`-mel` :option:`-mmul.x` :option:`-mno-crt0`
  *MSP430 Options*

  :option:`-msim` :option:`-masm-hex` :option:`-mmcu=` :option:`-mcpu=` :option:`-mlarge` :option:`-msmall` :option:`-mrelax` 
  :option:`-mcode-region=` :option:`-mdata-region=` 
  :option:`-mhwmult=` :option:`-minrt`
  *NDS32 Options*

  :option:`-mbig-endian` :option:`-mlittle-endian` 
  :option:`-mreduced-regs` :option:`-mfull-regs` 
  :option:`-mcmov` :option:`-mno-cmov` 
  :option:`-mperf-ext` :option:`-mno-perf-ext` 
  :option:`-mv3push` :option:`-mno-v3push` 
  :option:`-m16bit` :option:`-mno-16bit` 
  :option:`-misr-vector-size=```num`` 
  :option:`-mcache-block-size=```num`` 
  :option:`-march=```arch`` 
  :option:`-mcmodel=```code:option:`-model``` 
  :option:`-mctor-dtor` :option:`-mrelax`
  *Nios II Options*

  :option:`-G` ``num`` :option:`-mgpopt=```option`` :option:`-mgpopt` :option:`-mno-gpopt` 
  :option:`-mel` :option:`-meb` 
  :option:`-mno-bypass-cache` :option:`-mbypass-cache` 
  :option:`-mno-cache-volatile` :option:`-mcache-volatile` 
  :option:`-mno-fast-sw-div` :option:`-mfast-sw-div` 
  :option:`-mhw-mul` :option:`-mno-hw-mul` :option:`-mhw-mulx` :option:`-mno-hw-mulx` :option:`-mno-hw-div` :option:`-mhw-div` 
  :option:`-mcustom-```insn``=``N`` :option:`-mno-custom-```insn`` 
  :option:`-mcustom-fpu-cfg=```name`` 
  :option:`-mhal` :option:`-msmallc` :option:`-msys-crt0=```name`` :option:`-msys-lib=```name``
  *Nvidia PTX Options*

  :option:`-m32` :option:`-m64` :option:`-mmainkernel`
  *PDP-11 Options*

  :option:`-mfpu`  :option:`-msoft-float`  :option:`-mac0`  :option:`-mno-ac0`  :option:`-m40`  :option:`-m45`  :option:`-m10` 
  :option:`-mbcopy`  :option:`-mbcopy-builtin`  :option:`-mint32`  :option:`-mno-int16` 
  :option:`-mint16`  :option:`-mno-int32`  :option:`-mfloat32`  :option:`-mno-float64` 
  :option:`-mfloat64`  :option:`-mno-float32`  :option:`-mabshi`  :option:`-mno-abshi` 
  :option:`-mbranch-expensive`  :option:`-mbranch-cheap` 
  :option:`-munix-asm`  :option:`-mdec-asm`
  *picoChip Options*

  :option:`-mae=```ae_type`` :option:`-mvliw-lookahead=```N`` 
  :option:`-msymbol-as-address` :option:`-mno-inefficient-warnings`
  *PowerPC Options*
  See RS/6000 and PowerPC Options.

  *RL78 Options*

  :option:`-msim` :option:`-mmul=none` :option:`-mmul=g13` :option:`-mmul=g14` :option:`-mallregs` 
  :option:`-mcpu=g10` :option:`-mcpu=g13` :option:`-mcpu=g14` :option:`-mg10` :option:`-mg13` :option:`-mg14` 
  :option:`-m64bit-doubles` :option:`-m32bit-doubles`
  *RS/6000 and PowerPC Options*

  :option:`-mcpu=```cpu:option:`-type``` 
  :option:`-mtune=```cpu:option:`-type``` 
  :option:`-mcmodel=```code:option:`-model``` 
  :option:`-mpowerpc64` 
  :option:`-maltivec`  :option:`-mno-altivec` 
  :option:`-mpowerpc-gpopt`  :option:`-mno-powerpc-gpopt` 
  :option:`-mpowerpc-gfxopt`  :option:`-mno-powerpc-gfxopt` 
  :option:`-mmfcrf`  :option:`-mno-mfcrf`  :option:`-mpopcntb`  :option:`-mno-popcntb` :option:`-mpopcntd` :option:`-mno-popcntd` 
  :option:`-mfprnd`  :option:`-mno-fprnd` 
  :option:`-mcmpb` :option:`-mno-cmpb` :option:`-mmfpgpr` :option:`-mno-mfpgpr` :option:`-mhard-dfp` :option:`-mno-hard-dfp` 
  :option:`-mfull-toc`   :option:`-mminimal-toc`  :option:`-mno-fp-in-toc`  :option:`-mno-sum-in-toc` 
  :option:`-m64`  :option:`-m32`  :option:`-mxl-compat`  :option:`-mno-xl-compat`  :option:`-mpe` 
  :option:`-malign-power`  :option:`-malign-natural` 
  :option:`-msoft-float`  :option:`-mhard-float`  :option:`-mmultiple`  :option:`-mno-multiple` 
  :option:`-msingle-float` :option:`-mdouble-float` :option:`-msimple-fpu` 
  :option:`-mstring`  :option:`-mno-string`  :option:`-mupdate`  :option:`-mno-update` 
  :option:`-mavoid-indexed-addresses`  :option:`-mno-avoid-indexed-addresses` 
  :option:`-mfused-madd`  :option:`-mno-fused-madd`  :option:`-mbit-align`  :option:`-mno-bit-align` 
  :option:`-mstrict-align`  :option:`-mno-strict-align`  :option:`-mrelocatable` 
  :option:`-mno-relocatable`  :option:`-mrelocatable-lib`  :option:`-mno-relocatable-lib` 
  :option:`-mtoc`  :option:`-mno-toc`  :option:`-mlittle`  :option:`-mlittle-endian`  :option:`-mbig`  :option:`-mbig-endian` 
  :option:`-mdynamic-no-pic`  :option:`-maltivec` :option:`-mswdiv`  :option:`-msingle-pic-base` 
  :option:`-mprioritize-restricted-insns=```priority`` 
  :option:`-msched-costly-dep=```dependence_type`` 
  :option:`-minsert-sched-nops=```scheme`` 
  :option:`-mcall-sysv`  :option:`-mcall-netbsd` 
  :option:`-maix-struct-return`  :option:`-msvr4-struct-return` 
  :option:`-mabi=```abi:option:`-type``` :option:`-msecure-plt` :option:`-mbss-plt` 
  :option:`-mblock-move-inline-limit=```num`` 
  :option:`-misel` :option:`-mno-isel` 
  :option:`-misel=yes`  :option:`-misel=no` 
  :option:`-mspe` :option:`-mno-spe` 
  :option:`-mspe=yes`  :option:`-mspe=no` 
  :option:`-mpaired` 
  :option:`-mgen-cell-microcode` :option:`-mwarn-cell-microcode` 
  :option:`-mvrsave` :option:`-mno-vrsave` 
  :option:`-mmulhw` :option:`-mno-mulhw` 
  :option:`-mdlmzb` :option:`-mno-dlmzb` 
  :option:`-mfloat-gprs=yes`  :option:`-mfloat-gprs=no` :option:`-mfloat-gprs=single` :option:`-mfloat-gprs=double` 
  :option:`-mprototype`  :option:`-mno-prototype` 
  :option:`-msim`  :option:`-mmvme`  :option:`-mads`  :option:`-myellowknife`  :option:`-memb`  :option:`-msdata` 
  :option:`-msdata=```opt``  :option:`-mvxworks`  :option:`-G` ``num``  :option:`-pthread` 
  :option:`-mrecip` :option:`-mrecip=```opt`` :option:`-mno-recip` :option:`-mrecip-precision` 
  :option:`-mno-recip-precision` 
  :option:`-mveclibabi=```type`` :option:`-mfriz` :option:`-mno-friz` 
  :option:`-mpointers-to-nested-functions` :option:`-mno-pointers-to-nested-functions` 
  :option:`-msave-toc-indirect` :option:`-mno-save-toc-indirect` 
  :option:`-mpower8-fusion` :option:`-mno-mpower8-fusion` :option:`-mpower8-vector` :option:`-mno-power8-vector` 
  :option:`-mcrypto` :option:`-mno-crypto` :option:`-mdirect-move` :option:`-mno-direct-move` 
  :option:`-mquad-memory` :option:`-mno-quad-memory` 
  :option:`-mquad-memory-atomic` :option:`-mno-quad-memory-atomic` 
  :option:`-mcompat-align-parm` :option:`-mno-compat-align-parm` 
  :option:`-mupper-regs-df` :option:`-mno-upper-regs-df` :option:`-mupper-regs-sf` :option:`-mno-upper-regs-sf` 
  :option:`-mupper-regs` :option:`-mno-upper-regs`
  *RX Options*

  :option:`-m64bit-doubles`  :option:`-m32bit-doubles`  :option:`-fpu`  :option:`-nofpu`
  :option:`-mcpu=`
  :option:`-mbig-endian-data` :option:`-mlittle-endian-data` 
  :option:`-msmall-data` 
  :option:`-msim`  :option:`-mno-sim`
  :option:`-mas100-syntax` :option:`-mno-as100-syntax`
  :option:`-mrelax`
  :option:`-mmax-constant-size=`
  :option:`-mint-register=`
  :option:`-mpid`
  :option:`-mallow-string-insns` :option:`-mno-allow-string-insns`
  :option:`-mno-warn-multiple-fast-interrupts`
  :option:`-msave-acc-in-interrupts`
  *S/390 and zSeries Options*

  :option:`-mtune=```cpu:option:`-type```  :option:`-march=```cpu:option:`-type``` 
  :option:`-mhard-float`  :option:`-msoft-float`  :option:`-mhard-dfp` :option:`-mno-hard-dfp` 
  :option:`-mlong-double-64` :option:`-mlong-double-128` 
  :option:`-mbackchain`  :option:`-mno-backchain` :option:`-mpacked-stack`  :option:`-mno-packed-stack` 
  :option:`-msmall-exec`  :option:`-mno-small-exec`  :option:`-mmvcle` :option:`-mno-mvcle` 
  :option:`-m64`  :option:`-m31`  :option:`-mdebug`  :option:`-mno-debug`  :option:`-mesa`  :option:`-mzarch` 
  :option:`-mtpf-trace` :option:`-mno-tpf-trace`  :option:`-mfused-madd`  :option:`-mno-fused-madd` 
  :option:`-mwarn-framesize`  :option:`-mwarn-dynamicstack`  :option:`-mstack-size` :option:`-mstack-guard` 
  :option:`-mhotpatch=```halfwords``,``halfwords``
  *Score Options*

  :option:`-meb` :option:`-mel` 
  :option:`-mnhwloop` 
  :option:`-muls` 
  :option:`-mmac` 
  :option:`-mscore5` :option:`-mscore5u` :option:`-mscore7` :option:`-mscore7d`
  *SH Options*

  :option:`-m1`  :option:`-m2`  :option:`-m2e` 
  :option:`-m2a-nofpu` :option:`-m2a-single-only` :option:`-m2a-single` :option:`-m2a` 
  :option:`-m3`  :option:`-m3e` 
  :option:`-m4-nofpu`  :option:`-m4-single-only`  :option:`-m4-single`  :option:`-m4` 
  :option:`-m4a-nofpu` :option:`-m4a-single-only` :option:`-m4a-single` :option:`-m4a` :option:`-m4al` 
  :option:`-m5-64media`  :option:`-m5-64media-nofpu` 
  :option:`-m5-32media`  :option:`-m5-32media-nofpu` 
  :option:`-m5-compact`  :option:`-m5-compact-nofpu` 
  :option:`-mb`  :option:`-ml`  :option:`-mdalign`  :option:`-mrelax` 
  :option:`-mbigtable` :option:`-mfmovd` :option:`-mhitachi` :option:`-mrenesas` :option:`-mno-renesas` :option:`-mnomacsave` 
  :option:`-mieee` :option:`-mno-ieee` :option:`-mbitops`  :option:`-misize`  :option:`-minline-ic_invalidate` :option:`-mpadstruct` 
  :option:`-mspace` :option:`-mprefergot`  :option:`-musermode` :option:`-multcost=```number`` :option:`-mdiv=```strategy`` 
  :option:`-mdivsi3_libfunc=```name`` :option:`-mfixed-range=```register:option:`-range``` 
  :option:`-mindexed-addressing` :option:`-mgettrcost=```number`` :option:`-mpt-fixed` 
  :option:`-maccumulate-outgoing-args` :option:`-minvalid-symbols` 
  :option:`-matomic-model=```atomic:option:`-model``` 
  :option:`-mbranch-cost=```num`` :option:`-mzdcbranch` :option:`-mno-zdcbranch` 
  :option:`-mcbranch-force-delay-slot` 
  :option:`-mfused-madd` :option:`-mno-fused-madd` :option:`-mfsca` :option:`-mno-fsca` :option:`-mfsrra` :option:`-mno-fsrra` 
  :option:`-mpretend-cmove` :option:`-mtas`
  *Solaris 2 Options*

  :option:`-mclear-hwcap` :option:`-mno-clear-hwcap` :option:`-mimpure-text`  :option:`-mno-impure-text` 
  :option:`-pthreads` :option:`-pthread`
  *SPARC Options*

  :option:`-mcpu=```cpu:option:`-type``` 
  :option:`-mtune=```cpu:option:`-type``` 
  :option:`-mcmodel=```code:option:`-model``` 
  :option:`-mmemory-model=```mem:option:`-model``` 
  :option:`-m32`  :option:`-m64`  :option:`-mapp-regs`  :option:`-mno-app-regs` 
  :option:`-mfaster-structs`  :option:`-mno-faster-structs`  :option:`-mflat`  :option:`-mno-flat` 
  :option:`-mfpu`  :option:`-mno-fpu`  :option:`-mhard-float`  :option:`-msoft-float` 
  :option:`-mhard-quad-float`  :option:`-msoft-quad-float` 
  :option:`-mstack-bias`  :option:`-mno-stack-bias` 
  :option:`-munaligned-doubles`  :option:`-mno-unaligned-doubles` 
  :option:`-muser-mode`  :option:`-mno-user-mode` 
  :option:`-mv8plus`  :option:`-mno-v8plus`  :option:`-mvis`  :option:`-mno-vis` 
  :option:`-mvis2`  :option:`-mno-vis2`  :option:`-mvis3`  :option:`-mno-vis3` 
  :option:`-mcbcond` :option:`-mno-cbcond` 
  :option:`-mfmaf`  :option:`-mno-fmaf`  :option:`-mpopc`  :option:`-mno-popc` 
  :option:`-mfix-at697f` :option:`-mfix-ut699`
  *SPU Options*

  :option:`-mwarn-reloc` :option:`-merror-reloc` 
  :option:`-msafe-dma` :option:`-munsafe-dma` 
  :option:`-mbranch-hints` 
  :option:`-msmall-mem` :option:`-mlarge-mem` :option:`-mstdmain` 
  :option:`-mfixed-range=```register:option:`-range``` 
  :option:`-mea32` :option:`-mea64` 
  :option:`-maddress-space-conversion` :option:`-mno-address-space-conversion` 
  :option:`-mcache-size=```cache:option:`-size``` 
  :option:`-matomic-updates` :option:`-mno-atomic-updates`
  *System V Options*

  :option:`-Qy`  :option:`-Qn`  :option:`-YP,```paths``  :option:`-Ym,```dir``
  *TILE-Gx Options*

  :option:`-mcpu=CPU` :option:`-m32` :option:`-m64` :option:`-mbig-endian` :option:`-mlittle-endian` 
  :option:`-mcmodel=```code:option:`-model```
  *TILEPro Options*

  :option:`-mcpu=```cpu`` :option:`-m32`
  *V850 Options*

  :option:`-mlong-calls`  :option:`-mno-long-calls`  :option:`-mep`  :option:`-mno-ep` 
  :option:`-mprolog-function`  :option:`-mno-prolog-function`  :option:`-mspace` 
  :option:`-mtda=```n``  :option:`-msda=```n``  :option:`-mzda=```n`` 
  :option:`-mapp-regs`  :option:`-mno-app-regs` 
  :option:`-mdisable-callt`  :option:`-mno-disable-callt` 
  :option:`-mv850e2v3` :option:`-mv850e2` :option:`-mv850e1` :option:`-mv850es` 
  :option:`-mv850e` :option:`-mv850` :option:`-mv850e3v5` 
  :option:`-mloop` 
  :option:`-mrelax` 
  :option:`-mlong-jumps` 
  :option:`-msoft-float` 
  :option:`-mhard-float` 
  :option:`-mgcc-abi` 
  :option:`-mrh850-abi` 
  :option:`-mbig-switch`
  *VAX Options*

  :option:`-mg`  :option:`-mgnu`  :option:`-munix`
  *Visium Options*

  :option:`-mdebug` :option:`-msim` :option:`-mfpu` :option:`-mno-fpu` :option:`-mhard-float` :option:`-msoft-float` 
  :option:`-mcpu=```cpu:option:`-type``` :option:`-mtune=```cpu:option:`-type``` :option:`-msv-mode` :option:`-muser-mode`
  *VMS Options*

  :option:`-mvms-return-codes` :option:`-mdebug-main=```prefix`` :option:`-mmalloc64` 
  :option:`-mpointer-size=```size``
  *VxWorks Options*

  :option:`-mrtp`  :option:`-non-static`  :option:`-Bstatic`  :option:`-Bdynamic` 
  :option:`-Xbind-lazy`  :option:`-Xbind-now`
  *x86 Options*

  :option:`-mtune=```cpu:option:`-type```  :option:`-march=```cpu:option:`-type``` 
  :option:`-mtune-ctrl=```feature:option:`-list``` :option:`-mdump-tune-features` :option:`-mno-default` 
  :option:`-mfpmath=```unit`` 
  :option:`-masm=```dialect``  :option:`-mno-fancy-math-387` 
  :option:`-mno-fp-ret-in-387`  :option:`-msoft-float` 
  :option:`-mno-wide-multiply`  :option:`-mrtd`  :option:`-malign-double` 
  :option:`-mpreferred-stack-boundary=```num`` 
  :option:`-mincoming-stack-boundary=```num`` 
  :option:`-mcld` :option:`-mcx16` :option:`-msahf` :option:`-mmovbe` :option:`-mcrc32` 
  :option:`-mrecip` :option:`-mrecip=```opt`` 
  :option:`-mvzeroupper` :option:`-mprefer-avx128` 
  :option:`-mmmx`  :option:`-msse`  :option:`-msse2` :option:`-msse3` :option:`-mssse3` :option:`-msse4.1` :option:`-msse4.2` :option:`-msse4` :option:`-mavx` 
  :option:`-mavx2` :option:`-mavx512f` :option:`-mavx512pf` :option:`-mavx512er` :option:`-mavx512cd` :option:`-msha` 
  :option:`-maes` :option:`-mpclmul` :option:`-mfsgsbase` :option:`-mrdrnd` :option:`-mf16c` :option:`-mfma` :option:`-mprefetchwt1` 
  :option:`-mclflushopt` :option:`-mxsavec` :option:`-mxsaves` 
  :option:`-msse4a` :option:`-m3dnow` :option:`-mpopcnt` :option:`-mabm` :option:`-mbmi` :option:`-mtbm` :option:`-mfma4` :option:`-mxop` :option:`-mlzcnt` 
  :option:`-mbmi2` :option:`-mfxsr` :option:`-mxsave` :option:`-mxsaveopt` :option:`-mrtm` :option:`-mlwp` :option:`-mmpx` :option:`-mthreads` 
  :option:`-mno-align-stringops`  :option:`-minline-all-stringops` 
  :option:`-minline-stringops-dynamically` :option:`-mstringop-strategy=```alg`` 
  :option:`-mmemcpy-strategy=```strategy`` :option:`-mmemset-strategy=```strategy`` 
  :option:`-mpush-args`  :option:`-maccumulate-outgoing-args`  :option:`-m128bit-long-double` 
  :option:`-m96bit-long-double` :option:`-mlong-double-64` :option:`-mlong-double-80` :option:`-mlong-double-128` 
  :option:`-mregparm=```num``  :option:`-msseregparm` 
  :option:`-mveclibabi=```type`` :option:`-mvect8-ret-in-mem` 
  :option:`-mpc32` :option:`-mpc64` :option:`-mpc80` :option:`-mstackrealign` 
  :option:`-momit-leaf-frame-pointer`  :option:`-mno-red-zone` :option:`-mno-tls-direct-seg-refs` 
  :option:`-mcmodel=```code:option:`-model``` :option:`-mabi=```name`` :option:`-maddress-mode=```mode`` 
  :option:`-m32` :option:`-m64` :option:`-mx32` :option:`-m16` :option:`-mlarge-data-threshold=```num`` 
  :option:`-msse2avx` :option:`-mfentry` :option:`-mrecord-mcount` :option:`-mnop-mcount` :option:`-m8bit-idiv` 
  :option:`-mavx256-split-unaligned-load` :option:`-mavx256-split-unaligned-store` 
  :option:`-malign-data=```type`` :option:`-mstack-protector-guard=```guard``
  *x86 Windows Options*

  :option:`-mconsole` :option:`-mcygwin` :option:`-mno-cygwin` :option:`-mdll` 
  :option:`-mnop-fun-dllimport` :option:`-mthread` 
  :option:`-municode` :option:`-mwin32` :option:`-mwindows` :option:`-fno-set-stack-executable`
  *Xstormy16 Options*

  :option:`-msim`
  *Xtensa Options*

  :option:`-mconst16` :option:`-mno-const16` 
  :option:`-mfused-madd`  :option:`-mno-fused-madd` 
  :option:`-mforce-no-pic` 
  :option:`-mserialize-volatile`  :option:`-mno-serialize-volatile` 
  :option:`-mtext-section-literals`  :option:`-mno-text-section-literals` 
  :option:`-mtarget-align`  :option:`-mno-target-align` 
  :option:`-mlongcalls`  :option:`-mno-longcalls`
  *zSeries Options*
  See S/390 and zSeries Options.

*Code Generation Options*
  See :ref:`Options for Code Generation Conventions <code-gen-options>`.

  :option:`-fcall-saved-```reg``  :option:`-fcall-used-```reg`` 
  :option:`-ffixed-```reg``  :option:`-fexceptions` 
  :option:`-fnon-call-exceptions`  :option:`-fdelete-dead-exceptions`  :option:`-funwind-tables` 
  :option:`-fasynchronous-unwind-tables` 
  :option:`-fno-gnu-unique` 
  :option:`-finhibit-size-directive`  :option:`-finstrument-functions` 
  :option:`-finstrument-functions-exclude-function-list=```sym``,``sym``,... 
  :option:`-finstrument-functions-exclude-file-list=```file``,``file``,... 
  :option:`-fno-common`  :option:`-fno-ident` 
  :option:`-fpcc-struct-return`  :option:`-fpic`  :option:`-fPIC` :option:`-fpie` :option:`-fPIE` :option:`-fno-plt` 
  :option:`-fno-jump-tables` 
  :option:`-frecord-gcc-switches` 
  :option:`-freg-struct-return`  :option:`-fshort-enums` 
  :option:`-fshort-double`  :option:`-fshort-wchar` 
  :option:`-fverbose-asm`  :option:`-fpack-struct[=```n``]  :option:`-fstack-check` 
  :option:`-fstack-limit-register=```reg``  :option:`-fstack-limit-symbol=```sym`` 
  :option:`-fno-stack-limit` :option:`-fsplit-stack` 
  :option:`-fleading-underscore`  :option:`-ftls-model=```model`` 
  :option:`-fstack-reuse=```reuse_level`` 
  :option:`-ftrapv`  :option:`-fwrapv`  :option:`-fbounds-check` 
  :option:`-fvisibility=`[default|internal|hidden|protected] 
  :option:`-fstrict-volatile-bitfields` :option:`-fsync-libcalls`
