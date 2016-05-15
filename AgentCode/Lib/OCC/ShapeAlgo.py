# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _ShapeAlgo.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ShapeAlgo', [dirname(__file__)])
        except ImportError:
            import _ShapeAlgo
            return _ShapeAlgo
        if fp is not None:
            try:
                _mod = imp.load_module('_ShapeAlgo', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ShapeAlgo = swig_import_helper()
    del swig_import_helper
else:
    import _ShapeAlgo
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
    __swig_destroy__ = _ShapeAlgo.delete_SwigPyIterator
    def __iter__(self):
        return self
SwigPyIterator.value = new_instancemethod(_ShapeAlgo.SwigPyIterator_value, None, SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_ShapeAlgo.SwigPyIterator_incr, None, SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_ShapeAlgo.SwigPyIterator_decr, None, SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_ShapeAlgo.SwigPyIterator_distance, None, SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_ShapeAlgo.SwigPyIterator_equal, None, SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_ShapeAlgo.SwigPyIterator_copy, None, SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_ShapeAlgo.SwigPyIterator_next, None, SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_ShapeAlgo.SwigPyIterator___next__, None, SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_ShapeAlgo.SwigPyIterator_previous, None, SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_ShapeAlgo.SwigPyIterator_advance, None, SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_ShapeAlgo.SwigPyIterator___eq__, None, SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_ShapeAlgo.SwigPyIterator___ne__, None, SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_ShapeAlgo.SwigPyIterator___iadd__, None, SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_ShapeAlgo.SwigPyIterator___isub__, None, SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_ShapeAlgo.SwigPyIterator___add__, None, SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_ShapeAlgo.SwigPyIterator___sub__, None, SwigPyIterator)
SwigPyIterator_swigregister = _ShapeAlgo.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

import OCC.MMgt
import OCC.Standard
import OCC.ShapeFix
import OCC.TopoDS
import OCC.TCollection
import OCC.TopLoc
import OCC.gp
import OCC.TopAbs
import OCC.Message
import OCC.TColStd
import OCC.ShapeBuild
import OCC.Geom
import OCC.GeomAbs
import OCC.TColgp
import OCC.Geom2d
import OCC.BRepTools
import OCC.Bnd
import OCC.TopTools
import OCC.BRep
import OCC.Poly
import OCC.NCollection
import OCC.TShort
import OCC.ShapeExtend
import OCC.TColGeom
import OCC.ShapeConstruct
import OCC.BRepBuilderAPI
import OCC.ShapeAnalysis
import OCC.Adaptor3d
import OCC.Adaptor2d
import OCC.math
import OCC.GeomAdaptor
import OCC.IntRes2d
class shapealgo(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def Init(*args):
        """
        * Provides initerface to the algorithms from Shape Healing. Creates and initializes default AlgoContainer.

        :rtype: void

        """
        return _ShapeAlgo.shapealgo_Init(*args)

    Init = staticmethod(Init)

    def SetAlgoContainer(*args):
        """
        * Sets default AlgoContainer

        :param aContainer:
        :type aContainer: Handle_ShapeAlgo_AlgoContainer &
        :rtype: void

        """
        return _ShapeAlgo.shapealgo_SetAlgoContainer(*args)

    SetAlgoContainer = staticmethod(SetAlgoContainer)

    def AlgoContainer(*args):
        """
        * Returns default AlgoContainer

        :rtype: Handle_ShapeAlgo_AlgoContainer

        """
        return _ShapeAlgo.shapealgo_AlgoContainer(*args)

    AlgoContainer = staticmethod(AlgoContainer)

    def __init__(self):
        _ShapeAlgo.shapealgo_swiginit(self, _ShapeAlgo.new_shapealgo())

    def __del__(self):
    	try:
    		self.thisown = False
    		GarbageCollector.garbage.collect_object(self)
    	except:
    		pass


shapealgo._kill_pointed = new_instancemethod(_ShapeAlgo.shapealgo__kill_pointed, None, shapealgo)
shapealgo_swigregister = _ShapeAlgo.shapealgo_swigregister
shapealgo_swigregister(shapealgo)

def shapealgo_Init(*args):
    """
    * Provides initerface to the algorithms from Shape Healing. Creates and initializes default AlgoContainer.

    :rtype: void

    """
    return _ShapeAlgo.shapealgo_Init(*args)

def shapealgo_SetAlgoContainer(*args):
    """
    * Sets default AlgoContainer

    :param aContainer:
    :type aContainer: Handle_ShapeAlgo_AlgoContainer &
    :rtype: void

    """
    return _ShapeAlgo.shapealgo_SetAlgoContainer(*args)

def shapealgo_AlgoContainer(*args):
    """
    * Returns default AlgoContainer

    :rtype: Handle_ShapeAlgo_AlgoContainer

    """
    return _ShapeAlgo.shapealgo_AlgoContainer(*args)

class ShapeAlgo_ToolContainer(OCC.MMgt.MMgt_TShared):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        * Empty constructor

        :rtype: None

        """
        _ShapeAlgo.ShapeAlgo_ToolContainer_swiginit(self, _ShapeAlgo.new_ShapeAlgo_ToolContainer(*args))

    def FixShape(self, *args):
        """
        * Returns ShapeFix_Shape

        :rtype: Handle_ShapeFix_Shape

        """
        return _ShapeAlgo.ShapeAlgo_ToolContainer_FixShape(self, *args)


    def EdgeProjAux(self, *args):
        """
        * Returns ShapeFix_EdgeProjAux

        :rtype: Handle_ShapeFix_EdgeProjAux

        """
        return _ShapeAlgo.ShapeAlgo_ToolContainer_EdgeProjAux(self, *args)


    def _kill_pointed(self):
        """_kill_pointed(ShapeAlgo_ToolContainer self)"""
        return _ShapeAlgo.ShapeAlgo_ToolContainer__kill_pointed(self)


    def GetHandle(self):
        """GetHandle(ShapeAlgo_ToolContainer self) -> Handle_ShapeAlgo_ToolContainer"""
        return _ShapeAlgo.ShapeAlgo_ToolContainer_GetHandle(self)


    def __del__(self):
    	try:
    		self.thisown = False
    		GarbageCollector.garbage.collect_object(self)
    	except:
    		pass


ShapeAlgo_ToolContainer.FixShape = new_instancemethod(_ShapeAlgo.ShapeAlgo_ToolContainer_FixShape, None, ShapeAlgo_ToolContainer)
ShapeAlgo_ToolContainer.EdgeProjAux = new_instancemethod(_ShapeAlgo.ShapeAlgo_ToolContainer_EdgeProjAux, None, ShapeAlgo_ToolContainer)
ShapeAlgo_ToolContainer._kill_pointed = new_instancemethod(_ShapeAlgo.ShapeAlgo_ToolContainer__kill_pointed, None, ShapeAlgo_ToolContainer)
ShapeAlgo_ToolContainer.GetHandle = new_instancemethod(_ShapeAlgo.ShapeAlgo_ToolContainer_GetHandle, None, ShapeAlgo_ToolContainer)
ShapeAlgo_ToolContainer_swigregister = _ShapeAlgo.ShapeAlgo_ToolContainer_swigregister
ShapeAlgo_ToolContainer_swigregister(ShapeAlgo_ToolContainer)

class Handle_ShapeAlgo_ToolContainer(OCC.MMgt.Handle_MMgt_TShared):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _ShapeAlgo.Handle_ShapeAlgo_ToolContainer_swiginit(self, _ShapeAlgo.new_Handle_ShapeAlgo_ToolContainer(*args))
    DownCast = staticmethod(_ShapeAlgo.Handle_ShapeAlgo_ToolContainer_DownCast)

    def __del__(self):
        try:
            self.thisown = False
            GarbageCollector.garbage.collect_object(self)
        except:
            pass


Handle_ShapeAlgo_ToolContainer.Nullify = new_instancemethod(_ShapeAlgo.Handle_ShapeAlgo_ToolContainer_Nullify, None, Handle_ShapeAlgo_ToolContainer)
Handle_ShapeAlgo_ToolContainer.IsNull = new_instancemethod(_ShapeAlgo.Handle_ShapeAlgo_ToolContainer_IsNull, None, Handle_ShapeAlgo_ToolContainer)
Handle_ShapeAlgo_ToolContainer.GetObject = new_instancemethod(_ShapeAlgo.Handle_ShapeAlgo_ToolContainer_GetObject, None, Handle_ShapeAlgo_ToolContainer)
Handle_ShapeAlgo_ToolContainer._kill_pointed = new_instancemethod(_ShapeAlgo.Handle_ShapeAlgo_ToolContainer__kill_pointed, None, Handle_ShapeAlgo_ToolContainer)
Handle_ShapeAlgo_ToolContainer_swigregister = _ShapeAlgo.Handle_ShapeAlgo_ToolContainer_swigregister
Handle_ShapeAlgo_ToolContainer_swigregister(Handle_ShapeAlgo_ToolContainer)

def Handle_ShapeAlgo_ToolContainer_DownCast(AnObject):
    return _ShapeAlgo.Handle_ShapeAlgo_ToolContainer_DownCast(AnObject)
Handle_ShapeAlgo_ToolContainer_DownCast = _ShapeAlgo.Handle_ShapeAlgo_ToolContainer_DownCast



