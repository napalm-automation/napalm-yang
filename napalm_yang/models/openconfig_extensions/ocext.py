"""
This module provides extensions to the YANG language to allow
OpenConfig specific functionality and meta-data to be defined.
"""
from builtins import super
import weakref

from napalm_yang import *


class LocalNamespace(object):
    def __getattr__(self, name):
        import sys
        return globals()[name]

ocext = LocalNamespace()



# Imports

# openconfig-extensions



__namespace__ = "http://openconfig.net/yang/openconfig-ext"
__yang_version__ = "1"
__prefix__ = "ocext"
__contact__ = "OpenConfig working group\nwww.openconfig.net"
__organization__ = "OpenConfig working group"
__revision__ = {
    "2015-10-05": {
        "revision": "2015-10-05"
    }, 
    "2015-10-09": {
        "revision": "2015-10-09"
    }
}



# extensions
class OpenconfigVersion(Extension):
    """
     The OpenConfig version number for the module. This is
    expressed as a semantic version number of the form:
     x.y.z
    where:
     * x corresponds to the major version,
     * y corresponds to a minor version,
     * z corresponds to a patch version.
    This version corresponds to the model file within which it is
    defined, and does not cover the whole set of OpenConfig models.
    Where several modules are used to build up a single block of
    functionality, the same module version is specified across each
    file that makes up the module.

    A major version number of 0 indicates that this model is still
    in development (whether within OpenConfig or with industry
    partners), and is potentially subject to change.

    Following a release of major version 1, all modules will
    increment major revision number where backwards incompatible
    changes to the model are made.

    The minor version is changed when features are added to the
    model that do not impact current clients use of the model.

    The patch-level version is incremented when non-feature changes
    (such as bugfixes or clarifications to human-readable
    descriptions that do not impact model functionality) are made
    that maintain backwards compatibility.

    The version number is stored in the module meta-data.
    """
    yang_prefix = __prefix__

    def __init__(self, semver, ):
    
        self.semver = "semver"
        self._yin_element_semver = False
    

# features


# typedef


# Identities

# Classes to support containers and lists


# Top-uses

# Top-containers


# augments