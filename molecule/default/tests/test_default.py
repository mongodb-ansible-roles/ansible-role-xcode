import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_node_exporter(host):
    cmd = host.run(
            "/Applications/Xcode10.2.app/Contents/Developer/usr/bin/git"
            " --version")
    assert cmd.succeeded
    assert cmd.stdout == "git version 2.20.1 (Apple Git-117)\n"
