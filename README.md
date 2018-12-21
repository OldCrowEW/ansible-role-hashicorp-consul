# ansible-role-hashicorp-consul

[![Build Status](https://travis-ci.org/OldCrowEW/ansible-role-hashicorp-consul.svg?branch=master)](https://travis-ci.org/OldCrowEW/ansible-role-hashicorp-consul)

Consul is a distributed service mesh to connect, secure, and configure services across any runtime platform and public
or private cloud.

This role deploys one node with bootstrap, server and ui role(s).

## Requirements

You must have the unzip package installed on target machine for unarchive task to complete successfully.

## Role Variables

So many vars. Var all the things! Although this role only currently supports CentOS 7, it can easily be used on say a
raspberry pi by having a playbook such as:

    - hosts: consul
      become: yes

      vars:
        consul_arch: arm
        consul_sysconfig: /etc/default/consul
      roles:
         - ansible-role-hashicorp-consul

## Dependencies

None.

## Example Playbook

    - hosts: servers
      roles:
         - { role: ansible-role-hashicorp-consul }

## License

BSD

## Author Information

John Favorite