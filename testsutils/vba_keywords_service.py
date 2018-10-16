from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def open_api_definition():
    return jsonify(swagger='2.0',
                   definitions={
                       'VBAKeywords': {
                           'properties': {
                               'addhandler': {
                                },
                                'addressof': {
                                },
                                'alias': {
                                },
                                'and': {
                                },
                                'andalso': {
                                },
                                'as': {
                                },
                                'attribute': {
                                },
                                'boolean': {
                                },
                                'byref': {
                                },
                                'byte': {
                                },
                                'byval': {
                                },
                                'call': {
                                },
                                'case': {
                                },
                                'catch': {
                                },
                                'cbool': {
                                },
                                'cbyte': {
                                },
                                'cchar': {
                                },
                                'cdate': {
                                },
                                'cdbl': {
                                },
                                'cdec': {
                                },
                                'char': {
                                },
                                'cint': {
                                },
                                'class': {
                                },
                                'clng': {
                                },
                                'cobj': {
                                },
                                'const': {
                                },
                                'continue': {
                                },
                                'csbyte': {
                                },
                                'cshort': {
                                },
                                'csng': {
                                },
                                'cstr': {
                                },
                                'ctype': {
                                },
                                'cuint': {
                                },
                                'culng': {
                                },
                                'currency': {
                                },
                                'cushort': {
                                },
                                'date': {
                                },
                                'decimal': {
                                },
                                'declare': {
                                },
                                'default': {
                                },
                                'delegate': {
                                },
                                'dim': {
                                },
                                'directcast': {
                                },
                                'do': {
                                },
                                'double': {
                                },
                                'each': {
                                },
                                'else': {
                                },
                                'elseif': {
                                },
                                'end': {
                                },
                                'endif': {
                                },
                                'enum': {
                                },
                                'erase': {
                                },
                                'error': {
                                },
                                'event': {
                                },
                                'exit': {
                                },
                                'finally': {
                                },
                                'for': {
                                },
                                'friend': {
                                },
                                'function': {
                                },
                                'get': {
                                },
                                'gettype': {
                                },
                                'getxmlnamespace': {
                                },
                                'global': {
                                },
                                'gosub': {
                                },
                                'goto': {
                                },
                                'handles': {
                                },
                                'if': {
                                },
                                'implements': {
                                },
                                'imports': {
                                },
                                'in': {
                                },
                                'inherits': {
                                },
                                'integer': {
                                },
                                'interface': {
                                },
                                'is': {
                                },
                                'isnot': {
                                },
                                'let': {
                                },
                                'lib': {
                                },
                                'like': {
                                },
                                'long': {
                                },
                                'loop': {
                                },
                                'me': {
                                },
                                'mod': {
                                },
                                'module': {
                                },
                                'mustinherit': {
                                },
                                'mustoverride': {
                                },
                                'mybase': {
                                },
                                'myclass': {
                                },
                                'namespace': {
                                },
                                'narrowing': {
                                },
                                'new': {
                                },
                                'next': {
                                },
                                'not': {
                                },
                                'nothing': {
                                },
                                'notinheritable': {
                                },
                                'notoverridable': {
                                },
                                'object': {
                                },
                                'of': {
                                },
                                'on': {
                                },
                                'operator': {
                                },
                                'option': {
                                },
                                'optional': {
                                },
                                'or': {
                                },
                                'orelse': {
                                },
                                'overloads': {
                                },
                                'overridable': {
                                },
                                'overrides': {
                                },
                                'paramarray': {
                                },
                                'partial': {
                                },
                                'private': {
                                },
                                'property': {
                                },
                                'protected': {
                                },
                                'public': {
                                },
                                'raiseevent': {
                                },
                                'readonly': {
                                },
                                'redim': {
                                },
                                'rem': {
                                },
                                'removehandler': {
                                },
                                'resume': {
                                },
                                'return': {
                                },
                                'sbyte': {
                                },
                                'select': {
                                },
                                'set': {
                                },
                                'shadows': {
                                },
                                'shared': {
                                },
                                'short': {
                                },
                                'single': {
                                },
                                'static': {
                                },
                                'step': {
                                },
                                'stop': {
                                },
                                'string': {
                                },
                                'structure': {
                                },
                                'sub': {
                                },
                                'synclock': {
                                },
                                'then': {
                                },
                                'throw': {
                                },
                                'to': {
                                },
                                'try': {
                                },
                                'trycast': {
                                },
                                'type': {
                                },
                                'typeof': {
                                },
                                'uinteger': {
                                },
                                'ulong': {
                                },
                                'ushort': {
                                },
                                'using': {
                                },
                                'variant': {
                                },
                                'wend': {
                                },
                                'when': {
                                },
                                'while': {
                                },
                                'widening': {
                                },
                                'with': {
                                },
                                'withevents': {
                                },
                                'writeonly': {
                                },
                                'xor': {
                                }
                           }
                       },
                       'PythonKeywords': {
                           'properties': {
                               'with.a.dot': {
                                },
                           }
                       },
                   },
                   produces=[
                       "application/json"
                   ],
                   paths={
                       '/vba_restricted_keywords': {
                           'parameters': [
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'addhandler',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'addressof',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'alias',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'and',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'andalso',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'as',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'attribute',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'boolean',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'byref',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'byte',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'byval',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'call',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'case',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'catch',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'cbool',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'cbyte',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'cchar',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'cdate',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'cdbl',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'cdec',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'char',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'cint',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'class',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'clng',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'cobj',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'const',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'continue',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'csbyte',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'cshort',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'csng',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'cstr',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'ctype',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'cuint',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'culng',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'currency',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'cushort',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'date',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'decimal',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'declare',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'default',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'delegate',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'dim',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'directcast',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'do',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'double',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'each',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'else',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'elseif',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'end',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'endif',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'enum',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'erase',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'error',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'event',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'exit',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'finally',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'for',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'friend',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'function',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'get',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'gettype',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'getxmlnamespace',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'global',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'gosub',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'goto',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'handles',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'if',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'implements',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'imports',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'in',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'inherits',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'integer',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'interface',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'is',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'isnot',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'let',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'lib',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'like',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'long',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'loop',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'me',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'mod',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'module',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'mustinherit',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'mustoverride',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'mybase',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'myclass',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'namespace',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'narrowing',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'new',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'next',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'not',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'nothing',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'notinheritable',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'notoverridable',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'object',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'of',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'on',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'operator',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'option',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'optional',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'or',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'orelse',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'overloads',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'overridable',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'overrides',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'paramarray',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'partial',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'private',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'property',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'protected',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'public',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'raiseevent',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'readonly',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'redim',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'rem',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'removehandler',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'resume',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'return',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'sbyte',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'select',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'set',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'shadows',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'shared',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'short',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'single',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'static',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'step',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'stop',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'string',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'structure',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'sub',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'synclock',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'then',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'throw',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'to',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'try',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'trycast',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'type',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'typeof',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'uinteger',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'ulong',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'ushort',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'using',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'variant',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'wend',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'when',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'while',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'widening',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'with',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'withevents',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'writeonly',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'xor',
                                   'required': True,
                                   'type': 'string'
                               }
                           ],
                           'get': {
                               'operationId': 'get_vba_restricted_keywords',
                               'responses': {
                                   '200': {
                                       'description': 'return value',
                                       'schema': {
                                           '$ref': '#/definitions/VBAKeywords'
                                       }
                                   }
                               }
                           },
                           'post': {
                               'operationId': 'post_vba_restricted_keywords',
                               'responses': {
                                   '200': {
                                       'description': 'return value',
                                       '$ref': '#/definitions/VBAKeywords'
                                   }
                               },
                               'produces': [
                                   "application/json"
                               ]
                           },
                           'put': {
                               'operationId': 'put_vba_restricted_keywords',
                               'responses': {
                                   '200': {
                                       'description': 'return value',
                                       '$ref': '#/definitions/VBAKeywords'
                                   }
                                },
                               'produces': [
                                   "application/json"
                               ]
                           },
                           'delete': {
                               'operationId': 'delete_vba_restricted_keywords',
                               'responses': {
                                   '200': {
                                       'description': 'return value',
                                       '$ref': '#/definitions/VBAKeywords'
                                   }
                               },
                               'produces': [
                                   "application/json"
                               ]
                           }
                       },
                       '/{attribute}/vba/restricted/keyword/in/uri/parameter': {
                           'parameters': [
                               {
                                   'type': 'string',
                                   'in': 'path',
                                   'name': 'attribute',
                                   'description': 'attribute uri param',
                                   'required': True
                               }
                           ],
                           'get': {
                               'operationId': 'get_attribute_vba_restricted_keyword_in_uri_parameter',
                               'responses': {
                                   '200': {
                                       'description': 'return value',
                                       'schema': {
                                           '$ref': '#/definitions/VBAKeywords'
                                       }
                                   }
                               }
                           }
                       },
                       '/python_restricted_keywords': {
                           'parameters': [
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'with.a.dot',
                                   'required': True,
                                   'type': 'string'
                               },
                           ],
                           'get': {
                               'operationId': 'get_python_restricted_keywords',
                               'responses': {
                                   '200': {
                                       'description': 'return value',
                                       'schema': {
                                           '$ref': '#/definitions/PythonKeywords'
                                       }
                                   }
                               }
                           },
                           'post': {
                               'operationId': 'post_python_restricted_keywords',
                               'responses': {
                                   '200': {
                                       'description': 'return value',
                                       '$ref': '#/definitions/PythonKeywords'
                                   }
                               },
                               'produces': [
                                   "application/json"
                               ]
                           },
                           'put': {
                               'operationId': 'put_python_restricted_keywords',
                               'responses': {
                                   '200': {
                                       'description': 'return value',
                                       '$ref': '#/definitions/PythonKeywords'
                                   }
                                },
                               'produces': [
                                   "application/json"
                               ]
                           },
                           'delete': {
                               'operationId': 'delete_python_restricted_keywords',
                               'responses': {
                                   '200': {
                                       'description': 'return value',
                                       '$ref': '#/definitions/PythonKeywords'
                                   }
                               },
                               'produces': [
                                   "application/json"
                               ]
                           }
                       },
                   })


@app.route('/vba_restricted_keywords', methods=['GET', 'POST', 'PUT', 'DELETE'])
def vba_restricted_keywords():
    return jsonify(request.args)


@app.route('/<string:attribute>/vba/restricted/keyword/in/uri/parameter', methods=['GET'])
def get_attribute_vba_restricted_keyword_in_uri_parameter(attribute):
    return jsonify({'attribute': attribute})


@app.route('/python_restricted_keywords', methods=['GET', 'POST', 'PUT', 'DELETE'])
def python_restricted_keywords():
    return jsonify(request.args)


def start_server(port):
    app.run(port=port)


if __name__ == '__main__':
    start_server(8949)
