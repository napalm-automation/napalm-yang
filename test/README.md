# Writing Integration Tests #

## Testing Profiles ##
The script `test_profiles.py` handles the testing of parsing the config/state from mocked data
files and converting it to openconfig models. The script will also test translating openconfig 
models into the native configuration for a device, as well as test merging openconfig models.

All the tests for each profile are organized into directories for that profiles name under the
directory `test/integration/test_profiles`. The directory structure looks like the following 
```
eos
├── openconfig-interfaces
│   ├── config
│   │   ├── default
│   │   │   ├── candidate.json
│   │   │   ├── expected.json
│   │   │   ├── merge.txt
│   │   │   ├── mocked
│   │   │   │   └── cli.1.show_running_config_all.0
│   │   │   ├── replace.txt
│   │   │   └── translation.txt
│   │   └── l2_ports
│   │       ├── candidate.json
│   │       ├── expected.json
│   │       ├── merge.txt
│   │       ├── mocked
│   │       │   └── cli.1.show_running_config_all.0
│   │       ├── replace.txt
│   │       └── translation.txt
│   └── state
│       └── default
│           ├── expected.json
│           └── mocked
│               └── cli.1.show_interfaces.0
```
Where there is a high level directory for the profile, `eos` in this case.  Then a directories to 
show which openconfig model and mode is being tested, `openconfig-interfaces/config` and 
`openconfig-interfaces/state` here.  Then a break down of cases to test, `default` and `l2_ports`.

Under the config test case directory we the following
* mocked/... - this directory contains the mocked data
* expected.json - this json file is jsonified version of how the mocked data should be translated 
into the openconfig model
* translation.txt -  the native configuration code 
* candidate.json - a jsonified version of a new openconfig model to be added to the current config
* merge.txt - result native config after merging the candidate oc model with the "running config"
* replace.txt - result native config after replace the candidate oc model with the "running config"
 

