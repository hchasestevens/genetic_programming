import functools
import collections


REGISTERED_TYPES = set()
func = collections.namedtuple('Function', 'params rtype')


def __convert_type(t):
    if not t:
        converted = None
    elif isinstance(t, collections.Mapping):
        converted = (collections.Mapping, __convert_type(next(t.iterkeys())), __convert_type(next(t.itervalues())))
    elif isinstance(t, func):
        converted = (func, __convert_type(t.params), __convert_type(t.rtype))
    elif isinstance(t, collections.Iterable):
        converted = (collections.Iterable, __convert_type(t[0]))
    else:
        converted = t
    REGISTERED_TYPES.add(converted)
    return converted


def __prettify_converted_type(t):
    if t is None:
        return 'None'
    if isinstance(t, type):
        return t.__name__
    try:
        __, listed_t = t
        return '[{}]'.format(__prettify_converted_type(listed_t))
    except (ValueError, TypeError):
        pass
    try:
        outer, first_inner, second_inner = t
        formatted_inners = map(__prettify_converted_type, (first_inner, second_inner))
        if outer is collections.Mapping:
            return '{{{}: {}}}'.format(*formatted_inners)
        if outer == func:
            return '{} -> {}'.format(*formatted_inners)
    except (ValueError, TypeError):
        pass
    return str(t)


def __type_annotations_factory():
    RTYPES = collections.defaultdict(list)

    def allowed_children_factory(param_types):
        return lambda: [RTYPES[param_type] for param_type in param_types]

    def rtype(return_type, convert=True):
        convert_type = __convert_type if convert else lambda x: x
        def decorator(f):
            _return_type = convert_type(return_type)
            RTYPES[_return_type].append(f)
            f.readable_rtype = __prettify_converted_type(_return_type)
            return f
        return decorator

    def params(*param_types, **kwargs):
        convert_type = __convert_type if kwargs.get('convert', True) else lambda x: x
        def decorator(f):
            _param_types = map(convert_type, param_types)
            f.allowed_children = allowed_children_factory(_param_types)
            f.readable_params = ', '.join(map(__prettify_converted_type, _param_types))
            return f
        return decorator

    return rtype, params


rtype, params = __type_annotations_factory()
