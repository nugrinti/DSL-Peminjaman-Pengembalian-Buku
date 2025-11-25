# Generated from Workflow.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .WorkflowParser import WorkflowParser
else:
    from WorkflowParser import WorkflowParser

# This class defines a complete generic visitor for a parse tree produced by WorkflowParser.

class WorkflowVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by WorkflowParser#program.
    def visitProgram(self, ctx:WorkflowParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowParser#statement.
    def visitStatement(self, ctx:WorkflowParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowParser#defineStmt.
    def visitDefineStmt(self, ctx:WorkflowParser.DefineStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowParser#txnStmt.
    def visitTxnStmt(self, ctx:WorkflowParser.TxnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowParser#action.
    def visitAction(self, ctx:WorkflowParser.ActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowParser#target.
    def visitTarget(self, ctx:WorkflowParser.TargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowParser#updateStmt.
    def visitUpdateStmt(self, ctx:WorkflowParser.UpdateStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowParser#queryStmt.
    def visitQueryStmt(self, ctx:WorkflowParser.QueryStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowParser#selectClause.
    def visitSelectClause(self, ctx:WorkflowParser.SelectClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowParser#selectFields.
    def visitSelectFields(self, ctx:WorkflowParser.SelectFieldsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowParser#whereClause.
    def visitWhereClause(self, ctx:WorkflowParser.WhereClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowParser#ifStmt.
    def visitIfStmt(self, ctx:WorkflowParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowParser#condition.
    def visitCondition(self, ctx:WorkflowParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowParser#expression.
    def visitExpression(self, ctx:WorkflowParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowParser#fieldList.
    def visitFieldList(self, ctx:WorkflowParser.FieldListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowParser#fieldAssign.
    def visitFieldAssign(self, ctx:WorkflowParser.FieldAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowParser#paramList.
    def visitParamList(self, ctx:WorkflowParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowParser#paramAssign.
    def visitParamAssign(self, ctx:WorkflowParser.ParamAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowParser#field.
    def visitField(self, ctx:WorkflowParser.FieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WorkflowParser#value.
    def visitValue(self, ctx:WorkflowParser.ValueContext):
        return self.visitChildren(ctx)



del WorkflowParser