
import functools
import collections


func = collections.namedtuple('Function', 'params rtype')


def __convert_type(t):
    if not t:
        return None
    if isinstance(t, collections.Mapping):
        return (collections.Mapping, __convert_type(next(t.iterkeys())), __convert_type(next(t.itervalues())))
    if isinstance(t, collections.Iterable):
        return (collections.Iterable, __convert_type(t[0]))
    if isinstance(t, func):
        return (func, __convert_type(func.params), __convert_type(func.rtype))
    return t


def __type_annotations_factory():
    RTYPES = collections.defaultdict(list)

    def allowed_children_factory(param_types):
        return lambda: [RTYPES[param_type] for param_type in param_types]

    def rtype(return_type):
        def decorator(f):
            RTYPES[__convert_type(return_type)].append(f)  # TODO: analysis of return type
            return f
        return decorator

    def params(*param_types):
        def decorator(f):
            _param_types = map(__convert_type, param_types)
            f.allowed_children = allowed_children_factory(_param_types)
            return f
        return decorator

    return rtype, params


rtype, params = __type_annotations_factory()