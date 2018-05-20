# Katello-backup-restore-test # 
For testing of foreman-maintain [backup/restore](https://github.com/theforeman/foreman_maintain)

## Prerequisites ##
- Ansible 2.5+
- A production Katello instance, Foreman proxy with content, and/or any other systems you would like to test foreman-maintain's backup/restore commands on.

## Quick Setup ##
*Its a good idea to snapshot your machine before running tests, you can always revert it to have a clean environment*
1. on the system you are running ansible, copy your ssh key to the katello system: `ssh-copy-id root@<katello_machine>`
2. `cp inventory/inventory.sample inventory/inventory` and add the ip of the katello system under `[katello]`, the ip of the foreman-proxy under `[foreman-proxy]`, and/or the ip of a katello instance with a remote database under `[katello-remote-db]`. You can add multiple machines to each host group. You also do not need to fill out every host group.
3. The playbook can be run using `ansible-playbook test-backup-restore.yml`. You have to pass either `use_master_branch` or `pr_number` using `--extra-vars` param. To test a PR, run `ansible-playbook test-backup-restore.yml --extra-vars "pr_number=100"` replacing 100 with the PR number you are trying to test. To test the master branch, run `ansible-playbook test-backup-restore.yml --extra-vars "use_master_branch=true"`. Either command should be run from the projects root directory.
