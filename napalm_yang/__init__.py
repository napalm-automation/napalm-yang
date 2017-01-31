# pylama:skip=1
from napalm_yang.yang_base import *
from napalm_yang.yang_builtin_types import *

from napalm_yang.models.ietf import ietf_yang as yang
from napalm_yang.models.ietf import ietf_if
if_ = ietf_if
from napalm_yang.models.ietf import ietf_ianaift as ianaift
from napalm_yang.models.ietf import ietf_inet as inet

from napalm_yang.models.openconfig_extensions import ocext as oc_ext

from napalm_yang.models.interfaces import oc_if


from napalm_yang.models.acl import oc_pkt_match_types
from napalm_yang.models.acl import oc_pkt_match as oc_match
from napalm_yang.models.acl import oc_acl
