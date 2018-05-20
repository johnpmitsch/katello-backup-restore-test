# Katello-backup-restore-test # 
For testing of foreman-maintain [backup/restore](https://github.com/theforeman/foreman_maintain)

## Prerequisites ##
- Ansible 2.5+
- A production Katello instance (latest version) and/or foreman-proxy

## Quick Setup ##
*Its a good idea to snapshot your machine before running tests, you can always revert it to have a clean environment*
1. on the system you are running the machine, copy your ssh key to the katello system: `ssh-copy-id root@<katello_machine>`
2. `cp inventory.sample inventory` and add the ip of the katello system under `[katello]`, the ip of the foreman-proxy under `[foreman-proxy]`, and/or the ip of a katello instance with a remote database under `[katello-remote-db]`. You can add multiple machines to each host group. You also do not need to fill out every host group.
3. Update the inventory file with the pr number you want to test using `pr_number`. If you want to test the master branch, change `use_master_branch` to `True` (This will override the pr_number)
4. The ansible playbooks are separated by host group. To run all the playbooks the fastest, run each one separately in different terminals so they can run in parallel. `ansible-playbook katello.yml`, `ansible-playbook foreman_proxy.yml`, and `ansible-playbook katello_remote_db.yml`. Otherwise, you can run `ansible-playbook katello.yml && ansible-playbook foreman_proxy.yml && ansible-playbook katello_remote_db.yml` (be sure to check each output or logs for failures)
