.. _using-assembly-language-with-c:

How to Use Inline Assembly Language in C Code
*********************************************

.. index:: asm keyword

.. index:: assembly language in C

.. index:: inline assembly language

.. index:: mixing assembly language and C

The ``asm`` keyword allows you to embed assembler instructions
within C code.  GCC provides two forms of inline ``asm``
statements.  A :dfn:`basic ``asm``` statement is one with no
operands (see :ref:`basic-asm`), while an :dfn:`extended ``asm```
statement (see :ref:`extended-asm`) includes one or more operands.  
The extended form is preferred for mixing C and assembly language
within a function, but to include assembly language at
top level you must use basic ``asm``.

You can also use the ``asm`` keyword to override the assembler name
for a C symbol, or to place a C variable in a specific register.

.. toctree::

  Inline assembler without operands. <basic-asm>
  Inline assembler with operands. <extended-asm>
  Constraints for ``asm`` operands <constraints>
  Specifying the assembler name to use for a C symbol. <asm-labels>
  Defining variables residing in specified registers. <explicit-reg-vars>
  How GCC calculates the size of an ``asm`` block. <size-of-an-asm>

.. _basic-asm:

Basic Asm - Assembler Instructions Without Operands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index:: basic asm

.. index:: assembly language in C, basic

A basic ``asm`` statement has the following syntax:

.. code-block:: c++

  asm [ volatile ] ( ``AssemblerInstructions`` )

The ``asm`` keyword is a GNU extension.
When writing code that can be compiled with :option:`-ansi` and the
various :option:`-std` options, use ``__asm__`` instead of 
``asm`` (see :ref:`alternate-keywords`).

Qualifiers
^^^^^^^^^^

volatile
  The optional ``volatile`` qualifier has no effect. 
  All basic ``asm`` blocks are implicitly volatile.

Parameters
^^^^^^^^^^

AssemblerInstructions
  This is a literal string that specifies the assembler code. The string can 
  contain any instructions recognized by the assembler, including directives. 
  GCC does not parse the assembler instructions themselves and 
  does not know what they mean or even whether they are valid assembler input.

  You may place multiple assembler instructions together in a single ``asm`` 
  string, separated by the characters normally used in assembly code for the 
  system. A combination that works in most places is a newline to break the 
  line, plus a tab character (written as \n\t).
  Some assemblers allow semicolons as a line separator. However, 
  note that some assembler dialects use semicolons to start a comment. 

Remarks
^^^^^^^

Using extended ``asm`` typically produces smaller, safer, and more
efficient code, and in most cases it is a better solution than basic
``asm``.  However, there are two situations where only basic ``asm``
can be used:

* Extended ``asm`` statements have to be inside a C
  function, so to write inline assembly language at file scope ('top-level'),
  outside of C functions, you must use basic ``asm``.
  You can use this technique to emit assembler directives,
  define assembly language macros that can be invoked elsewhere in the file,
  or write entire functions in assembly language.

* Functions declared
  with the ``naked`` attribute also require basic ``asm``
  (see :ref:`function-attributes`).

Safely accessing C data and calling functions from basic ``asm`` is more 
complex than it may appear. To access C data, it is better to use extended 
``asm``.

Do not expect a sequence of ``asm`` statements to remain perfectly 
consecutive after compilation. If certain instructions need to remain 
consecutive in the output, put them in a single multi-instruction ``asm``
statement. Note that GCC's optimizers can move ``asm`` statements 
relative to other code, including across jumps.

``asm`` statements may not perform jumps into other ``asm`` statements. 
GCC does not know about these jumps, and therefore cannot take 
account of them when deciding how to optimize. Jumps from ``asm`` to C 
labels are only supported in extended ``asm``.

Under certain circumstances, GCC may duplicate (or remove duplicates of) your 
assembly code when optimizing. This can lead to unexpected duplicate 
symbol errors during compilation if your assembly code defines symbols or 
labels.

Since GCC does not parse the ``AssemblerInstructions``, it has no 
visibility of any symbols it references. This may result in GCC discarding 
those symbols as unreferenced.

The compiler copies the assembler instructions in a basic ``asm`` 
verbatim to the assembly language output file, without 
processing dialects or any of the % operators that are available with
extended ``asm``. This results in minor differences between basic 
``asm`` strings and extended ``asm`` templates. For example, to refer to 
registers you might use %eax in basic ``asm`` and
%%eax in extended ``asm``.

On targets such as x86 that support multiple assembler dialects,
all basic ``asm`` blocks use the assembler dialect specified by the 
:option:`-masm` command-line option (see :ref:`x86-options`).  
Basic ``asm`` provides no
mechanism to provide different assembler strings for different dialects.

Here is an example of basic ``asm`` for i386:

.. code-block:: c++

  /* Note that this code will not compile with -masm=intel */
  #define DebugBreak() asm("int $3")

.. _extended-asm:

Extended Asm - Assembler Instructions with C Expression Operands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index:: extended asm

.. index:: assembly language in C, extended

With extended ``asm`` you can read and write C variables from 
assembler and perform jumps from assembler code to C labels.  
Extended ``asm`` syntax uses colons (:) to delimit
the operand parameters after the assembler template:

.. code-block:: c++

  asm [volatile] ( ``AssemblerTemplate`` 
                   : ``OutputOperands`` 
                   [ : ``InputOperands``
                   [ : ``Clobbers`` ] ])

  asm [volatile] goto ( ``AssemblerTemplate`` 
                        : 
                        : ``InputOperands``
                        : ``Clobbers``
                        : ``GotoLabels``)

The ``asm`` keyword is a GNU extension.
When writing code that can be compiled with :option:`-ansi` and the
various :option:`-std` options, use ``__asm__`` instead of 
``asm`` (see :ref:`alternate-keywords`).

Qualifiers
^^^^^^^^^^

volatile
  The typical use of extended ``asm`` statements is to manipulate input 
  values to produce output values. However, your ``asm`` statements may 
  also produce side effects. If so, you may need to use the ``volatile`` 
  qualifier to disable certain optimizations. See :ref:`volatile`.

goto
  This qualifier informs the compiler that the ``asm`` statement may 
  perform a jump to one of the labels listed in the ``GotoLabels``.
  See :ref:`gotolabels`.

Parameters
^^^^^^^^^^

AssemblerTemplate
  This is a literal string that is the template for the assembler code. It is a 
  combination of fixed text and tokens that refer to the input, output, 
  and goto parameters. See :ref:`assemblertemplate`.

OutputOperands
  A comma-separated list of the C variables modified by the instructions in the 
  ``AssemblerTemplate``.  An empty list is permitted.  See :ref:`outputoperands`.

InputOperands
  A comma-separated list of C expressions read by the instructions in the 
  ``AssemblerTemplate``.  An empty list is permitted.  See :ref:`inputoperands`.

Clobbers
  A comma-separated list of registers or other values changed by the 
  ``AssemblerTemplate``, beyond those listed as outputs.
  An empty list is permitted.  See :ref:`clobbers`.

GotoLabels
  When you are using the ``goto`` form of ``asm``, this section contains 
  the list of all C labels to which the code in the 
  ``AssemblerTemplate`` may jump. 
  See :ref:`gotolabels`.

  ``asm`` statements may not perform jumps into other ``asm`` statements,
  only to the listed ``GotoLabels``.
  GCC's optimizers do not know about other jumps; therefore they cannot take 
  account of them when deciding how to optimize.

  The total number of input + output + goto operands is limited to 30.

Remarks
^^^^^^^

The ``asm`` statement allows you to include assembly instructions directly 
within C code. This may help you to maximize performance in time-sensitive 
code or to access assembly instructions that are not readily available to C 
programs.

Note that extended ``asm`` statements must be inside a function. Only 
basic ``asm`` may be outside functions (see :ref:`basic-asm`).
Functions declared with the ``naked`` attribute also require basic 
``asm`` (see :ref:`function-attributes`).

While the uses of ``asm`` are many and varied, it may help to think of an 
``asm`` statement as a series of low-level instructions that convert input 
parameters to output parameters. So a simple (if not particularly useful) 
example for i386 using ``asm`` might look like this:

.. code-block:: c++

  int src = 1;
  int dst;   

  asm ("mov %1, %0\n\t"
      "add $1, %0"
      : "=r" (dst) 
      : "r" (src));

  printf("%d\n", dst);

This code copies ``src`` to ``dst`` and add 1 to ``dst``.

.. _volatile:

Volatile
~~~~~~~~

.. index:: volatile asm

.. index:: asm volatile

GCC's optimizers sometimes discard ``asm`` statements if they determine 
there is no need for the output variables. Also, the optimizers may move 
code out of loops if they believe that the code will always return the same 
result (i.e. none of its input values change between calls). Using the 
``volatile`` qualifier disables these optimizations. ``asm`` statements 
that have no output operands, including ``asm goto`` statements, 
are implicitly volatile.

This i386 code demonstrates a case that does not use (or require) the 
``volatile`` qualifier. If it is performing assertion checking, this code 
uses ``asm`` to perform the validation. Otherwise, ``dwRes`` is 
unreferenced by any code. As a result, the optimizers can discard the 
``asm`` statement, which in turn removes the need for the entire 
``DoCheck`` routine. By omitting the ``volatile`` qualifier when it 
isn't needed you allow the optimizers to produce the most efficient code 
possible.

.. code-block:: c++

  void DoCheck(uint32_t dwSomeValue)
  {
     uint32_t dwRes;

     // Assumes dwSomeValue is not zero.
     asm ("bsfl %1,%0"
       : "=r" (dwRes)
       : "r" (dwSomeValue)
       : "cc");

     assert(dwRes > 3);
  }

The next example shows a case where the optimizers can recognize that the input 
(``dwSomeValue``) never changes during the execution of the function and can 
therefore move the ``asm`` outside the loop to produce more efficient code. 
Again, using ``volatile`` disables this type of optimization.

.. code-block:: c++

  void do_print(uint32_t dwSomeValue)
  {
     uint32_t dwRes;

     for (uint32_t x=0; x < 5; x++)
     {
        // Assumes dwSomeValue is not zero.
        asm ("bsfl %1,%0"
          : "=r" (dwRes)
          : "r" (dwSomeValue)
          : "cc");

        printf("%u: %u %u\n", x, dwSomeValue, dwRes);
     }
  }

The following example demonstrates a case where you need to use the 
``volatile`` qualifier. 
It uses the x86 ``rdtsc`` instruction, which reads 
the computer's time-stamp counter. Without the ``volatile`` qualifier, 
the optimizers might assume that the ``asm`` block will always return the 
same value and therefore optimize away the second call.

.. code-block:: c++

  uint64_t msr;

  asm volatile ( "rdtsc\n\t"    // Returns the time in EDX:EAX.
          "shl $32, %%rdx\n\t"  // Shift the upper bits left.
          "or %%rdx, %0"        // 'Or' in the lower bits.
          : "=a" (msr)
          : 
          : "rdx");

  printf("msr: %llx\n", msr);

  // Do other work...

  // Reprint the timestamp
  asm volatile ( "rdtsc\n\t"    // Returns the time in EDX:EAX.
          "shl $32, %%rdx\n\t"  // Shift the upper bits left.
          "or %%rdx, %0"        // 'Or' in the lower bits.
          : "=a" (msr)
          : 
          : "rdx");

  printf("msr: %llx\n", msr);

GCC's optimizers do not treat this code like the non-volatile code in the 
earlier examples. They do not move it out of loops or omit it on the 
assumption that the result from a previous call is still valid.

Note that the compiler can move even volatile ``asm`` instructions relative 
to other code, including across jump instructions. For example, on many 
targets there is a system register that controls the rounding mode of 
floating-point operations. Setting it with a volatile ``asm``, as in the 
following PowerPC example, does not work reliably.

.. code-block:: c++

  asm volatile("mtfsf 255, %0" : : "f" (fpenv));
  sum = x + y;

The compiler may move the addition back before the volatile ``asm``. To 
make it work as expected, add an artificial dependency to the ``asm`` by 
referencing a variable in the subsequent code, for example: 

.. code-block:: c++

  asm volatile ("mtfsf 255,%1" : "=X" (sum) : "f" (fpenv));
  sum = x + y;

Under certain circumstances, GCC may duplicate (or remove duplicates of) your 
assembly code when optimizing. This can lead to unexpected duplicate symbol 
errors during compilation if your asm code defines symbols or labels. 
Using %= 
(see :ref:`assemblertemplate`) may help resolve this problem.

.. _assemblertemplate:

Assembler Template
~~~~~~~~~~~~~~~~~~

.. index:: asm assembler template

An assembler template is a literal string containing assembler instructions.
The compiler replaces tokens in the template that refer 
to inputs, outputs, and goto labels,
and then outputs the resulting string to the assembler. The 
string can contain any instructions recognized by the assembler, including 
directives. GCC does not parse the assembler instructions 
themselves and does not know what they mean or even whether they are valid 
assembler input. However, it does count the statements 
(see :ref:`size-of-an-asm`).

You may place multiple assembler instructions together in a single ``asm`` 
string, separated by the characters normally used in assembly code for the 
system. A combination that works in most places is a newline to break the 
line, plus a tab character to move to the instruction field (written as 
\n\t). 
Some assemblers allow semicolons as a line separator. However, note 
that some assembler dialects use semicolons to start a comment. 

Do not expect a sequence of ``asm`` statements to remain perfectly 
consecutive after compilation, even when you are using the ``volatile`` 
qualifier. If certain instructions need to remain consecutive in the output, 
put them in a single multi-instruction asm statement.

Accessing data from C programs without using input/output operands (such as 
by using global symbols directly from the assembler template) may not work as 
expected. Similarly, calling functions directly from an assembler template 
requires a detailed understanding of the target assembler and ABI.

Since GCC does not parse the assembler template,
it has no visibility of any 
symbols it references. This may result in GCC discarding those symbols as 
unreferenced unless they are also listed as input, output, or goto operands.

Special format strings
^^^^^^^^^^^^^^^^^^^^^^

In addition to the tokens described by the input, output, and goto operands, 
these tokens have special meanings in the assembler template:

%% 
  Outputs a single % into the assembler code.

%= 
  Outputs a number that is unique to each instance of the ``asm`` 
  statement in the entire compilation. This option is useful when creating local 
  labels and referring to them multiple times in a single template that 
  generates multiple assembler instructions. 

%{ %| %}
  Outputs {, |, and } characters (respectively)
  into the assembler code.  When unescaped, these characters have special
  meaning to indicate multiple assembler dialects, as described below.

Multiple assembler dialects in ``asm`` templatesOn targets such as x86, GCC supports multiple assembler dialects.
The :option:`-masm` option controls which dialect GCC uses as its 
default for inline assembler. The target-specific documentation for the 
:option:`-masm` option contains the list of supported dialects, as well as the 
default dialect if the option is not specified. This information may be 
important to understand, since assembler code that works correctly when 
compiled using one dialect will likely fail if compiled using another.
See :ref:`x86-options`.

If your code needs to support multiple assembler dialects (for example, if 
you are writing public headers that need to support a variety of compilation 
options), use constructs of this form:

.. code-block:: c++

  { dialect0 | dialect1 | dialect2... }

This construct outputs ``dialect0`` 
when using dialect #0 to compile the code, 
``dialect1`` for dialect #1, etc. If there are fewer alternatives within the 
braces than the number of dialects the compiler supports, the construct 
outputs nothing.

For example, if an x86 compiler supports two dialects
(att, intel), an 
assembler template such as this:

.. code-block:: c++

  "bt{l %[Offset],%[Base] | %[Base],%[Offset]}; jc %l2"

is equivalent to one of

.. code-block:: c++

  "btl %[Offset],%[Base] ; jc %l2"   /* att dialect */
  "bt %[Base],%[Offset]; jc %l2"     /* intel dialect */

Using that same compiler, this code:

.. code-block:: c++

  "xchg{l}\t{%%}ebx, %1"

corresponds to either

.. code-block:: c++

  "xchgl\t%%ebx, %1"                 /* att dialect */
  "xchg\tebx, %1"                    /* intel dialect */

There is no support for nesting dialect alternatives.

.. _outputoperands:

Output Operands
~~~~~~~~~~~~~~~

.. index:: asm output operands

An ``asm`` statement has zero or more output operands indicating the names
of C variables modified by the assembler code.

In this i386 example, ``old`` (referred to in the template string as 
``%0``) and ``*Base`` (as ``%1``) are outputs and ``Offset`` 
(``%2``) is an input:

.. code-block:: c++

  bool old;

  __asm__ ("btsl %2,%1\n\t" // Turn on zero-based bit #Offset in Base.
           "sbb %0,%0"      // Use the CF to calculate old.
     : "=r" (old), "+rm" (*Base)
     : "Ir" (Offset)
     : "cc");

  return old;

Operands are separated by commas.  Each operand has this format:

.. code-block:: c++

  [ [``asmSymbolicName``] ] ``constraint`` (``cvariablename``)

asmSymbolicName
  Specifies a symbolic name for the operand.
  Reference the name in the assembler template 
  by enclosing it in square brackets 
  (i.e. %[Value]). The scope of the name is the ``asm`` statement 
  that contains the definition. Any valid C variable name is acceptable, 
  including names already defined in the surrounding code. No two operands 
  within the same ``asm`` statement can use the same symbolic name.

  When not using an ``asmSymbolicName``, use the (zero-based) position
  of the operand 
  in the list of operands in the assembler template. For example if there are 
  three output operands, use %0 in the template to refer to the first, 
  %1 for the second, and %2 for the third. 

constraint
  A string constant specifying constraints on the placement of the operand; 
  See :ref:`constraints`, for details.

  Output constraints must begin with either = (a variable overwriting an 
  existing value) or + (when reading and writing). When using 
  =, do not assume the location contains the existing value
  on entry to the ``asm``, except 
  when the operand is tied to an input; see :ref:`Input Operands <inputoperands>`.

  After the prefix, there must be one or more additional constraints 
  (see :ref:`constraints`) that describe where the value resides. Common 
  constraints include r for register and m for memory. 
  When you list more than one possible location (for example, ``"=rm"``),
  the compiler chooses the most efficient one based on the current context. 
  If you list as many alternates as the ``asm`` statement allows, you permit 
  the optimizers to produce the best possible code. 
  If you must use a specific register, but your Machine Constraints do not
  provide sufficient control to select the specific register you want, 
  local register variables may provide a solution (see :ref:`local-reg-vars`).

cvariablename
  Specifies a C lvalue expression to hold the output, typically a variable name.
  The enclosing parentheses are a required part of the syntax.

  When the compiler selects the registers to use to 
represent the output operands, it does not use any of the clobbered registers 
(see :ref:`clobbers`).

Output operand expressions must be lvalues. The compiler cannot check whether 
the operands have data types that are reasonable for the instruction being 
executed. For output expressions that are not directly addressable (for 
example a bit-field), the constraint must allow a register. In that case, GCC 
uses the register as the output of the ``asm``, and then stores that 
register into the output. 

Operands using the + constraint modifier count as two operands 
(that is, both as input and output) towards the total maximum of 30 operands
per ``asm`` statement.

Use the & constraint modifier (see :ref:`modifiers`) on all output
operands that must not overlap an input.  Otherwise, 
GCC may allocate the output operand in the same register as an unrelated 
input operand, on the assumption that the assembler code consumes its 
inputs before producing outputs. This assumption may be false if the assembler 
code actually consists of more than one instruction.

The same problem can occur if one output parameter (``a``) allows a register 
constraint and another output parameter (``b``) allows a memory constraint.
The code generated by GCC to access the memory address in ``b`` can contain
registers which *might* be shared by ``a``, and GCC considers those 
registers to be inputs to the asm. As above, GCC assumes that such input
registers are consumed before any outputs are written. This assumption may 
result in incorrect behavior if the asm writes to ``a`` before using 
``b``. Combining the & modifier with the register constraint on ``a``
ensures that modifying ``a`` does not affect the address referenced by 
``b``. Otherwise, the location of ``b`` 
is undefined if ``a`` is modified before using ``b``.

``asm`` supports operand modifiers on operands (for example %k2 
instead of simply %2). Typically these qualifiers are hardware 
dependent. The list of supported modifiers for x86 is found at 
x86Operandmodifiersx86 Operand modifiers.

If the C code that follows the ``asm`` makes no use of any of the output 
operands, use ``volatile`` for the ``asm`` statement to prevent the 
optimizers from discarding the ``asm`` statement as unneeded 
(see Volatile).

This code makes no use of the optional ``asmSymbolicName``. Therefore it 
references the first output operand as ``%0`` (were there a second, it 
would be ``%1``, etc). The number of the first input operand is one greater 
than that of the last output operand. In this i386 example, that makes 
``Mask`` referenced as ``%1``:

.. code-block:: c++

  uint32_t Mask = 1234;
  uint32_t Index;

    asm ("bsfl %1, %0"
       : "=r" (Index)
       : "r" (Mask)
       : "cc");

That code overwrites the variable ``Index`` (=),
placing the value in a register (r).
Using the generic r constraint instead of a constraint for a specific 
register allows the compiler to pick the register to use, which can result 
in more efficient code. This may not be possible if an assembler instruction 
requires a specific register.

The following i386 example uses the ``asmSymbolicName`` syntax.
It produces the 
same result as the code above, but some may consider it more readable or more 
maintainable since reordering index numbers is not necessary when adding or 
removing operands. The names ``aIndex`` and ``aMask``
are only used in this example to emphasize which 
names get used where.
It is acceptable to reuse the names ``Index`` and ``Mask``.

.. code-block:: c++

  uint32_t Mask = 1234;
  uint32_t Index;

    asm ("bsfl %[aMask], %[aIndex]"
       : [aIndex] "=r" (Index)
       : [aMask] "r" (Mask)
       : "cc");

Here are some more examples of output operands.

.. code-block:: c++

  uint32_t c = 1;
  uint32_t d;
  uint32_t *e = &c;

  asm ("mov %[e], %[d]"
     : [d] "=rm" (d)
     : [e] "rm" (*e));

Here, ``d`` may either be in a register or in memory. Since the compiler 
might already have the current value of the ``uint32_t`` location
pointed to by ``e``
in a register, you can enable it to choose the best location
for ``d`` by specifying both constraints.

.. _inputoperands:

Input Operands
~~~~~~~~~~~~~~

.. index:: asm input operands

.. index:: asm expressions

Input operands make values from C variables and expressions available to the 
assembly code.

Operands are separated by commas.  Each operand has this format:

.. code-block:: c++

  [ [``asmSymbolicName``] ] ``constraint`` (``cexpression``)

asmSymbolicName
  Specifies a symbolic name for the operand.
  Reference the name in the assembler template 
  by enclosing it in square brackets 
  (i.e. %[Value]). The scope of the name is the ``asm`` statement 
  that contains the definition. Any valid C variable name is acceptable, 
  including names already defined in the surrounding code. No two operands 
  within the same ``asm`` statement can use the same symbolic name.

  When not using an ``asmSymbolicName``, use the (zero-based) position
  of the operand 
  in the list of operands in the assembler template. For example if there are
  two output operands and three inputs,
  use %2 in the template to refer to the first input operand,
  %3 for the second, and %4 for the third. 

constraint
  A string constant specifying constraints on the placement of the operand; 
  See :ref:`constraints`, for details.

  Input constraint strings may not begin with either = or +.
  When you list more than one possible location (for example, "irm"), 
  the compiler chooses the most efficient one based on the current context.
  If you must use a specific register, but your Machine Constraints do not
  provide sufficient control to select the specific register you want, 
  local register variables may provide a solution (see :ref:`local-reg-vars`).

  Input constraints can also be digits (for example, ``"0"``). This indicates 
  that the specified input must be in the same place as the output constraint 
  at the (zero-based) index in the output constraint list. 
  When using ``asmSymbolicName`` syntax for the output operands,
  you may use these names (enclosed in brackets []) instead of digits.

cexpression
  This is the C variable or expression being passed to the ``asm`` statement 
  as input.  The enclosing parentheses are a required part of the syntax.

  When the compiler selects the registers to use to represent the input 
operands, it does not use any of the clobbered registers (see :ref:`clobbers`).

If there are no output operands but there are input operands, place two 
consecutive colons where the output operands would go:

.. code-block:: c++

  __asm__ ("some instructions"
     : /* No outputs. */
     : "r" (Offset / 8));

Warning: Do *not* modify the contents of input-only operands 
(except for inputs tied to outputs). The compiler assumes that on exit from 
the ``asm`` statement these operands contain the same values as they 
had before executing the statement. 
It is *not* possible to use clobbers
to inform the compiler that the values in these inputs are changing. One 
common work-around is to tie the changing input variable to an output variable 
that never gets used. Note, however, that if the code that follows the 
``asm`` statement makes no use of any of the output operands, the GCC 
optimizers may discard the ``asm`` statement as unneeded 
(see Volatile).

``asm`` supports operand modifiers on operands (for example %k2 
instead of simply %2). Typically these qualifiers are hardware 
dependent. The list of supported modifiers for x86 is found at 
x86Operandmodifiersx86 Operand modifiers.

In this example using the fictitious ``combine`` instruction, the 
constraint ``"0"`` for input operand 1 says that it must occupy the same 
location as output operand 0. Only input operands may use numbers in 
constraints, and they must each refer to an output operand. Only a number (or 
the symbolic assembler name) in the constraint can guarantee that one operand 
is in the same place as another. The mere fact that ``foo`` is the value of 
both operands is not enough to guarantee that they are in the same place in 
the generated assembler code.

.. code-block:: c++

  asm ("combine %2, %0" 
     : "=r" (foo) 
     : "0" (foo), "g" (bar));

Here is an example using symbolic names.

.. code-block:: c++

  asm ("cmoveq %1, %2, %[result]" 
     : [result] "=r"(result) 
     : "r" (test), "r" (new), "[result]" (old));

.. _clobbers:

Clobbers
~~~~~~~~

.. index:: asm clobbers

While the compiler is aware of changes to entries listed in the output 
operands, the inline ``asm`` code may modify more than just the outputs. For 
example, calculations may require additional registers, or the processor may 
overwrite a register as a side effect of a particular assembler instruction. 
In order to inform the compiler of these changes, list them in the clobber 
list. Clobber list items are either register names or the special clobbers 
(listed below). Each clobber list item is a string constant 
enclosed in double quotes and separated by commas.

Clobber descriptions may not in any way overlap with an input or output 
operand. For example, you may not have an operand describing a register class 
with one member when listing that register in the clobber list. Variables 
declared to live in specific registers (see :ref:`explicit-reg-vars`) and used 
as ``asm`` input or output operands must have no part mentioned in the 
clobber description. In particular, there is no way to specify that input 
operands get modified without also specifying them as output operands.

When the compiler selects which registers to use to represent input and output 
operands, it does not use any of the clobbered registers. As a result, 
clobbered registers are available for any use in the assembler code.

Here is a realistic example for the VAX showing the use of clobbered 
registers:

.. code-block:: c++

  asm volatile ("movc3 %0, %1, %2"
                     : /* No outputs. */
                     : "g" (from), "g" (to), "g" (count)
                     : "r0", "r1", "r2", "r3", "r4", "r5");

Also, there are two special clobber arguments:

"cc"
  The ``"cc"`` clobber indicates that the assembler code modifies the flags 
  register. On some machines, GCC represents the condition codes as a specific 
  hardware register; ``"cc"`` serves to name this register.
  On other machines, condition code handling is different, 
  and specifying ``"cc"`` has no effect. But 
  it is valid no matter what the target.

"memory"
  The ``"memory"`` clobber tells the compiler that the assembly code
  performs memory 
  reads or writes to items other than those listed in the input and output 
  operands (for example, accessing the memory pointed to by one of the input 
  parameters). To ensure memory contains correct values, GCC may need to flush 
  specific register values to memory before executing the ``asm``. Further, 
  the compiler does not assume that any values read from memory before an 
  ``asm`` remain unchanged after that ``asm``; it reloads them as 
  needed.  
  Using the ``"memory"`` clobber effectively forms a read/write
  memory barrier for the compiler.

  Note that this clobber does not prevent the *processor* from doing 
  speculative reads past the ``asm`` statement. To prevent that, you need 
  processor-specific fence instructions.

  Flushing registers to memory has performance implications and may be an issue 
  for time-sensitive code.  You can use a trick to avoid this if the size of 
  the memory being accessed is known at compile time. For example, if accessing 
  ten bytes of a string, use a memory input like:

  ``{"m"( ({ struct { char x[10]; } *p = (void *)ptr ; *p; }) )}``.

  .. _gotolabels:

Goto Labels
~~~~~~~~~~~

.. index:: asm goto labels

``asm goto`` allows assembly code to jump to one or more C labels.  The
``GotoLabels`` section in an ``asm goto`` statement contains 
a comma-separated 
list of all C labels to which the assembler code may jump. GCC assumes that 
``asm`` execution falls through to the next statement (if this is not the 
case, consider using the ``__builtin_unreachable`` intrinsic after the 
``asm`` statement). Optimization of ``asm goto`` may be improved by 
using the ``hot`` and ``cold`` label attributes (see :ref:`label--attributes`).

An ``asm goto`` statement cannot have outputs.
This is due to an internal restriction of 
the compiler: control transfer instructions cannot have outputs. 
If the assembler code does modify anything, use the ``"memory"`` clobber 
to force the 
optimizers to flush all register values to memory and reload them if 
necessary after the ``asm`` statement.

Also note that an ``asm goto`` statement is always implicitly
considered volatile.

To reference a label in the assembler template,
prefix it with %l (lowercase L) followed 
by its (zero-based) position in ``GotoLabels`` plus the number of input 
operands.  For example, if the ``asm`` has three inputs and references two 
labels, refer to the first label as %l3 and the second as %l4).

Alternately, you can reference labels using the actual C label name enclosed
in brackets.  For example, to reference a label named ``carry``, you can
use %l[carry].  The label must still be listed in the ``GotoLabels``
section when using this approach.

Here is an example of ``asm goto`` for i386:

.. code-block:: c++

  asm goto (
      "btl %1, %0\n\t"
      "jc %l2"
      : /* No outputs. */
      : "r" (p1), "r" (p2) 
      : "cc" 
      : carry);

  return 0;

  carry:
  return 1;

The following example shows an ``asm goto`` that uses a memory clobber.

.. code-block:: c++

  int frob(int x)
  {
    int y;
    asm goto ("frob %%r5, %1; jc %l[error]; mov (%2), %%r5"
              : /* No outputs. */
              : "r"(x), "r"(&y)
              : "r5", "memory" 
              : error);
    return y;
  error:
    return -1;
  }

.. _x86operandmodifiers:

x86 Operand Modifiers
~~~~~~~~~~~~~~~~~~~~~

References to input, output, and goto operands in the assembler template
of extended ``asm`` statements can use 
modifiers to affect the way the operands are formatted in 
the code output to the assembler. For example, the 
following code uses the h and b modifiers for x86:

.. code-block:: c++

  uint16_t  num;
  asm volatile ("xchg %h0, %b0" : "+a" (num) );

These modifiers generate this assembler code:

.. code-block:: c++

  xchg %ah, %al

The rest of this discussion uses the following code for illustrative purposes.

.. code-block:: c++

  int main()
  {
     int iInt = 1;

  top:

     asm volatile goto ("some assembler instructions here"
     : /* No outputs. */
     : "q" (iInt), "X" (sizeof(unsigned char) + 1)
     : /* No clobbers. */
     : top);
  }

With no modifiers, this is what the output from the operands would be for the 
att and intel dialects of assembler:

=======  ========  ===================
Operand  masm=att  masm=intel
=======  ========  ===================
``%0``   ``%eax``  ``eax``
``%1``   ``$2``    ``2``
``%2``   ``$.L2``  ``OFFSET FLAT:.L2``
=======  ========  ===================
The table below shows the list of supported modifiers and their effects.

========  =====================================================================================================  =======  ========  ==========
Modifier  Description                                                                                            Operand  masm=att  masm=intel
========  =====================================================================================================  =======  ========  ==========
``z``     Print the opcode suffix for the size of the current integer operand (one of ``b``/``w``/``l``/``q``).  ``%z0``  ``l``
``b``     Print the QImode name of the register.                                                                 ``%b0``  ``%al``   ``al``
``h``     Print the QImode name for a 'high' register.                                                           ``%h0``  ``%ah``   ``ah``
``w``     Print the HImode name of the register.                                                                 ``%w0``  ``%ax``   ``ax``
``k``     Print the SImode name of the register.                                                                 ``%k0``  ``%eax``  ``eax``
``q``     Print the DImode name of the register.                                                                 ``%q0``  ``%rax``  ``rax``
``l``     Print the label name with no punctuation.                                                              ``%l2``  ``.L2``   ``.L2``
``c``     Require a constant operand and print the constant expression with no punctuation.                      ``%c1``  ``2``     ``2``
========  =====================================================================================================  =======  ========  ==========
.. _x86floatingpointasmoperands:

x86 Floating-Point ``asm`` OperandsOn x86 targets, there are several rules on the usage of stack-like registers
in the operands of an ``asm``.  These rules apply only to the operands
that are stack-like registers:

* Given a set of input registers that die in an ``asm``, it is
  necessary to know which are implicitly popped by the ``asm``, and
  which must be explicitly popped by GCC.

  An input register that is implicitly popped by the ``asm`` must be
  explicitly clobbered, unless it is constrained to match an
  output operand.

* For any input register that is implicitly popped by an ``asm``, it is
  necessary to know how to adjust the stack to compensate for the pop.
  If any non-popped input is closer to the top of the reg-stack than
  the implicitly popped register, it would not be possible to know what the
  stack looked like-it's not clear how the rest of the stack 'slides
  up'.

  All implicitly popped input registers must be closer to the top of
  the reg-stack than any input that is not implicitly popped.

  It is possible that if an input dies in an ``asm``, the compiler might
  use the input register for an output reload.  Consider this example:

  .. code-block:: c++

    asm ("foo" : "=t" (a) : "f" (b));

  This code says that input ``b`` is not popped by the ``asm``, and that
  the ``asm`` pushes a result onto the reg-stack, i.e., the stack is one
  deeper after the ``asm`` than it was before.  But, it is possible that
  reload may think that it can use the same register for both the input and
  the output.

  To prevent this from happening,
  if any input operand uses the f constraint, all output register
  constraints must use the & early-clobber modifier.

  The example above is correctly written as:

  .. code-block:: c++

    asm ("foo" : "=&t" (a) : "f" (b));

* Some operands need to be in particular places on the stack.  All
  output operands fall in this category-GCC has no other way to
  know which registers the outputs appear in unless you indicate
  this in the constraints.

  Output operands must specifically indicate which register an output
  appears in after an ``asm``.  =f is not allowed: the operand
  constraints must select a class with a single register.

* Output operands may not be 'inserted' between existing stack registers.
  Since no 387 opcode uses a read/write operand, all output operands
  are dead before the ``asm``, and are pushed by the ``asm``.
  It makes no sense to push anywhere but the top of the reg-stack.

  Output operands must start at the top of the reg-stack: output
  operands may not 'skip' a register.

* Some ``asm`` statements may need extra stack space for internal
  calculations.  This can be guaranteed by clobbering stack registers
  unrelated to the inputs and outputs.

This ``asm``
takes one input, which is internally popped, and produces two outputs.

.. code-block:: c++

  asm ("fsincos" : "=t" (cos), "=u" (sin) : "0" (inp));

This ``asm`` takes two inputs, which are popped by the ``fyl2xp1`` opcode,
and replaces them with one output.  The ``st(1)`` clobber is necessary 
for the compiler to know that ``fyl2xp1`` pops both inputs.

.. code-block:: c++

  asm ("fyl2xp1" : "=t" (result) : "0" (x), "u" (y) : "st(1)");

.. Copyright (C) 1988-2015 Free Software Foundation, Inc.
   This is part of the GCC manual.
   For copying conditions, see the file gcc.texi.
   Most of this node appears by itself (in a different place) even
   when the INTERNALS flag is clear.  Passages that require the internals
   manual's context are conditionalized to appear only in the internals manual.

.. _constraints:

Constraints for ``asm`` Operands
.. index:: operand constraints, asm

.. index:: constraints, asm

.. index:: asm constraints

Here are specific details on what constraint letters you can use with
``asm`` operands.
Constraints can say whether
an operand may be in a register, and which kinds of register; whether the
operand can be a memory reference, and which kinds of address; whether the
operand may be an immediate constant, and which possible values it may
have.  Constraints can also require two operands to match.
Side-effects aren't allowed in operands of inline ``asm``, unless
< or > constraints are used, because there is no guarantee
that the side-effects will happen exactly once in an instruction that can update
the addressing register.

.. toctree::

  Basic use of constraints. <simple-constraints>
  When an insn has two alternative constraint-patterns. <multi-alternative>
  More precise control over effects of constraints. <modifiers>
  Special constraints for some particular machines. <machine-constraints>

.. _simple-constraints:

Simple Constraints
~~~~~~~~~~~~~~~~~~

.. index:: simple constraints

The simplest kind of constraint is a string full of letters, each of
which describes one kind of operand that is permitted.  Here are
the letters that are allowed:

whitespace
  Whitespace characters are ignored and can be inserted at any position
  except the first.  This enables each alternative for different operands to
  be visually aligned in the machine description even if they have different
  number of constraints and modifiers.

  .. index:: m in constraint

  .. index:: memory references in constraints

m
  A memory operand is allowed, with any kind of address that the machine
  supports in general.
  Note that the letter used for the general memory constraint can be
  re-defined by a back end using the ``TARGET_MEM_CONSTRAINT`` macro.

  .. index:: offsettable address

  .. index:: o in constraint

o
  A memory operand is allowed, but only if the address is
  :dfn:`offsettable`.  This means that adding a small integer (actually,
  the width in bytes of the operand, as determined by its machine mode)
  may be added to the address and the result is also a valid memory
  address.

  .. index:: autoincrement/decrement addressing

  For example, an address which is constant is offsettable; so is an
  address that is the sum of a register and a constant (as long as a
  slightly larger constant is also within the range of address-offsets
  supported by the machine); but an autoincrement or autodecrement
  address is not offsettable.  More complicated indirect/indexed
  addresses may or may not be offsettable depending on the other
  addressing modes that the machine supports.

  Note that in an output operand which can be matched by another
  operand, the constraint letter o is valid only when accompanied
  by both < (if the target machine has predecrement addressing)
  and > (if the target machine has preincrement addressing).

  .. index:: V in constraint

V
  A memory operand that is not offsettable.  In other words, anything that
  would fit the m constraint but not the o constraint.

  .. index:: < in constraint

<
  A memory operand with autodecrement addressing (either predecrement or
  postdecrement) is allowed.  In inline ``asm`` this constraint is only
  allowed if the operand is used exactly once in an instruction that can
  handle the side-effects.  Not using an operand with < in constraint
  string in the inline ``asm`` pattern at all or using it in multiple
  instructions isn't valid, because the side-effects wouldn't be performed
  or would be performed more than once.  Furthermore, on some targets
  the operand with < in constraint string must be accompanied by
  special instruction suffixes like ``%U0`` instruction suffix on PowerPC
  or ``%P0`` on IA-64.

  .. index:: > in constraint

>
  A memory operand with autoincrement addressing (either preincrement or
  postincrement) is allowed.  In inline ``asm`` the same restrictions
  as for < apply.

  .. index:: r in constraint

  .. index:: registers in constraints

r
  A register operand is allowed provided that it is in a general
  register.

  .. index:: constants in constraints

  .. index:: i in constraint

i
  An immediate integer operand (one with constant value) is allowed.
  This includes symbolic constants whose values will be known only at
  assembly time or later.

  .. index:: n in constraint

n
  An immediate integer operand with a known numeric value is allowed.
  Many systems cannot support assembly-time constants for operands less
  than a word wide.  Constraints for these operands should use n
  rather than i.

  .. index:: I in constraint

I, J, K, ... P
  Other letters in the range I through P may be defined in
  a machine-dependent fashion to permit immediate integer operands with
  explicit integer values in specified ranges.  For example, on the
  68000, I is defined to stand for the range of values 1 to 8.
  This is the range permitted as a shift count in the shift
  instructions.

  .. index:: E in constraint

E
  An immediate floating operand (expression code ``const_double``) is
  allowed, but only if the target floating point format is the same as
  that of the host machine (on which the compiler is running).

  .. index:: F in constraint

F
  An immediate floating operand (expression code ``const_double`` or
  ``const_vector``) is allowed.

  .. index:: G in constraint

  .. index:: H in constraint

G, H
  G and H may be defined in a machine-dependent fashion to
  permit immediate floating operands in particular ranges of values.

  .. index:: s in constraint

s
  An immediate integer operand whose value is not an explicit integer is
  allowed.

  This might appear strange; if an insn allows a constant operand with a
  value not known at compile time, it certainly must allow any known
  value.  So why use s instead of i?  Sometimes it allows
  better code to be generated.

  For example, on the 68000 in a fullword instruction it is possible to
  use an immediate operand; but if the immediate value is between -128
  and 127, better code results from loading the value into a register and
  using the register.  This is because the load into the register can be
  done with a moveq instruction.  We arrange for this to happen
  by defining the letter K to mean 'any integer outside the
  range -128 to 127', and then specifying Ks in the operand
  constraints.

  .. index:: g in constraint

g
  Any register, memory or immediate integer operand is allowed, except for
  registers that are not general registers.

  .. index:: X in constraint

X
  Any operand whatsoever is allowed.

  .. index:: 0 in constraint

  .. index:: digits in constraint

0, 1, 2, ... 9
  An operand that matches the specified operand number is allowed.  If a
  digit is used together with letters within the same alternative, the
  digit should come last.

  This number is allowed to be more than a single digit.  If multiple
  digits are encountered consecutively, they are interpreted as a single
  decimal integer.  There is scant chance for ambiguity, since to-date
  it has never been desirable that 10 be interpreted as matching
  either operand 1 *or* operand 0.  Should this be desired, one
  can use multiple alternatives instead.

  .. index:: matching constraint

  .. index:: constraint, matching

  This is called a :dfn:`matching constraint` and what it really means is
  that the assembler has only a single operand that fills two roles
  which ``asm`` distinguishes.  For example, an add instruction uses
  two input operands and an output operand, but on most CISC
  machines an add instruction really has only two operands, one of them an
  input-output operand:

  .. code-block:: c++

    addl #35,r12

  Matching constraints are used in these circumstances.
  More precisely, the two operands that match must include one input-only
  operand and one output-only operand.  Moreover, the digit must be a
  smaller number than the number of the operand that uses it in the
  constraint.

  .. index:: load address instruction

  .. index:: push address instruction

  .. index:: address constraints

  .. index:: p in constraint

p
  An operand that is a valid memory address is allowed.  This is
  for 'load address' and 'push address' instructions.

  .. index:: address_operand

  p in the constraint must be accompanied by ``address_operand``
  as the predicate in the ``match_operand``.  This predicate interprets
  the mode specified in the ``match_operand`` as the mode of the memory
  reference for which the address would be valid.

  .. index:: other register constraints

  .. index:: extensible constraints

``other-letters``
  Other letters can be defined in machine-dependent fashion to stand for
  particular classes of registers or other arbitrary operand types.
  d, a and f are defined on the 68000/68020 to stand
  for data, address and floating point registers.

  .. _multi-alternative:

Multiple Alternative Constraints
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. index:: multiple alternative constraints

Sometimes a single instruction has multiple alternative sets of possible
operands.  For example, on the 68000, a logical-or instruction can combine
register or an immediate value into memory, or it can combine any kind of
operand into a register; but it cannot combine one memory location into
another.

These constraints are represented as multiple alternatives.  An alternative
can be described by a series of letters for each operand.  The overall
constraint for an operand is made from the letters for this operand
from the first alternative, a comma, the letters for this operand from
the second alternative, a comma, and so on until the last alternative.

.. FIXME Is this ? and ! stuff of use in asm()?  If not, hide unless INTERNAL

If all the operands fit any one alternative, the instruction is valid.
Otherwise, for each alternative, the compiler counts how many instructions
must be added to copy the operands so that that alternative applies.
The alternative requiring the least copying is chosen.  If two alternatives
need the same amount of copying, the one that comes first is chosen.
These choices can be altered with the ? and ! characters:

.. index:: ? in constraint

.. index:: question mark

?
  Disparage slightly the alternative that the ? appears in,
  as a choice when no alternative applies exactly.  The compiler regards
  this alternative as one unit more costly for each ? that appears
  in it.

  .. index:: ! in constraint

  .. index:: exclamation point

!
  Disparage severely the alternative that the ! appears in.
  This alternative can still be used if it fits without reloading,
  but if reloading is needed, some other alternative will be used.

  .. index:: ^ in constraint

  .. index:: caret

^
  This constraint is analogous to ? but it disparages slightly
  the alternative only if the operand with the ^ needs a reload.

  .. index:: $ in constraint

  .. index:: dollar sign

$
  This constraint is analogous to ! but it disparages severely
  the alternative only if the operand with the $ needs a reload.

  .. _modifiers:

Constraint Modifier Characters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. index:: modifiers in constraints

.. index:: constraint modifier characters

.. prevent bad page break with this line

Here are constraint modifier characters.

.. index:: = in constraint

=
  Means that this operand is written to by this instruction:
  the previous value is discarded and replaced by new data.

  .. index:: + in constraint

+
  Means that this operand is both read and written by the instruction.

  When the compiler fixes up the operands to satisfy the constraints,
  it needs to know which operands are read by the instruction and
  which are written by it.  = identifies an operand which is only
  written; + identifies an operand that is both read and written; all
  other operands are assumed to only be read.

  If you specify = or + in a constraint, you put it in the
  first character of the constraint string.

  .. index:: & in constraint

  .. index:: earlyclobber operand

&
  Means (in a particular alternative) that this operand is an
  :dfn:`earlyclobber` operand, which is written before the instruction is
  finished using the input operands.  Therefore, this operand may not lie
  in a register that is read by the instruction or as part of any memory
  address.

  & applies only to the alternative in which it is written.  In
  constraints with multiple alternatives, sometimes one alternative
  requires & while others do not.  See, for example, the
  movdf insn of the 68000.

  A operand which is read by the instruction can be tied to an earlyclobber
  operand if its only use as an input occurs before the early result is
  written.  Adding alternatives of this form often allows GCC to produce
  better code when only some of the read operands can be affected by the
  earlyclobber. See, for example, the mulsi3 insn of the ARM.

  Furthermore, if the :dfn:`earlyclobber` operand is also a read/write
  operand, then that operand is written only after it's used.

  & does not obviate the need to write = or +.  As
  :dfn:`earlyclobber` operands are always written, a read-only
  :dfn:`earlyclobber` operand is ill-formed and will be rejected by the
  compiler.

  .. index:: % in constraint

%
  Declares the instruction to be commutative for this operand and the
  following operand.  This means that the compiler may interchange the
  two operands if that is the cheapest way to make all operands fit the
  constraints.  % applies to all alternatives and must appear as
  the first character in the constraint.  Only read-only operands can use
  %.

  GCC can only handle one commutative pair in an asm; if you use more,
  the compiler may fail.  Note that you need not use the modifier if
  the two alternatives are strictly identical; this would only waste
  time in the reload pass.  The modifier is not operational after
  register allocation, so the result of ``define_peephole2``
  and ``define_split``s performed after reload cannot rely on
  % to make the intended insn match.

  .. index:: # in constraint

#
  Says that all following characters, up to the next comma, are to be
  ignored as a constraint.  They are significant only for choosing
  register preferences.

  .. index:: * in constraint

*
  Says that the following character should be ignored when choosing
  register preferences.  * has no effect on the meaning of the
  constraint as a constraint, and no effect on reloading.  For LRA
  * additionally disparages slightly the alternative if the
  following character matches the operand.

  .. _machine-constraints:

Constraints for Particular Machines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. index:: machine specific constraints

.. index:: constraints, machine specific

Whenever possible, you should use the general-purpose constraint letters
in ``asm`` arguments, since they will convey meaning more readily to
people reading your code.  Failing that, use the constraint letters
that usually have very similar meanings across architectures.  The most
commonly used constraints are m and r (for memory and
general-purpose registers respectively; see :ref:`simple-constraints`), and
I, usually the letter indicating the most common
immediate-constant format.

Each architecture defines additional constraints.  These constraints
are used by the compiler itself for instruction generation, as well as
for ``asm`` statements; therefore, some of the constraints are not
particularly useful for ``asm``.  Here is a summary of some of the
machine-dependent constraints available on some particular machines;
it includes both constraints that are useful for ``asm`` and
constraints that aren't.  The compiler source file mentioned in the
table heading for each architecture is the definitive reference for
the meanings of that architecture's constraints.

.. Please keep this table alphabetized by target!

AArch64 family-config/aarch64/constraints.md

  k
    The stack pointer register (``SP``)

  w
    Floating point or SIMD vector register

  I
    Integer constant that is valid as an immediate operand in an ``ADD``
    instruction

  J
    Integer constant that is valid as an immediate operand in a ``SUB``
    instruction (once negated)

  K
    Integer constant that can be used with a 32-bit logical instruction

  L
    Integer constant that can be used with a 64-bit logical instruction

  M
    Integer constant that is valid as an immediate operand in a 32-bit ``MOV``
    pseudo instruction. The ``MOV`` may be assembled to one of several different
    machine instructions depending on the value

  N
    Integer constant that is valid as an immediate operand in a 64-bit ``MOV``
    pseudo instruction

  S
    An absolute symbolic address or a label reference

  Y
    Floating point constant zero

  Z
    Integer constant zero

  Ush
    The high part (bits 12 and upwards) of the pc-relative address of a symbol
    within 4GB of the instruction

  Q
    A memory address which uses a single base register with no offset

  Ump
    A memory address suitable for a load/store pair instruction in SI, DI, SF and
    DF modes

ARC -config/arc/constraints.md

  q
    Registers usable in ARCompact 16-bit instructions: ``r0``-``r3``,
    ``r12``-``r15``.  This constraint can only match when the :option:`-mq`
    option is in effect.

  e
    Registers usable as base-regs of memory addresses in ARCompact 16-bit memory
    instructions: ``r0``-``r3``, ``r12``-``r15``, ``sp``.
    This constraint can only match when the :option:`-mq`
    option is in effect.

  D
    ARC FPX (dpfp) 64-bit registers. ``D0``, ``D1``.

  I
    A signed 12-bit integer constant.

  Cal
    constant for arithmetic/logical operations.  This might be any constant
    that can be put into a long immediate by the assmbler or linker without
    involving a PIC relocation.

  K
    A 3-bit unsigned integer constant.

  L
    A 6-bit unsigned integer constant.

  CnL
    One's complement of a 6-bit unsigned integer constant.

  CmL
    Two's complement of a 6-bit unsigned integer constant.

  M
    A 5-bit unsigned integer constant.

  O
    A 7-bit unsigned integer constant.

  P
    A 8-bit unsigned integer constant.

  H
    Any const_double value.

ARM family-config/arm/constraints.md

  h
    In Thumb state, the core registers ``r8``-``r15``.

  k
    The stack pointer register.

  l
    In Thumb State the core registers ``r0``-``r7``.  In ARM state this
    is an alias for the ``r`` constraint.

  t
    VFP floating-point registers ``s0``-``s31``.  Used for 32 bit values.

  w
    VFP floating-point registers ``d0``-``d31`` and the appropriate
    subset ``d0``-``d15`` based on command line options.
    Used for 64 bit values only.  Not valid for Thumb1.

  y
    The iWMMX co-processor registers.

  z
    The iWMMX GR registers.

  G
    The floating-point constant 0.0

  I
    Integer that is valid as an immediate operand in a data processing
    instruction.  That is, an integer in the range 0 to 255 rotated by a
    multiple of 2

  J
    Integer in the range -4095 to 4095

  K
    Integer that satisfies constraint I when inverted (ones complement)

  L
    Integer that satisfies constraint I when negated (twos complement)

  M
    Integer in the range 0 to 32

  Q
    A memory reference where the exact address is in a single register
    ('m' is preferable for ``asm`` statements)

  R
    An item in the constant pool

  S
    A symbol in the text segment of the current file

  Uv
    A memory reference suitable for VFP load/store insns (reg+constant offset)

  Uy
    A memory reference suitable for iWMMXt load/store instructions.

  Uq
    A memory reference suitable for the ARMv4 ldrsb instruction.

AVR family-config/avr/constraints.md

  l
    Registers from r0 to r15

  a
    Registers from r16 to r23

  d
    Registers from r16 to r31

  w
    Registers from r24 to r31.  These registers can be used in adiw command

  e
    Pointer register (r26-r31)

  b
    Base pointer register (r28-r31)

  q
    Stack pointer register (SPH:SPL)

  t
    Temporary register r0

  x
    Register pair X (r27:r26)

  y
    Register pair Y (r29:r28)

  z
    Register pair Z (r31:r30)

  I
    Constant greater than -1, less than 64

  J
    Constant greater than -64, less than 1

  K
    Constant integer 2

  L
    Constant integer 0

  M
    Constant that fits in 8 bits

  N
    Constant integer -1

  O
    Constant integer 8, 16, or 24

  P
    Constant integer 1

  G
    A floating point constant 0.0

  Q
    A memory address based on Y or Z pointer with displacement.

Blackfin family-config/bfin/constraints.md

  a
    P register

  d
    D register

  z
    A call clobbered P register.

  q``n``
    A single register.  If ``n`` is in the range 0 to 7, the corresponding D
    register.  If it is ``A``, then the register P0.

  D
    Even-numbered D register

  W
    Odd-numbered D register

  e
    Accumulator register.

  A
    Even-numbered accumulator register.

  B
    Odd-numbered accumulator register.

  b
    I register

  v
    B register

  f
    M register

  c
    Registers used for circular buffering, i.e. I, B, or L registers.

  C
    The CC register.

  t
    LT0 or LT1.

  k
    LC0 or LC1.

  u
    LB0 or LB1.

  x
    Any D, P, B, M, I or L register.

  y
    Additional registers typically used only in prologues and epilogues: RETS,
    RETN, RETI, RETX, RETE, ASTAT, SEQSTAT and USP.

  w
    Any register except accumulators or CC.

  Ksh
    Signed 16 bit integer (in the range -32768 to 32767)

  Kuh
    Unsigned 16 bit integer (in the range 0 to 65535)

  Ks7
    Signed 7 bit integer (in the range -64 to 63)

  Ku7
    Unsigned 7 bit integer (in the range 0 to 127)

  Ku5
    Unsigned 5 bit integer (in the range 0 to 31)

  Ks4
    Signed 4 bit integer (in the range -8 to 7)

  Ks3
    Signed 3 bit integer (in the range -3 to 4)

  Ku3
    Unsigned 3 bit integer (in the range 0 to 7)

  P``n``
    Constant ``n``, where ``n`` is a single-digit constant in the range 0 to 4.

  PA
    An integer equal to one of the MACFLAG_XXX constants that is suitable for
    use with either accumulator.

  PB
    An integer equal to one of the MACFLAG_XXX constants that is suitable for
    use only with accumulator A1.

  M1
    Constant 255.

  M2
    Constant 65535.

  J
    An integer constant with exactly a single bit set.

  L
    An integer constant with all bits set except exactly one.

  H

  Q
    Any SYMBOL_REF.

CR16 Architecture-config/cr16/cr16.h

  b
    Registers from r0 to r14 (registers without stack pointer)

  t
    Register from r0 to r11 (all 16-bit registers)

  p
    Register from r12 to r15 (all 32-bit registers)

  I
    Signed constant that fits in 4 bits

  J
    Signed constant that fits in 5 bits

  K
    Signed constant that fits in 6 bits

  L
    Unsigned constant that fits in 4 bits

  M
    Signed constant that fits in 32 bits

  N
    Check for 64 bits wide constants for add/sub instructions

  G
    Floating point constant that is legal for store immediate

Epiphany-config/epiphany/constraints.md

  U16
    An unsigned 16-bit constant.

  K
    An unsigned 5-bit constant.

  L
    A signed 11-bit constant.

  Cm1
    A signed 11-bit constant added to -1.
    Can only match when the :option:`-m1reg-``reg``` option is active.

  Cl1
    Left-shift of -1, i.e., a bit mask with a block of leading ones, the rest
    being a block of trailing zeroes.
    Can only match when the :option:`-m1reg-``reg``` option is active.

  Cr1
    Right-shift of -1, i.e., a bit mask with a trailing block of ones, the
    rest being zeroes.  Or to put it another way, one less than a power of two.
    Can only match when the :option:`-m1reg-``reg``` option is active.

  Cal
    Constant for arithmetic/logical operations.
    This is like ``i``, except that for position independent code,
    no symbols / expressions needing relocations are allowed.

  Csy
    Symbolic constant for call/jump instruction.

  Rcs
    The register class usable in short insns.  This is a register class
    constraint, and can thus drive register allocation.
    This constraint won't match unless :option:`-mprefer-short-insn-regs` is
    in effect.

  Rsc
    The the register class of registers that can be used to hold a
    sibcall call address.  I.e., a caller-saved register.

  Rct
    Core control register class.

  Rgs
    The register group usable in short insns.
    This constraint does not use a register class, so that it only
    passively matches suitable registers, and doesn't drive register allocation.

  Rra
    Matches the return address if it can be replaced with the link register.

  Rcc
    Matches the integer condition code register.

  Sra
    Matches the return address if it is in a stack slot.

  Cfm
    Matches control register values to switch fp mode, which are encapsulated in
    ``UNSPEC_FP_MODE``.

FRV-config/frv/frv.h

  a
    Register in the class ``ACC_REGS`` (``acc0`` to ``acc7``).

  b
    Register in the class ``EVEN_ACC_REGS`` (``acc0`` to ``acc7``).

  c
    Register in the class ``CC_REGS`` (``fcc0`` to ``fcc3`` and
    ``icc0`` to ``icc3``).

  d
    Register in the class ``GPR_REGS`` (``gr0`` to ``gr63``).

  e
    Register in the class ``EVEN_REGS`` (``gr0`` to ``gr63``).
    Odd registers are excluded not in the class but through the use of a machine
    mode larger than 4 bytes.

  f
    Register in the class ``FPR_REGS`` (``fr0`` to ``fr63``).

  h
    Register in the class ``FEVEN_REGS`` (``fr0`` to ``fr63``).
    Odd registers are excluded not in the class but through the use of a machine
    mode larger than 4 bytes.

  l
    Register in the class ``LR_REG`` (the ``lr`` register).

  q
    Register in the class ``QUAD_REGS`` (``gr2`` to ``gr63``).
    Register numbers not divisible by 4 are excluded not in the class but through
    the use of a machine mode larger than 8 bytes.

  t
    Register in the class ``ICC_REGS`` (``icc0`` to ``icc3``).

  u
    Register in the class ``FCC_REGS`` (``fcc0`` to ``fcc3``).

  v
    Register in the class ``ICR_REGS`` (``cc4`` to ``cc7``).

  w
    Register in the class ``FCR_REGS`` (``cc0`` to ``cc3``).

  x
    Register in the class ``QUAD_FPR_REGS`` (``fr0`` to ``fr63``).
    Register numbers not divisible by 4 are excluded not in the class but through
    the use of a machine mode larger than 8 bytes.

  z
    Register in the class ``SPR_REGS`` (``lcr`` and ``lr``).

  A
    Register in the class ``QUAD_ACC_REGS`` (``acc0`` to ``acc7``).

  B
    Register in the class ``ACCG_REGS`` (``accg0`` to ``accg7``).

  C
    Register in the class ``CR_REGS`` (``cc0`` to ``cc7``).

  G
    Floating point constant zero

  I
    6-bit signed integer constant

  J
    10-bit signed integer constant

  L
    16-bit signed integer constant

  M
    16-bit unsigned integer constant

  N
    12-bit signed integer constant that is negative-i.e. in the
    range of -2048 to -1

  O
    Constant zero

  P
    12-bit signed integer constant that is greater than zero-i.e. in the
    range of 1 to 2047.

Hewlett-Packard PA-RISC-config/pa/pa.h

  a
    General register 1

  f
    Floating point register

  q
    Shift amount register

  x
    Floating point register (deprecated)

  y
    Upper floating point register (32-bit), floating point register (64-bit)

  Z
    Any register

  I
    Signed 11-bit integer constant

  J
    Signed 14-bit integer constant

  K
    Integer constant that can be deposited with a ``zdepi`` instruction

  L
    Signed 5-bit integer constant

  M
    Integer constant 0

  N
    Integer constant that can be loaded with a ``ldil`` instruction

  O
    Integer constant whose value plus one is a power of 2

  P
    Integer constant that can be used for ``and`` operations in ``depi``
    and ``extru`` instructions

  S
    Integer constant 31

  U
    Integer constant 63

  G
    Floating-point constant 0.0

  A
    A ``lo_sum`` data-linkage-table memory operand

  Q
    A memory operand that can be used as the destination operand of an
    integer store instruction

  R
    A scaled or unscaled indexed memory operand

  T
    A memory operand for floating-point loads and stores

  W
    A register indirect memory operand

Intel IA-64-config/ia64/ia64.h

  a
    General register ``r0`` to ``r3`` for ``addl`` instruction

  b
    Branch register

  c
    Predicate register (c as in 'conditional')

  d
    Application register residing in M-unit

  e
    Application register residing in I-unit

  f
    Floating-point register

  m
    Memory operand.  If used together with < or >,
    the operand can have postincrement and postdecrement which
    require printing with %Pn on IA-64.

  G
    Floating-point constant 0.0 or 1.0

  I
    14-bit signed integer constant

  J
    22-bit signed integer constant

  K
    8-bit signed integer constant for logical instructions

  L
    8-bit adjusted signed integer constant for compare pseudo-ops

  M
    6-bit unsigned integer constant for shift counts

  N
    9-bit signed integer constant for load and store postincrements

  O
    The constant zero

  P
    0 or -1 for ``dep`` instruction

  Q
    Non-volatile memory for floating-point loads and stores

  R
    Integer constant in the range 1 to 4 for ``shladd`` instruction

  S
    Memory operand except postincrement and postdecrement.  This is
    now roughly the same as m when not used together with <
    or >.

M32C-config/m32c/m32c.c

  Rsp Rfb Rsb
    $sp, $fb, $sb.

  Rcr
    Any control register, when they're 16 bits wide (nothing if control
    registers are 24 bits wide)

  Rcl
    Any control register, when they're 24 bits wide.

  R0w R1w R2w R3w
    $r0, $r1, $r2, $r3.

  R02
    $r0 or $r2, or $r2r0 for 32 bit values.

  R13
    $r1 or $r3, or $r3r1 for 32 bit values.

  Rdi
    A register that can hold a 64 bit value.

  Rhl
    $r0 or $r1 (registers with addressable high/low bytes)

  R23
    $r2 or $r3

  Raa
    Address registers

  Raw
    Address registers when they're 16 bits wide.

  Ral
    Address registers when they're 24 bits wide.

  Rqi
    Registers that can hold QI values.

  Rad
    Registers that can be used with displacements ($a0, $a1, $sb).

  Rsi
    Registers that can hold 32 bit values.

  Rhi
    Registers that can hold 16 bit values.

  Rhc
    Registers chat can hold 16 bit values, including all control
    registers.

  Rra
    $r0 through R1, plus $a0 and $a1.

  Rfl
    The flags register.

  Rmm
    The memory-based pseudo-registers $mem0 through $mem15.

  Rpi
    Registers that can hold pointers (16 bit registers for r8c, m16c; 24
    bit registers for m32cm, m32c).

  Rpa
    Matches multiple registers in a PARALLEL to form a larger register.
    Used to match function return values.

  Is3
    -8 ... 7

  IS1
    -128 ... 127

  IS2
    -32768 ... 32767

  IU2
    0 ... 65535

  In4
    -8 ... -1 or 1 ... 8

  In5
    -16 ... -1 or 1 ... 16

  In6
    -32 ... -1 or 1 ... 32

  IM2
    -65536 ... -1

  Ilb
    An 8 bit value with exactly one bit set.

  Ilw
    A 16 bit value with exactly one bit set.

  Sd
    The common src/dest memory addressing modes.

  Sa
    Memory addressed using $a0 or $a1.

  Si
    Memory addressed with immediate addresses.

  Ss
    Memory addressed using the stack pointer ($sp).

  Sf
    Memory addressed using the frame base register ($fb).

  Ss
    Memory addressed using the small base register ($sb).

  S1
    $r1h

MeP-config/mep/constraints.md

  a
    The $sp register.

  b
    The $tp register.

  c
    Any control register.

  d
    Either the $hi or the $lo register.

  em
    Coprocessor registers that can be directly loaded ($c0-$c15).

  ex
    Coprocessor registers that can be moved to each other.

  er
    Coprocessor registers that can be moved to core registers.

  h
    The $hi register.

  j
    The $rpc register.

  l
    The $lo register.

  t
    Registers which can be used in $tp-relative addressing.

  v
    The $gp register.

  x
    The coprocessor registers.

  y
    The coprocessor control registers.

  z
    The $0 register.

  A
    User-defined register set A.

  B
    User-defined register set B.

  C
    User-defined register set C.

  D
    User-defined register set D.

  I
    Offsets for $gp-rel addressing.

  J
    Constants that can be used directly with boolean insns.

  K
    Constants that can be moved directly to registers.

  L
    Small constants that can be added to registers.

  M
    Long shift counts.

  N
    Small constants that can be compared to registers.

  O
    Constants that can be loaded into the top half of registers.

  S
    Signed 8-bit immediates.

  T
    Symbols encoded for $tp-rel or $gp-rel addressing.

  U
    Non-constant addresses for loading/saving coprocessor registers.

  W
    The top half of a symbol's value.

  Y
    A register indirect address without offset.

  Z
    Symbolic references to the control bus.

MicroBlaze-config/microblaze/constraints.md

  d
    A general register (``r0`` to ``r31``).

  z
    A status register (``rmsr``, ``$fcc1`` to ``$fcc7``).

MIPS-config/mips/constraints.md

  d
    An address register.  This is equivalent to ``r`` unless
    generating MIPS16 code.

  f
    A floating-point register (if available).

  h
    Formerly the ``hi`` register.  This constraint is no longer supported.

  l
    The ``lo`` register.  Use this register to store values that are
    no bigger than a word.

  x
    The concatenated ``hi`` and ``lo`` registers.  Use this register
    to store doubleword values.

  c
    A register suitable for use in an indirect jump.  This will always be
    ``$25`` for :option:`-mabicalls`.

  v
    Register ``$3``.  Do not use this constraint in new code;
    it is retained only for compatibility with glibc.

  y
    Equivalent to ``r``; retained for backwards compatibility.

  z
    A floating-point condition code register.

  I
    A signed 16-bit constant (for arithmetic instructions).

  J
    Integer zero.

  K
    An unsigned 16-bit constant (for logic instructions).

  L
    A signed 32-bit constant in which the lower 16 bits are zero.
    Such constants can be loaded using ``lui``.

  M
    A constant that cannot be loaded using ``lui``, ``addiu``
    or ``ori``.

  N
    A constant in the range -65535 to -1 (inclusive).

  O
    A signed 15-bit constant.

  P
    A constant in the range 1 to 65535 (inclusive).

  G
    Floating-point zero.

  R
    An address that can be used in a non-macro load or store.

  ZC
    A memory operand whose address is formed by a base register and offset
    that is suitable for use in instructions with the same addressing mode
    as ``ll`` and ``sc``.

  ZD
    An address suitable for a ``prefetch`` instruction, or for any other
    instruction with the same addressing mode as ``prefetch``.

Motorola 680x0-config/m68k/constraints.md

  a
    Address register

  d
    Data register

  f
    68881 floating-point register, if available

  I
    Integer in the range 1 to 8

  J
    16-bit signed number

  K
    Signed number whose magnitude is greater than 0x80

  L
    Integer in the range -8 to -1

  M
    Signed number whose magnitude is greater than 0x100

  N
    Range 24 to 31, rotatert:SI 8 to 1 expressed as rotate

  O
    16 (for rotate using swap)

  P
    Range 8 to 15, rotatert:HI 8 to 1 expressed as rotate

  R
    Numbers that mov3q can handle

  G
    Floating point constant that is not a 68881 constant

  S
    Operands that satisfy 'm' when -mpcrel is in effect

  T
    Operands that satisfy 's' when -mpcrel is not in effect

  Q
    Address register indirect addressing mode

  U
    Register offset addressing

  W
    const_call_operand

  Cs
    symbol_ref or const

  Ci
    const_int

  C0
    const_int 0

  Cj
    Range of signed numbers that don't fit in 16 bits

  Cmvq
    Integers valid for mvq

  Capsw
    Integers valid for a moveq followed by a swap

  Cmvz
    Integers valid for mvz

  Cmvs
    Integers valid for mvs

  Ap
    push_operand

  Ac
    Non-register operands allowed in clr

Moxie-config/moxie/constraints.md

  A
    An absolute address

  B
    An offset address

  W
    A register indirect memory operand

  I
    A constant in the range of 0 to 255.

  N
    A constant in the range of 0 to -255.

MSP430-config/msp430/constraints.md

  R12
    Register R12.

  R13
    Register R13.

  K
    Integer constant 1.

  L
    Integer constant -1^20..1^19.

  M
    Integer constant 1-4.

  Ya
    Memory references which do not require an extended MOVX instruction.

  Yl
    Memory reference, labels only.

  Ys
    Memory reference, stack only.

NDS32-config/nds32/constraints.md

  w
    LOW register class $r0 to $r7 constraint for V3/V3M ISA.

  l
    LOW register class $r0 to $r7.

  d
    MIDDLE register class $r0 to $r11, $r16 to $r19.

  h
    HIGH register class $r12 to $r14, $r20 to $r31.

  t
    Temporary assist register $ta (i.e. $r15).

  k
    Stack register $sp.

  Iu03
    Unsigned immediate 3-bit value.

  In03
    Negative immediate 3-bit value in the range of -7-0.

  Iu04
    Unsigned immediate 4-bit value.

  Is05
    Signed immediate 5-bit value.

  Iu05
    Unsigned immediate 5-bit value.

  In05
    Negative immediate 5-bit value in the range of -31-0.

  Ip05
    Unsigned immediate 5-bit value for movpi45 instruction with range 16-47.

  Iu06
    Unsigned immediate 6-bit value constraint for addri36.sp instruction.

  Iu08
    Unsigned immediate 8-bit value.

  Iu09
    Unsigned immediate 9-bit value.

  Is10
    Signed immediate 10-bit value.

  Is11
    Signed immediate 11-bit value.

  Is15
    Signed immediate 15-bit value.

  Iu15
    Unsigned immediate 15-bit value.

  Ic15
    A constant which is not in the range of imm15u but ok for bclr instruction.

  Ie15
    A constant which is not in the range of imm15u but ok for bset instruction.

  It15
    A constant which is not in the range of imm15u but ok for btgl instruction.

  Ii15
    A constant whose compliment value is in the range of imm15u
    and ok for bitci instruction.

  Is16
    Signed immediate 16-bit value.

  Is17
    Signed immediate 17-bit value.

  Is19
    Signed immediate 19-bit value.

  Is20
    Signed immediate 20-bit value.

  Ihig
    The immediate value that can be simply set high 20-bit.

  Izeb
    The immediate value 0xff.

  Izeh
    The immediate value 0xffff.

  Ixls
    The immediate value 0x01.

  Ix11
    The immediate value 0x7ff.

  Ibms
    The immediate value with power of 2.

  Ifex
    The immediate value with power of 2 minus 1.

  U33
    Memory constraint for 333 format.

  U45
    Memory constraint for 45 format.

  U37
    Memory constraint for 37 format.

Nios II family-config/nios2/constraints.md

  I
    Integer that is valid as an immediate operand in an
    instruction taking a signed 16-bit number. Range
    -32768 to 32767.

  J
    Integer that is valid as an immediate operand in an
    instruction taking an unsigned 16-bit number. Range
    0 to 65535.

  K
    Integer that is valid as an immediate operand in an
    instruction taking only the upper 16-bits of a
    32-bit number. Range 32-bit numbers with the lower
    16-bits being 0.

  L
    Integer that is valid as an immediate operand for a 
    shift instruction. Range 0 to 31.

  M
    Integer that is valid as an immediate operand for
    only the value 0. Can be used in conjunction with
    the format modifier ``z`` to use ``r0``
    instead of ``0`` in the assembly output.

  N
    Integer that is valid as an immediate operand for
    a custom instruction opcode. Range 0 to 255.

  S
    Matches immediates which are addresses in the small
    data section and therefore can be added to ``gp``
    as a 16-bit immediate to re-create their 32-bit value.

PDP-11-config/pdp11/constraints.md

  a
    Floating point registers AC0 through AC3.  These can be loaded from/to
    memory with a single instruction.

  d
    Odd numbered general registers (R1, R3, R5).  These are used for
    16-bit multiply operations.

  f
    Any of the floating point registers (AC0 through AC5).

  G
    Floating point constant 0.

  I
    An integer constant that fits in 16 bits.

  J
    An integer constant whose low order 16 bits are zero.

  K
    An integer constant that does not meet the constraints for codes
    I or J.

  L
    The integer constant 1.

  M
    The integer constant -1.

  N
    The integer constant 0.

  O
    Integer constants -4 through -1 and 1 through 4; shifts by these
    amounts are handled as multiple single-bit shifts rather than a single
    variable-length shift.

  Q
    A memory reference which requires an additional word (address or
    offset) after the opcode.

  R
    A memory reference that is encoded within the opcode.

PowerPC and IBM RS6000-config/rs6000/constraints.md

  b
    Address base register

  d
    Floating point register (containing 64-bit value)

  f
    Floating point register (containing 32-bit value)

  v
    Altivec vector register

  wa
    Any VSX register if the -mvsx option was used or NO_REGS.

  wd
    VSX vector register to hold vector double data or NO_REGS.

  wf
    VSX vector register to hold vector float data or NO_REGS.

  wg
    If :option:`-mmfpgpr` was used, a floating point register or NO_REGS.

  wh
    Floating point register if direct moves are available, or NO_REGS.

  wi
    FP or VSX register to hold 64-bit integers for VSX insns or NO_REGS.

  wj
    FP or VSX register to hold 64-bit integers for direct moves or NO_REGS.

  wk
    FP or VSX register to hold 64-bit doubles for direct moves or NO_REGS.

  wl
    Floating point register if the LFIWAX instruction is enabled or NO_REGS.

  wm
    VSX register if direct move instructions are enabled, or NO_REGS.

  wn
    No register (NO_REGS).

  wr
    General purpose register if 64-bit instructions are enabled or NO_REGS.

  ws
    VSX vector register to hold scalar double values or NO_REGS.

  wt
    VSX vector register to hold 128 bit integer or NO_REGS.

  wu
    Altivec register to use for float/32-bit int loads/stores  or NO_REGS.

  wv
    Altivec register to use for double loads/stores  or NO_REGS.

  ww
    FP or VSX register to perform float operations under :option:`-mvsx` or NO_REGS.

  wx
    Floating point register if the STFIWX instruction is enabled or NO_REGS.

  wy
    FP or VSX register to perform ISA 2.07 float ops or NO_REGS.

  wz
    Floating point register if the LFIWZX instruction is enabled or NO_REGS.

  wD
    Int constant that is the element number of the 64-bit scalar in a vector.

  wQ
    A memory address that will work with the ``lq`` and ``stq``
    instructions.

  h
    MQ, CTR, or LINK register

  q
    MQ register

  c
    CTR register

  l
    LINK register

  x
    CR register (condition register) number 0

  y
    CR register (condition register)

  z
    XER[CA] carry bit (part of the XER register)

  I
    Signed 16-bit constant

  J
    Unsigned 16-bit constant shifted left 16 bits (use L instead for
    ``SImode`` constants)

  K
    Unsigned 16-bit constant

  L
    Signed 16-bit constant shifted left 16 bits

  M
    Constant larger than 31

  N
    Exact power of 2

  O
    Zero

  P
    Constant whose negation is a signed 16-bit constant

  G
    Floating point constant that can be loaded into a register with one
    instruction per word

  H
    Integer/Floating point constant that can be loaded into a register using
    three instructions

  m
    Memory operand.
    Normally, ``m`` does not allow addresses that update the base register.
    If < or > constraint is also used, they are allowed and
    therefore on PowerPC targets in that case it is only safe
    to use m<> in an ``asm`` statement if that ``asm`` statement
    accesses the operand exactly once.  The ``asm`` statement must also
    use %U``<opno>`` as a placeholder for the 'update' flag in the
    corresponding load or store instruction.  For example:

    .. code-block:: c++

      asm ("st%U0 %1,%0" : "=m<>" (mem) : "r" (val));

    is correct but:

    .. code-block:: c++

      asm ("st %1,%0" : "=m<>" (mem) : "r" (val));

    is not.

  es
    A 'stable' memory operand; that is, one which does not include any
    automodification of the base register.  This used to be useful when
    m allowed automodification of the base register, but as those are now only
    allowed when < or > is used, es is basically the same
    as m without < and >.

  Q
    Memory operand that is an offset from a register (it is usually better
    to use m or es in ``asm`` statements)

  Z
    Memory operand that is an indexed or indirect from a register (it is
    usually better to use m or es in ``asm`` statements)

  R
    AIX TOC entry

  a
    Address operand that is an indexed or indirect from a register (p is
    preferable for ``asm`` statements)

  S
    Constant suitable as a 64-bit mask operand

  T
    Constant suitable as a 32-bit mask operand

  U
    System V Release 4 small data area reference

  t
    AND masks that can be performed by two rldic{l, r} instructions

  W
    Vector constant that does not require memory

  j
    Vector constant that is all zeros.

RL78-config/rl78/constraints.md

  Int3
    An integer constant in the range 1 ... 7.

  Int8
    An integer constant in the range 0 ... 255.

  J
    An integer constant in the range -255 ... 0

  K
    The integer constant 1.

  L
    The integer constant -1.

  M
    The integer constant 0.

  N
    The integer constant 2.

  O
    The integer constant -2.

  P
    An integer constant in the range 1 ... 15.

  Qbi
    The built-in compare types-eq, ne, gtu, ltu, geu, and leu.

  Qsc
    The synthetic compare types-gt, lt, ge, and le.

  Wab
    A memory reference with an absolute address.

  Wbc
    A memory reference using ``BC`` as a base register, with an optional offset.

  Wca
    A memory reference using ``AX``, ``BC``, ``DE``, or ``HL`` for the address, for calls.

  Wcv
    A memory reference using any 16-bit register pair for the address, for calls.

  Wd2
    A memory reference using ``DE`` as a base register, with an optional offset.

  Wde
    A memory reference using ``DE`` as a base register, without any offset.

  Wfr
    Any memory reference to an address in the far address space.

  Wh1
    A memory reference using ``HL`` as a base register, with an optional one-byte offset.

  Whb
    A memory reference using ``HL`` as a base register, with ``B`` or ``C`` as the index register.

  Whl
    A memory reference using ``HL`` as a base register, without any offset.

  Ws1
    A memory reference using ``SP`` as a base register, with an optional one-byte offset.

  Y
    Any memory reference to an address in the near address space.

  A
    The ``AX`` register.

  B
    The ``BC`` register.

  D
    The ``DE`` register.

  R
    ``A`` through ``L`` registers.

  S
    The ``SP`` register.

  T
    The ``HL`` register.

  Z08W
    The 16-bit ``R8`` register.

  Z10W
    The 16-bit ``R10`` register.

  Zint
    The registers reserved for interrupts (``R24`` to ``R31``).

  a
    The ``A`` register.

  b
    The ``B`` register.

  c
    The ``C`` register.

  d
    The ``D`` register.

  e
    The ``E`` register.

  h
    The ``H`` register.

  l
    The ``L`` register.

  v
    The virtual registers.

  w
    The ``PSW`` register.

  x
    The ``X`` register.

RX-config/rx/constraints.md

  Q
    An address which does not involve register indirect addressing or
    pre/post increment/decrement addressing.

  Symbol
    A symbol reference.

  Int08
    A constant in the range -256 to 255, inclusive.

  Sint08
    A constant in the range -128 to 127, inclusive.

  Sint16
    A constant in the range -32768 to 32767, inclusive.

  Sint24
    A constant in the range -8388608 to 8388607, inclusive.

  Uint04
    A constant in the range 0 to 15, inclusive.

S/390 and zSeries-config/s390/s390.h

  a
    Address register (general purpose register except r0)

  c
    Condition code register

  d
    Data register (arbitrary general purpose register)

  f
    Floating-point register

  I
    Unsigned 8-bit constant (0-255)

  J
    Unsigned 12-bit constant (0-4095)

  K
    Signed 16-bit constant (-32768-32767)

  L
    Value appropriate as displacement.

    (0..4095)
      for short displacement

    (-524288..524287)
      for long displacement

  M
    Constant integer with a value of 0x7fffffff.

  N
    Multiple letter constraint followed by 4 parameter letters.

    0..9:
      number of the part counting from most to least significant

    H,Q:
      mode of the part

    D,S,H:
      mode of the containing operand

    0,F:
      value of the other parts (F-all bits set)

      The constraint matches if the specified part of a constant
    has a value different from its other parts.

  Q
    Memory reference without index register and with short displacement.

  R
    Memory reference with index register and short displacement.

  S
    Memory reference without index register but with long displacement.

  T
    Memory reference with index register and long displacement.

  U
    Pointer with short displacement.

  W
    Pointer with long displacement.

  Y
    Shift count operand.

SPARC-config/sparc/sparc.h

  f
    Floating-point register on the SPARC-V8 architecture and
    lower floating-point register on the SPARC-V9 architecture.

  e
    Floating-point register.  It is equivalent to f on the
    SPARC-V8 architecture and contains both lower and upper
    floating-point registers on the SPARC-V9 architecture.

  c
    Floating-point condition code register.

  d
    Lower floating-point register.  It is only valid on the SPARC-V9
    architecture when the Visual Instruction Set is available.

  b
    Floating-point register.  It is only valid on the SPARC-V9 architecture
    when the Visual Instruction Set is available.

  h
    64-bit global or out register for the SPARC-V8+ architecture.

  C
    The constant all-ones, for floating-point.

  A
    Signed 5-bit constant

  D
    A vector constant

  I
    Signed 13-bit constant

  J
    Zero

  K
    32-bit constant with the low 12 bits clear (a constant that can be
    loaded with the ``sethi`` instruction)

  L
    A constant in the range supported by ``movcc`` instructions (11-bit
    signed immediate)

  M
    A constant in the range supported by ``movrcc`` instructions (10-bit
    signed immediate)

  N
    Same as K, except that it verifies that bits that are not in the
    lower 32-bit range are all zero.  Must be used instead of K for
    modes wider than ``SImode``

  O
    The constant 4096

  G
    Floating-point zero

  H
    Signed 13-bit constant, sign-extended to 32 or 64 bits

  P
    The constant -1

  Q
    Floating-point constant whose integral representation can
    be moved into an integer register using a single sethi
    instruction

  R
    Floating-point constant whose integral representation can
    be moved into an integer register using a single mov
    instruction

  S
    Floating-point constant whose integral representation can
    be moved into an integer register using a high/lo_sum
    instruction sequence

  T
    Memory address aligned to an 8-byte boundary

  U
    Even register

  W
    Memory address for e constraint registers

  w
    Memory address with only a base register

  Y
    Vector zero

SPU-config/spu/spu.h

  a
    An immediate which can be loaded with the il/ila/ilh/ilhu instructions.  const_int is treated as a 64 bit value.

  c
    An immediate for and/xor/or instructions.  const_int is treated as a 64 bit value.

  d
    An immediate for the ``iohl`` instruction.  const_int is treated as a 64 bit value.

  f
    An immediate which can be loaded with ``fsmbi``.

  A
    An immediate which can be loaded with the il/ila/ilh/ilhu instructions.  const_int is treated as a 32 bit value.

  B
    An immediate for most arithmetic instructions.  const_int is treated as a 32 bit value.

  C
    An immediate for and/xor/or instructions.  const_int is treated as a 32 bit value.

  D
    An immediate for the ``iohl`` instruction.  const_int is treated as a 32 bit value.

  I
    A constant in the range [-64, 63] for shift/rotate instructions.

  J
    An unsigned 7-bit constant for conversion/nop/channel instructions.

  K
    A signed 10-bit constant for most arithmetic instructions.

  M
    A signed 16 bit immediate for ``stop``.

  N
    An unsigned 16-bit constant for ``iohl`` and ``fsmbi``.

  O
    An unsigned 7-bit constant whose 3 least significant bits are 0.

  P
    An unsigned 3-bit constant for 16-byte rotates and shifts

  R
    Call operand, reg, for indirect calls

  S
    Call operand, symbol, for relative calls.

  T
    Call operand, const_int, for absolute calls.

  U
    An immediate which can be loaded with the il/ila/ilh/ilhu instructions.  const_int is sign extended to 128 bit.

  W
    An immediate for shift and rotate instructions.  const_int is treated as a 32 bit value.

  Y
    An immediate for and/xor/or instructions.  const_int is sign extended as a 128 bit.

  Z
    An immediate for the ``iohl`` instruction.  const_int is sign extended to 128 bit.

TI C6X family-config/c6x/constraints.md

  a
    Register file A (A0-A31).

  b
    Register file B (B0-B31).

  A
    Predicate registers in register file A (A0-A2 on C64X and
    higher, A1 and A2 otherwise).

  B
    Predicate registers in register file B (B0-B2).

  C
    A call-used register in register file B (B0-B9, B16-B31).

  Da
    Register file A, excluding predicate registers (A3-A31,
    plus A0 if not C64X or higher).

  Db
    Register file B, excluding predicate registers (B3-B31).

  Iu4
    Integer constant in the range 0 ... 15.

  Iu5
    Integer constant in the range 0 ... 31.

  In5
    Integer constant in the range -31 ... 0.

  Is5
    Integer constant in the range -16 ... 15.

  I5x
    Integer constant that can be the operand of an ADDA or a SUBA insn.

  IuB
    Integer constant in the range 0 ... 65535.

  IsB
    Integer constant in the range -32768 ... 32767.

  IsC
    Integer constant in the range -2^{20} ... 2^{20} - 1.

  Jc
    Integer constant that is a valid mask for the clr instruction.

  Js
    Integer constant that is a valid mask for the set instruction.

  Q
    Memory location with A base register.

  R
    Memory location with B base register.

  Z
    Register B14 (aka DP).

TILE-Gx-config/tilegx/constraints.md

  R00 R01 R02 R03 R04 R05 R06 R07 R08 R09 R10
    Each of these represents a register constraint for an individual
    register, from r0 to r10.

  I
    Signed 8-bit integer constant.

  J
    Signed 16-bit integer constant.

  K
    Unsigned 16-bit integer constant.

  L
    Integer constant that fits in one signed byte when incremented by one
    (-129 ... 126).

  m
    Memory operand.  If used together with < or >, the
    operand can have postincrement which requires printing with %In
    and %in on TILE-Gx.  For example:

    .. code-block:: c++

      asm ("st_add %I0,%1,%i0" : "=m<>" (*mem) : "r" (val));

  M
    A bit mask suitable for the BFINS instruction.

  N
    Integer constant that is a byte tiled out eight times.

  O
    The integer zero constant.

  P
    Integer constant that is a sign-extended byte tiled out as four shorts.

  Q
    Integer constant that fits in one signed byte when incremented
    (-129 ... 126), but excluding -1.

  S
    Integer constant that has all 1 bits consecutive and starting at bit 0.

  T
    A 16-bit fragment of a got, tls, or pc-relative reference.

  U
    Memory operand except postincrement.  This is roughly the same as
    m when not used together with < or >.

  W
    An 8-element vector constant with identical elements.

  Y
    A 4-element vector constant with identical elements.

  Z0
    The integer constant 0xffffffff.

  Z1
    The integer constant 0xffffffff00000000.

TILEPro-config/tilepro/constraints.md

  R00 R01 R02 R03 R04 R05 R06 R07 R08 R09 R10
    Each of these represents a register constraint for an individual
    register, from r0 to r10.

  I
    Signed 8-bit integer constant.

  J
    Signed 16-bit integer constant.

  K
    Nonzero integer constant with low 16 bits zero.

  L
    Integer constant that fits in one signed byte when incremented by one
    (-129 ... 126).

  m
    Memory operand.  If used together with < or >, the
    operand can have postincrement which requires printing with %In
    and %in on TILEPro.  For example:

    .. code-block:: c++

      asm ("swadd %I0,%1,%i0" : "=m<>" (mem) : "r" (val));

  M
    A bit mask suitable for the MM instruction.

  N
    Integer constant that is a byte tiled out four times.

  O
    The integer zero constant.

  P
    Integer constant that is a sign-extended byte tiled out as two shorts.

  Q
    Integer constant that fits in one signed byte when incremented
    (-129 ... 126), but excluding -1.

  T
    A symbolic operand, or a 16-bit fragment of a got, tls, or pc-relative
    reference.

  U
    Memory operand except postincrement.  This is roughly the same as
    m when not used together with < or >.

  W
    A 4-element vector constant with identical elements.

  Y
    A 2-element vector constant with identical elements.

Visium-config/visium/constraints.md

  b
    EAM register ``mdb``

  c
    EAM register ``mdc``

  f
    Floating point register

  l
    General register, but not ``r29``, ``r30`` and ``r31``

  t
    Register ``r1``

  u
    Register ``r2``

  v
    Register ``r3``

  G
    Floating-point constant 0.0

  J
    Integer constant in the range 0 .. 65535 (16-bit immediate)

  K
    Integer constant in the range 1 .. 31 (5-bit immediate)

  L
    Integer constant in the range -65535 .. -1 (16-bit negative immediate)

  M
    Integer constant -1

  O
    Integer constant 0

  P
    Integer constant 32

x86 family-config/i386/constraints.md

  R
    Legacy register-the eight integer registers available on all
    i386 processors (``a``, ``b``, ``c``, ``d``,
    ``si``, ``di``, ``bp``, ``sp``).

  q
    Any register accessible as ````r``l``.  In 32-bit mode, ``a``,
    ``b``, ``c``, and ``d``; in 64-bit mode, any integer register.

  Q
    Any register accessible as ````r``h``: ``a``, ``b``,
    ``c``, and ``d``.

  a
    The ``a`` register.

  b
    The ``b`` register.

  c
    The ``c`` register.

  d
    The ``d`` register.

  S
    The ``si`` register.

  D
    The ``di`` register.

  A
    The ``a`` and ``d`` registers.  This class is used for instructions
    that return double word results in the ``ax:dx`` register pair.  Single
    word values will be allocated either in ``ax`` or ``dx``.
    For example on i386 the following implements ``rdtsc``:

    .. code-block:: c++

      unsigned long long rdtsc (void)
      {
        unsigned long long tick;
        __asm__ __volatile__("rdtsc":"=A"(tick));
        return tick;
      }

    This is not correct on x86-64 as it would allocate tick in either ``ax``
    or ``dx``.  You have to use the following variant instead:

    .. code-block:: c++

      unsigned long long rdtsc (void)
      {
        unsigned int tickl, tickh;
        __asm__ __volatile__("rdtsc":"=a"(tickl),"=d"(tickh));
        return ((unsigned long long)tickh << 32)|tickl;
      }

  f
    Any 80387 floating-point (stack) register.

  t
    Top of 80387 floating-point stack (``%st(0)``).

  u
    Second from top of 80387 floating-point stack (``%st(1)``).

  y
    Any MMX register.

  x
    Any SSE register.

  Yz
    First SSE register (``%xmm0``).

  I
    Integer constant in the range 0 ... 31, for 32-bit shifts.

  J
    Integer constant in the range 0 ... 63, for 64-bit shifts.

  K
    Signed 8-bit integer constant.

  L
    ``0xFF`` or ``0xFFFF``, for andsi as a zero-extending move.

  M
    0, 1, 2, or 3 (shifts for the ``lea`` instruction).

  N
    Unsigned 8-bit integer constant (for ``in`` and ``out``
    instructions).

  G
    Standard 80387 floating point constant.

  C
    Standard SSE floating point constant.

  e
    32-bit signed integer constant, or a symbolic reference known
    to fit that range (for immediate operands in sign-extending x86-64
    instructions).

  Z
    32-bit unsigned integer constant, or a symbolic reference known
    to fit that range (for immediate operands in zero-extending x86-64
    instructions).

Xstormy16-config/stormy16/stormy16.h

  a
    Register r0.

  b
    Register r1.

  c
    Register r2.

  d
    Register r8.

  e
    Registers r0 through r7.

  t
    Registers r0 and r1.

  y
    The carry register.

  z
    Registers r8 and r9.

  I
    A constant between 0 and 3 inclusive.

  J
    A constant that has exactly one bit set.

  K
    A constant that has exactly one bit clear.

  L
    A constant between 0 and 255 inclusive.

  M
    A constant between -255 and 0 inclusive.

  N
    A constant between -3 and 0 inclusive.

  O
    A constant between 1 and 4 inclusive.

  P
    A constant between -4 and -1 inclusive.

  Q
    A memory reference that is a stack push.

  R
    A memory reference that is a stack pop.

  S
    A memory reference that refers to a constant address of known value.

  T
    The register indicated by Rx (not implemented yet).

  U
    A constant that is not between 2 and 15 inclusive.

  Z
    The constant 0.

Xtensa-config/xtensa/constraints.md

  a
    General-purpose 32-bit register

  b
    One-bit boolean register

  A
    MAC16 40-bit accumulator register

  I
    Signed 12-bit integer constant, for use in MOVI instructions

  J
    Signed 8-bit integer constant, for use in ADDI instructions

  K
    Integer constant valid for BccI instructions

  L
    Unsigned constant valid for BccUI instructions

.. Each of the following nodes are wrapped in separate
   "@ifset INTERNALS" to work around memory limits for the default
   configuration in older tetex distributions.  Known to not work:
   tetex-1.0.7, known to work: tetex-2.0.2.

.. _asm-labels:

Controlling Names Used in Assembler Code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index:: assembler names for identifiers

.. index:: names used in assembler code

.. index:: identifiers, names in assembler code

You can specify the name to be used in the assembler code for a C
function or variable by writing the ``asm`` (or ``__asm__``)
keyword after the declarator as follows:

.. code-block:: c++

  int foo asm ("myfoo") = 2;

This specifies that the name to be used for the variable ``foo`` in
the assembler code should be myfoo rather than the usual
_foo.

On systems where an underscore is normally prepended to the name of a C
function or variable, this feature allows you to define names for the
linker that do not start with an underscore.

It does not make sense to use this feature with a non-static local
variable since such variables do not have assembler names.  If you are
trying to put the variable in a particular register, see Explicit
Reg Vars.  GCC presently accepts such code with a warning, but will
probably be changed to issue an error, rather than a warning, in the
future.

You cannot use ``asm`` in this way in a function *definition*; but
you can get the same effect by writing a declaration for the function
before its definition and putting ``asm`` there, like this:

.. code-block:: c++

  extern func () asm ("FUNC");

  func (x, y)
       int x, y;
  /* ... */

It is up to you to make sure that the assembler names you choose do not
conflict with any other assembler symbols.  Also, you must not use a
register name; that would produce completely invalid assembler code.  GCC
does not as yet have the ability to store static variables in registers.
Perhaps that will be added.

.. _explicit-reg-vars:

Variables in Specified Registers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index:: explicit register variables

.. index:: variables in specified registers

.. index:: specified registers

.. index:: registers, global allocation

GNU C allows you to put a few global variables into specified hardware
registers.  You can also specify the register in which an ordinary
register variable should be allocated.

* Global register variables reserve registers throughout the program.
  This may be useful in programs such as programming language
  interpreters that have a couple of global variables that are accessed
  very often.

* Local register variables in specific registers do not reserve the
  registers, except at the point where they are used as input or output
  operands in an ``asm`` statement and the ``asm`` statement itself is
  not deleted.  The compiler's data flow analysis is capable of determining
  where the specified registers contain live values, and where they are
  available for other uses.  Stores into local register variables may be deleted
  when they appear to be dead according to dataflow analysis.  References
  to local register variables may be deleted or moved or simplified.

  These local variables are sometimes convenient for use with the extended
  ``asm`` feature (see :ref:`extended-asm`), if you want to write one
  output of the assembler instruction directly into a particular register.
  (This works provided the register you specify fits the constraints
  specified for that operand in the ``asm``.)

.. toctree::

   <global-reg-vars>
   <local-reg-vars>

.. _global-reg-vars:

Defining Global Register Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. index:: global register variables

.. index:: registers, global variables in

You can define a global register variable in GNU C like this:

.. code-block:: c++

  register int *foo asm ("a5");

Here ``a5`` is the name of the register that should be used.  Choose a
register that is normally saved and restored by function calls on your
machine, so that library routines will not clobber it.

Naturally the register name is CPU-dependent, so you need to
conditionalize your program according to CPU type.  The register
``a5`` is a good choice on a 68000 for a variable of pointer
type.  On machines with register windows, be sure to choose a 'global'
register that is not affected magically by the function call mechanism.

In addition, different operating systems on the same CPU may differ in how they
name the registers; then you need additional conditionals.  For
example, some 68000 operating systems call this register ``%a5``.

Eventually there may be a way of asking the compiler to choose a register
automatically, but first we need to figure out how it should choose and
how to enable you to guide the choice.  No solution is evident.

Defining a global register variable in a certain register reserves that
register entirely for this use, at least within the current compilation.
The register is not allocated for any other purpose in the functions
in the current compilation, and is not saved and restored by
these functions.  Stores into this register are never deleted even if they
appear to be dead, but references may be deleted or moved or
simplified.

It is not safe to access the global register variables from signal
handlers, or from more than one thread of control, because the system
library routines may temporarily use the register for other things (unless
you recompile them specially for the task at hand).

.. index:: qsort, and global register variables

It is not safe for one function that uses a global register variable to
call another such function ``foo`` by way of a third function
``lose`` that is compiled without knowledge of this variable (i.e. in a
different source file in which the variable isn't declared).  This is
because ``lose`` might save the register and put some other value there.
For example, you can't expect a global register variable to be available in
the comparison-function that you pass to ``qsort``, since ``qsort``
might have put something else in that register.  (If you are prepared to
recompile ``qsort`` with the same global register variable, you can
solve this problem.)

If you want to recompile ``qsort`` or other source files that do not
actually use your global register variable, so that they do not use that
register for any other purpose, then it suffices to specify the compiler
option :option:`-ffixed-``reg```.  You need not actually add a global
register declaration to their source code.

A function that can alter the value of a global register variable cannot
safely be called from a function compiled without this variable, because it
could clobber the value the caller expects to find there on return.
Therefore, the function that is the entry point into the part of the
program that uses the global register variable must explicitly save and
restore the value that belongs to its caller.

.. index:: register variable after longjmp

.. index:: global register after longjmp

.. index:: value after longjmp

.. index:: longjmp

.. index:: setjmp

On most machines, ``longjmp`` restores to each global register
variable the value it had at the time of the ``setjmp``.  On some
machines, however, ``longjmp`` does not change the value of global
register variables.  To be portable, the function that called ``setjmp``
should make other arrangements to save the values of the global register
variables, and to restore them in a ``longjmp``.  This way, the same
thing happens regardless of what ``longjmp`` does.

All global register variable declarations must precede all function
definitions.  If such a declaration could appear after function
definitions, the declaration would be too late to prevent the register from
being used for other purposes in the preceding functions.

Global register variables may not have initial values, because an
executable file has no means to supply initial contents for a register.

On the SPARC, there are reports that g3 ... g7 are suitable
registers, but certain library functions, such as ``getwd``, as well
as the subroutines for division and remainder, modify g3 and g4.  g1 and
g2 are local temporaries.

On the 68000, a2 ... a5 should be suitable, as should d2 ... d7.
Of course, it does not do to use more than a few of those.

.. _local-reg-vars:

Specifying Registers for Local Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. index:: local variables, specifying registers

.. index:: specifying registers for local variables

.. index:: registers for local variables

You can define a local register variable with a specified register
like this:

.. code-block:: c++

  register int *foo asm ("a5");

Here ``a5`` is the name of the register that should be used.  Note
that this is the same syntax used for defining global register
variables, but for a local variable it appears within a function.

Naturally the register name is CPU-dependent, but this is not a
problem, since specific registers are most often useful with explicit
assembler instructions (see :ref:`extended-asm`).  Both of these things
generally require that you conditionalize your program according to
CPU type.

In addition, operating systems on one type of CPU may differ in how they
name the registers; then you need additional conditionals.  For
example, some 68000 operating systems call this register ``%a5``.

Defining such a register variable does not reserve the register; it
remains available for other uses in places where flow control determines
the variable's value is not live.

This option does not guarantee that GCC generates code that has
this variable in the register you specify at all times.  You may not
code an explicit reference to this register in the assembler
instruction template part of an ``asm`` statement and assume it
always refers to this variable.
However, using the variable as an input or output operand to the ``asm``
guarantees that the specified register is used for that operand.  
See :ref:`extended-asm`, for more information.

Stores into local register variables may be deleted when they appear to be dead
according to dataflow analysis.  References to local register variables may
be deleted or moved or simplified.

As with global register variables, it is recommended that you choose a
register that is normally saved and restored by function calls on
your machine, so that library routines will not clobber it.

Sometimes when writing inline ``asm`` code, you need to make an operand be a 
specific register, but there's no matching constraint letter for that 
register. To force the operand into that register, create a local variable 
and specify the register in the variable's declaration. Then use the local 
variable for the asm operand and specify any constraint letter that matches 
the register:

.. code-block:: c++

  register int *p1 asm ("r0") = ...;
  register int *p2 asm ("r1") = ...;
  register int *result asm ("r0");
  asm ("sysint" : "=r" (result) : "0" (p1), "r" (p2));

*Warning:* In the above example, be aware that a register (for example r0) can be 
call-clobbered by subsequent code, including function calls and library calls 
for arithmetic operators on other variables (for example the initialization 
of p2). In this case, use temporary variables for expressions between the 
register assignments:

.. code-block:: c++

  int t1 = ...;
  register int *p1 asm ("r0") = ...;
  register int *p2 asm ("r1") = t1;
  register int *result asm ("r0");
  asm ("sysint" : "=r" (result) : "0" (p1), "r" (p2));

.. _size-of-an-asm:

Size of an ``asm``Some targets require that GCC track the size of each instruction used
in order to generate correct code.  Because the final length of the
code produced by an ``asm`` statement is only known by the
assembler, GCC must make an estimate as to how big it will be.  It
does this by counting the number of instructions in the pattern of the
``asm`` and multiplying that by the length of the longest
instruction supported by that processor.  (When working out the number
of instructions, it assumes that any occurrence of a newline or of
whatever statement separator character is supported by the assembler -
typically ; - indicates the end of an instruction.)

Normally, GCC's estimate is adequate to ensure that correct
code is generated, but it is possible to confuse the compiler if you use
pseudo instructions or assembler macros that expand into multiple real
instructions, or if you use assembler directives that expand to more
space in the object file than is needed for a single instruction.
If this happens then the assembler may produce a diagnostic saying that
a label is unreachable.

