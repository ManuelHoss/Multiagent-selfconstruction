# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _GraphDS.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_GraphDS', [dirname(__file__)])
        except ImportError:
            import _GraphDS
            return _GraphDS
        if fp is not None:
            try:
                _mod = imp.load_module('_GraphDS', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _GraphDS = swig_import_helper()
    del swig_import_helper
else:
    import _GraphDS
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



def _swig_setattr_nondynamic_method(set):
    def set_attr(self, name, value):
        if (name == "thisown"):
            return self.this.own(value)
        if hasattr(self, name) or (name == "this"):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


class SwigPyIterator(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _GraphDS.delete_SwigPyIterator
    def __iter__(self):
        return self
SwigPyIterator.value = new_instancemethod(_GraphDS.SwigPyIterator_value, None, SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_GraphDS.SwigPyIterator_incr, None, SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_GraphDS.SwigPyIterator_decr, None, SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_GraphDS.SwigPyIterator_distance, None, SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_GraphDS.SwigPyIterator_equal, None, SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_GraphDS.SwigPyIterator_copy, None, SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_GraphDS.SwigPyIterator_next, None, SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_GraphDS.SwigPyIterator___next__, None, SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_GraphDS.SwigPyIterator_previous, None, SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_GraphDS.SwigPyIterator_advance, None, SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_GraphDS.SwigPyIterator___eq__, None, SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_GraphDS.SwigPyIterator___ne__, None, SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_GraphDS.SwigPyIterator___iadd__, None, SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_GraphDS.SwigPyIterator___isub__, None, SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_GraphDS.SwigPyIterator___add__, None, SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_GraphDS.SwigPyIterator___sub__, None, SwigPyIterator)
SwigPyIterator_swigregister = _GraphDS.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

import OCC.TCollection
import OCC.Standard
import OCC.MMgt

_GraphDS.GraphDS_OnlyInput_swigconstant(_GraphDS)
GraphDS_OnlyInput = _GraphDS.GraphDS_OnlyInput

_GraphDS.GraphDS_OnlyOutput_swigconstant(_GraphDS)
GraphDS_OnlyOutput = _GraphDS.GraphDS_OnlyOutput

_GraphDS.GraphDS_InputAndOutput_swigconstant(_GraphDS)
GraphDS_InputAndOutput = _GraphDS.GraphDS_InputAndOutput

_GraphDS.GraphDS_OnlyFront_swigconstant(_GraphDS)
GraphDS_OnlyFront = _GraphDS.GraphDS_OnlyFront

_GraphDS.GraphDS_OnlyBack_swigconstant(_GraphDS)
GraphDS_OnlyBack = _GraphDS.GraphDS_OnlyBack

_GraphDS.GraphDS_FrontAndBack_swigconstant(_GraphDS)
GraphDS_FrontAndBack = _GraphDS.GraphDS_FrontAndBack
class GraphDS_DataMapIteratorOfEntityRoleMap(OCC.TCollection.TCollection_BasicMapIterator):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        :rtype: None

        :param aMap:
        :type aMap: GraphDS_EntityRoleMap &
        :rtype: None

        """
        _GraphDS.GraphDS_DataMapIteratorOfEntityRoleMap_swiginit(self, _GraphDS.new_GraphDS_DataMapIteratorOfEntityRoleMap(*args))

    def Initialize(self, *args):
        """
        :param aMap:
        :type aMap: GraphDS_EntityRoleMap &
        :rtype: None

        """
        return _GraphDS.GraphDS_DataMapIteratorOfEntityRoleMap_Initialize(self, *args)


    def Key(self, *args):
        """
        :rtype: Handle_Standard_Transient

        """
        return _GraphDS.GraphDS_DataMapIteratorOfEntityRoleMap_Key(self, *args)


    def Value(self, *args):
        """
        :rtype: GraphDS_EntityRole

        """
        return _GraphDS.GraphDS_DataMapIteratorOfEntityRoleMap_Value(self, *args)


    def __del__(self):
    	try:
    		self.thisown = False
    		GarbageCollector.garbage.collect_object(self)
    	except:
    		pass


GraphDS_DataMapIteratorOfEntityRoleMap.Initialize = new_instancemethod(_GraphDS.GraphDS_DataMapIteratorOfEntityRoleMap_Initialize, None, GraphDS_DataMapIteratorOfEntityRoleMap)
GraphDS_DataMapIteratorOfEntityRoleMap.Key = new_instancemethod(_GraphDS.GraphDS_DataMapIteratorOfEntityRoleMap_Key, None, GraphDS_DataMapIteratorOfEntityRoleMap)
GraphDS_DataMapIteratorOfEntityRoleMap.Value = new_instancemethod(_GraphDS.GraphDS_DataMapIteratorOfEntityRoleMap_Value, None, GraphDS_DataMapIteratorOfEntityRoleMap)
GraphDS_DataMapIteratorOfEntityRoleMap._kill_pointed = new_instancemethod(_GraphDS.GraphDS_DataMapIteratorOfEntityRoleMap__kill_pointed, None, GraphDS_DataMapIteratorOfEntityRoleMap)
GraphDS_DataMapIteratorOfEntityRoleMap_swigregister = _GraphDS.GraphDS_DataMapIteratorOfEntityRoleMap_swigregister
GraphDS_DataMapIteratorOfEntityRoleMap_swigregister(GraphDS_DataMapIteratorOfEntityRoleMap)

class GraphDS_DataMapNodeOfEntityRoleMap(OCC.TCollection.TCollection_MapNode):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        :param K:
        :type K: Handle_Standard_Transient &
        :param I:
        :type I: GraphDS_EntityRole &
        :param n:
        :type n: TCollection_MapNodePtr &
        :rtype: None

        """
        _GraphDS.GraphDS_DataMapNodeOfEntityRoleMap_swiginit(self, _GraphDS.new_GraphDS_DataMapNodeOfEntityRoleMap(*args))

    def Key(self, *args):
        """
        :rtype: Handle_Standard_Transient

        """
        return _GraphDS.GraphDS_DataMapNodeOfEntityRoleMap_Key(self, *args)


    def Value(self, *args):
        """
        :rtype: GraphDS_EntityRole

        """
        return _GraphDS.GraphDS_DataMapNodeOfEntityRoleMap_Value(self, *args)


    def _kill_pointed(self):
        """_kill_pointed(GraphDS_DataMapNodeOfEntityRoleMap self)"""
        return _GraphDS.GraphDS_DataMapNodeOfEntityRoleMap__kill_pointed(self)


    def GetHandle(self):
        """GetHandle(GraphDS_DataMapNodeOfEntityRoleMap self) -> Handle_GraphDS_DataMapNodeOfEntityRoleMap"""
        return _GraphDS.GraphDS_DataMapNodeOfEntityRoleMap_GetHandle(self)


    def __del__(self):
    	try:
    		self.thisown = False
    		GarbageCollector.garbage.collect_object(self)
    	except:
    		pass


GraphDS_DataMapNodeOfEntityRoleMap.Key = new_instancemethod(_GraphDS.GraphDS_DataMapNodeOfEntityRoleMap_Key, None, GraphDS_DataMapNodeOfEntityRoleMap)
GraphDS_DataMapNodeOfEntityRoleMap.Value = new_instancemethod(_GraphDS.GraphDS_DataMapNodeOfEntityRoleMap_Value, None, GraphDS_DataMapNodeOfEntityRoleMap)
GraphDS_DataMapNodeOfEntityRoleMap._kill_pointed = new_instancemethod(_GraphDS.GraphDS_DataMapNodeOfEntityRoleMap__kill_pointed, None, GraphDS_DataMapNodeOfEntityRoleMap)
GraphDS_DataMapNodeOfEntityRoleMap.GetHandle = new_instancemethod(_GraphDS.GraphDS_DataMapNodeOfEntityRoleMap_GetHandle, None, GraphDS_DataMapNodeOfEntityRoleMap)
GraphDS_DataMapNodeOfEntityRoleMap_swigregister = _GraphDS.GraphDS_DataMapNodeOfEntityRoleMap_swigregister
GraphDS_DataMapNodeOfEntityRoleMap_swigregister(GraphDS_DataMapNodeOfEntityRoleMap)

class Handle_GraphDS_DataMapNodeOfEntityRoleMap(OCC.TCollection.Handle_TCollection_MapNode):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _GraphDS.Handle_GraphDS_DataMapNodeOfEntityRoleMap_swiginit(self, _GraphDS.new_Handle_GraphDS_DataMapNodeOfEntityRoleMap(*args))
    DownCast = staticmethod(_GraphDS.Handle_GraphDS_DataMapNodeOfEntityRoleMap_DownCast)

    def __del__(self):
        try:
            self.thisown = False
            GarbageCollector.garbage.collect_object(self)
        except:
            pass


Handle_GraphDS_DataMapNodeOfEntityRoleMap.Nullify = new_instancemethod(_GraphDS.Handle_GraphDS_DataMapNodeOfEntityRoleMap_Nullify, None, Handle_GraphDS_DataMapNodeOfEntityRoleMap)
Handle_GraphDS_DataMapNodeOfEntityRoleMap.IsNull = new_instancemethod(_GraphDS.Handle_GraphDS_DataMapNodeOfEntityRoleMap_IsNull, None, Handle_GraphDS_DataMapNodeOfEntityRoleMap)
Handle_GraphDS_DataMapNodeOfEntityRoleMap.GetObject = new_instancemethod(_GraphDS.Handle_GraphDS_DataMapNodeOfEntityRoleMap_GetObject, None, Handle_GraphDS_DataMapNodeOfEntityRoleMap)
Handle_GraphDS_DataMapNodeOfEntityRoleMap._kill_pointed = new_instancemethod(_GraphDS.Handle_GraphDS_DataMapNodeOfEntityRoleMap__kill_pointed, None, Handle_GraphDS_DataMapNodeOfEntityRoleMap)
Handle_GraphDS_DataMapNodeOfEntityRoleMap_swigregister = _GraphDS.Handle_GraphDS_DataMapNodeOfEntityRoleMap_swigregister
Handle_GraphDS_DataMapNodeOfEntityRoleMap_swigregister(Handle_GraphDS_DataMapNodeOfEntityRoleMap)

def Handle_GraphDS_DataMapNodeOfEntityRoleMap_DownCast(AnObject):
    return _GraphDS.Handle_GraphDS_DataMapNodeOfEntityRoleMap_DownCast(AnObject)
Handle_GraphDS_DataMapNodeOfEntityRoleMap_DownCast = _GraphDS.Handle_GraphDS_DataMapNodeOfEntityRoleMap_DownCast

class GraphDS_EntityRoleMap(OCC.TCollection.TCollection_BasicMap):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        :param NbBuckets: default value is 1
        :type NbBuckets: int
        :rtype: None

        """
        _GraphDS.GraphDS_EntityRoleMap_swiginit(self, _GraphDS.new_GraphDS_EntityRoleMap(*args))

    def Assign(self, *args):
        """
        :param Other:
        :type Other: GraphDS_EntityRoleMap &
        :rtype: GraphDS_EntityRoleMap

        """
        return _GraphDS.GraphDS_EntityRoleMap_Assign(self, *args)


    def Set(self, *args):
        """
        :param Other:
        :type Other: GraphDS_EntityRoleMap &
        :rtype: GraphDS_EntityRoleMap

        """
        return _GraphDS.GraphDS_EntityRoleMap_Set(self, *args)


    def ReSize(self, *args):
        """
        :param NbBuckets:
        :type NbBuckets: int
        :rtype: None

        """
        return _GraphDS.GraphDS_EntityRoleMap_ReSize(self, *args)


    def Clear(self, *args):
        """
        :rtype: None

        """
        return _GraphDS.GraphDS_EntityRoleMap_Clear(self, *args)


    def Bind(self, *args):
        """
        :param K:
        :type K: Handle_Standard_Transient &
        :param I:
        :type I: GraphDS_EntityRole &
        :rtype: bool

        """
        return _GraphDS.GraphDS_EntityRoleMap_Bind(self, *args)


    def IsBound(self, *args):
        """
        :param K:
        :type K: Handle_Standard_Transient &
        :rtype: bool

        """
        return _GraphDS.GraphDS_EntityRoleMap_IsBound(self, *args)


    def UnBind(self, *args):
        """
        :param K:
        :type K: Handle_Standard_Transient &
        :rtype: bool

        """
        return _GraphDS.GraphDS_EntityRoleMap_UnBind(self, *args)


    def Find(self, *args):
        """
        :param K:
        :type K: Handle_Standard_Transient &
        :rtype: GraphDS_EntityRole

        """
        return _GraphDS.GraphDS_EntityRoleMap_Find(self, *args)


    def ChangeFind(self, *args):
        """
        :param K:
        :type K: Handle_Standard_Transient &
        :rtype: GraphDS_EntityRole

        """
        return _GraphDS.GraphDS_EntityRoleMap_ChangeFind(self, *args)


    def Find1(self, *args):
        """
        :param K:
        :type K: Handle_Standard_Transient &
        :rtype: Standard_Address

        """
        return _GraphDS.GraphDS_EntityRoleMap_Find1(self, *args)


    def ChangeFind1(self, *args):
        """
        :param K:
        :type K: Handle_Standard_Transient &
        :rtype: Standard_Address

        """
        return _GraphDS.GraphDS_EntityRoleMap_ChangeFind1(self, *args)


    def _kill_pointed(self):
        """_kill_pointed(GraphDS_EntityRoleMap self)"""
        return _GraphDS.GraphDS_EntityRoleMap__kill_pointed(self)


    def __del__(self):
    	try:
    		self.thisown = False
    		GarbageCollector.garbage.collect_object(self)
    	except:
    		pass


GraphDS_EntityRoleMap.Assign = new_instancemethod(_GraphDS.GraphDS_EntityRoleMap_Assign, None, GraphDS_EntityRoleMap)
GraphDS_EntityRoleMap.Set = new_instancemethod(_GraphDS.GraphDS_EntityRoleMap_Set, None, GraphDS_EntityRoleMap)
GraphDS_EntityRoleMap.ReSize = new_instancemethod(_GraphDS.GraphDS_EntityRoleMap_ReSize, None, GraphDS_EntityRoleMap)
GraphDS_EntityRoleMap.Clear = new_instancemethod(_GraphDS.GraphDS_EntityRoleMap_Clear, None, GraphDS_EntityRoleMap)
GraphDS_EntityRoleMap.Bind = new_instancemethod(_GraphDS.GraphDS_EntityRoleMap_Bind, None, GraphDS_EntityRoleMap)
GraphDS_EntityRoleMap.IsBound = new_instancemethod(_GraphDS.GraphDS_EntityRoleMap_IsBound, None, GraphDS_EntityRoleMap)
GraphDS_EntityRoleMap.UnBind = new_instancemethod(_GraphDS.GraphDS_EntityRoleMap_UnBind, None, GraphDS_EntityRoleMap)
GraphDS_EntityRoleMap.Find = new_instancemethod(_GraphDS.GraphDS_EntityRoleMap_Find, None, GraphDS_EntityRoleMap)
GraphDS_EntityRoleMap.ChangeFind = new_instancemethod(_GraphDS.GraphDS_EntityRoleMap_ChangeFind, None, GraphDS_EntityRoleMap)
GraphDS_EntityRoleMap.Find1 = new_instancemethod(_GraphDS.GraphDS_EntityRoleMap_Find1, None, GraphDS_EntityRoleMap)
GraphDS_EntityRoleMap.ChangeFind1 = new_instancemethod(_GraphDS.GraphDS_EntityRoleMap_ChangeFind1, None, GraphDS_EntityRoleMap)
GraphDS_EntityRoleMap._kill_pointed = new_instancemethod(_GraphDS.GraphDS_EntityRoleMap__kill_pointed, None, GraphDS_EntityRoleMap)
GraphDS_EntityRoleMap_swigregister = _GraphDS.GraphDS_EntityRoleMap_swigregister
GraphDS_EntityRoleMap_swigregister(GraphDS_EntityRoleMap)



