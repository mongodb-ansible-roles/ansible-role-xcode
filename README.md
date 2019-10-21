Ansible role for xcode
==================================

Installs xcode on Mac hosts

[![CircleCI](https://img.shields.io/circleci/build/github/mongodb-ansible-roles/ansible-role-xcode/master?style=flat-square)](https://circleci.com/gh/mongodb-ansible-roles/ansible-role-xcode)

Requirements
------------

Command line tools must be installed. This is taken care of by the command-line-tools role

Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-------:|:--------:|
| xcode\_versions | List of xcode versions with minor versions to install | List of objects | See example | true |

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - role: ansible-role-xcode
      vars:
        xcode_versions:
          - major: 10.2
            minor: 0
            gm_licence: EA1478
```

Development
-----------

Testing this role locally requires the CircleCI [Local CLI](https://circleci.com/docs/2.0/local-cli/).

To install the CLI for macOS and Linux, invoke the following command:

    $ curl -fLSs https://circle.ci/cli | DESTDIR=/usr/local/bin bash

After installing the CLI, invoke the following command to run the Molecule tests:

    $ make test

License
-------

[Apache License](LICENSE)
