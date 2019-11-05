# Qiskit RFCs
The purpose of a Qiskit Request for Comments (RFC) is to communicate and engage with the community in the development and direction of Qiskit. RFCs enable engineering and research stakeholders to communicate large design changes.

# Template
Use the [Qiskit RFC template](####-template.md) to prepare your RFC.

# Process
To prepare an RFC:
- Fork the [Qiskit repository](https://github.com/Qiskit/qiskit)
- Copy the template [####-template.md](####-template.md) to `####-rfc-title.md`, do not yet assign a number. If the RFC requires additional files, it may be placed in a folder with name `####-rfc-title`.
- Fill in the template with your RFC. Be thorough and convincing, pay attention to proper grammar. The aim of an RFC is to convey both a change and a vision for the future it will enable, you must convince the larger Qiskit team that it is valuable.
- Submit a pull request to the Qiskit meta-package titled "[RFC] New Feature""
- Each RFC will be labelled with the relevant packages, so that the respective maintainers of the packages may be notified of the RFC and it may be assigned to a maintainer(s) of the relevant Qiskit packages. If the submitter is themselves a maintainer of the relevant packages, they should not be assigned to their own issue.
- Interested parties should discuss and modify the RFC within the pull-request. Efforts should be made to summarize offline discussion within the PR. The aim is to capture the outcome of discussion within the RFC, and the flow of development within the PR.
- The RFC will go through many iterations at this stage, *do not* squash/rebase the RFC commits. The aim is to capture the history of the document.
- When the RFC has satisfied all assigned developers, they should review and approve the PR.
- Upon approval by all assignees, the RFC will be assigned a number of `max(rfc_####) + 1`, the filename updated to reflect this and validate that the authors list is correct.
- The RFC will then be merged by one of the assignees.
- The contents of the RFC may now proceed with development.

# RFC Life-cycle
To be decided

# When Should You Write an RFC?
RFC's should be reserved for 'large' engineering changes to the Qiskit meta-package, its members and the RFC process itself. By this we mean changes where the implementation path is not immediately clear and needs to be deconstructed by the larger Qiskit team.

Questions you might ask yourself:
- Will the implementation involve many developers?
- Will the implementation cross multiple points in the stack?
- Will the changes cause ramifications for the average user?
- Does the project require approvals from outside sources?

## Sub-package guidelines
For more details on RFCs for specific Qiskit projects see the guidelines for:
