
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import state
import default_metric
import delay_metric
import expense_metric
import error_metric
class prefixes(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/ipv4-external-reachability/prefixes/prefixes. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: IPv4 external prefixes and reachability attributes.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__state','__default_metric','__delay_metric','__expense_metric','__error_metric',)

  _yang_name = 'prefixes'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__default_metric = YANGDynClass(base=default_metric.default_metric, is_container='container', yang_name="default-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__delay_metric = YANGDynClass(base=delay_metric.delay_metric, is_container='container', yang_name="delay-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__error_metric = YANGDynClass(base=error_metric.error_metric, is_container='container', yang_name="error-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__expense_metric = YANGDynClass(base=expense_metric.expense_metric, is_container='container', yang_name="expense-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'levels', u'level', u'link-state-database', u'lsp', u'tlvs', u'tlv', u'ipv4-external-reachability', u'prefixes', u'prefixes']

  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_external_reachability/prefixes/prefixes/state (container)

    YANG Description: State parameters of IPv4 standard prefix.
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_external_reachability/prefixes/prefixes/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State parameters of IPv4 standard prefix.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_default_metric(self):
    """
    Getter method for default_metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_external_reachability/prefixes/prefixes/default_metric (container)

    YANG Description: This container defines ISIS Default Metric.
    """
    return self.__default_metric
      
  def _set_default_metric(self, v, load=False):
    """
    Setter method for default_metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_external_reachability/prefixes/prefixes/default_metric (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_default_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_default_metric() directly.

    YANG Description: This container defines ISIS Default Metric.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=default_metric.default_metric, is_container='container', yang_name="default-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """default_metric must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=default_metric.default_metric, is_container='container', yang_name="default-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__default_metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_default_metric(self):
    self.__default_metric = YANGDynClass(base=default_metric.default_metric, is_container='container', yang_name="default-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_delay_metric(self):
    """
    Getter method for delay_metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_external_reachability/prefixes/prefixes/delay_metric (container)

    YANG Description: This container defines the ISIS delay metric.
    """
    return self.__delay_metric
      
  def _set_delay_metric(self, v, load=False):
    """
    Setter method for delay_metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_external_reachability/prefixes/prefixes/delay_metric (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_delay_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_delay_metric() directly.

    YANG Description: This container defines the ISIS delay metric.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=delay_metric.delay_metric, is_container='container', yang_name="delay-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """delay_metric must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=delay_metric.delay_metric, is_container='container', yang_name="delay-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__delay_metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_delay_metric(self):
    self.__delay_metric = YANGDynClass(base=delay_metric.delay_metric, is_container='container', yang_name="delay-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_expense_metric(self):
    """
    Getter method for expense_metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_external_reachability/prefixes/prefixes/expense_metric (container)

    YANG Description: This container defines the ISIS expense metric.
    """
    return self.__expense_metric
      
  def _set_expense_metric(self, v, load=False):
    """
    Setter method for expense_metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_external_reachability/prefixes/prefixes/expense_metric (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_expense_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_expense_metric() directly.

    YANG Description: This container defines the ISIS expense metric.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=expense_metric.expense_metric, is_container='container', yang_name="expense-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """expense_metric must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=expense_metric.expense_metric, is_container='container', yang_name="expense-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__expense_metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_expense_metric(self):
    self.__expense_metric = YANGDynClass(base=expense_metric.expense_metric, is_container='container', yang_name="expense-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_error_metric(self):
    """
    Getter method for error_metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_external_reachability/prefixes/prefixes/error_metric (container)

    YANG Description: This container defines the ISIS error metric.
    """
    return self.__error_metric
      
  def _set_error_metric(self, v, load=False):
    """
    Setter method for error_metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_external_reachability/prefixes/prefixes/error_metric (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_error_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_error_metric() directly.

    YANG Description: This container defines the ISIS error metric.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=error_metric.error_metric, is_container='container', yang_name="error-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """error_metric must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=error_metric.error_metric, is_container='container', yang_name="error-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__error_metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_error_metric(self):
    self.__error_metric = YANGDynClass(base=error_metric.error_metric, is_container='container', yang_name="error-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  state = __builtin__.property(_get_state)
  default_metric = __builtin__.property(_get_default_metric)
  delay_metric = __builtin__.property(_get_delay_metric)
  expense_metric = __builtin__.property(_get_expense_metric)
  error_metric = __builtin__.property(_get_error_metric)


  _pyangbind_elements = {'state': state, 'default_metric': default_metric, 'delay_metric': delay_metric, 'expense_metric': expense_metric, 'error_metric': error_metric, }


import state
import default_metric
import delay_metric
import expense_metric
import error_metric
class prefixes(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/ipv4-external-reachability/prefixes/prefixes. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: IPv4 external prefixes and reachability attributes.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__state','__default_metric','__delay_metric','__expense_metric','__error_metric',)

  _yang_name = 'prefixes'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__default_metric = YANGDynClass(base=default_metric.default_metric, is_container='container', yang_name="default-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__delay_metric = YANGDynClass(base=delay_metric.delay_metric, is_container='container', yang_name="delay-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__error_metric = YANGDynClass(base=error_metric.error_metric, is_container='container', yang_name="error-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__expense_metric = YANGDynClass(base=expense_metric.expense_metric, is_container='container', yang_name="expense-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'levels', u'level', u'link-state-database', u'lsp', u'tlvs', u'tlv', u'ipv4-external-reachability', u'prefixes', u'prefixes']

  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_external_reachability/prefixes/prefixes/state (container)

    YANG Description: State parameters of IPv4 standard prefix.
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_external_reachability/prefixes/prefixes/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State parameters of IPv4 standard prefix.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_default_metric(self):
    """
    Getter method for default_metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_external_reachability/prefixes/prefixes/default_metric (container)

    YANG Description: This container defines ISIS Default Metric.
    """
    return self.__default_metric
      
  def _set_default_metric(self, v, load=False):
    """
    Setter method for default_metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_external_reachability/prefixes/prefixes/default_metric (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_default_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_default_metric() directly.

    YANG Description: This container defines ISIS Default Metric.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=default_metric.default_metric, is_container='container', yang_name="default-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """default_metric must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=default_metric.default_metric, is_container='container', yang_name="default-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__default_metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_default_metric(self):
    self.__default_metric = YANGDynClass(base=default_metric.default_metric, is_container='container', yang_name="default-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_delay_metric(self):
    """
    Getter method for delay_metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_external_reachability/prefixes/prefixes/delay_metric (container)

    YANG Description: This container defines the ISIS delay metric.
    """
    return self.__delay_metric
      
  def _set_delay_metric(self, v, load=False):
    """
    Setter method for delay_metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_external_reachability/prefixes/prefixes/delay_metric (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_delay_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_delay_metric() directly.

    YANG Description: This container defines the ISIS delay metric.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=delay_metric.delay_metric, is_container='container', yang_name="delay-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """delay_metric must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=delay_metric.delay_metric, is_container='container', yang_name="delay-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__delay_metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_delay_metric(self):
    self.__delay_metric = YANGDynClass(base=delay_metric.delay_metric, is_container='container', yang_name="delay-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_expense_metric(self):
    """
    Getter method for expense_metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_external_reachability/prefixes/prefixes/expense_metric (container)

    YANG Description: This container defines the ISIS expense metric.
    """
    return self.__expense_metric
      
  def _set_expense_metric(self, v, load=False):
    """
    Setter method for expense_metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_external_reachability/prefixes/prefixes/expense_metric (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_expense_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_expense_metric() directly.

    YANG Description: This container defines the ISIS expense metric.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=expense_metric.expense_metric, is_container='container', yang_name="expense-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """expense_metric must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=expense_metric.expense_metric, is_container='container', yang_name="expense-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__expense_metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_expense_metric(self):
    self.__expense_metric = YANGDynClass(base=expense_metric.expense_metric, is_container='container', yang_name="expense-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_error_metric(self):
    """
    Getter method for error_metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_external_reachability/prefixes/prefixes/error_metric (container)

    YANG Description: This container defines the ISIS error metric.
    """
    return self.__error_metric
      
  def _set_error_metric(self, v, load=False):
    """
    Setter method for error_metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_external_reachability/prefixes/prefixes/error_metric (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_error_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_error_metric() directly.

    YANG Description: This container defines the ISIS error metric.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=error_metric.error_metric, is_container='container', yang_name="error-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """error_metric must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=error_metric.error_metric, is_container='container', yang_name="error-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__error_metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_error_metric(self):
    self.__error_metric = YANGDynClass(base=error_metric.error_metric, is_container='container', yang_name="error-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  state = __builtin__.property(_get_state)
  default_metric = __builtin__.property(_get_default_metric)
  delay_metric = __builtin__.property(_get_delay_metric)
  expense_metric = __builtin__.property(_get_expense_metric)
  error_metric = __builtin__.property(_get_error_metric)


  _pyangbind_elements = {'state': state, 'default_metric': default_metric, 'delay_metric': delay_metric, 'expense_metric': expense_metric, 'error_metric': error_metric, }


