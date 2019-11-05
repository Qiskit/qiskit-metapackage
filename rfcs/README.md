# Qiskit RFCs
The purpose of a Qiskit Request for Comments (RFC) is to communicate and engage with the community in the development and direction of Qiskit. RFCs enable engineering and research stakeholders to communicate large design changes.

# Process
- Fork the [Qiskit repository](https://github.com/Qiskit/qiskit)
- Copy the template [####-template.md](\####-template.md) to `####-rfc-title.md`, do not yet assign a number. If the RFC requires additional files, it may be placed in a folder with the name `####-rfc-title`.
- Fill in the template with your RFC. Be thorough and convincing, use proper grammar and technical language where appropriate. The aim of an RFC is to convey both a change and a vision for the future it will enable, you must convince the larger Qiskit team that it is valuable.
- Submit a pull request to the Qiskit meta-package titled "[RFC] RFC Title"
- Each RFC will be labeled with the relevant packages, so that the respective maintainers of the packages may be notified of the RFC.
- The RFC will be triaged and if it is of sufficient quality a *review committee* will be formed by assigning the PR to a group of *committee members* who are each maintainer(s) of the relevant Qiskit packages. Committee members are responsible for moderating the development of the RFC and acceptance or closure of the RFC. It is expected that RFC should fail in the early, rather than later stages of the development cycle. If the RFC author is themselves a maintainer of one of the relevant packages, they should not be a committee member for their own RFC.
- Interested parties should discuss and modify the RFC within the pull-request. Efforts should be made to summarize offline discussions within the PR. The aim is to capture the outcome of discussion within the RFC, and the flow of development within the PR.
- The RFC will go through many iterations at this stage, *do not* squash/rebase the RFC commits. The aim is to capture the history of the document.
- When the RFC has satisfied a committee member, they should review and approve the PR. If it is not progressing satisfactorily, or supported by the review committee it may be closed at any time. This may be petitioned by reopening the PR, along with a potential request for a new review committee.
- Upon approval by all review committee members, the RFC will be assigned a number of `max(rfc_####) + 1`, the filename will be updated to reflect this and the author list should be validated. Note that as Qiskit is still undergoing rapid-development there is no required grace period between acceptance and merger, as the project matures this is expected to change.
- The RFC will then be merged by one of the committee members.
- After acceptance, the implementation of the contents of the RFC may proceed.

# Contributors
An *RFC author* write and champions and RFC through the process.

A *community member* provides feedback on an RFC either as a PR comment, or an edit to the RFC.

A *review committee* is the group *committee members*, all of which are RFC PR assignees and are maintainers of one or many of the Qiskit meta-package projects. The committee is responsible for guiding, reviewing and finally closing/approving the RFC.

# When Should You Write an RFC?
RFC's should be reserved for 'large' engineering changes to the Qiskit meta-package, its members and the RFC process itself. By this, we mean changes where the implementation path is not immediately clear and needs to be deconstructed by the larger Qiskit team.

Questions you might ask yourself:
- Will the implementation involve many developers?
- Will the implementation span across multiple points in the Qiskit stack?
- Will the changes cause ramifications for the average user?
- Will the changes require collaboration with outside sources?

## Sub-package guidelines
For more details on RFCs for specific Qiskit projects see the guidelines for:

# Template
Use the [Qiskit RFC template](####-template.md) to prepare your RFC.
