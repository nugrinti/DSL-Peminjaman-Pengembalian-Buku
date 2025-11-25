# Generated from Workflow.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .WorkflowParser import WorkflowParser
else:
    from WorkflowParser import WorkflowParser

# This class defines a complete listener for a parse tree produced by WorkflowParser.
class WorkflowListener(ParseTreeListener):

    # Enter a parse tree produced by WorkflowParser#program.
    def enterProgram(self, ctx:WorkflowParser.ProgramContext):
        pass

    # Exit a parse tree produced by WorkflowParser#program.
    def exitProgram(self, ctx:WorkflowParser.ProgramContext):
        pass


    # Enter a parse tree produced by WorkflowParser#statement.
    def enterStatement(self, ctx:WorkflowParser.StatementContext):
        pass

    # Exit a parse tree produced by WorkflowParser#statement.
    def exitStatement(self, ctx:WorkflowParser.StatementContext):
        pass


    # Enter a parse tree produced by WorkflowParser#defineStmt.
    def enterDefineStmt(self, ctx:WorkflowParser.DefineStmtContext):
        pass

    # Exit a parse tree produced by WorkflowParser#defineStmt.
    def exitDefineStmt(self, ctx:WorkflowParser.DefineStmtContext):
        pass


    # Enter a parse tree produced by WorkflowParser#txnStmt.
    def enterTxnStmt(self, ctx:WorkflowParser.TxnStmtContext):
        pass

    # Exit a parse tree produced by WorkflowParser#txnStmt.
    def exitTxnStmt(self, ctx:WorkflowParser.TxnStmtContext):
        pass


    # Enter a parse tree produced by WorkflowParser#action.
    def enterAction(self, ctx:WorkflowParser.ActionContext):
        pass

    # Exit a parse tree produced by WorkflowParser#action.
    def exitAction(self, ctx:WorkflowParser.ActionContext):
        pass


    # Enter a parse tree produced by WorkflowParser#target.
    def enterTarget(self, ctx:WorkflowParser.TargetContext):
        pass

    # Exit a parse tree produced by WorkflowParser#target.
    def exitTarget(self, ctx:WorkflowParser.TargetContext):
        pass


    # Enter a parse tree produced by WorkflowParser#updateStmt.
    def enterUpdateStmt(self, ctx:WorkflowParser.UpdateStmtContext):
        pass

    # Exit a parse tree produced by WorkflowParser#updateStmt.
    def exitUpdateStmt(self, ctx:WorkflowParser.UpdateStmtContext):
        pass


    # Enter a parse tree produced by WorkflowParser#queryStmt.
    def enterQueryStmt(self, ctx:WorkflowParser.QueryStmtContext):
        pass

    # Exit a parse tree produced by WorkflowParser#queryStmt.
    def exitQueryStmt(self, ctx:WorkflowParser.QueryStmtContext):
        pass


    # Enter a parse tree produced by WorkflowParser#selectClause.
    def enterSelectClause(self, ctx:WorkflowParser.SelectClauseContext):
        pass

    # Exit a parse tree produced by WorkflowParser#selectClause.
    def exitSelectClause(self, ctx:WorkflowParser.SelectClauseContext):
        pass


    # Enter a parse tree produced by WorkflowParser#selectFields.
    def enterSelectFields(self, ctx:WorkflowParser.SelectFieldsContext):
        pass

    # Exit a parse tree produced by WorkflowParser#selectFields.
    def exitSelectFields(self, ctx:WorkflowParser.SelectFieldsContext):
        pass


    # Enter a parse tree produced by WorkflowParser#whereClause.
    def enterWhereClause(self, ctx:WorkflowParser.WhereClauseContext):
        pass

    # Exit a parse tree produced by WorkflowParser#whereClause.
    def exitWhereClause(self, ctx:WorkflowParser.WhereClauseContext):
        pass


    # Enter a parse tree produced by WorkflowParser#ifStmt.
    def enterIfStmt(self, ctx:WorkflowParser.IfStmtContext):
        pass

    # Exit a parse tree produced by WorkflowParser#ifStmt.
    def exitIfStmt(self, ctx:WorkflowParser.IfStmtContext):
        pass


    # Enter a parse tree produced by WorkflowParser#condition.
    def enterCondition(self, ctx:WorkflowParser.ConditionContext):
        pass

    # Exit a parse tree produced by WorkflowParser#condition.
    def exitCondition(self, ctx:WorkflowParser.ConditionContext):
        pass


    # Enter a parse tree produced by WorkflowParser#expression.
    def enterExpression(self, ctx:WorkflowParser.ExpressionContext):
        pass

    # Exit a parse tree produced by WorkflowParser#expression.
    def exitExpression(self, ctx:WorkflowParser.ExpressionContext):
        pass


    # Enter a parse tree produced by WorkflowParser#fieldList.
    def enterFieldList(self, ctx:WorkflowParser.FieldListContext):
        pass

    # Exit a parse tree produced by WorkflowParser#fieldList.
    def exitFieldList(self, ctx:WorkflowParser.FieldListContext):
        pass


    # Enter a parse tree produced by WorkflowParser#fieldAssign.
    def enterFieldAssign(self, ctx:WorkflowParser.FieldAssignContext):
        pass

    # Exit a parse tree produced by WorkflowParser#fieldAssign.
    def exitFieldAssign(self, ctx:WorkflowParser.FieldAssignContext):
        pass


    # Enter a parse tree produced by WorkflowParser#paramList.
    def enterParamList(self, ctx:WorkflowParser.ParamListContext):
        pass

    # Exit a parse tree produced by WorkflowParser#paramList.
    def exitParamList(self, ctx:WorkflowParser.ParamListContext):
        pass


    # Enter a parse tree produced by WorkflowParser#paramAssign.
    def enterParamAssign(self, ctx:WorkflowParser.ParamAssignContext):
        pass

    # Exit a parse tree produced by WorkflowParser#paramAssign.
    def exitParamAssign(self, ctx:WorkflowParser.ParamAssignContext):
        pass


    # Enter a parse tree produced by WorkflowParser#field.
    def enterField(self, ctx:WorkflowParser.FieldContext):
        pass

    # Exit a parse tree produced by WorkflowParser#field.
    def exitField(self, ctx:WorkflowParser.FieldContext):
        pass


    # Enter a parse tree produced by WorkflowParser#value.
    def enterValue(self, ctx:WorkflowParser.ValueContext):
        pass

    # Exit a parse tree produced by WorkflowParser#value.
    def exitValue(self, ctx:WorkflowParser.ValueContext):
        pass



del WorkflowParser