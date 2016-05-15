# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _ShapeBuild.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ShapeBuild', [dirname(__file__)])
        except ImportError:
            import _ShapeBuild
            return _ShapeBuild
        if fp is not None:
            try:
                _mod = imp.load_module('_ShapeBuild', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ShapeBuild = swig_import_helper()
    del swig_import_helper
else:
    import _ShapeBuild
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
    __swig_destroy__ = _ShapeBuild.delete_SwigPyIterator
    def __iter__(self):
        return self
SwigPyIterator.value = new_instancemethod(_ShapeBuild.SwigPyIterator_value, None, SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_ShapeBuild.SwigPyIterator_incr, None, SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_ShapeBuild.SwigPyIterator_decr, None, SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_ShapeBuild.SwigPyIterator_distance, None, SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_ShapeBuild.SwigPyIterator_equal, None, SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_ShapeBuild.SwigPyIterator_copy, None, SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_ShapeBuild.SwigPyIterator_next, None, SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_ShapeBuild.SwigPyIterator___next__, None, SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_ShapeBuild.SwigPyIterator_previous, None, SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_ShapeBuild.SwigPyIterator_advance, None, SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_ShapeBuild.SwigPyIterator___eq__, None, SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_ShapeBuild.SwigPyIterator___ne__, None, SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_ShapeBuild.SwigPyIterator___iadd__, None, SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_ShapeBuild.SwigPyIterator___isub__, None, SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_ShapeBuild.SwigPyIterator___add__, None, SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_ShapeBuild.SwigPyIterator___sub__, None, SwigPyIterator)
SwigPyIterator_swigregister = _ShapeBuild.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

import OCC.Geom
import OCC.MMgt
import OCC.Standard
import OCC.gp
import OCC.TCollection
import OCC.GeomAbs
import OCC.TColgp
import OCC.TColStd
import OCC.TopoDS
import OCC.TopLoc
import OCC.TopAbs
import OCC.Geom2d
import OCC.BRepTools
import OCC.Bnd
import OCC.TopTools
import OCC.Message
import OCC.BRep
import OCC.Poly
import OCC.NCollection
import OCC.TShort
import OCC.ShapeExtend
import OCC.TColGeom
class shapebuild(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def PlaneXOY(*args):
        """
        * Rebuilds a shape with substitution of some components Returns a Geom_Surface which is the Plane XOY (Z positive) This allows to consider an UV space homologous to a 3D space, with this support surface

        :rtype: Handle_Geom_Plane

        """
        return _ShapeBuild.shapebuild_PlaneXOY(*args)

    PlaneXOY = staticmethod(PlaneXOY)

    def __init__(self):
        _ShapeBuild.shapebuild_swiginit(self, _ShapeBuild.new_shapebuild())

    def __del__(self):
    	try:
    		self.thisown = False
    		GarbageCollector.garbage.collect_object(self)
    	except:
    		pass


shapebuild._kill_pointed = new_instancemethod(_ShapeBuild.shapebuild__kill_pointed, None, shapebuild)
shapebuild_swigregister = _ShapeBuild.shapebuild_swigregister
shapebuild_swigregister(shapebuild)

def shapebuild_PlaneXOY(*args):
    """
    * Rebuilds a shape with substitution of some components Returns a Geom_Surface which is the Plane XOY (Z positive) This allows to consider an UV space homologous to a 3D space, with this support surface

    :rtype: Handle_Geom_Plane

    """
    return _ShapeBuild.shapebuild_PlaneXOY(*args)

class ShapeBuild_Edge(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def CopyReplaceVertices(self, *args):
        """
        * Copy edge and replace one or both its vertices to a given one(s). Vertex V1 replaces FORWARD vertex, and V2 - REVERSED, as they are found by TopoDS_Iterator. If V1 or V2 is NULL, the original vertex is taken

        :param edge:
        :type edge: TopoDS_Edge &
        :param V1:
        :type V1: TopoDS_Vertex &
        :param V2:
        :type V2: TopoDS_Vertex &
        :rtype: TopoDS_Edge

        """
        return _ShapeBuild.ShapeBuild_Edge_CopyReplaceVertices(self, *args)


    def CopyRanges(self, *args):
        """
        * Copies ranges for curve3d and all common pcurves from edge <fromedge> into edge <toedge>.

        :param toedge:
        :type toedge: TopoDS_Edge &
        :param fromedge:
        :type fromedge: TopoDS_Edge &
        :param alpha: default value is 0
        :type alpha: float
        :param beta: default value is 1
        :type beta: float
        :rtype: None

        """
        return _ShapeBuild.ShapeBuild_Edge_CopyRanges(self, *args)


    def SetRange3d(self, *args):
        """
        * Sets range on 3d curve only.

        :param edge:
        :type edge: TopoDS_Edge &
        :param first:
        :type first: float
        :param last:
        :type last: float
        :rtype: None

        """
        return _ShapeBuild.ShapeBuild_Edge_SetRange3d(self, *args)


    def CopyPCurves(self, *args):
        """
        * Makes a copy of pcurves from edge <fromedge> into edge <toedge>. Pcurves which are already present in <toedge>, are replaced by copies, other are copied. Ranges are also copied.

        :param toedge:
        :type toedge: TopoDS_Edge &
        :param fromedge:
        :type fromedge: TopoDS_Edge &
        :rtype: None

        """
        return _ShapeBuild.ShapeBuild_Edge_CopyPCurves(self, *args)


    def Copy(self, *args):
        """
        * Make a copy of <edge> by call to CopyReplaceVertices() (i.e. construct new TEdge with the same pcurves and vertices). If <sharepcurves> is False, pcurves are also replaced by their copies with help of method CopyPCurves

        :param edge:
        :type edge: TopoDS_Edge &
        :param sharepcurves: default value is Standard_True
        :type sharepcurves: bool
        :rtype: TopoDS_Edge

        """
        return _ShapeBuild.ShapeBuild_Edge_Copy(self, *args)


    def RemovePCurve(self, *args):
        """
        * Removes the PCurve(s) which could be recorded in an Edge for the given Face

        :param edge:
        :type edge: TopoDS_Edge &
        :param face:
        :type face: TopoDS_Face &
        :rtype: None

        * Removes the PCurve(s) which could be recorded in an Edge for the given Surface

        :param edge:
        :type edge: TopoDS_Edge &
        :param surf:
        :type surf: Handle_Geom_Surface &
        :rtype: None

        * Removes the PCurve(s) which could be recorded in an Edge for the given Surface, with given Location

        :param edge:
        :type edge: TopoDS_Edge &
        :param surf:
        :type surf: Handle_Geom_Surface &
        :param loc:
        :type loc: TopLoc_Location &
        :rtype: None

        """
        return _ShapeBuild.ShapeBuild_Edge_RemovePCurve(self, *args)


    def ReplacePCurve(self, *args):
        """
        * Replace the PCurve in an Edge for the given Face In case if edge is seam, i.e. has 2 pcurves on that face, only pcurve corresponding to the orientation of the edge is replaced

        :param edge:
        :type edge: TopoDS_Edge &
        :param pcurve:
        :type pcurve: Handle_Geom2d_Curve &
        :param face:
        :type face: TopoDS_Face &
        :rtype: None

        """
        return _ShapeBuild.ShapeBuild_Edge_ReplacePCurve(self, *args)


    def ReassignPCurve(self, *args):
        """
        * Reassign edge pcurve lying on face <old> to another face <sub>. If edge has two pcurves on <old> face, only one of them will be reassigned, and other will left alone. Similarly, if edge already had a pcurve on face <sub>, it will have two pcurves on it. Returns True if succeeded, False if no pcurve lying on <old> found.

        :param edge:
        :type edge: TopoDS_Edge &
        :param old:
        :type old: TopoDS_Face &
        :param sub:
        :type sub: TopoDS_Face &
        :rtype: bool

        """
        return _ShapeBuild.ShapeBuild_Edge_ReassignPCurve(self, *args)


    def TransformPCurve(self, *args):
        """
        * Transforms the PCurve with given matrix and affinity U factor.

        :param pcurve:
        :type pcurve: Handle_Geom2d_Curve &
        :param trans:
        :type trans: gp_Trsf2d
        :param uFact:
        :type uFact: float
        :param aFirst:
        :type aFirst: float &
        :param aLast:
        :type aLast: float &
        :rtype: Handle_Geom2d_Curve

        """
        return _ShapeBuild.ShapeBuild_Edge_TransformPCurve(self, *args)


    def RemoveCurve3d(self, *args):
        """
        * Removes the Curve3D recorded in an Edge

        :param edge:
        :type edge: TopoDS_Edge &
        :rtype: None

        """
        return _ShapeBuild.ShapeBuild_Edge_RemoveCurve3d(self, *args)


    def BuildCurve3d(self, *args):
        """
        * Calls BRepTools::BuildCurve3D

        :param edge:
        :type edge: TopoDS_Edge &
        :rtype: bool

        """
        return _ShapeBuild.ShapeBuild_Edge_BuildCurve3d(self, *args)


    def MakeEdge(self, *args):
        """
        * Makes edge with curve and location

        :param edge:
        :type edge: TopoDS_Edge &
        :param curve:
        :type curve: Handle_Geom_Curve &
        :param L:
        :type L: TopLoc_Location &
        :rtype: None

        * Makes edge with curve, location and range [p1, p2]

        :param edge:
        :type edge: TopoDS_Edge &
        :param curve:
        :type curve: Handle_Geom_Curve &
        :param L:
        :type L: TopLoc_Location &
        :param p1:
        :type p1: float
        :param p2:
        :type p2: float
        :rtype: None

        * Makes edge with pcurve and face

        :param edge:
        :type edge: TopoDS_Edge &
        :param pcurve:
        :type pcurve: Handle_Geom2d_Curve &
        :param face:
        :type face: TopoDS_Face &
        :rtype: None

        * Makes edge with pcurve, face and range [p1, p2]

        :param edge:
        :type edge: TopoDS_Edge &
        :param pcurve:
        :type pcurve: Handle_Geom2d_Curve &
        :param face:
        :type face: TopoDS_Face &
        :param p1:
        :type p1: float
        :param p2:
        :type p2: float
        :rtype: None

        * Makes edge with pcurve, surface and location

        :param edge:
        :type edge: TopoDS_Edge &
        :param pcurve:
        :type pcurve: Handle_Geom2d_Curve &
        :param S:
        :type S: Handle_Geom_Surface &
        :param L:
        :type L: TopLoc_Location &
        :rtype: None

        * Makes edge with pcurve, surface, location and range [p1, p2]

        :param edge:
        :type edge: TopoDS_Edge &
        :param pcurve:
        :type pcurve: Handle_Geom2d_Curve &
        :param S:
        :type S: Handle_Geom_Surface &
        :param L:
        :type L: TopLoc_Location &
        :param p1:
        :type p1: float
        :param p2:
        :type p2: float
        :rtype: None

        """
        return _ShapeBuild.ShapeBuild_Edge_MakeEdge(self, *args)


    def __init__(self):
        _ShapeBuild.ShapeBuild_Edge_swiginit(self, _ShapeBuild.new_ShapeBuild_Edge())

    def __del__(self):
    	try:
    		self.thisown = False
    		GarbageCollector.garbage.collect_object(self)
    	except:
    		pass


ShapeBuild_Edge.CopyReplaceVertices = new_instancemethod(_ShapeBuild.ShapeBuild_Edge_CopyReplaceVertices, None, ShapeBuild_Edge)
ShapeBuild_Edge.CopyRanges = new_instancemethod(_ShapeBuild.ShapeBuild_Edge_CopyRanges, None, ShapeBuild_Edge)
ShapeBuild_Edge.SetRange3d = new_instancemethod(_ShapeBuild.ShapeBuild_Edge_SetRange3d, None, ShapeBuild_Edge)
ShapeBuild_Edge.CopyPCurves = new_instancemethod(_ShapeBuild.ShapeBuild_Edge_CopyPCurves, None, ShapeBuild_Edge)
ShapeBuild_Edge.Copy = new_instancemethod(_ShapeBuild.ShapeBuild_Edge_Copy, None, ShapeBuild_Edge)
ShapeBuild_Edge.RemovePCurve = new_instancemethod(_ShapeBuild.ShapeBuild_Edge_RemovePCurve, None, ShapeBuild_Edge)
ShapeBuild_Edge.ReplacePCurve = new_instancemethod(_ShapeBuild.ShapeBuild_Edge_ReplacePCurve, None, ShapeBuild_Edge)
ShapeBuild_Edge.ReassignPCurve = new_instancemethod(_ShapeBuild.ShapeBuild_Edge_ReassignPCurve, None, ShapeBuild_Edge)
ShapeBuild_Edge.TransformPCurve = new_instancemethod(_ShapeBuild.ShapeBuild_Edge_TransformPCurve, None, ShapeBuild_Edge)
ShapeBuild_Edge.RemoveCurve3d = new_instancemethod(_ShapeBuild.ShapeBuild_Edge_RemoveCurve3d, None, ShapeBuild_Edge)
ShapeBuild_Edge.BuildCurve3d = new_instancemethod(_ShapeBuild.ShapeBuild_Edge_BuildCurve3d, None, ShapeBuild_Edge)
ShapeBuild_Edge.MakeEdge = new_instancemethod(_ShapeBuild.ShapeBuild_Edge_MakeEdge, None, ShapeBuild_Edge)
ShapeBuild_Edge._kill_pointed = new_instancemethod(_ShapeBuild.ShapeBuild_Edge__kill_pointed, None, ShapeBuild_Edge)
ShapeBuild_Edge_swigregister = _ShapeBuild.ShapeBuild_Edge_swigregister
ShapeBuild_Edge_swigregister(ShapeBuild_Edge)

class ShapeBuild_ReShape(OCC.BRepTools.BRepTools_ReShape):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        * Returns an empty Reshape

        :rtype: None

        """
        _ShapeBuild.ShapeBuild_ReShape_swiginit(self, _ShapeBuild.new_ShapeBuild_ReShape(*args))

    def Apply(self, *args):
        """
        * Applies the substitutions requests to a shape  <until> gives the level of type until which requests are taken into account. For subshapes of the type <until> no rebuild and futher exploring are done. ACTUALLY, NOT IMPLEMENTED BELOW TopAbs_FACE  <buildmode> says how to do on a SOLID,SHELL ... if one of its sub-shapes has been changed: 0: at least one Replace or Remove -> COMPOUND, else as such 1: at least one Remove (Replace are ignored) -> COMPOUND 2: Replace and Remove are both ignored If Replace/Remove are ignored or absent, the result as same type as the starting shape

        :param shape:
        :type shape: TopoDS_Shape &
        :param until:
        :type until: TopAbs_ShapeEnum
        :param buildmode:
        :type buildmode: int
        :rtype: TopoDS_Shape

        * Applies the substitutions requests to a shape.  <until> gives the level of type until which requests are taken into account. For subshapes of the type <until> no rebuild and futher exploring are done.  NOTE: each subshape can be replaced by shape of the same type or by shape containing only shapes of that type (for example, TopoDS_Edge can be replaced by TopoDS_Edge, TopoDS_Wire or TopoDS_Compound containing TopoDS_Edges). If incompatible shape type is encountered, it is ignored and flag FAIL1 is set in Status.

        :param shape:
        :type shape: TopoDS_Shape &
        :param until: default value is TopAbs_SHAPE
        :type until: TopAbs_ShapeEnum
        :rtype: TopoDS_Shape

        """
        return _ShapeBuild.ShapeBuild_ReShape_Apply(self, *args)


    def Status(self, *args):
        """
        * Returns a complete substitution status for a shape 0 : not recorded, <newsh> = original <shape> < 0: to be removed, <newsh> is NULL > 0: to be replaced, <newsh> is a new item If <last> is False, returns status and new shape recorded in the map directly for the shape, if True and status > 0 then recursively searches for the last status and new shape.

        :param shape:
        :type shape: TopoDS_Shape &
        :param newsh:
        :type newsh: TopoDS_Shape &
        :param last: default value is Standard_False
        :type last: bool
        :rtype: int

        * Queries the status of last call to Apply(shape,enum) OK : no (sub)shapes replaced or removed DONE1: source (starting) shape replaced DONE2: source (starting) shape removed DONE3: some subshapes replaced DONE4: some subshapes removed FAIL1: some replacements not done because of bad type of subshape

        :param status:
        :type status: ShapeExtend_Status
        :rtype: bool

        """
        return _ShapeBuild.ShapeBuild_ReShape_Status(self, *args)


    def _kill_pointed(self):
        """_kill_pointed(ShapeBuild_ReShape self)"""
        return _ShapeBuild.ShapeBuild_ReShape__kill_pointed(self)


    def GetHandle(self):
        """GetHandle(ShapeBuild_ReShape self) -> Handle_ShapeBuild_ReShape"""
        return _ShapeBuild.ShapeBuild_ReShape_GetHandle(self)


    def __del__(self):
    	try:
    		self.thisown = False
    		GarbageCollector.garbage.collect_object(self)
    	except:
    		pass


ShapeBuild_ReShape.Apply = new_instancemethod(_ShapeBuild.ShapeBuild_ReShape_Apply, None, ShapeBuild_ReShape)
ShapeBuild_ReShape.Status = new_instancemethod(_ShapeBuild.ShapeBuild_ReShape_Status, None, ShapeBuild_ReShape)
ShapeBuild_ReShape._kill_pointed = new_instancemethod(_ShapeBuild.ShapeBuild_ReShape__kill_pointed, None, ShapeBuild_ReShape)
ShapeBuild_ReShape.GetHandle = new_instancemethod(_ShapeBuild.ShapeBuild_ReShape_GetHandle, None, ShapeBuild_ReShape)
ShapeBuild_ReShape_swigregister = _ShapeBuild.ShapeBuild_ReShape_swigregister
ShapeBuild_ReShape_swigregister(ShapeBuild_ReShape)

class Handle_ShapeBuild_ReShape(OCC.BRepTools.Handle_BRepTools_ReShape):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _ShapeBuild.Handle_ShapeBuild_ReShape_swiginit(self, _ShapeBuild.new_Handle_ShapeBuild_ReShape(*args))
    DownCast = staticmethod(_ShapeBuild.Handle_ShapeBuild_ReShape_DownCast)

    def __del__(self):
        try:
            self.thisown = False
            GarbageCollector.garbage.collect_object(self)
        except:
            pass


Handle_ShapeBuild_ReShape.Nullify = new_instancemethod(_ShapeBuild.Handle_ShapeBuild_ReShape_Nullify, None, Handle_ShapeBuild_ReShape)
Handle_ShapeBuild_ReShape.IsNull = new_instancemethod(_ShapeBuild.Handle_ShapeBuild_ReShape_IsNull, None, Handle_ShapeBuild_ReShape)
Handle_ShapeBuild_ReShape.GetObject = new_instancemethod(_ShapeBuild.Handle_ShapeBuild_ReShape_GetObject, None, Handle_ShapeBuild_ReShape)
Handle_ShapeBuild_ReShape._kill_pointed = new_instancemethod(_ShapeBuild.Handle_ShapeBuild_ReShape__kill_pointed, None, Handle_ShapeBuild_ReShape)
Handle_ShapeBuild_ReShape_swigregister = _ShapeBuild.Handle_ShapeBuild_ReShape_swigregister
Handle_ShapeBuild_ReShape_swigregister(Handle_ShapeBuild_ReShape)

def Handle_ShapeBuild_ReShape_DownCast(AnObject):
    return _ShapeBuild.Handle_ShapeBuild_ReShape_DownCast(AnObject)
Handle_ShapeBuild_ReShape_DownCast = _ShapeBuild.Handle_ShapeBuild_ReShape_DownCast

class ShapeBuild_Vertex(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def CombineVertex(self, *args):
        """
        * Combines new vertex from two others. This new one is the smallest vertex which comprises both of the source vertices. The function takes into account the positions and tolerances of the source vertices. The tolerance of the new vertex will be equal to the minimal tolerance that is required to comprise source vertices multiplied by tolFactor (in order to avoid errors because of discreteness of calculations).

        :param V1:
        :type V1: TopoDS_Vertex &
        :param V2:
        :type V2: TopoDS_Vertex &
        :param tolFactor: default value is 1.0001
        :type tolFactor: float
        :rtype: TopoDS_Vertex

        * The same function as above, except that it accepts two points and two tolerances instead of vertices

        :param pnt1:
        :type pnt1: gp_Pnt
        :param pnt2:
        :type pnt2: gp_Pnt
        :param tol1:
        :type tol1: float
        :param tol2:
        :type tol2: float
        :param tolFactor: default value is 1.0001
        :type tolFactor: float
        :rtype: TopoDS_Vertex

        """
        return _ShapeBuild.ShapeBuild_Vertex_CombineVertex(self, *args)


    def __init__(self):
        _ShapeBuild.ShapeBuild_Vertex_swiginit(self, _ShapeBuild.new_ShapeBuild_Vertex())

    def __del__(self):
    	try:
    		self.thisown = False
    		GarbageCollector.garbage.collect_object(self)
    	except:
    		pass


ShapeBuild_Vertex.CombineVertex = new_instancemethod(_ShapeBuild.ShapeBuild_Vertex_CombineVertex, None, ShapeBuild_Vertex)
ShapeBuild_Vertex._kill_pointed = new_instancemethod(_ShapeBuild.ShapeBuild_Vertex__kill_pointed, None, ShapeBuild_Vertex)
ShapeBuild_Vertex_swigregister = _ShapeBuild.ShapeBuild_Vertex_swigregister
ShapeBuild_Vertex_swigregister(ShapeBuild_Vertex)



