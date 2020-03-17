# -*- coding: utf-8 -*

# This code is part of Qiskit.
#
# (C) Copyright IBM 2018, 2019.
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
from qiskit.pulse import Schedule, Gaussian, DriveChannel, SamplePulse


def build_schedule(my_pulse, number_of_unique_pulses, number_of_channels):
    sched = Schedule()
    for _ in range(number_of_unique_pulses):
        for channel in range(number_of_channels):
            sched += my_pulse((DriveChannel(channel)))

    return sched


def sample_pulse(number_of_unique_pulses, number_of_channels):
    my_pulse = SamplePulse(np.random.random(50),
                           name="short_gaussian_pulse")

    return (build_schedule(my_pulse,
                           number_of_unique_pulses,
                           number_of_channels))


def parametric_pulse(number_of_unique_pulses, number_of_channels):
    my_pulse = Gaussian(duration=25, sigma=4, amp=0.5j)

    return (build_schedule(my_pulse,
                           number_of_unique_pulses,
                           number_of_channels))


class ScheduleConstructionBench:
    params = ([1, 2, 5], [8, 128, 2048])
    param_names = ['number_of_unique_pulses', 'number_of_channels']
    timeout = 600

    def setup(self, number_of_unique_pulses, number_of_channels):
        self.empty_sched = sample_pulse(number_of_unique_pulses, 0)
        self.sample_sched = sample_pulse(number_of_unique_pulses,
                                         number_of_channels)
        self.parametric_sched = parametric_pulse(number_of_unique_pulses,
                                                 number_of_channels)

    def time_append_instruction(self, _, __):
        self.sample_sched.append(self.parametric_sched)

    def time_insert_instruction_left_to_right(self, _, __):
        if self.parametric_sched.stop_time >= self.sample_sched.start_time:
            sched = self.sample_sched.shift(self.parametric_sched.stop_time)

        sched.insert(self.parametric_sched.start_time,
                     self.parametric_sched)

    # def instruction_to_schedule():
    #     pass
