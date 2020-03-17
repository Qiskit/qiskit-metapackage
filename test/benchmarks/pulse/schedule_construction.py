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

from qiskit.pulse import Schedule, Gaussian, DriveChannel, SamplePulse


def build_schedule(my_pulse, number_of_unique_pulses, number_of_channels):
    sched = Schedule()
    for i in range(number_of_unique_pulses):
        for channel in range(number_of_channels):
            sched += my_pulse((DriveChannel(channel)))

    return sched


def sample_pulse(number_of_unique_pulses, number_of_channels):
    my_pulse = SamplePulse([0.00043, 0.0007 , 0.00112, 0.00175, 0.00272,
                            0.00414, 0.00622,0.00919, 0.01337, 0.01916,
                            0.02702, 0.03751, 0.05127, 0.06899, 0.09139,
                            0.1192 , 0.15306, 0.19348, 0.24079, 0.29502,
                            0.35587, 0.4226 , 0.49407, 0.56867, 0.64439,
                            0.71887, 0.78952, 0.85368, 0.90873, 0.95234,
                            0.98258, 0.99805, 0.99805, 0.98258, 0.95234,
                            0.90873, 0.85368, 0.78952, 0.71887, 0.64439,
                            0.56867, 0.49407, 0.4226 , 0.35587, 0.29502,
                            0.24079, 0.19348, 0.15306, 0.1192, 0.09139,
                            0.06899, 0.05127, 0.03751, 0.02702, 0.01916,
                            0.01337, 0.00919, 0.00622, 0.00414, 0.00272,
                            0.00175, 0.00112, 0.0007, 0.00043],
                           name="short_gaussian_pulse")

    return (build_schedule(my_pulse,
                           number_of_unique_pulses,
                           number_of_channels))


def parametric_pulse(self, number_of_unique_pulses, number_of_channels):
    my_pulse = Gaussian(duration=25, sigma=4, amp=0.5j)

    return (build_schedule(my_pulse,
                           number_of_unique_pulses,
                           number_of_channels))


class ScheduleConstructionBench:
    params = ([1, 2, 5, 8, 14, 20], [8, 128, 2048, 8192, 32768, 131072])
    param_names = ['number_of_unique_pulses', 'number_of_channels']
    timeout = 600

    def setup(self, number_of_unique_pulses, number_of_channels):
        self.empty_sched = sample_pulse(number_of_unique_pulses, 0)
        self.sample_sched = sample_pulse(number_of_unique_pulses,
                                            number_of_channels)
        self.parametric_sched = parametric_pulse(number_of_unique_pulses,
                                                 number_of_channels)

    def track_append_instruction(self,
                                 number_of_unique_pulses,
                                 number_of_channels):
        self.sample_sched.append(self.parametric_sched)

    def track_insert_instruction_left_to_right():
        if (self.parametric_sched.stop_time >= self.sample_sched.start_time):
            sched = self.sample_sched.shift(self.parametric_sched.stop_time)

        self.sched.insert(self.parametric_sched.start_time,
                          self.parametric_sched)

    # def instruction_to_schedule():
    #     pass
