The main goal of the benchmarking framework is to detect regressions during development, but one can run benchmarks at any specific commit just to see how it performs, this can be a very useful tool for Aer developers so they can make sure their changes don't introduce important performance regressions.

Our benchmarking framework is based on [Airspeed Velocity](https://asv.readthedocs.io/).
We have only implemented benchmarks for the Qiskit Addon, not the standalone mode.

# Where are the benchmarks
All the benchmarks are under the `test/benchmark` directory.
There you'll find a bunch of `*_benchmarks.py` files which represent the different type of benchmarks we will run:
- Quantum Volume with different number of qubits and noise models
- Simple one-gate circuits with different number of qubits and noise models.


# How to run the benchmarks
All prerequistes for building the project need to be installed in the system, take a look at the [CONTRIBUTING guide](.github/CONTRIBUTING.md) if you don't have them already installed.

Install Airspeed Velocity (`ASV`):
```
$ pip install asv
```

Move to the `test/benchmarks/aer` directory:
```
$ cd test/benchmarks/aer
```

And run `asv` using the correct configuration file, depeding on what O.S. you are executing them:
Linux:
```
$ asv run --config asv.linux.conf.json -ve --launch-method spawn NEW
```

MacOS:
```
$ asv run --config asv.macos.conf.json -ve --launch-method spawn NEW
```

The NEW parameter at the end of the command will tell ASV to run all new commits that haven't been benchmarked yet (it has an internal database with all the benchmarks already run in this machine).
There are other parameters that will change benchmarking behavior, so we recommend going to the official website to read the [doc](https://asv.readthedocs.io/en/stable/index.html).


NOTE: We only support Linux and MacOS at the moment

Depending on your system, benchmarks will take a while to complete.
After the completion of the tests, you will see the results with a format similar like this:
```
· Creating environments
· Discovering benchmarks
· Running 3 total benchmarks (1 commits * 1 environments * 3 benchmarks)
[  0.00%] · For qiskit-aer commit 8b4f4de1 <master>:
[  0.00%] ·· Benchmarking conda-py3.7
[ 16.67%] ··· Running (quantum_volume_benchmarks.QuantumVolumeTimeSuite.time_quantum_volume--)..
[ 50.00%] ··· Running (simple_benchmarks.SimpleU3TimeSuite.time_simple_u3--).
[ 66.67%] ··· quantum_volume_benchmarks.QuantumVolumeTimeSuite.time_quantum_volume
[ 66.67%] ··· ================= ========== ===================== ============= =============
              --                                        Noise Model                         
              ----------------- ------------------------------------------------------------
                Quantum Volume   No Noise   Mixed Unitary Noise   Reset Noise   Kraus Noise 
              ================= ========== ===================== ============= =============
                Num. qubits: 5   123±4ms          124±10ms          154±20ms      145±20ms  
               Num. qubits: 10   292±10ms         319±50ms          299±10ms      346±2ms   
               Num. qubits: 15   3.17±2s          2.38±2s           2.19±2s       9.76±2s   
              ================= ========== ===================== ============= =============

[ 83.33%] ··· simple_benchmarks.SimpleCxTimeSuite.time_simple_cx
[ 83.33%] ··· ====================== ========== ===================== ============= =============
              --                                             Noise Model                         
              ---------------------- ------------------------------------------------------------
               Simple cnot circuits   No Noise   Mixed Unitary Noise   Reset Noise   Kraus Noise 
              ====================== ========== ===================== ============= =============
                  Num. qubits: 5      47.2±2ms         111±40ms          46.8±1ms     21.1±0.2ms 
                 Num. qubits: 10      117±60ms         172±60ms          164±30ms     28.6±0.3ms 
                 Num. qubits: 15      213±30ms         223±80ms          223±90ms      258±5ms   
              ====================== ========== ===================== ============= =============

[100.00%] ··· simple_benchmarks.SimpleU3TimeSuite.time_simple_u3
[100.00%] ··· ==================== ============ ===================== ============= =============
              --                                            Noise Model                          
              -------------------- --------------------------------------------------------------
               Simple u3 circuits    No Noise    Mixed Unitary Noise   Reset Noise   Kraus Noise 
              ==================== ============ ===================== ============= =============
                 Num. qubits: 5     20.3±0.3ms        21.3±0.5ms        20.7±0.4ms    21.5±0.1ms 
                Num. qubits: 10     26.6±0.2ms        27.8±0.3ms        27.6±0.5ms    28.4±0.2ms 
                Num. qubits: 15      244±40ms          312±70ms         295±100ms     179±100ms  
              ==================== ============ ===================== ============= =============

```

# Interpreting the data

The output format is pretty self-explanatory, so every row starting with the text: `Num. quits:` repesents all the benchmarks run for this number of quibits configuration, more precisely, we run 4 benchmarks for every number of qubits configuration, and each of the benchmarks are run with a different noise model, so for example, this line:
```
  Quantum Volume   No Noise   Mixed Unitary Noise   Reset Noise   Kraus Noise
================= ========== ===================== ============= =============
  Num. qubits: 15   3.17±2s          2.38±2s           2.19±2s       9.76±2s
```
it's telling us that for our Quantum Volume circuit the time it took to complete was:
- 3.17 seconds with no noise at all
- 2.38 seconds with Mixed unitary noise
- 2.19 seconds with Reset noise
- 9.76 seconds with Kraus noise

