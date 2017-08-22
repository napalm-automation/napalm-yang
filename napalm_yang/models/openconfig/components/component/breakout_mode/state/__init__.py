
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
  import builtins as __builtin__
  long = int
  unicode = str
elif six.PY2:
  import __builtin__

class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-platform - based on the path /components/component/breakout-mode/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for port breakout
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__num_channels','__channel_speed',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__channel_speed = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'SPEED_100GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_10GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_100GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_25GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_UNKNOWN': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_1GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_1GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_10GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_25GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_10MB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_40GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_40GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_UNKNOWN': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_100MB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_50GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_50GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_10MB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_100MB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}},), is_leaf=True, yang_name="channel-speed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/port', defining_module='openconfig-platform-port', yang_type='identityref', is_config=False)
    self.__num_channels = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="num-channels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/port', defining_module='openconfig-platform-port', yang_type='uint8', is_config=False)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'components', u'component', u'breakout-mode', u'state']

  def _get_num_channels(self):
    """
    Getter method for num_channels, mapped from YANG variable /components/component/breakout_mode/state/num_channels (uint8)

    YANG Description: Sets the number of channels to 'breakout' on a port
capable of channelization
    """
    return self.__num_channels
      
  def _set_num_channels(self, v, load=False):
    """
    Setter method for num_channels, mapped from YANG variable /components/component/breakout_mode/state/num_channels (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_num_channels is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_num_channels() directly.

    YANG Description: Sets the number of channels to 'breakout' on a port
capable of channelization
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="num-channels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/port', defining_module='openconfig-platform-port', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """num_channels must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="num-channels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/port', defining_module='openconfig-platform-port', yang_type='uint8', is_config=False)""",
        })

    self.__num_channels = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_num_channels(self):
    self.__num_channels = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="num-channels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/port', defining_module='openconfig-platform-port', yang_type='uint8', is_config=False)


  def _get_channel_speed(self):
    """
    Getter method for channel_speed, mapped from YANG variable /components/component/breakout_mode/state/channel_speed (identityref)

    YANG Description: Sets the channel speed on each channel -- the
supported values are defined by the
ETHERNET_SPEED identity
    """
    return self.__channel_speed
      
  def _set_channel_speed(self, v, load=False):
    """
    Setter method for channel_speed, mapped from YANG variable /components/component/breakout_mode/state/channel_speed (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_channel_speed is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_channel_speed() directly.

    YANG Description: Sets the channel speed on each channel -- the
supported values are defined by the
ETHERNET_SPEED identity
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'SPEED_100GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_10GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_100GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_25GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_UNKNOWN': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_1GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_1GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_10GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_25GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_10MB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_40GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_40GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_UNKNOWN': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_100MB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_50GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_50GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_10MB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_100MB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}},), is_leaf=True, yang_name="channel-speed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/port', defining_module='openconfig-platform-port', yang_type='identityref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """channel_speed must be of a type compatible with identityref""",
          'defined-type': "openconfig-platform-port:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'SPEED_100GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_10GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_100GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_25GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_UNKNOWN': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_1GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_1GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_10GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_25GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_10MB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_40GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_40GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_UNKNOWN': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_100MB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_50GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_50GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_10MB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_100MB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}},), is_leaf=True, yang_name="channel-speed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/port', defining_module='openconfig-platform-port', yang_type='identityref', is_config=False)""",
        })

    self.__channel_speed = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_channel_speed(self):
    self.__channel_speed = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'SPEED_100GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_10GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_100GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_25GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_UNKNOWN': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_1GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_1GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_10GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_25GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_10MB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_40GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_40GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_UNKNOWN': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_100MB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_50GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_50GB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'oc-eth:SPEED_10MB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}, u'SPEED_100MB': {'@namespace': u'http://openconfig.net/yang/interfaces/ethernet', '@module': u'openconfig-if-ethernet'}},), is_leaf=True, yang_name="channel-speed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/port', defining_module='openconfig-platform-port', yang_type='identityref', is_config=False)

  num_channels = __builtin__.property(_get_num_channels)
  channel_speed = __builtin__.property(_get_channel_speed)


  _pyangbind_elements = {'num_channels': num_channels, 'channel_speed': channel_speed, }


