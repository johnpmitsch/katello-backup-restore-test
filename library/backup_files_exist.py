#!/usr/bin/python

from ansible.module_utils.basic import *
import os.path

def clean_up_input(f, directory):
    f = f.rstrip()
    directory = directory.rstrip()
    if not directory.endswith("/"):
        directory = directory + "/"
    return f, directory

def files_in_dir(data):
    good_files = data["good_files"]
    bad_files = data["bad_files"]
    directory = data["directory"]
    
    for f in good_files:
        f, directory = clean_up_input(f, directory)
        if not os.path.exists(directory + f):
            return False, {"status": "{0} is not found in {1}".format(f, directory)}

    for f in bad_files:
        f, directory = clean_up_input(f, directory)
        if os.path.exists(directory + f):
            return False, {"status": "{0} is found in {1} and shouldn't be there!".format(f, directory)}

    return True, {"status": "all files found!"}
    

def main():
    fields = {
        "good_files": {"required": True, "type": "list" },
        "bad_files": {"required": True, "type": "list" },
        "directory": {"required": True, "type": "str"},
    }

    module = AnsibleModule(argument_spec=fields)
    success, msg = files_in_dir(module.params)
    if success:
        module.exit_json(changed=False, meta=msg)
    else:
        module.fail_json(msg=msg)


if __name__ == '__main__':  
    main()
