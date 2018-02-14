# https://stackoverflow.com/questions/35847269/nameerror-global-name-dot-parser-is-not-defined?lq=1
# https://habrahabr.ru/post/239081/
#------------------------begining----------------------------
'''
from pyparsing import *
s = 'import matplotlib.pyplot as plt'
module_name = Word(alphas + '_')
full_module_name = module_name + ZeroOrMore('.' + module_name)
import_as = Optional('as' + module_name)
parse_module = 'import' + full_module_name + import_as
print(parse_module.parseString(s).asList())'''


#------------------end result--------------------
from pyparsing import Word, alphas, ZeroOrMore, Suppress, Optional
module_name = Word(alphas + "_")
full_module_name = (module_name + ZeroOrMore(Suppress('.') + module_name))('modules')
import_as = (Optional(Suppress('as') + module_name))('import_as')
parse_module = (Suppress('import') + full_module_name + import_as).setParseAction(lambda t: {'import': t.modules.asList(), 'as': t.import_as.asList()[0]})
