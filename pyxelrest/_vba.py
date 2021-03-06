# Some parameter names might be VBA keywords, this dictionary is used to use valid VBA parameter names.
# Values should be lower cased
# Source: https://msdn.microsoft.com/en-us/library/ksh7h19t(v=vs.90).aspx?f=255&MSPPError=-2147217396
keywords = [
    "addhandler",
    "addressof",
    "alias",
    "and",
    "andalso",
    "as",
    "attribute",
    "boolean",
    "byref",
    "byte",
    "byval",
    "call",
    # xlwings parameter with a specific meaning
    "caller",
    "case",
    "catch",
    "cbool",
    "cbyte",
    "cchar",
    "cdate",
    "cdbl",
    "cdec",
    "char",
    "cint",
    "class",
    "clng",
    "cobj",
    "const",
    "continue",
    "csbyte",
    "cshort",
    "csng",
    "cstr",
    "ctype",
    "cuint",
    "culng",
    "currency",
    "cushort",
    "date",
    "decimal",
    "declare",
    "default",
    "delegate",
    "dim",
    "directcast",
    "do",
    "double",
    "each",
    "else",
    "elseif",
    "end",
    "endif",
    "enum",
    "erase",
    "error",
    "event",
    # pyxelrest parameter with a specific meaning
    "excel_application",
    "exit",
    "finally",
    "for",
    "friend",
    "function",
    "get",
    "gettype",
    "getxmlnamespace",
    "global",
    "gosub",
    "goto",
    "handles",
    "if",
    "implements",
    "imports",
    "in",
    "inherits",
    "integer",
    "interface",
    "is",
    "isnot",
    "let",
    "lib",
    "like",
    "long",
    "loop",
    "me",
    "mod",
    "module",
    "mustinherit",
    "mustoverride",
    "mybase",
    "myclass",
    "namespace",
    "narrowing",
    "new",
    "next",
    "not",
    "nothing",
    "notinheritable",
    "notoverridable",
    "object",
    "of",
    "on",
    "operator",
    "option",
    "optional",
    "or",
    "orelse",
    "overloads",
    "overridable",
    "overrides",
    "paramarray",
    "partial",
    "private",
    "property",
    "protected",
    "public",
    "raiseevent",
    "readonly",
    "redim",
    "rem",
    "removehandler",
    "resume",
    "return",
    "sbyte",
    "select",
    "set",
    "shadows",
    "shared",
    "short",
    "single",
    "static",
    "step",
    "stop",
    # python function
    "str",
    "string",
    "structure",
    "sub",
    "synclock",
    "then",
    "throw",
    "to",
    "try",
    "trycast",
    "type",
    "typeof",
    "uinteger",
    "ulong",
    "ushort",
    "using",
    "variant",
    "wend",
    "when",
    "while",
    "widening",
    "with",
    "withevents",
    "writeonly",
    "xor",
]

vba_restricted_keywords = {keyword: keyword + "_visual_basic" for keyword in keywords}
