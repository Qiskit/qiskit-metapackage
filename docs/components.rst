Component Status
================

Qiskit is developing so fast that is it is hard to keep all different parts
of the API supported for various versions. We do our best and we use 
the rule that for one minor version update, for example 0.6 to 0.7,
we will keep the API working with a deprecated warning. Please don’t
ignore these warnings. Sometimes there are cases in which this can’t
be done and for these in the release history we will outline these in
great details. 

This being said as we work towards Qiskit 1.0 there are some modules 
that have become stable and the table below is our attempt to label them 

 

Modules
-------

+---------------+------------+------------------------------------+
| Name          | status     | Note                               |
+===============+============+====================================+
| circuit       | unstable   | the goal is stable version in 0.8  |
+---------------+------------+------------------------------------+
| converters    | unstable   | the goal is stable version in 0.9  |
+---------------+------------+------------------------------------+
| compiler      | unstable   | the goal is stable version in 0.10 |
+---------------+------------+------------------------------------+
| dagcircuit    | remove     | will be part of circuits           |
+---------------+------------+------------------------------------+
| extensions    | remove     | will be part of circuits           |
+---------------+------------+------------------------------------+
| mapper        | remove     | will be part of transpiler         |
+---------------+------------+------------------------------------+
| providers     | stable     | completed in version 0.7           |
+---------------+------------+------------------------------------+
| pulse         | unstable   | the goal is stable in version 0.10 |
+---------------+------------+------------------------------------+
| qasm          | unstable   | passer location to be determined   |
+---------------+------------+------------------------------------+
| qobj          | unstable   | the goal is stable version in 0.8  |
+---------------+------------+------------------------------------+
| quantum_info  | unstable   | the goal is stable version in 0.10 |
+---------------+------------+------------------------------------+
| result        | stable     | completed in version 0.7           |
+---------------+------------+------------------------------------+
| schemas       | stable     | completed in version 0.7           |
+---------------+------------+------------------------------------+
| tools         | unstable   | various elements to be removed     |
+---------------+------------+------------------------------------+
| transpiler    | unstable   | the goal is stable version in 0.9  |
+---------------+------------+------------------------------------+
| validation    | stable     | completed in version 0.7           |
+---------------+------------+------------------------------------+
| visualization | unstable   | the goal is stable version in 0.8  |
+---------------+------------+------------------------------------+

Basic Aer Provider
------------------

This is stable the addition here a name change of the folder to basicaer in version 0.8

Aer Provider
------------

TBD


