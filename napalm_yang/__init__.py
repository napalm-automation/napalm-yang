# pylama:skip=1
from napalm_yang.yang_base import *
from napalm_yang.yang_builtin_types import *

from napalm_yang.models.ietf import ietf_yang as yang
from napalm_yang.models.ietf import ietf_if
if_ = ietf_if
from napalm_yang.models.ietf import ietf_ianaift as ianaift
ift = ianaift
from napalm_yang.models.ietf import ietf_inet as inet

from napalm_yang.models.openconfig_extensions import ocext as oc_ext
from napalm_yang.models.openconfig_types import oc_types

from napalm_yang.models.interfaces import oc_if
from napalm_yang.models.interfaces import oc_eth
from napalm_yang.models.interfaces import oc_lag

from napalm_yang.models.policy import oc_pol_types
from napalm_yang.models.policy import oc_rpol

from napalm_yang.models.bgp import oc_bgp_types
from napalm_yang.models.bgp import oc_bgp

from napalm_yang.models.vlan import oc_vlan_types
from napalm_yang.models.vlan import oc_vlan

from napalm_yang.models.interfaces import oc_ip


from napalm_yang.models.acl import oc_pkt_match_types
from napalm_yang.models.acl import oc_pkt_match as oc_match
from napalm_yang.models.acl import oc_acl

from napalm_yang.models.platform import oc_platform_types
from napalm_yang.models.platform import oc_platform

from napalm_yang.models.interfaces import napalm_ip
