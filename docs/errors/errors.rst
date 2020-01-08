.. _errors:

#############################
IBM Quantum Cloud Error Codes
#############################

.. contents:: Error Codes
   :local:

1XXX
====
.. _1xxx:

================  ============================================================
Error codes       Messages
================  ============================================================
**1000**          :Error message: API Internal error.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**1001**          :Error message: qObject is larger than the maximum size.
                  :Solution: Run a small Job. Split the circuits
                             in smaller jobs.

**1002**          :Error message: Error in the validation process of the job.
                  :Solution: Check the Job, it is not valid to run on this
                             backend.

**1003**          :Error message: Error in transpilation process.
                  :Solution: Check the Job, it is not valid to run on this
                             backend.

**1004**          :Error message: The Backend is not available.
                  :Solution: Use another backend to run the job.

**1005**          :Error message: Basis gates not available.
                  :Solution: Use another backend with basis gates.

**1006**          :Error message: Error during call to converter microservice.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**1007**          :Error message: Backend not found.
                  :Solution: Check the backend name, maybe it is wrong.

**1008**          :Error message: Error during the validation process of
                                  a job.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**1009**          :Error message: Required backend information not found.
                  :Solution: Use another backend to run the job.

**1010**          :Error message: Error returned at backend level.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**1011**          :Error message: Error publishing job at the backend queue
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**1012**          :Error message: The user reached the maximum number of
                                  jobs running concurrently.
                  :Solution: Wait until some previous jobs were finished.
                             You can cancel pending jobs to run new jobs.

================  ============================================================


2XXX
====
.. _2xxx:

================  ============================================================
Error codes       Messages
================  ============================================================
**2000**          :Error message: Backend not found.
                  :Solution: Check the backend name, maybe it is wrong.

**2001**          :Error message: Backend not available for booking.
                  :Solution: Use another backend to book a time slot.

**2002**          :Error message: Backend not available for this action.
                  :Solution: Use another backend.

**2100**          :Error message: Invalid URL to Upload to Bluemix.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**2200**          :Error message: A booking already exists.
                  :Solution: Select another dates to book.

**2201**          :Error message: Booking data is not valid.
                  :Solution: Check the booking data, maybe it is wrong.

**2202**          :Error message: Cannot cancel booking.
                  :Solution: Check the booking to cancel.

**2203**          :Error message: Provider does not have enough remaining
                                  time to book.
                  :Solution: Use another provider to book or contact with
                             your Group Administrator.

**2204**          :Error message: User already has a booking on that date.
                  :Solution: Select another dates to book.

**2205**          :Error message: Booking not found.
                  :Solution: Check the booking data, maybe it is wrong.

**2206**          :Error message: Booking on calibration time.
                  :Solution: Select another dates to book.

**2300**          :Error message: Code ID not found.
                  :Solution: Check the code data, maybe it is wrong.

**2301**          :Error message: Code not updated.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**2302**          :Error message: Code wrong.
                  :Solution: Check the code data, maybe it is wrong.

**2304**          :Error message: Error parsing QASM.
                  :Solution: Check the code data, maybe it is wrong.

**2305**          :Error message: Invalid Code.
                  :Solution: Check the code data, maybe it is wrong.

**2306**          :Error message: Invalid result.
                  :Solution: Check the code data, maybe it is wrong.

**2307**          :Error message: QASM transpilation error.
                  :Solution: Check the code data, maybe it is wrong.

**2308**          :Error message: User role not found.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**2309**          :Error message: Code not found.
                  :Solution: Check the code data, maybe it is wrong.

**2310**          :Error message: Failed to export.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**2311**          :Error message: Image wrong.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**2313**          :Error message: QASM not found.
                  :Solution: Check the code data, maybe it is wrong.

**2400**          :Error message: Error wrong data received.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**2402**          :Error message: Maximum attempts reached.
                  :Solution: Reduce the number of concurrent requests

**2403**          :Error message: Missing data in HTTP request.
                  :Solution: Check your request to the endpoint.

**2404**          :Error message: Model not found in database.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**2405**          :Error message: Error saving new data.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**2407**          :Error message: Authentication required.
                  :Solution: Try to login again.

**2408**          :Error message: Invalid Access Token.
                  :Solution: Try to login again.

**2409**          :Error message: Forbidden.
                  :Solution: You dont have access to do the action.

**2410**          :Error message: Service not accesible.
                  :Solution: You dont have access to do the action.

**2411**          :Error message: Operation not available.
                  :Solution: You dont have access to do the action.

**2412**          :Error message: Error retrieving data from database.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**2600**          :Error message: Configuration not available for this device.
                  :Solution: Try to use another backend.

**2602**          :Error message: Device not allowed.
                  :Solution: Try to use another backend.

**2603**          :Error message: Error getting topology attributes.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**2604**          :Error message: Error getting topology queues.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**2609**          :Error message: Properties are empty.
                  :Solution: Try to use another backend.

**2614**          :Error message: Topology without kind established.
                  :Solution: Try to use another backend. Contact an IBM Q
                             Administrator

**2615**          :Error message: The device is not available.
                  :Solution: Try to use another backend.

**2616**          :Error message: This device can only be used for running jobs.
                                  Try the Jobs API.
                  :Solution: Try to use anohter backend.

**2618**          :Error message: Basis gates not available.
                  :Solution: Try to use another backend.

**2620**          :Error message: Device not found.
                  :Solution: Try to use another backend.

**2622**          :Error message: Properties not found.
                  :Solution: Try to use another backend.

**2900**          :Error message: An error occur getting the hub.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**2901**          :Error message: Error checking hub or group administrators.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**2902**          :Error message: Error checking devices in the Hub.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**2903**          :Error message: Hub info not found.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**2904**          :Error message: Invalid backend to configure for booking.
                  :Solution: Use another backend.

**2905**          :Error message: Invalid parameters to configure for booking.
                  :Solution: Check the booking configuration.

**2906**          :Error message: Invalid priority value.
                  :Solution: Change the priority Value.

**2907**          :Error message: Device not available for Hub.
                  :Solution: Use another backend.

**2908**          :Error message: Error checking user in the Hub.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**2909**          :Error message: Group not found.
                  :Solution: Use another Group.

**2910**          :Error message: Hub not found.
                  :Solution: Use another Hub.

**2911**          :Error message: Invalid Hub/Group/Project.
                  :Solution: Use another provider.

**2912**          :Error message: Invalid mode to configure for booking.
                  :Solution: Use another mode to book a backend.

**2913**          :Error message: Project not found.
                  :Solution: Use another project.

**2914**          :Error message: This hub is not allowed to view analytics.
                  :Solution: Use another hub.

================  ============================================================


3XXX
====
.. _3xxx:

================  ============================================================
Error codes       Messages
================  ============================================================
**3200**          :Error message: Backend not valid.
                  :Solution: Use another backend.

**3202**          :Error message: Cannot get presigned download url.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**3203**          :Error message: Cannot get presigned upload url.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**3204**          :Error message: Error during call to converter microservice.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**3207**          :Error message: Job access not allowed.
                  :Solution: Access to another Job.

**3208**          :Error message: Job not cancelled.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**3209**          :Error message: Job not running.
                  :Solution: Check if the action makes sense.

**3210**          :Error message: Job not saved.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**3211**          :Error message: Job not valid.
                  :Solution: Check the Job sent, maybe it is wrong.

**3212**          :Error message: Job not validated.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**3213**          :Error message: Job status not valid.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**3214**          :Error message: Job transition not valid.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**3215**          :Error message: Job without code identificator.
                  :Solution: Check the Job sent, maybe it is wrong.

**3216**          :Error message: Limit not valid.
                  :Solution: Change the limit sent into the request.

**3218**          :Error message: Number of Shots not allowed.
                  :Solution: Change the number of shots.

**3220**          :Error message: Payload not valid.
                  :Solution: Change the body sent into the request. Maybe it
                             has a wrong format.

**3224**          :Error message: Q-Object memory not allowed.
                  :Solution: Disable the memory parameter in the Job.

**3226**          :Error message: Q-Object not valid.
                  :Solution: Check the format of the Job. Maybe it is wrong.

**3228**          :Error message: Q-Object-External-Storage property is not
                                  allowed in this backend.
                  :Solution: Send the content of the Job inside of the body.

**3229**          :Error message: QASM no longer accepted.
                  :Solution: Use Q-Object format.

**3230**          :Error message: Seed not allowed.
                  :Solution: Dont send seed parameter.

**3233**          :Error message: The job cant be created.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**3234**          :Error message: The job cant be validated.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**3235**          :Error message: Job cost can not be calculated.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**3236**          :Error message: The job is empty.
                  :Solution: Check the job sent. Maybe it is empty.

**3237**          :Error message: The job is invalid.
                  :Solution: Check the job sent. Maybe it is wrong.

**3239**          :Error message: Number of registers exceed the number
                                  of qubits.
                  :Solution: Define the same creg than qreg.

**3242**          :Error message: Circuit count exceeded.
                  :Solution: Send less number of circuits in the Job.

**3243**          :Error message: Circuit is too big.
                  :Solution: Reduce the content of the circuit.

**3245**          :Error message: The queue is disabled.
                  :Solution: Use another backend.

**3246**          :Error message: The queue is unavailable.
                  :Solution: Use another backend.

**3248**          :Error message: Your job is too long.
                  :Solution: Reduce the content of the job.

**3249**          :Error message: Job fields are empty.
                  :Solution: Check the Job content. Maybe it is empty.

**3250**          :Error message: Job not found.
                  :Solution: Check the job Id to query. It is wrong.

**3251**          :Error message: Job not uploaded to object storage.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**3252**          :Error message: Object storage not allowed.
                  :Solution: Send the job into the body of the request.

**3254**          :Error message: The job is not in queue.
                  :Solution: Check the status of the job.

**3255**          :Error message: Invalid share level.
                  :Solution: Update the share level.

**3253**          :Error message: Timeout getting the result.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**3300**          :Error message: Can not download job data.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**3301**          :Error message: Can not upload job data.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**3302**          :Error message: Job not found.
                  :Solution: Check the job information. Maybe it is wrong

**3400**          :Error message: License not found.
                  :Solution: Accept the license.

**3402**          :Error message: API key not found.
                  :Solution: Regenerate the API Token.

**3405**          :Error message: Codes not deleted.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**3407**          :Error message: User API token not valid.
                  :Solution: Check the API Token.

**3409**          :Error message: Error deleting entities from user.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**3410**          :Error message: Error deleting user relations.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**3418**          :Error message: Failed to create the token for the user.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**3422**          :Error message: Old password is incorrect.
                  :Solution: Check your old password. It is wrong.

**3423**          :Error message: Passwords do not match.
                  :Solution: Check the password. It is wrong.

**3424**          :Error message: Retrieving last version licenses,
                                  including future ones.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**3425**          :Error message: Retrieving last version licenses.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**3440**          :Error message: Authentication is required to perform
                                  that action.
                  :Solution: Try to login again.

**3443**          :Error message: Failed to check login.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**3444**          :Error message: License required. You need to accept
                                  the License.
                  :Solution: Accept the license.

**3445**          :Error message: Login with IBM ID required.
                  :Solution: Login using IBM ID.

**3446**          :Error message: Login failed.
                  :Solution: Try to login again.

**3452**          :Error message: The license is not accepted.
                  :Solution: Accept the License.

**3453**          :Error message: The license is required.
                  :Solution: Accept the License.

**3458**          :Error message: User reached the maximum limits of
                                  concurrent jobs.
                  :Solution: Wait until some previous jobs were finished.
                             You can cancel pending jobs to run new jobs.

**3459**          :Error message: User is blocked by wrong password.
                  :Solution: Wait 5 minutes to login again.

**3460**          :Error message: User is blocked.
                  :Solution: Contact an IBM Q Administrator.

**3467**          :Error message: Failed to create or renew API token.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**3468**          :Error message: Failed to get API token.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**3500**          :Error message: Body is wrong.
                  :Solution: Check the body of the request.

**3704**          :Error message: Error to get status from Queue.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**3811**          :Error message: Request not found.
                  :Solution: Check the request that you are trying to do.

**3900**          :Error message: Empty response from the stats micro-service.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**3901**          :Error message: Error parsing stats.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**3902**          :Error message: Error retrieving stats.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**3903**          :Error message: Invalid date.
                  :Solution: Update the dates

**3904**          :Error message: Invalid end date.
                  :Solution: Update the end date.

**3905**          :Error message: Invalid input to the stats micro-service.
                  :Solution: Check the query. It is wrong.

**3906**          :Error message: Invalid key.
                  :Solution: Check the query. It is wrong.

**3907**          :Error message: Invalid start date.
                  :Solution: Update the start date.

**3908**          :Error message: Invalid stats type.
                  :Solution: Check the query. It is wrong.

**3909**          :Error message: Missing mandatory user stats info.
                  :Solution: Check the query. It is wrong.

**3910**          :Error message: Number of months too big.
                  :Solution: Reduce the number of months.

**3911**          :Error message: Stats micro-service is not available.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**3912**          :Error message: Stats not found.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**3913**          :Error message: Analytics stats not found.
                  :Solution: Retry the action again. If it happens again
                             contact IBM Quantum via email or slack for help.

**3914**          :Error message: Project level does not support aggregated
                                analytics stats.
                  :Solution: Try to use another project.

**3915**          :Error message: Missing start and end dates and allTime not
                                  set to true for analytics stats.
                  :Solution: Set start and end date in the query.

================  ============================================================


5XXX
====
.. _5xxx:

================  ============================================================
Error codes       Messages
================  ============================================================
**5201**          :Error message: Job timed out after {} seconds.
                  :Solution: Reduce the complexity of the job, or number of
                             shots.

**5202**          :Error message: Job was canceled
                  :Solution: None. Job was canceled.
================  ============================================================


6XXX
====
.. _6xxx:

================  ============================================================
Error codes       Messages
================  ============================================================
**6000**          :Error message: Too many shots given ({} > {}).
                  :Solution: Reduce the requested number of shots.

**6001**          :Error message: Too few shots given ({} < {}).
                  :Solution: Increase the number of shots.

**6002**          :Error message: Too many experiments given ({} > {}).
                  :Solution: Reduce the number of experiments given at once.

**6003**          :Error message: Too few experiments given ({} < {}).
                  :Solution: Increase number of experiments.

================  ============================================================


7XXX
====
.. _7xxx:

================  ============================================================
Error codes       Messages
================  ============================================================
**7000**          :Error message: Instruction not in basis gates:
                                  instruction: {}, qubits: {}, params: {}
                  :Solution: Instruction not supported by backend. Please
                             remove the instruction shown in the error message.

**7001**          :Error message: Instruction {} is not supported.
                  :Solution: Remove unsupported instruction, or run on a
                             simulator that supports it.

**7002**          :Error message: Memory output is disabled.
                  :Solution: Select a different backend or set
                             `memory=False` in transpile / execute.

**7003**          :Error message: qubits: {} and classical bits: {} do not
                                  have equal lengths.
                  :Solution: Length of memory slots must be same as number of
                              qubits used

**7004**          :Error message: Qubit measured multiple times in circuit.
                  :Solution: Remove multiple measurements on qubits.

**7005**          :Error message: Error in supplied instruction.
                  :Solution: Please refer to IQX gate overview and make sure
                             the instructions are correct.

**7006**          :Error message: Qubit measurement is followed by instructions.
                  :Solution: Cannot perform any instruction on a measured qubit.
                             Please remove all instructions following a measurement.

================  ============================================================


8XXX
====
.. _8xxx:

================  ============================================================
Error codes       Messages
================  ============================================================
**8000**          :Error message: Channel {}{} lo setting: {} is not within
                                  acceptable range of {}.
                  :Solution: Set channel LO within specified range.

**8001**          :Error message: qubits {} in measurement are not mapped.
                  :Solution: Assign qubits to a classical memory slot.

**8002**          :Error message: Total samples exceeds the maximum number of
                                  samples for channel {}. ({} > {}).
                  :Solution: Reduce number of samples below specified limit.

**8003**          :Error message: Total pulses exceeds the maximum number of
                                  pulses for channel: {}, ({} > {}).
                  :Solution: Reduce number of pulses below specified limit.

**8004**	  :Error message: Channel {}{} is not available.
                  :Solution: Must use available drive channels.

**8006**	  :Error message: Gate {}in line {}s not understood ({}).
                  :Solution: This instruction is not supported. Please make
                              sure that the gate name is correct and it is within
                              the gate overview section of IQX website.

**8007**	  :Error message: Qasm gate not understood: {}.
                  :Solution: The instruction is not understood. Please refer to IQX
                             website and make sure the instruction is within the gate
                             overview section.

**8008**	  :Error message: Unconnected Qubits.
                  :Solution: Please refer to the qubit mapping for this backend in
                             IQX website and make sure the qubits are connected.

**8009**          :Error message: Measurement level is not supported..
                  :Solution: The given measurement level is not supported on this backend.
                             Please change it to 0-2 except the measurement level specified.

**8011**	  :Error message: Pulse experiments are not supported on this system..
                  :Solution: Pulse experiment is not supported on this backend.
                             Please use a backend that support pulse to run this experiment.

**8013**	  :Error message: This backend does not support conditional pulses.
                  :Solution: Conditionals are not supported on this backend.
                             Please remove the conditional instruction in your program.

**8014**	  :Error message: reset instructions are not supported.
                  :Solution: Reset instructions are not supported at this time for this
                             backend. Please remove the reset instruction.

**8016**          :Error message: Pulse {} has too few samples ({} > {}).
                  :Solution: Please add more samples.

**8017**          :Error message: Pulse not a multiple of {} samples.
                  :Solution: Due to hardware limitations pulses must be a multiple of a
                             given number of samples.

================  ============================================================


9XXX
====
.. _9XXX:

================  ============================================================
Error codes       Messages
================  ============================================================
**9999**          :Error message: Internal error.
                  :Solution: Contact IBM Quantum via email or slack for help.
================  ============================================================
