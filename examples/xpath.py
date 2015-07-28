from genetic_programming import *
from lxml.etree import XPathSyntaxError, XPath
 
 
class Element:
    pass
 
class Attribute:
    pass
 
class ValidExpression:
    pass
 
 
@params(Element, Element)
@rtype(Element)
def child(parent_elem, child_elem):
    return '{}/{}'.format(parent_elem, child_elem)
 
@params(Element, Element)
@rtype(Element)
def descendant(parent_elem, descendant_elem):
    return '{}//{}'.format(parent_elem, descendant_elem)
 
@params(str, str)
@rtype(bool)
def contains(s1, s2):
    return 'contains({}, {})'.format(s1, s2)
 
@params(bool, bool)
@rtype(bool)
def xpath_and(cond1, cond2):
    return '{} and {}'.format(cond1, cond2)
 
@params(bool, bool)
@rtype(bool)
def xpath_or(cond1, cond2):
    return '{} or {}'.format(cond1, cond2)
 
#@params(Element)
#@rtype(bool)
#def condition_on_elem(elem):
#    return elem
 
@params(int)
@rtype(bool)
def nonzero(n):
    return 'boolean({})'.format(n)

@params(Element, Attribute)
@rtype(str)
def get_attribute(elem, attr):
    return '{}/@{}'.format(elem, attr)
 
@params()
@rtype(Element)
def this():
    return '.'
 
@params()
@rtype(Element)
def parent():
    return '..'
 
@params(Element, bool)
@rtype(Element)
def condition_on(elem, cond):
    return '{}[{}]'.format(elem, cond)
 
@params(Element)
@rtype(int)
def count(elem):
    return 'count({})'.format(elem)
 
@params(int, int)
@rtype(bool)
def greater_than(num1, num2):
    return '{} > {}'.format(num1, num2)
 
@params(int, int)
@rtype(bool)
def num_eq(num1, num2):
    return '{} = {}'.format(num1, num2)
 
@params(str, str)
@rtype(bool)
def str_eq(s1, s2):
    return '{} = {}'.format(s1, s2)
 
@params()
@rtype(Element)
def wildcard():
    return '*'
 
@params(Element)
@rtype(ValidExpression)
def validate(expr):
    new_expr = expr.replace('][', ' and ').replace('/.[', '/*[').replace('(*', '(./*').replace('(.[', '(*[')
    if not new_expr.startswith('./'):
        new_expr = './' + new_expr
    try:
        XPath(new_expr)
    except XPathSyntaxError:
        return ''
    return new_expr