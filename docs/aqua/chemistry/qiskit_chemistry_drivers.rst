.. _drivers:

=======
Drivers
=======

Qiskit Chemistry requires a computational chemistry program or library, known as *driver*, to be
installed on the system for the electronic-structure computation.  When launched via the Qiskit
Chemistry :ref:`qiskit-chemistry-command-line`,
:ref:`qiskit-chemistry-gui`, or :ref:`qiskit-chemistry-programmable-interface`,
Qiskit Chemistry expects a driver to be specified, and a
molecular configuration to be passed in the format compatible with that driver.
Qiskit Chemistry uses the driver not only as a frontend input language, to allow the user to
configure a chemistry problem in a language that an experienced chemist is already familiar with,
but also to compute some intermediate data, which will be later on used to form the input to one
of the :ref:`algorithms`.  Such intermediate date
includes the following:

1. One- and two-body integrals in Molecular Orbital (MO) basis
2. Dipole integrals
3. Molecular orbital coefficients
4. :ref:`hartree-fock` energy
5. Nuclear repulsion energy

Once extracted, the structure of this intermediate data is independent of the
driver that was used to compute it.  The only thing that could still depend on the driver
is the level of accuracy of such data; most likely,
a more elaborate driver will produce more accurate data.
Qiskit Chemistry offers the option to serialize this data in a binary format known as
`Hierarchical Data Format 5 (HDF5) <https://support.hdfgroup.org/HDF5/>`__.
This is done to allow chemists to reuse the same input data in the future
and to enable researchers to exchange
input data with each other --- which is especially useful to researchers who may not have
particular computational chemistry drivers installed on their computers.

In order for a driver to be usable by Qiskit Chemistry, an interface to that driver
must be built in Qiskit Chemistry.  Qiskit Chemistry offers the ``BaseDriver``
Application Programming Interface (API) to support interfacing new drivers.

Currently, Qiskit Chemistry comes with interfaces prebuilt
for the following four computational chemistry software drivers:

1. :ref:`gaussian-16`, a commercial chemistry program
2. :ref:`psi4`, an open-source chemistry program built on Python
3. :ref:`pyscf`, an open-source Python chemistry program
4. :ref:`pyquante`, a pure Python cross-platform open-source chemistry program

.. topic:: The HDF5 Driver

    A fifth driver, called HDF5, comes prebuilt in Qiskit Chemistry.  This is, in fact, the only
    driver that does not require the installation or configuration of any external computational
    chemistry software, since it is already part of Qiskit Chemistry. The HDF5 driver allows for
    chemistry input, in the form of an HDF5 file as specified above, to be passed into the
    computation.

.. topic:: Extending Qiskit Chemistry with Support for New Drivers

    The driver support in Qiskit Chemistry was designed to make the drivers pluggable and
    discoverable. In order for Qiskit Chemistry to be able to interface a driver library, the
    ``BaseDriver`` base class must be implemented in order to provide the interfacing code, or
    *wrapper*.  As part of this process, the required
    `JavaScript Object Notation (JSON) <http://json.org>`__ schema for the driver interface must
    be provided in a file named ``configuration.json``.  The interfacing code in the driver wrapper
    is responsible for constructing and populating a ``QMolecule`` instance with the electronic
    structure data listed above.  Driver wrappers implementing the ``BaseDriver`` class and the
    associated ``configuration.json`` schema file are organized in subfolders of the ``drivers``
    folder for automatic discovery and dynamic lookup.  Consulting the existing driver interface
    implementations may be helpful in accomplishing the task of extending .

The remainder of this section describes how to install and configure the drivers currently supported
by Qiskit Chemistry.

.. _gaussian-16:

------------
Gaussian™ 16
------------

`Gaussian™ 16 <http://gaussian.com/gaussian16/>`__ is a commercial program for computational chemistry.
The corresponding driver wrapper in Qiskit Chemistry accesses electronic structure information
from Gaussian™ 16 via the Gaussian-supplied open-source
`interfacing code <http://www.gaussian.com/interfacing/>`__.

In the ``qiskit_chemistry/drivers/gaussiand/gauopen`` folder of the
`Qiskit Chemistry GitHub repository <https://github.com/Qiskit/qiskit-chemistry>`__,
the Python part of the above interfacing code, as needed by Qiskit Chemistry,
has been made available. It is licensed under a
`Gaussian Open-Source Public License
<https://github.com/Qiskit/qiskit-chemistry/blob/master/qiskit_chemistry/drivers/gaussiand/gauopen/LICENSE.txt>`__.

Part of this interfacing code --- specifically, the Fortran file ``qcmatrixio.F`` --- requires
compilation to a Python native extension. However, Qiskit Chemistry comes with pre-built binaries
for most common platforms. If there is no pre-built binary matching your platform, then it will be
necessary to compile this file as per the instructions below.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Compiling the Fortran Interfacing Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If no prebuilt native extension binary, as supplied with Qiskit Chemistry, works for your
platform, then to use the Gaussian™ 16 driver on your machine, the Fortran file ``qcmatrixio.F``
must be compiled into object code that can be used by Python. This is accomplished using the
`Fortran to Python Interface Generator (F2PY) <https://docs.scipy.org/doc/numpy/f2py/>`__,
which is part of the `NumPy <http://www.numpy.org/>`__ Python library.
Specifically, on your command prompt window, change directory to the
``qiskit_chemistry/drivers/gaussiand/gauopen`` directory inside the Qiskit Chemistry
installation directory, and while in the Python environment created for Aqua and Qiskit Chemistry,
invoke ``f2py`` on ``qcmatrixio.F`` as explained below.


^^^^^^^^^^^^^^^^^^^^^
Apple macOS and Linux
^^^^^^^^^^^^^^^^^^^^^

The full syntax of the ``f2py`` command on macOS and Linux is as follows:

.. code:: sh

    f2py -c -m qcmatrixio qcmatrixio.F

This command will generate a file with name prefix ``qcmatrixio`` and extension ``so``, for example
``qcmatrixio.cpython-36m-x86_64-linux-gnu.so``.
In order for the command above to work and such file to be generated, you will need a supported
Fortran compiler installed. On macOS, you may have to download the
`GNU Compiler Collection (GCC) <https://gcc.gnu.org/>`__ and, in particular, the
`GFortran Compiler <https://gcc.gnu.org/fortran/>`__ source and compile it first
if you do not a suitable Fortran compiler installed
On Linux you may be able to download and install a supported Fortran compiler via your
distribution's installer.

.. topic:: Special Notes for macOS X

    If your account is using the bash shell on a macOS X machine, you can edit the
    ``.bash_profile`` file in your home directory and add the following lines:


    .. code:: sh

        export GAUSS_SCRDIR=~/.gaussian
        export g16root=/Applications
        alias enable_gaussian='. $g16root/g16/bsd/g16.profile'

    The above assumes that the application Gaussian™ 16 was placed in the ``/Applications`` folder
    and that ``~/.gaussian`` is the full path to
    the selected scratch folder, where Gaussian™ 16 stores its temporary files.

    Now, before Qiskit Chemistry can properly interface Gaussian™ 16, you will have to run the
    ``enable_gaussian`` command defined above.  This, however, may generate the following error:

    .. code:: sh

        bash: ulimit: open files: cannot modify limit: Invalid argument

    While this error is not harmful, you might want to suppress it, which can be done by entering
    the following sequence of commands on the command line:

    .. code:: sh

        echo kern.maxfiles=65536 | sudo tee -a /etc/sysctl.conf
        echo kern.maxfilesperproc=65536 | sudo tee -a /etc/sysctl.conf
        sudo sysctl -w kern.maxfiles=65536
        sudo sysctl -w kern.maxfilesperproc=65536
        ulimit -n 65536 65536

    as well as finally adding the following line to the ``.bash_profile`` file in your account's
    home directory:

    .. code:: sh

        ulimit -n 65536 65536

    At the end of this configuration, the ``.bash_profile`` in your account's home directory
    should have a section in it like in the following script snippet:

    .. code:: sh

        # Gaussian 16
        export GAUSS_SCRDIR=~/.gaussian
        export g16root=/Applications
        alias enable_gaussian='. $g16root/g16/bsd/g16.profile'
        ulimit -n 65536 65536


^^^^^^^^^^^^^^^^^
Microsoft Windows
^^^^^^^^^^^^^^^^^

The following steps can be used with the Intel Fortran compiler on the Microsoft Windows platform:

1. Set up the environment by adding the following line to ``ifortvars.bat``:

   .. code:: sh

       ifortvars -arch intel64

2. Issue the following command from within the ``gauopen`` directory:

   .. code:: sh

       f2py -c --fcompiler=intelvem -m qcmatrixio qcmatrixio.F

   Upon successful execution, the ``f2py`` command above will generate a file with name prefix
   ``qcmatrixio`` and extension ``so``, for example ``qcmatrixio.cp36-win_amd64.pyd``.  However,
   in order for the ``f2py`` command above to work, ``#ifdef`` may need to be manually edited if it
   is not recognized or supported during the processing of the ``f2py`` command above.  For
   example, with ``f2py`` from Intel Visual Fortran Compiler with Microsoft Visual Studio, the
   following code snippet originally shows two occurrences of the line
   ``Parameter (Len12D=8,Len4D=8)``, as shown next:

   .. code::

       #ifdef USE_I8
           Parameter (Len12D=8,Len4D=8)
       #else
           Parameter (Len12D=4,Len4D=4)
       #endif

   This may need to be simplified by deleting the first three lines and the last line, leaving just the fourth line, as follows:

   .. code::

       Parameter (Len12D=4,Len4D=4)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Verifying Path and Environment Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You should also make sure the Gaussian™ 16 ``g16`` executable can be run from a command line.
This requires verifying that the ``g16`` executable is reachable via the system environment path,
and appropriate exports, such as ``GAUSS_EXEDIR``, have been configured as per
`Gaussian installation instructions <http://gaussian.com/techsupport/#install]>`__.

~~~~~~~~~~~~~~~~~~
Input File Example
~~~~~~~~~~~~~~~~~~

To use Gaussian™ 16 to configure a molecule on which to do a chemistry experiment with
Qiskit Chemistry, set the ``name`` field in the ``driver`` section of the
:ref:`qiskit-chemistry-input-file` to ``GAUSSIAN`` and then create a ``gaussian`` section in the
input file as per the example below, which shows the configuration of a molecule of
hydrogen, :math:`H_2`.  Here, the molecule, basis set and other options are specified according
to the Gaussian™ 16 control file, so the syntax specified by Gaussian™ 16 should be followed:

.. code::

    &gaussian
       # rhf/sto-3g scf(conventional)

       h2 molecule

       0 1
       H   0.0  0.0    0.0
       H   0.0  0.0    0.74
    &end

Experienced chemists who already have existing Gaussian™ 16 control files can simply paste the
contents of those files into the ``gaussian`` section of the input file.  This configuration can
also be easily achieved using the Qiskit Chemistry :ref:`qiskit-chemistry-gui`.

.. _psi4:

----
PSI4
----
`PSI4 <http://www.psicode.org/>`__ is an open-source program for computational chemistry.
In order for Qiskit Chemistry to interface PSI4, accept PSI4 input files and execute PSI4 to extract
the electronic structure information necessary for the computation of the input to the quantum
algorithm, PSI4 must be `installed <http://www.psicode.org/downloads.html>`__ and discoverable on
the system where Qiskit Chemistry is also installed.
Therefore, once PSI4 has been installed, the ``psi4`` executable must be reachable via the system
environment path. For example, on macOS, this can be achieved by adding the following section to
the ``.bash_profile`` file in the user's home directory:

.. code:: sh

    # PSI4
    alias enable_psi4='export PATH=/Users/username/psi4conda/bin:$PATH'

where ``username`` should be replaced with the user's account name.
In order for Qiskit Chemistry to discover PSI4 at run time, it is then necessary to execute the
``enable_psi4`` command before launching Qiskit Chemistry.

To use PSI4 to configure a molecule on which to do a chemistry experiment with Qiskit Chemistry,
set the ``name`` field in the ``driver`` section of the :ref:`qiskit-chemistry-input-file` to
``PSI4`` and then create a ``psi4`` section in the input file as per the example below, which shows
the configuration of a molecule of hydrogen, :math:`H_2`.  Here, the molecule, basis set and other
options are specified according to the PSI4 control file, so the syntax specified by PSI4 should be
followed:

.. code:: python

    &psi4
       molecule h2 {
          0 1
          H 0.0 0.0 0.0
          H 0.0 0.0 0.74
       }

       set {
          basis sto-3g
          scf_type pk
       }
    &end

Experienced chemists who already have existing PSI4 control files can simply paste the contents of
those files into the ``psi4`` section of the input file.  This configuration can also be easily
achieved using the Qiskit Chemistry :ref:`qiskit-chemistry-gui`.

.. _pyscf:

-----
PySCF
-----
`PySCF <https://github.com/sunqm/pyscf>`__ is an open-source library for computational chemistry.
In order for Qiskit Chemistry to interface PySCF, accept PySCF input files and execute PySCF to
extract the electronic structure information necessary for the computation of the input to the
quantum algorithm, PySCF must be installed.  According to the
`installation instructions <http://sunqm.github.io/pyscf/install.html>`__,
the preferred installation method for PySCF is via the pip package management system.  Doing so
while in the Python virtual environment where Qiskit Chemistry is also installed will automatically
make PySCF dynamically discoverable by Qiskit Chemistry at run time.

To use PySCF to configure a molecule on which to do a chemistry experiment with Qiskit Chemistry,
set the ``name`` field in the ``driver`` section of the :ref:`qiskit-chemistry-input-file` to
``PYSCF`` and then create a ``pyscf`` section in the input file as per the example below, which
shows the configuration of a molecule of hydrogen, :math:`H_2`.  Here, the molecule, basis set and
other options are specified as key/value pairs, according to the syntax expected by PySCF. In PySCF,
these are the arguments as passed to the ``pyscf.gto.Mole`` class.

The ``atom`` field can be in xyz format, as per the example below. Here each atom is identified by
its symbol along with its position in the x, y, z coordinate space. Atoms are separated by the
semicolon symbol.

The ``atom`` field can also be in `ZMatrix <https://en.wikipedia.org/wiki/Z-matrix_(chemistry)>`__
format. Here again atoms are separate by semicolon. This is an example for H2O (water):
"H; O 1 1.08; H 2 1.08 1 107.5". Dummy atom(s) using symbol 'X' may be added to allow or facilitate
conversion to xyz coordinates, as used internally for processing, and are removed from the molecule
following the conversion.

.. code:: python

    &pyscf
       atom=H .0 .0 .0; H .0 .0 0.74
       unit=Angstrom
       charge=0
       spin=0
       basis=sto3g
    &end

Experienced chemists who already have existing PySCF control files can simply paste the contents of
those files into the ``pyscf`` section of the input file.  This configuration can also be easily
achieved using the Qiskit Chemistry :ref:`qiskit-chemistry-gui`.

.. _pyquante:

--------
PyQuante
--------
`PyQuante <https://github.com/rpmuller/pyquante2/>`__ is an open-source library for computational
chemistry. Qiskit Chemistry specifically requires PyQuante V2, also known as PyQuante2.
In order for Qiskit Chemistry to interface PyQuante, accept PyQuante input files and execute
PyQuante to extract the electronic structure information necessary for the computation of the input
to the quantum algorithm, PyQuante2 must be installed and discoverable on the system where
Qiskit Chemistry is also installed.  Installing PyQuante2 according to the
`installation instructions <https://github.com/rpmuller/pyquante2/blob/master/README.md>`__ while
in the Python virtual environment where Qiskit Chemistry has also been installed will automatically
make PyQuante2 dynamically discovered by Qiskit Chemistry at run time.

The Qiskit Chemistry PyQuante2 driver wrapper contains two methods, in ``transform.py``, taken from
from `Pyquante V1 <http://pyquante.sourceforge.net/>`__, which is
`licensed <http://pyquante.sourceforge.net/#license>`__
under a `modified BSD license <https://opensource.org/licenses/BSD-3-Clause>`__.

.. note::
    Like all the other drivers currently interfaced by Qiskit Chemistry,
    PyQuante2 provides enough intermediate data for Qiskit Chemistry to compute a molecule's ground
    state molecular energy.  However, unlike the other drivers, the data computed by PyQuante is not sufficient for
    Qiskit Chemistry to compute a molecule's dipole moment.  Therefore, PyQuante is currently
    the only driver interfaced by Qiskit Chemistry that does not allow for the computation of a molecule's
    dipole moment.

To use PyQuante to configure a molecule on which to do a chemistry experiment with Qiskit Chemistry,
set the ``name`` field in the ``driver`` section of the :ref:`qiskit-chemistry-input-file` to
``PYQUANTE`` and then create a ``pyquante`` section in the input file as per the example below,
which shows the configuration of a molecule of
hydrogen, :math:`H_2`.  Here, the molecule, basis set and other options are specified according
to the PyQuante control file, so the syntax specified by PyQuante should be followed.
Specifically, a molecule is configured as a list of atoms.  Each atom's chemical symbol is followed
by the atom's :math:`x, y, z`
geometrical coordinates separated by a blank space.  Atom configurations are separated by
semicolons.

The molecule in the ``atoms`` field can also be in
`ZMatrix <https://en.wikipedia.org/wiki/Z-matrix_(chemistry)>`__ format.
Here again atoms are separated by semicolons; within an atom the symbol and positional information
separated by spaces. This is an example for H2O (water): "H; O 1 1.08; H 2 1.08 1 107.5". Dummy
atom(s) using symbol 'X' may be added to allow or facilitate conversion to xyz coordinates, as used
internally for processing, and are removed from the molecule following the conversion.

.. code:: python

    &pyquante
       atoms=H .0 .0 .0; H .0 .0 0.74
       units=Angstrom
       charge=0
       multiplicity=1
       basis=sto3g
    &end

Experienced chemists who already have existing PyQuante control files can simply paste the contents
of those files into the ``pyquante`` section of the input file.  This configuration can also be
easily achieved using the Qiskit Chemistry :ref:`qiskit-chemistry-gui`.

.. _hdf5:

----
HDF5
----

Qiskit Chemistry uses a molecular input file written on top of one of the classical computational
software drivers that it interfaces.  Qiskit Chemistry executes a driver classically,
only to the extent necessary to compute some intermediate data which, combined with the molecular
configuration, can later be used to form the input to one of the
Aqua :ref:`quantum-algorithms`.

As mentioned above, the intermediate data extracted from the classical computational software
consists of the following:

1. One- and two-body integrals in Molecular Orbital (MO) basis
2. Dipole integrals
3. Molecular orbital coefficients
4. Hartree-Fock energy
5. Nuclear repulsion energy

Once extracted, the structure of this intermediate data is independent of the classical driver
that was used to compute it.
However, the level of accuracy of such data does depend on the computational chemistry software;
more elaborate software packages are more likely to produce more accurate data.

Qiskit Chemistry offers the option to serialize this data in a binary format known as
`Hierarchical Data Format 5 (HDF5) <https://support.hdfgroup.org/HDF5/>`__.
This is done for future reuse and exchange of input data among researchers who may not have a
particular computational
chemistry driver installed on their computers, or may have a different version of that driver.
HDF5 is configured as a prebuilt driver in Aqua because it allows for chemistry input to be passed
into the computation.  In fact, HDF5 is the only driver that does not require any installation
other the installation of Qiskit Chemistry itself.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Generation of an HDF5 Input File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The most intuitive way to generate an HDF5 input file is by using the Qiskit Chemistry
:ref:`qiskit-chemistry-gui`.
Through the GUI, you can load an existing :ref:`qiskit-chemistry-input-file` from the ``chemistry``
folder of the `Qiskit Tutorials GitHub repository <https://github.com/Qiskit/qiskit-tutorials>`__
(which must have been installed on your file system via a ``git clone`` command)
by selecting **Open...** from the **File** menu.  Alternatively, you can create and then potentially
customize a brand new :ref:`qiskit-chemistry-input-file` by choosing **New** from the **File** menu.
Once you have configured the chemistry experiment in one of the existing classical drivers
(:ref:`gaussian-16`, :ref:`psi4`, :ref:`pyscf` or :ref:`pyquante`),
you can specify the name of the file where you want the HDF5 file to be serialized.  This can be
done by assigning a value to the ``hdf5_output`` field of the ``driver`` section.
Upon completing its execution, Qiskit Chemistry displays the following message:

.. code:: sh

    HDF5 file saved '/Users/username/Documents/temp/molecule.hdf5'

assuming that ``molecule.hdf5`` and ``/Users/username/Documents/temp`` are the file name
and directory path you chose, respectively.

Using the GUI is the most intuitive option to generate the HDF5 file corresponding to a given
experiment. The same result can be obtained by assigning a value to the ``hdf5_output`` field of
the ``driver`` section of an :ref:`qiskit-chemistry-input-file` and then invoking the Qiskit
Chemistry :ref:`qiskit-chemistry-command-line` tool with the name of that file as the input
parameter.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Using an HDF5 File as the Input to an Experiment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you later want the HDF5 file to be deserialized and its contents used as the input for a
chemistry experiment, you can select ``HDF5`` as the driver in an
:ref:`qiskit-chemistry-input-file`.  Doing so will require the ``hdf5`` section in the input
file to be configured by assigning a valid fully qualified file name to the ``hdf5_input``
field, as shown:

.. code:: python

    &hdf5
       hdf5_input=molecule.hdf5
    &end
