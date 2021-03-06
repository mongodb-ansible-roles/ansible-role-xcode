Ansible role for xcode
==================================

Installs xcode on Mac hosts. This role may fail if the certificate attached to the xcode xip file is expired.
You can take a look at this issue for more information: https://forums.developer.apple.com/thread/125108
The fix would be to redownload a new xip from Apple's developer page, which should have an updated certificate

[![CircleCI](https://img.shields.io/circleci/build/github/mongodb-ansible-roles/ansible-role-xcode/master?style=flat-square)](https://circleci.com/gh/mongodb-ansible-roles/ansible-role-xcode)

Requirements
------------

Command line tools must be installed. This is taken care of by the command-line-tools role. Please make sure the command line tools are the correct version

Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-------:|:--------:|
| xcode\_versions | List of xcode versions with minor versions to install | List of objects | See example | true |

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

License
-------

[Apache License](LICENSE)
