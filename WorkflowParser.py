# Generated from Workflow.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,38,200,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        5,0,42,8,0,10,0,12,0,45,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,3,1,62,8,1,1,2,1,2,1,2,1,2,1,2,3,2,69,8,
        2,1,2,1,2,1,2,1,2,1,2,3,2,76,8,2,1,2,3,2,79,8,2,1,3,1,3,1,3,1,3,
        3,3,85,8,3,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,3,5,95,8,5,1,6,1,6,1,
        6,1,6,1,6,1,7,1,7,3,7,104,8,7,1,7,3,7,107,8,7,1,8,1,8,1,8,1,9,1,
        9,1,9,1,9,5,9,116,8,9,10,9,12,9,119,9,9,3,9,121,8,9,1,10,1,10,1,
        10,1,11,1,11,1,11,1,11,1,11,5,11,131,8,11,10,11,12,11,134,9,11,1,
        11,1,11,1,11,1,11,5,11,140,8,11,10,11,12,11,143,9,11,1,11,3,11,146,
        8,11,1,12,1,12,1,12,5,12,151,8,12,10,12,12,12,154,9,12,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,3,13,164,8,13,1,14,1,14,1,14,5,14,
        169,8,14,10,14,12,14,172,9,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,
        5,16,181,8,16,10,16,12,16,184,9,16,1,17,1,17,1,17,1,17,1,18,1,18,
        1,18,5,18,193,8,18,10,18,12,18,196,9,18,1,19,1,19,1,19,0,0,20,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,0,2,1,0,2,6,
        2,0,17,18,23,25,201,0,43,1,0,0,0,2,61,1,0,0,0,4,78,1,0,0,0,6,80,
        1,0,0,0,8,86,1,0,0,0,10,94,1,0,0,0,12,96,1,0,0,0,14,101,1,0,0,0,
        16,108,1,0,0,0,18,120,1,0,0,0,20,122,1,0,0,0,22,125,1,0,0,0,24,147,
        1,0,0,0,26,163,1,0,0,0,28,165,1,0,0,0,30,173,1,0,0,0,32,177,1,0,
        0,0,34,185,1,0,0,0,36,189,1,0,0,0,38,197,1,0,0,0,40,42,3,2,1,0,41,
        40,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,46,1,0,0,
        0,45,43,1,0,0,0,46,47,5,0,0,1,47,1,1,0,0,0,48,49,3,4,2,0,49,50,5,
        30,0,0,50,62,1,0,0,0,51,52,3,6,3,0,52,53,5,30,0,0,53,62,1,0,0,0,
        54,55,3,12,6,0,55,56,5,30,0,0,56,62,1,0,0,0,57,58,3,14,7,0,58,59,
        5,30,0,0,59,62,1,0,0,0,60,62,3,22,11,0,61,48,1,0,0,0,61,51,1,0,0,
        0,61,54,1,0,0,0,61,57,1,0,0,0,61,60,1,0,0,0,62,3,1,0,0,0,63,64,5,
        7,0,0,64,65,5,26,0,0,65,66,5,19,0,0,66,68,5,34,0,0,67,69,3,28,14,
        0,68,67,1,0,0,0,68,69,1,0,0,0,69,70,1,0,0,0,70,79,5,35,0,0,71,72,
        5,7,0,0,72,73,5,20,0,0,73,75,5,34,0,0,74,76,3,28,14,0,75,74,1,0,
        0,0,75,76,1,0,0,0,76,77,1,0,0,0,77,79,5,35,0,0,78,63,1,0,0,0,78,
        71,1,0,0,0,79,5,1,0,0,0,80,81,3,8,4,0,81,84,3,10,5,0,82,83,5,15,
        0,0,83,85,3,32,16,0,84,82,1,0,0,0,84,85,1,0,0,0,85,7,1,0,0,0,86,
        87,7,0,0,0,87,9,1,0,0,0,88,89,5,26,0,0,89,95,5,19,0,0,90,91,5,20,
        0,0,91,92,5,36,0,0,92,93,5,26,0,0,93,95,5,19,0,0,94,88,1,0,0,0,94,
        90,1,0,0,0,95,11,1,0,0,0,96,97,5,8,0,0,97,98,3,10,5,0,98,99,5,16,
        0,0,99,100,3,28,14,0,100,13,1,0,0,0,101,103,5,9,0,0,102,104,3,16,
        8,0,103,102,1,0,0,0,103,104,1,0,0,0,104,106,1,0,0,0,105,107,3,20,
        10,0,106,105,1,0,0,0,106,107,1,0,0,0,107,15,1,0,0,0,108,109,5,10,
        0,0,109,110,3,18,9,0,110,17,1,0,0,0,111,121,5,38,0,0,112,117,3,36,
        18,0,113,114,5,31,0,0,114,116,3,36,18,0,115,113,1,0,0,0,116,119,
        1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,121,1,0,0,0,119,117,
        1,0,0,0,120,111,1,0,0,0,120,112,1,0,0,0,121,19,1,0,0,0,122,123,5,
        11,0,0,123,124,3,24,12,0,124,21,1,0,0,0,125,126,5,12,0,0,126,127,
        3,24,12,0,127,128,5,13,0,0,128,132,5,34,0,0,129,131,3,2,1,0,130,
        129,1,0,0,0,131,134,1,0,0,0,132,130,1,0,0,0,132,133,1,0,0,0,133,
        135,1,0,0,0,134,132,1,0,0,0,135,145,5,35,0,0,136,137,5,14,0,0,137,
        141,5,34,0,0,138,140,3,2,1,0,139,138,1,0,0,0,140,143,1,0,0,0,141,
        139,1,0,0,0,141,142,1,0,0,0,142,144,1,0,0,0,143,141,1,0,0,0,144,
        146,5,35,0,0,145,136,1,0,0,0,145,146,1,0,0,0,146,23,1,0,0,0,147,
        152,3,26,13,0,148,149,5,22,0,0,149,151,3,26,13,0,150,148,1,0,0,0,
        151,154,1,0,0,0,152,150,1,0,0,0,152,153,1,0,0,0,153,25,1,0,0,0,154,
        152,1,0,0,0,155,156,3,36,18,0,156,157,5,21,0,0,157,158,3,38,19,0,
        158,164,1,0,0,0,159,160,5,32,0,0,160,161,3,24,12,0,161,162,5,33,
        0,0,162,164,1,0,0,0,163,155,1,0,0,0,163,159,1,0,0,0,164,27,1,0,0,
        0,165,170,3,30,15,0,166,167,5,31,0,0,167,169,3,30,15,0,168,166,1,
        0,0,0,169,172,1,0,0,0,170,168,1,0,0,0,170,171,1,0,0,0,171,29,1,0,
        0,0,172,170,1,0,0,0,173,174,3,36,18,0,174,175,5,37,0,0,175,176,3,
        38,19,0,176,31,1,0,0,0,177,182,3,34,17,0,178,179,5,31,0,0,179,181,
        3,34,17,0,180,178,1,0,0,0,181,184,1,0,0,0,182,180,1,0,0,0,182,183,
        1,0,0,0,183,33,1,0,0,0,184,182,1,0,0,0,185,186,5,26,0,0,186,187,
        5,37,0,0,187,188,3,38,19,0,188,35,1,0,0,0,189,194,5,26,0,0,190,191,
        5,1,0,0,191,193,5,26,0,0,192,190,1,0,0,0,193,196,1,0,0,0,194,192,
        1,0,0,0,194,195,1,0,0,0,195,37,1,0,0,0,196,194,1,0,0,0,197,198,7,
        1,0,0,198,39,1,0,0,0,19,43,61,68,75,78,84,94,103,106,117,120,132,
        141,145,152,163,170,182,194
    ]

class WorkflowParser ( Parser ):

    grammarFileName = "Workflow.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "'borrow'", "'return'", "'reserve'", 
                     "'extend'", "<INVALID>", "'define'", "'update'", "'query'", 
                     "'select'", "'where'", "'if'", "'then'", "'else'", 
                     "'with'", "'set'", "'true'", "'false'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "';'", "','", "'('", "')'", 
                     "'{'", "'}'", "'->'", "'='", "'*'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "BORROW", "RETURN", "RESERVE", 
                      "EXTEND", "MARK_LOST", "DEFINE", "UPDATE", "QUERY", 
                      "SELECT", "WHERE", "IF", "THEN", "ELSE", "WITH", "SET", 
                      "TRUE", "FALSE", "ITEM_ID", "MEMBER_ID", "COMPARISON", 
                      "LOGICAL_OP", "STRING", "DATE", "NUMBER", "ID", "COMMENT", 
                      "COMMENT_LINE", "WS", "SEMICOLON", "COMMA", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "ARROW", "EQ", "STAR" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_defineStmt = 2
    RULE_txnStmt = 3
    RULE_action = 4
    RULE_target = 5
    RULE_updateStmt = 6
    RULE_queryStmt = 7
    RULE_selectClause = 8
    RULE_selectFields = 9
    RULE_whereClause = 10
    RULE_ifStmt = 11
    RULE_condition = 12
    RULE_expression = 13
    RULE_fieldList = 14
    RULE_fieldAssign = 15
    RULE_paramList = 16
    RULE_paramAssign = 17
    RULE_field = 18
    RULE_value = 19

    ruleNames =  [ "program", "statement", "defineStmt", "txnStmt", "action", 
                   "target", "updateStmt", "queryStmt", "selectClause", 
                   "selectFields", "whereClause", "ifStmt", "condition", 
                   "expression", "fieldList", "fieldAssign", "paramList", 
                   "paramAssign", "field", "value" ]

    EOF = Token.EOF
    T__0=1
    BORROW=2
    RETURN=3
    RESERVE=4
    EXTEND=5
    MARK_LOST=6
    DEFINE=7
    UPDATE=8
    QUERY=9
    SELECT=10
    WHERE=11
    IF=12
    THEN=13
    ELSE=14
    WITH=15
    SET=16
    TRUE=17
    FALSE=18
    ITEM_ID=19
    MEMBER_ID=20
    COMPARISON=21
    LOGICAL_OP=22
    STRING=23
    DATE=24
    NUMBER=25
    ID=26
    COMMENT=27
    COMMENT_LINE=28
    WS=29
    SEMICOLON=30
    COMMA=31
    LPAREN=32
    RPAREN=33
    LBRACE=34
    RBRACE=35
    ARROW=36
    EQ=37
    STAR=38

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(WorkflowParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WorkflowParser.StatementContext)
            else:
                return self.getTypedRuleContext(WorkflowParser.StatementContext,i)


        def getRuleIndex(self):
            return WorkflowParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = WorkflowParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 5116) != 0):
                self.state = 40
                self.statement()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 46
            self.match(WorkflowParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def defineStmt(self):
            return self.getTypedRuleContext(WorkflowParser.DefineStmtContext,0)


        def SEMICOLON(self):
            return self.getToken(WorkflowParser.SEMICOLON, 0)

        def txnStmt(self):
            return self.getTypedRuleContext(WorkflowParser.TxnStmtContext,0)


        def updateStmt(self):
            return self.getTypedRuleContext(WorkflowParser.UpdateStmtContext,0)


        def queryStmt(self):
            return self.getTypedRuleContext(WorkflowParser.QueryStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(WorkflowParser.IfStmtContext,0)


        def getRuleIndex(self):
            return WorkflowParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = WorkflowParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.defineStmt()
                self.state = 49
                self.match(WorkflowParser.SEMICOLON)
                pass
            elif token in [2, 3, 4, 5, 6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.txnStmt()
                self.state = 52
                self.match(WorkflowParser.SEMICOLON)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.updateStmt()
                self.state = 55
                self.match(WorkflowParser.SEMICOLON)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 57
                self.queryStmt()
                self.state = 58
                self.match(WorkflowParser.SEMICOLON)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 60
                self.ifStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefineStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFINE(self):
            return self.getToken(WorkflowParser.DEFINE, 0)

        def ID(self):
            return self.getToken(WorkflowParser.ID, 0)

        def ITEM_ID(self):
            return self.getToken(WorkflowParser.ITEM_ID, 0)

        def LBRACE(self):
            return self.getToken(WorkflowParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(WorkflowParser.RBRACE, 0)

        def fieldList(self):
            return self.getTypedRuleContext(WorkflowParser.FieldListContext,0)


        def MEMBER_ID(self):
            return self.getToken(WorkflowParser.MEMBER_ID, 0)

        def getRuleIndex(self):
            return WorkflowParser.RULE_defineStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefineStmt" ):
                listener.enterDefineStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefineStmt" ):
                listener.exitDefineStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefineStmt" ):
                return visitor.visitDefineStmt(self)
            else:
                return visitor.visitChildren(self)




    def defineStmt(self):

        localctx = WorkflowParser.DefineStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_defineStmt)
        self._la = 0 # Token type
        try:
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.match(WorkflowParser.DEFINE)
                self.state = 64
                self.match(WorkflowParser.ID)
                self.state = 65
                self.match(WorkflowParser.ITEM_ID)
                self.state = 66
                self.match(WorkflowParser.LBRACE)
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26:
                    self.state = 67
                    self.fieldList()


                self.state = 70
                self.match(WorkflowParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.match(WorkflowParser.DEFINE)
                self.state = 72
                self.match(WorkflowParser.MEMBER_ID)
                self.state = 73
                self.match(WorkflowParser.LBRACE)
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26:
                    self.state = 74
                    self.fieldList()


                self.state = 77
                self.match(WorkflowParser.RBRACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TxnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def action(self):
            return self.getTypedRuleContext(WorkflowParser.ActionContext,0)


        def target(self):
            return self.getTypedRuleContext(WorkflowParser.TargetContext,0)


        def WITH(self):
            return self.getToken(WorkflowParser.WITH, 0)

        def paramList(self):
            return self.getTypedRuleContext(WorkflowParser.ParamListContext,0)


        def getRuleIndex(self):
            return WorkflowParser.RULE_txnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTxnStmt" ):
                listener.enterTxnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTxnStmt" ):
                listener.exitTxnStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTxnStmt" ):
                return visitor.visitTxnStmt(self)
            else:
                return visitor.visitChildren(self)




    def txnStmt(self):

        localctx = WorkflowParser.TxnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_txnStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.action()
            self.state = 81
            self.target()
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 82
                self.match(WorkflowParser.WITH)
                self.state = 83
                self.paramList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BORROW(self):
            return self.getToken(WorkflowParser.BORROW, 0)

        def RETURN(self):
            return self.getToken(WorkflowParser.RETURN, 0)

        def RESERVE(self):
            return self.getToken(WorkflowParser.RESERVE, 0)

        def EXTEND(self):
            return self.getToken(WorkflowParser.EXTEND, 0)

        def MARK_LOST(self):
            return self.getToken(WorkflowParser.MARK_LOST, 0)

        def getRuleIndex(self):
            return WorkflowParser.RULE_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAction" ):
                listener.enterAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAction" ):
                listener.exitAction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAction" ):
                return visitor.visitAction(self)
            else:
                return visitor.visitChildren(self)




    def action(self):

        localctx = WorkflowParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_action)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 124) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TargetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(WorkflowParser.ID, 0)

        def ITEM_ID(self):
            return self.getToken(WorkflowParser.ITEM_ID, 0)

        def MEMBER_ID(self):
            return self.getToken(WorkflowParser.MEMBER_ID, 0)

        def ARROW(self):
            return self.getToken(WorkflowParser.ARROW, 0)

        def getRuleIndex(self):
            return WorkflowParser.RULE_target

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTarget" ):
                listener.enterTarget(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTarget" ):
                listener.exitTarget(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTarget" ):
                return visitor.visitTarget(self)
            else:
                return visitor.visitChildren(self)




    def target(self):

        localctx = WorkflowParser.TargetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_target)
        try:
            self.state = 94
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.match(WorkflowParser.ID)
                self.state = 89
                self.match(WorkflowParser.ITEM_ID)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.match(WorkflowParser.MEMBER_ID)
                self.state = 91
                self.match(WorkflowParser.ARROW)
                self.state = 92
                self.match(WorkflowParser.ID)
                self.state = 93
                self.match(WorkflowParser.ITEM_ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UPDATE(self):
            return self.getToken(WorkflowParser.UPDATE, 0)

        def target(self):
            return self.getTypedRuleContext(WorkflowParser.TargetContext,0)


        def SET(self):
            return self.getToken(WorkflowParser.SET, 0)

        def fieldList(self):
            return self.getTypedRuleContext(WorkflowParser.FieldListContext,0)


        def getRuleIndex(self):
            return WorkflowParser.RULE_updateStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUpdateStmt" ):
                listener.enterUpdateStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUpdateStmt" ):
                listener.exitUpdateStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdateStmt" ):
                return visitor.visitUpdateStmt(self)
            else:
                return visitor.visitChildren(self)




    def updateStmt(self):

        localctx = WorkflowParser.UpdateStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_updateStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(WorkflowParser.UPDATE)
            self.state = 97
            self.target()
            self.state = 98
            self.match(WorkflowParser.SET)
            self.state = 99
            self.fieldList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUERY(self):
            return self.getToken(WorkflowParser.QUERY, 0)

        def selectClause(self):
            return self.getTypedRuleContext(WorkflowParser.SelectClauseContext,0)


        def whereClause(self):
            return self.getTypedRuleContext(WorkflowParser.WhereClauseContext,0)


        def getRuleIndex(self):
            return WorkflowParser.RULE_queryStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQueryStmt" ):
                listener.enterQueryStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQueryStmt" ):
                listener.exitQueryStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQueryStmt" ):
                return visitor.visitQueryStmt(self)
            else:
                return visitor.visitChildren(self)




    def queryStmt(self):

        localctx = WorkflowParser.QueryStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_queryStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(WorkflowParser.QUERY)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 102
                self.selectClause()


            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 105
                self.whereClause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(WorkflowParser.SELECT, 0)

        def selectFields(self):
            return self.getTypedRuleContext(WorkflowParser.SelectFieldsContext,0)


        def getRuleIndex(self):
            return WorkflowParser.RULE_selectClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectClause" ):
                listener.enterSelectClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectClause" ):
                listener.exitSelectClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectClause" ):
                return visitor.visitSelectClause(self)
            else:
                return visitor.visitChildren(self)




    def selectClause(self):

        localctx = WorkflowParser.SelectClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_selectClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(WorkflowParser.SELECT)
            self.state = 109
            self.selectFields()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectFieldsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(WorkflowParser.STAR, 0)

        def field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WorkflowParser.FieldContext)
            else:
                return self.getTypedRuleContext(WorkflowParser.FieldContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(WorkflowParser.COMMA)
            else:
                return self.getToken(WorkflowParser.COMMA, i)

        def getRuleIndex(self):
            return WorkflowParser.RULE_selectFields

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectFields" ):
                listener.enterSelectFields(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectFields" ):
                listener.exitSelectFields(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectFields" ):
                return visitor.visitSelectFields(self)
            else:
                return visitor.visitChildren(self)




    def selectFields(self):

        localctx = WorkflowParser.SelectFieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_selectFields)
        self._la = 0 # Token type
        try:
            self.state = 120
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.match(WorkflowParser.STAR)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.field()
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==31:
                    self.state = 113
                    self.match(WorkflowParser.COMMA)
                    self.state = 114
                    self.field()
                    self.state = 119
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhereClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(WorkflowParser.WHERE, 0)

        def condition(self):
            return self.getTypedRuleContext(WorkflowParser.ConditionContext,0)


        def getRuleIndex(self):
            return WorkflowParser.RULE_whereClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhereClause" ):
                listener.enterWhereClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhereClause" ):
                listener.exitWhereClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhereClause" ):
                return visitor.visitWhereClause(self)
            else:
                return visitor.visitChildren(self)




    def whereClause(self):

        localctx = WorkflowParser.WhereClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_whereClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(WorkflowParser.WHERE)
            self.state = 123
            self.condition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(WorkflowParser.IF, 0)

        def condition(self):
            return self.getTypedRuleContext(WorkflowParser.ConditionContext,0)


        def THEN(self):
            return self.getToken(WorkflowParser.THEN, 0)

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(WorkflowParser.LBRACE)
            else:
                return self.getToken(WorkflowParser.LBRACE, i)

        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(WorkflowParser.RBRACE)
            else:
                return self.getToken(WorkflowParser.RBRACE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WorkflowParser.StatementContext)
            else:
                return self.getTypedRuleContext(WorkflowParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(WorkflowParser.ELSE, 0)

        def getRuleIndex(self):
            return WorkflowParser.RULE_ifStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = WorkflowParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(WorkflowParser.IF)
            self.state = 126
            self.condition()
            self.state = 127
            self.match(WorkflowParser.THEN)
            self.state = 128
            self.match(WorkflowParser.LBRACE)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 5116) != 0):
                self.state = 129
                self.statement()
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 135
            self.match(WorkflowParser.RBRACE)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 136
                self.match(WorkflowParser.ELSE)
                self.state = 137
                self.match(WorkflowParser.LBRACE)
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 5116) != 0):
                    self.state = 138
                    self.statement()
                    self.state = 143
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 144
                self.match(WorkflowParser.RBRACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WorkflowParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(WorkflowParser.ExpressionContext,i)


        def LOGICAL_OP(self, i:int=None):
            if i is None:
                return self.getTokens(WorkflowParser.LOGICAL_OP)
            else:
                return self.getToken(WorkflowParser.LOGICAL_OP, i)

        def getRuleIndex(self):
            return WorkflowParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = WorkflowParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.expression()
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 148
                self.match(WorkflowParser.LOGICAL_OP)
                self.state = 149
                self.expression()
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field(self):
            return self.getTypedRuleContext(WorkflowParser.FieldContext,0)


        def COMPARISON(self):
            return self.getToken(WorkflowParser.COMPARISON, 0)

        def value(self):
            return self.getTypedRuleContext(WorkflowParser.ValueContext,0)


        def LPAREN(self):
            return self.getToken(WorkflowParser.LPAREN, 0)

        def condition(self):
            return self.getTypedRuleContext(WorkflowParser.ConditionContext,0)


        def RPAREN(self):
            return self.getToken(WorkflowParser.RPAREN, 0)

        def getRuleIndex(self):
            return WorkflowParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = WorkflowParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expression)
        try:
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.field()
                self.state = 156
                self.match(WorkflowParser.COMPARISON)
                self.state = 157
                self.value()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.match(WorkflowParser.LPAREN)
                self.state = 160
                self.condition()
                self.state = 161
                self.match(WorkflowParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldAssign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WorkflowParser.FieldAssignContext)
            else:
                return self.getTypedRuleContext(WorkflowParser.FieldAssignContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(WorkflowParser.COMMA)
            else:
                return self.getToken(WorkflowParser.COMMA, i)

        def getRuleIndex(self):
            return WorkflowParser.RULE_fieldList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldList" ):
                listener.enterFieldList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldList" ):
                listener.exitFieldList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldList" ):
                return visitor.visitFieldList(self)
            else:
                return visitor.visitChildren(self)




    def fieldList(self):

        localctx = WorkflowParser.FieldListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_fieldList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.fieldAssign()
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 166
                self.match(WorkflowParser.COMMA)
                self.state = 167
                self.fieldAssign()
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field(self):
            return self.getTypedRuleContext(WorkflowParser.FieldContext,0)


        def EQ(self):
            return self.getToken(WorkflowParser.EQ, 0)

        def value(self):
            return self.getTypedRuleContext(WorkflowParser.ValueContext,0)


        def getRuleIndex(self):
            return WorkflowParser.RULE_fieldAssign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldAssign" ):
                listener.enterFieldAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldAssign" ):
                listener.exitFieldAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldAssign" ):
                return visitor.visitFieldAssign(self)
            else:
                return visitor.visitChildren(self)




    def fieldAssign(self):

        localctx = WorkflowParser.FieldAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_fieldAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.field()
            self.state = 174
            self.match(WorkflowParser.EQ)
            self.state = 175
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramAssign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WorkflowParser.ParamAssignContext)
            else:
                return self.getTypedRuleContext(WorkflowParser.ParamAssignContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(WorkflowParser.COMMA)
            else:
                return self.getToken(WorkflowParser.COMMA, i)

        def getRuleIndex(self):
            return WorkflowParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = WorkflowParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.paramAssign()
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 178
                self.match(WorkflowParser.COMMA)
                self.state = 179
                self.paramAssign()
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(WorkflowParser.ID, 0)

        def EQ(self):
            return self.getToken(WorkflowParser.EQ, 0)

        def value(self):
            return self.getTypedRuleContext(WorkflowParser.ValueContext,0)


        def getRuleIndex(self):
            return WorkflowParser.RULE_paramAssign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamAssign" ):
                listener.enterParamAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamAssign" ):
                listener.exitParamAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamAssign" ):
                return visitor.visitParamAssign(self)
            else:
                return visitor.visitChildren(self)




    def paramAssign(self):

        localctx = WorkflowParser.ParamAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_paramAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(WorkflowParser.ID)
            self.state = 186
            self.match(WorkflowParser.EQ)
            self.state = 187
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(WorkflowParser.ID)
            else:
                return self.getToken(WorkflowParser.ID, i)

        def getRuleIndex(self):
            return WorkflowParser.RULE_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField" ):
                listener.enterField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField" ):
                listener.exitField(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField" ):
                return visitor.visitField(self)
            else:
                return visitor.visitChildren(self)




    def field(self):

        localctx = WorkflowParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(WorkflowParser.ID)
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 190
                self.match(WorkflowParser.T__0)
                self.state = 191
                self.match(WorkflowParser.ID)
                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(WorkflowParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(WorkflowParser.NUMBER, 0)

        def DATE(self):
            return self.getToken(WorkflowParser.DATE, 0)

        def TRUE(self):
            return self.getToken(WorkflowParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(WorkflowParser.FALSE, 0)

        def getRuleIndex(self):
            return WorkflowParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = WorkflowParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 59113472) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





