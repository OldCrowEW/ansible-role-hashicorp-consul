import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_consul_user(host):
    user = host.user("consul")

    assert user.exists
    assert user.group == "consul"
    assert user.shell == "/sbin/nologin"
    assert user.home == "/var/run/consul"


def test_consul_bin_file(host):
    f = host.file('/usr/sbin/consul')

    assert f.exists
    assert f.is_file


def test_consul_conf_dir(host):
    f = host.file('/etc/consul')

    assert f.exists
    assert f.is_directory


def test_consul_config(host):
    f = host.file('/etc/consul/consul.hcl')

    assert f.exists
    assert f.is_file
    assert f.user == 'consul'
    assert f.group == 'consul'
    assert f.mode == 0o640


def test_consul_confd_dir(host):
    f = host.file('/etc/consul/conf.d')

    assert f.exists
    assert f.is_directory
    assert f.user == 'consul'
    assert f.group == 'consul'


def test_consul_sysconfig(host):
    f = host.file('/etc/sysconfig/consul')

    assert f.exists
    assert f.is_file


def test_consul_data_dir(host):
    f = host.file('/var/lib/consul')

    assert f.exists
    assert f.is_directory


def test_consul_run_dir(host):
    f = host.file('/var/run/consul')

    assert f.exists
    assert f.is_directory


def test_consul_systemd_file(host):
    f = host.file('/lib/systemd/system/consul.service')

    assert f.exists
    assert f.is_file


def test_consul_running_and_enabled(host):
    service = host.service('consul')

    assert service.is_running
    assert service.is_enabled
