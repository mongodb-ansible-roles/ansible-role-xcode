import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_node_exporter(host):
    cmd = host.run("xcode-select -p")
    assert cmd.succeeded
    assert cmd.stdout == "/Applications/Xcode_12.2.app/Contents/Developer\n"
