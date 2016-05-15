# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _LocalAnalysis.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_LocalAnalysis', [dirname(__file__)])
        except ImportError:
            import _LocalAnalysis
            return _LocalAnalysis
        if fp is not None:
            try:
                _mod = imp.load_module('_LocalAnalysis', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _LocalAnalysis = swig_import_helper()
    del swig_import_helper
else:
    import _LocalAnalysis
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
    __swig_destroy__ = _LocalAnalysis.delete_SwigPyIterator
    def __iter__(self):
        return self
SwigPyIterator.value = new_instancemethod(_LocalAnalysis.SwigPyIterator_value, None, SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_LocalAnalysis.SwigPyIterator_incr, None, SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_LocalAnalysis.SwigPyIterator_decr, None, SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_LocalAnalysis.SwigPyIterator_distance, None, SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_LocalAnalysis.SwigPyIterator_equal, None, SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_LocalAnalysis.SwigPyIterator_copy, None, SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_LocalAnalysis.SwigPyIterator_next, None, SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_LocalAnalysis.SwigPyIterator___next__, None, SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_LocalAnalysis.SwigPyIterator_previous, None, SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_LocalAnalysis.SwigPyIterator_advance, None, SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_LocalAnalysis.SwigPyIterator___eq__, None, SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_LocalAnalysis.SwigPyIterator___ne__, None, SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_LocalAnalysis.SwigPyIterator___iadd__, None, SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_LocalAnalysis.SwigPyIterator___isub__, None, SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_LocalAnalysis.SwigPyIterator___add__, None, SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_LocalAnalysis.SwigPyIterator___sub__, None, SwigPyIterator)
SwigPyIterator_swigregister = _LocalAnalysis.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

import OCC.Standard
import OCC.Geom
import OCC.MMgt
import OCC.gp
import OCC.TCollection
import OCC.GeomAbs
import OCC.TColgp
import OCC.TColStd
import OCC.Geom2d
import OCC.GeomLProp

_LocalAnalysis.LocalAnalysis_NullFirstDerivative_swigconstant(_LocalAnalysis)
LocalAnalysis_NullFirstDerivative = _LocalAnalysis.LocalAnalysis_NullFirstDerivative

_LocalAnalysis.LocalAnalysis_NullSecondDerivative_swigconstant(_LocalAnalysis)
LocalAnalysis_NullSecondDerivative = _LocalAnalysis.LocalAnalysis_NullSecondDerivative

_LocalAnalysis.LocalAnalysis_TangentNotDefined_swigconstant(_LocalAnalysis)
LocalAnalysis_TangentNotDefined = _LocalAnalysis.LocalAnalysis_TangentNotDefined

_LocalAnalysis.LocalAnalysis_NormalNotDefined_swigconstant(_LocalAnalysis)
LocalAnalysis_NormalNotDefined = _LocalAnalysis.LocalAnalysis_NormalNotDefined

_LocalAnalysis.LocalAnalysis_CurvatureNotDefined_swigconstant(_LocalAnalysis)
LocalAnalysis_CurvatureNotDefined = _LocalAnalysis.LocalAnalysis_CurvatureNotDefined
class localanalysis(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def Dump(*args):
        """
        * This class compute s and gives tools to check the local continuity between two points situated on 2 curves) This fonction gives informations about a variable CurveContinuity

        :param surfconti:
        :type surfconti: LocalAnalysis_SurfaceContinuity &
        :param o:
        :type o: Standard_OStream &
        :rtype: void

        * This fonction gives informations about a variable SurfaceContinuity

        :param curvconti:
        :type curvconti: LocalAnalysis_CurveContinuity &
        :param o:
        :type o: Standard_OStream &
        :rtype: void

        """
        return _LocalAnalysis.localanalysis_Dump(*args)

    Dump = staticmethod(Dump)

    def __init__(self):
        _LocalAnalysis.localanalysis_swiginit(self, _LocalAnalysis.new_localanalysis())

    def __del__(self):
    	try:
    		self.thisown = False
    		GarbageCollector.garbage.collect_object(self)
    	except:
    		pass


localanalysis._kill_pointed = new_instancemethod(_LocalAnalysis.localanalysis__kill_pointed, None, localanalysis)
localanalysis_swigregister = _LocalAnalysis.localanalysis_swigregister
localanalysis_swigregister(localanalysis)

def localanalysis_Dump(*args):
    """
    * This class compute s and gives tools to check the local continuity between two points situated on 2 curves) This fonction gives informations about a variable CurveContinuity

    :param surfconti:
    :type surfconti: LocalAnalysis_SurfaceContinuity &
    :param o:
    :type o: Standard_OStream &
    :rtype: void

    * This fonction gives informations about a variable SurfaceContinuity

    :param curvconti:
    :type curvconti: LocalAnalysis_CurveContinuity &
    :param o:
    :type o: Standard_OStream &
    :rtype: void

    """
    return _LocalAnalysis.localanalysis_Dump(*args)

class LocalAnalysis_CurveContinuity(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        * -u1 is the parameter of the point on Curv1 -u2 is the parameter of the point on Curv2 -Order is the required continuity:  GeomAbs_C0 GeomAbs_C1 GeomAbs_C2  GeomAbs_G1 GeomAbs_G2 -EpsNul is used to detect a a vector with nul magnitude (in mm) -EpsC0 is used for C0 continuity to confuse two  points (in mm) -EpsC1 is an angular tolerance in radians used  for C1 continuity to compare the angle between  the first derivatives -EpsC2 is an angular tolerance in radians used for C2 continuity to compare the angle between the second derivatives -EpsG1 is an angular tolerance in radians used for G1 continuity to compare the angle between the tangents -EpsG2 is an angular tolerance in radians used for G2 continuity to compare the angle between the normals - percent : percentage of curvature variation (unitless) used for G2 continuity - Maxlen is the maximum length of Curv1 or Curv2 in meters used to detect nul curvature (in mm)  the constructor computes the quantities which are necessary to check the continuity in the following cases: case C0 -------- - the distance between P1 and P2 with P1=Curv1 (u1) and P2=Curv2(u2) case C1 ------- - the angle between the first derivatives dCurv1(u1)  dCurv2(u2) -------- and --------- du  du - the ratio between the magnitudes of the first derivatives the angle value is between 0 and PI/2 case C2 ------- - the angle between the second derivatives 2  2  d Curv1(u1) d Curv2(u2)  ---------- ---------- 2  2  du du the angle value is between 0 and PI/2 - the ratio between the magnitudes of the second derivatives case G1 ------- the angle between the tangents at each point the angle value is between 0 and PI/2 case G2 ------- -the angle between the normals at each point the angle value is between 0 and PI/2 - the relative variation of curvature:  |curvat1-curvat2|  ------------------  1/2  (curvat1*curvat2)  where curvat1 is the curvature at the first point and curvat2 the curvature at the second point

        :param Curv1:
        :type Curv1: Handle_Geom_Curve &
        :param u1:
        :type u1: float
        :param Curv2:
        :type Curv2: Handle_Geom_Curve &
        :param u2:
        :type u2: float
        :param Order:
        :type Order: GeomAbs_Shape
        :param EpsNul: default value is 0.001
        :type EpsNul: float
        :param EpsC0: default value is 0.001
        :type EpsC0: float
        :param EpsC1: default value is 0.001
        :type EpsC1: float
        :param EpsC2: default value is 0.001
        :type EpsC2: float
        :param EpsG1: default value is 0.001
        :type EpsG1: float
        :param EpsG2: default value is 0.001
        :type EpsG2: float
        :param Percent: default value is 0.01
        :type Percent: float
        :param Maxlen: default value is 10000
        :type Maxlen: float
        :rtype: None

        """
        _LocalAnalysis.LocalAnalysis_CurveContinuity_swiginit(self, _LocalAnalysis.new_LocalAnalysis_CurveContinuity(*args))

    def IsDone(self, *args):
        """
        :rtype: bool

        """
        return _LocalAnalysis.LocalAnalysis_CurveContinuity_IsDone(self, *args)


    def StatusError(self, *args):
        """
        :rtype: LocalAnalysis_StatusErrorType

        """
        return _LocalAnalysis.LocalAnalysis_CurveContinuity_StatusError(self, *args)


    def ContinuityStatus(self, *args):
        """
        :rtype: GeomAbs_Shape

        """
        return _LocalAnalysis.LocalAnalysis_CurveContinuity_ContinuityStatus(self, *args)


    def C0Value(self, *args):
        """
        :rtype: float

        """
        return _LocalAnalysis.LocalAnalysis_CurveContinuity_C0Value(self, *args)


    def C1Angle(self, *args):
        """
        :rtype: float

        """
        return _LocalAnalysis.LocalAnalysis_CurveContinuity_C1Angle(self, *args)


    def C1Ratio(self, *args):
        """
        :rtype: float

        """
        return _LocalAnalysis.LocalAnalysis_CurveContinuity_C1Ratio(self, *args)


    def C2Angle(self, *args):
        """
        :rtype: float

        """
        return _LocalAnalysis.LocalAnalysis_CurveContinuity_C2Angle(self, *args)


    def C2Ratio(self, *args):
        """
        :rtype: float

        """
        return _LocalAnalysis.LocalAnalysis_CurveContinuity_C2Ratio(self, *args)


    def G1Angle(self, *args):
        """
        :rtype: float

        """
        return _LocalAnalysis.LocalAnalysis_CurveContinuity_G1Angle(self, *args)


    def G2Angle(self, *args):
        """
        :rtype: float

        """
        return _LocalAnalysis.LocalAnalysis_CurveContinuity_G2Angle(self, *args)


    def G2CurvatureVariation(self, *args):
        """
        :rtype: float

        """
        return _LocalAnalysis.LocalAnalysis_CurveContinuity_G2CurvatureVariation(self, *args)


    def IsC0(self, *args):
        """
        :rtype: bool

        """
        return _LocalAnalysis.LocalAnalysis_CurveContinuity_IsC0(self, *args)


    def IsC1(self, *args):
        """
        :rtype: bool

        """
        return _LocalAnalysis.LocalAnalysis_CurveContinuity_IsC1(self, *args)


    def IsC2(self, *args):
        """
        :rtype: bool

        """
        return _LocalAnalysis.LocalAnalysis_CurveContinuity_IsC2(self, *args)


    def IsG1(self, *args):
        """
        :rtype: bool

        """
        return _LocalAnalysis.LocalAnalysis_CurveContinuity_IsG1(self, *args)


    def IsG2(self, *args):
        """
        :rtype: bool

        """
        return _LocalAnalysis.LocalAnalysis_CurveContinuity_IsG2(self, *args)


    def __del__(self):
    	try:
    		self.thisown = False
    		GarbageCollector.garbage.collect_object(self)
    	except:
    		pass


LocalAnalysis_CurveContinuity.IsDone = new_instancemethod(_LocalAnalysis.LocalAnalysis_CurveContinuity_IsDone, None, LocalAnalysis_CurveContinuity)
LocalAnalysis_CurveContinuity.StatusError = new_instancemethod(_LocalAnalysis.LocalAnalysis_CurveContinuity_StatusError, None, LocalAnalysis_CurveContinuity)
LocalAnalysis_CurveContinuity.ContinuityStatus = new_instancemethod(_LocalAnalysis.LocalAnalysis_CurveContinuity_ContinuityStatus, None, LocalAnalysis_CurveContinuity)
LocalAnalysis_CurveContinuity.C0Value = new_instancemethod(_LocalAnalysis.LocalAnalysis_CurveContinuity_C0Value, None, LocalAnalysis_CurveContinuity)
LocalAnalysis_CurveContinuity.C1Angle = new_instancemethod(_LocalAnalysis.LocalAnalysis_CurveContinuity_C1Angle, None, LocalAnalysis_CurveContinuity)
LocalAnalysis_CurveContinuity.C1Ratio = new_instancemethod(_LocalAnalysis.LocalAnalysis_CurveContinuity_C1Ratio, None, LocalAnalysis_CurveContinuity)
LocalAnalysis_CurveContinuity.C2Angle = new_instancemethod(_LocalAnalysis.LocalAnalysis_CurveContinuity_C2Angle, None, LocalAnalysis_CurveContinuity)
LocalAnalysis_CurveContinuity.C2Ratio = new_instancemethod(_LocalAnalysis.LocalAnalysis_CurveContinuity_C2Ratio, None, LocalAnalysis_CurveContinuity)
LocalAnalysis_CurveContinuity.G1Angle = new_instancemethod(_LocalAnalysis.LocalAnalysis_CurveContinuity_G1Angle, None, LocalAnalysis_CurveContinuity)
LocalAnalysis_CurveContinuity.G2Angle = new_instancemethod(_LocalAnalysis.LocalAnalysis_CurveContinuity_G2Angle, None, LocalAnalysis_CurveContinuity)
LocalAnalysis_CurveContinuity.G2CurvatureVariation = new_instancemethod(_LocalAnalysis.LocalAnalysis_CurveContinuity_G2CurvatureVariation, None, LocalAnalysis_CurveContinuity)
LocalAnalysis_CurveContinuity.IsC0 = new_instancemethod(_LocalAnalysis.LocalAnalysis_CurveContinuity_IsC0, None, LocalAnalysis_CurveContinuity)
LocalAnalysis_CurveContinuity.IsC1 = new_instancemethod(_LocalAnalysis.LocalAnalysis_CurveContinuity_IsC1, None, LocalAnalysis_CurveContinuity)
LocalAnalysis_CurveContinuity.IsC2 = new_instancemethod(_LocalAnalysis.LocalAnalysis_CurveContinuity_IsC2, None, LocalAnalysis_CurveContinuity)
LocalAnalysis_CurveContinuity.IsG1 = new_instancemethod(_LocalAnalysis.LocalAnalysis_CurveContinuity_IsG1, None, LocalAnalysis_CurveContinuity)
LocalAnalysis_CurveContinuity.IsG2 = new_instancemethod(_LocalAnalysis.LocalAnalysis_CurveContinuity_IsG2, None, LocalAnalysis_CurveContinuity)
LocalAnalysis_CurveContinuity._kill_pointed = new_instancemethod(_LocalAnalysis.LocalAnalysis_CurveContinuity__kill_pointed, None, LocalAnalysis_CurveContinuity)
LocalAnalysis_CurveContinuity_swigregister = _LocalAnalysis.LocalAnalysis_CurveContinuity_swigregister
LocalAnalysis_CurveContinuity_swigregister(LocalAnalysis_CurveContinuity)

class LocalAnalysis_SurfaceContinuity(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        * -u1,v1 are the parameters of the point on Surf1 -u2,v2 are the parameters of the point on Surf2 -Order is the required continuity:  GeomAbs_C0 GeomAbs_C1 GeomAbs_C2  GeomAbs_G1 GeomAbs_G2 -EpsNul is used to detect a a vector with nul magnitude -EpsC0 is used for C0 continuity to confuse two  points (in mm) -EpsC1 is an angular tolerance in radians used  for C1 continuity to compare the angle between  the first derivatives -EpsC2 is an angular tolerance in radians used for C2 continuity to compare the angle between the second derivatives -EpsG1 is an angular tolerance in radians used for G1 continuity to compare the angle between the normals  -Percent : percentage of curvature variation (unitless) used for G2 continuity - Maxlen is the maximum length of Surf1 or Surf2 in meters used to detect null curvature (in mm)  the constructor computes the quantities which are necessary to check the continuity in the following cases: case C0 -------- - the distance between P1 and P2 with P1=Surf (u1,v1) and P2=Surfv2(u2,v2)  case C1 ------- - the angle between the first derivatives in u :  dSurf1(u1,v1) dSurf2(u2,v2) ----------- and --------- du  du  the angle value is between 0 and PI/2 - the angle between the first derivatives in v :  dSurf1(u1,v1) dSurf2(u2,v2) -------- and --------- dv  dv - the ratio between the magnitudes of the first derivatives in u - the ratio between the magnitudes of the first derivatives in v  the angle value is between 0 and pi/2 case C2 ------- - the angle between the second derivatives in u 2 2  d Surf1(u1,v1) d Surf2(u2,v2)  ---------- ---------- 2 2  d u d u  - the ratio between the magnitudes of the second derivatives in u - the ratio between the magnitudes of the second derivatives in v the angle value is between 0 and PI/2 case G1 ------- -the angle between the normals at each point the angle value is between 0 and PI/2 case G2 ------- - the maximum normal curvature gap between the two points

        :param Surf1:
        :type Surf1: Handle_Geom_Surface &
        :param u1:
        :type u1: float
        :param v1:
        :type v1: float
        :param Surf2:
        :type Surf2: Handle_Geom_Surface &
        :param u2:
        :type u2: float
        :param v2:
        :type v2: float
        :param Order:
        :type Order: GeomAbs_Shape
        :param EpsNul: default value is 0.001
        :type EpsNul: float
        :param EpsC0: default value is 0.001
        :type EpsC0: float
        :param EpsC1: default value is 0.001
        :type EpsC1: float
        :param EpsC2: default value is 0.001
        :type EpsC2: float
        :param EpsG1: default value is 0.001
        :type EpsG1: float
        :param Percent: default value is 0.01
        :type Percent: float
        :param Maxlen: default value is 10000
        :type Maxlen: float
        :rtype: None

        :param curv1:
        :type curv1: Handle_Geom2d_Curve &
        :param curv2:
        :type curv2: Handle_Geom2d_Curve &
        :param U:
        :type U: float
        :param Surf1:
        :type Surf1: Handle_Geom_Surface &
        :param Surf2:
        :type Surf2: Handle_Geom_Surface &
        :param Order:
        :type Order: GeomAbs_Shape
        :param EpsNul: default value is 0.001
        :type EpsNul: float
        :param EpsC0: default value is 0.001
        :type EpsC0: float
        :param EpsC1: default value is 0.001
        :type EpsC1: float
        :param EpsC2: default value is 0.001
        :type EpsC2: float
        :param EpsG1: default value is 0.001
        :type EpsG1: float
        :param Percent: default value is 0.01
        :type Percent: float
        :param Maxlen: default value is 10000
        :type Maxlen: float
        :rtype: None

        * This constructor is used when we want to compute many analysis. After we use the method ComputeAnalysis

        :param EpsNul: default value is 0.001
        :type EpsNul: float
        :param EpsC0: default value is 0.001
        :type EpsC0: float
        :param EpsC1: default value is 0.001
        :type EpsC1: float
        :param EpsC2: default value is 0.001
        :type EpsC2: float
        :param EpsG1: default value is 0.001
        :type EpsG1: float
        :param Percent: default value is 0.01
        :type Percent: float
        :param Maxlen: default value is 10000
        :type Maxlen: float
        :rtype: None

        """
        _LocalAnalysis.LocalAnalysis_SurfaceContinuity_swiginit(self, _LocalAnalysis.new_LocalAnalysis_SurfaceContinuity(*args))

    def ComputeAnalysis(self, *args):
        """
        :param Surf1:
        :type Surf1: GeomLProp_SLProps &
        :param Surf2:
        :type Surf2: GeomLProp_SLProps &
        :param Order:
        :type Order: GeomAbs_Shape
        :rtype: None

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_ComputeAnalysis(self, *args)


    def IsDone(self, *args):
        """
        :rtype: bool

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_IsDone(self, *args)


    def ContinuityStatus(self, *args):
        """
        :rtype: GeomAbs_Shape

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_ContinuityStatus(self, *args)


    def StatusError(self, *args):
        """
        :rtype: LocalAnalysis_StatusErrorType

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_StatusError(self, *args)


    def C0Value(self, *args):
        """
        :rtype: float

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_C0Value(self, *args)


    def C1UAngle(self, *args):
        """
        :rtype: float

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_C1UAngle(self, *args)


    def C1URatio(self, *args):
        """
        :rtype: float

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_C1URatio(self, *args)


    def C1VAngle(self, *args):
        """
        :rtype: float

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_C1VAngle(self, *args)


    def C1VRatio(self, *args):
        """
        :rtype: float

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_C1VRatio(self, *args)


    def C2UAngle(self, *args):
        """
        :rtype: float

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_C2UAngle(self, *args)


    def C2URatio(self, *args):
        """
        :rtype: float

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_C2URatio(self, *args)


    def C2VAngle(self, *args):
        """
        :rtype: float

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_C2VAngle(self, *args)


    def C2VRatio(self, *args):
        """
        :rtype: float

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_C2VRatio(self, *args)


    def G1Angle(self, *args):
        """
        :rtype: float

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_G1Angle(self, *args)


    def G2CurvatureGap(self, *args):
        """
        :rtype: float

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_G2CurvatureGap(self, *args)


    def IsC0(self, *args):
        """
        :rtype: bool

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_IsC0(self, *args)


    def IsC1(self, *args):
        """
        :rtype: bool

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_IsC1(self, *args)


    def IsC2(self, *args):
        """
        :rtype: bool

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_IsC2(self, *args)


    def IsG1(self, *args):
        """
        :rtype: bool

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_IsG1(self, *args)


    def IsG2(self, *args):
        """
        :rtype: bool

        """
        return _LocalAnalysis.LocalAnalysis_SurfaceContinuity_IsG2(self, *args)


    def __del__(self):
    	try:
    		self.thisown = False
    		GarbageCollector.garbage.collect_object(self)
    	except:
    		pass


LocalAnalysis_SurfaceContinuity.ComputeAnalysis = new_instancemethod(_LocalAnalysis.LocalAnalysis_SurfaceContinuity_ComputeAnalysis, None, LocalAnalysis_SurfaceContinuity)
LocalAnalysis_SurfaceContinuity.IsDone = new_instancemethod(_LocalAnalysis.LocalAnalysis_SurfaceContinuity_IsDone, None, LocalAnalysis_SurfaceContinuity)
LocalAnalysis_SurfaceContinuity.ContinuityStatus = new_instancemethod(_LocalAnalysis.LocalAnalysis_SurfaceContinuity_ContinuityStatus, None, LocalAnalysis_SurfaceContinuity)
LocalAnalysis_SurfaceContinuity.StatusError = new_instancemethod(_LocalAnalysis.LocalAnalysis_SurfaceContinuity_StatusError, None, LocalAnalysis_SurfaceContinuity)
LocalAnalysis_SurfaceContinuity.C0Value = new_instancemethod(_LocalAnalysis.LocalAnalysis_SurfaceContinuity_C0Value, None, LocalAnalysis_SurfaceContinuity)
LocalAnalysis_SurfaceContinuity.C1UAngle = new_instancemethod(_LocalAnalysis.LocalAnalysis_SurfaceContinuity_C1UAngle, None, LocalAnalysis_SurfaceContinuity)
LocalAnalysis_SurfaceContinuity.C1URatio = new_instancemethod(_LocalAnalysis.LocalAnalysis_SurfaceContinuity_C1URatio, None, LocalAnalysis_SurfaceContinuity)
LocalAnalysis_SurfaceContinuity.C1VAngle = new_instancemethod(_LocalAnalysis.LocalAnalysis_SurfaceContinuity_C1VAngle, None, LocalAnalysis_SurfaceContinuity)
LocalAnalysis_SurfaceContinuity.C1VRatio = new_instancemethod(_LocalAnalysis.LocalAnalysis_SurfaceContinuity_C1VRatio, None, LocalAnalysis_SurfaceContinuity)
LocalAnalysis_SurfaceContinuity.C2UAngle = new_instancemethod(_LocalAnalysis.LocalAnalysis_SurfaceContinuity_C2UAngle, None, LocalAnalysis_SurfaceContinuity)
LocalAnalysis_SurfaceContinuity.C2URatio = new_instancemethod(_LocalAnalysis.LocalAnalysis_SurfaceContinuity_C2URatio, None, LocalAnalysis_SurfaceContinuity)
LocalAnalysis_SurfaceContinuity.C2VAngle = new_instancemethod(_LocalAnalysis.LocalAnalysis_SurfaceContinuity_C2VAngle, None, LocalAnalysis_SurfaceContinuity)
LocalAnalysis_SurfaceContinuity.C2VRatio = new_instancemethod(_LocalAnalysis.LocalAnalysis_SurfaceContinuity_C2VRatio, None, LocalAnalysis_SurfaceContinuity)
LocalAnalysis_SurfaceContinuity.G1Angle = new_instancemethod(_LocalAnalysis.LocalAnalysis_SurfaceContinuity_G1Angle, None, LocalAnalysis_SurfaceContinuity)
LocalAnalysis_SurfaceContinuity.G2CurvatureGap = new_instancemethod(_LocalAnalysis.LocalAnalysis_SurfaceContinuity_G2CurvatureGap, None, LocalAnalysis_SurfaceContinuity)
LocalAnalysis_SurfaceContinuity.IsC0 = new_instancemethod(_LocalAnalysis.LocalAnalysis_SurfaceContinuity_IsC0, None, LocalAnalysis_SurfaceContinuity)
LocalAnalysis_SurfaceContinuity.IsC1 = new_instancemethod(_LocalAnalysis.LocalAnalysis_SurfaceContinuity_IsC1, None, LocalAnalysis_SurfaceContinuity)
LocalAnalysis_SurfaceContinuity.IsC2 = new_instancemethod(_LocalAnalysis.LocalAnalysis_SurfaceContinuity_IsC2, None, LocalAnalysis_SurfaceContinuity)
LocalAnalysis_SurfaceContinuity.IsG1 = new_instancemethod(_LocalAnalysis.LocalAnalysis_SurfaceContinuity_IsG1, None, LocalAnalysis_SurfaceContinuity)
LocalAnalysis_SurfaceContinuity.IsG2 = new_instancemethod(_LocalAnalysis.LocalAnalysis_SurfaceContinuity_IsG2, None, LocalAnalysis_SurfaceContinuity)
LocalAnalysis_SurfaceContinuity._kill_pointed = new_instancemethod(_LocalAnalysis.LocalAnalysis_SurfaceContinuity__kill_pointed, None, LocalAnalysis_SurfaceContinuity)
LocalAnalysis_SurfaceContinuity_swigregister = _LocalAnalysis.LocalAnalysis_SurfaceContinuity_swigregister
LocalAnalysis_SurfaceContinuity_swigregister(LocalAnalysis_SurfaceContinuity)



