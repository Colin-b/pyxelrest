# Some parameter names might be VBA keywords, this dictionary is used to use valid VBA parameter names.
keywords = "AddHandler,AddressOf,Alias,And,AndAlso,As,Boolean,ByRef,Byte," \
           "ByVal,Call,Case,Catch,CBool,CByte,CChar,CDate,CDbl,CDec,Char," \
           "CInt,Class,CLng,CObj,Const,Continue,CSByte,CShort,CSng,CStr," \
           "CType,CUInt,CULng,CUShort,Date,Decimal,Declare,Default,Delegate," \
           "Dim,DirectCast,Do,Double,Each,Else,ElseIf,End,EndIf,Enum,Erase," \
           "Error,Event,Exit,Finally,For,Friend,Function,Get,GetType," \
           "GetXMLNamespace,Global,GoSub,GoTo,Handles,If,Implements,Imports," \
           "In,Inherits,Integer,Interface,Is,IsNot,Let,Lib,Like,Long,Loop,Me," \
           "Mod,Module,MustInherit,MustOverride,MyBase,MyClass,Namespace," \
           "Narrowing,New,Next,Not,Nothing,NotInheritable,NotOverridable," \
           "Object,Of,On,Operator,Option,Optional,Or,OrElse,Overloads," \
           "Overridable,Overrides,ParamArray,Partial,Private,Property," \
           "Protected,Public,RaiseEvent,ReadOnly,ReDim,REM,RemoveHandler," \
           "Resume,Return,SByte,Select,Set,Shadows,Shared,Short,Single,Static," \
           "Step,Stop,String,Structure,Sub,SyncLock,Then,Throw,To,Try,TryCast," \
           "TypeOf,UInteger,ULong,UShort,Using,Variant,Wend,When,While," \
           "Widening,With,WithEvents,WriteOnly,Xor".split(",")

vba_restricted_keywords = {k.lower(): k.lower() + "_visual_basic" for k in keywords}

vba_restricted_keywords.update({
    'currency': 'currency_visual_basic',
    'end': 'end_visual_basic',
    'type': 'type_visual_basic'
})
