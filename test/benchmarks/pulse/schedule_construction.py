# -*- coding: utf-8 -*

# This code is part of Qiskit.
#
# (C) Copyright IBM 2020.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

# pylint: disable=missing-docstring,invalid-name,no-member
# pylint: disable=attribute-defined-outside-init

import numpy as np
from qiskit import schedule, QuantumCircuit, QuantumRegister
from qiskit.circuit import Gate
from qiskit.pulse import Schedule, Gaussian, DriveChannel, SamplePulse
from qiskit.test.mock import FakeOpenPulse2Q


def build_schedule(my_pulse, number_of_unique_pulses, number_of_channels):
    sched = Schedule()
    for _ in range(number_of_unique_pulses):
        for channel in range(number_of_channels):
            sched += my_pulse((DriveChannel(channel)))
    return sched


def build_sample_pulse_schedule(number_of_unique_pulses, number_of_channels):
    my_pulse = SamplePulse(np.random.random(50),
                           name="short_gaussian_pulse")
    return build_schedule(my_pulse,
                          number_of_unique_pulses,
                          number_of_channels)


def build_parametric_pulse_schedule(number_of_unique_pulses,
                                    number_of_channels):
    my_pulse = Gaussian(duration=25, sigma=4, amp=0.5j)
    return build_schedule(my_pulse,
                          number_of_unique_pulses,
                          number_of_channels)


class ScheduleConstructionBench:
    params = ([1, 2, 5], [8, 128, 2048])
    param_names = ['number_of_unique_pulses', 'number_of_channels']
    timeout = 600

    def setup(self, unique_pulses, channels):
        self.sample_sched = build_sample_pulse_schedule(unique_pulses,
                                                        channels)
        self.parametric_sched = build_parametric_pulse_schedule(unique_pulses,
                                                                channels)

        qr = QuantumRegister(1)
        self.qc = QuantumCircuit(qr)
        self.qc.append(Gate('my_pulse', 1, []), qargs=[qr[0]])
        self.backend = FakeOpenPulse2Q()
        self.inst_map = self.backend.defaults().instruction_schedule_map
        self.add_inst_map = self.inst_map.add('my_pulse', [0], self.parametric_sched)

    def time_sample_pulse_schedule_construction(self,
                                                unique_pulses,
                                                channels):
        build_sample_pulse_schedule(unique_pulses, channels)

    def time_parametric_pulse_schedule_construction(self,
                                                    unique_pulses,
                                                    channels):
        build_parametric_pulse_schedule(unique_pulses, channels)

    def time_append_instruction(self, _, __):
        self.sample_sched.append(self.parametric_sched)

    def time_insert_instruction_left_to_right(self, _, __):
        sched = self.sample_sched.shift(self.parametric_sched.stop_time)
        sched.insert(self.parametric_sched.start_time,
                     self.parametric_sched)

    def time_build_instruction(self, _, __):
        self.inst_map.add('my_pulse', [0], self.parametric_sched)

    def time_instruction_to_schedule(self, _, __):
        sched = Schedule()
        sched.union(schedule(self.qc, self.backend, inst_map=self.add_inst_map))
