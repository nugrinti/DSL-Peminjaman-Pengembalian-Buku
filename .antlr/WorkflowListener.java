// Generated from c:/Users/Hp/OneDrive/Dokumen/GitHub/DSL-Peminjaman-Pengembalian-Buku/Workflow.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link WorkflowParser}.
 */
public interface WorkflowListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link WorkflowParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(WorkflowParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link WorkflowParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(WorkflowParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link WorkflowParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(WorkflowParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link WorkflowParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(WorkflowParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link WorkflowParser#defineStmt}.
	 * @param ctx the parse tree
	 */
	void enterDefineStmt(WorkflowParser.DefineStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link WorkflowParser#defineStmt}.
	 * @param ctx the parse tree
	 */
	void exitDefineStmt(WorkflowParser.DefineStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link WorkflowParser#txnStmt}.
	 * @param ctx the parse tree
	 */
	void enterTxnStmt(WorkflowParser.TxnStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link WorkflowParser#txnStmt}.
	 * @param ctx the parse tree
	 */
	void exitTxnStmt(WorkflowParser.TxnStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link WorkflowParser#action}.
	 * @param ctx the parse tree
	 */
	void enterAction(WorkflowParser.ActionContext ctx);
	/**
	 * Exit a parse tree produced by {@link WorkflowParser#action}.
	 * @param ctx the parse tree
	 */
	void exitAction(WorkflowParser.ActionContext ctx);
	/**
	 * Enter a parse tree produced by {@link WorkflowParser#target}.
	 * @param ctx the parse tree
	 */
	void enterTarget(WorkflowParser.TargetContext ctx);
	/**
	 * Exit a parse tree produced by {@link WorkflowParser#target}.
	 * @param ctx the parse tree
	 */
	void exitTarget(WorkflowParser.TargetContext ctx);
	/**
	 * Enter a parse tree produced by {@link WorkflowParser#updateStmt}.
	 * @param ctx the parse tree
	 */
	void enterUpdateStmt(WorkflowParser.UpdateStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link WorkflowParser#updateStmt}.
	 * @param ctx the parse tree
	 */
	void exitUpdateStmt(WorkflowParser.UpdateStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link WorkflowParser#queryStmt}.
	 * @param ctx the parse tree
	 */
	void enterQueryStmt(WorkflowParser.QueryStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link WorkflowParser#queryStmt}.
	 * @param ctx the parse tree
	 */
	void exitQueryStmt(WorkflowParser.QueryStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link WorkflowParser#selectClause}.
	 * @param ctx the parse tree
	 */
	void enterSelectClause(WorkflowParser.SelectClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link WorkflowParser#selectClause}.
	 * @param ctx the parse tree
	 */
	void exitSelectClause(WorkflowParser.SelectClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link WorkflowParser#selectFields}.
	 * @param ctx the parse tree
	 */
	void enterSelectFields(WorkflowParser.SelectFieldsContext ctx);
	/**
	 * Exit a parse tree produced by {@link WorkflowParser#selectFields}.
	 * @param ctx the parse tree
	 */
	void exitSelectFields(WorkflowParser.SelectFieldsContext ctx);
	/**
	 * Enter a parse tree produced by {@link WorkflowParser#whereClause}.
	 * @param ctx the parse tree
	 */
	void enterWhereClause(WorkflowParser.WhereClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link WorkflowParser#whereClause}.
	 * @param ctx the parse tree
	 */
	void exitWhereClause(WorkflowParser.WhereClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link WorkflowParser#ifStmt}.
	 * @param ctx the parse tree
	 */
	void enterIfStmt(WorkflowParser.IfStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link WorkflowParser#ifStmt}.
	 * @param ctx the parse tree
	 */
	void exitIfStmt(WorkflowParser.IfStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link WorkflowParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(WorkflowParser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link WorkflowParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(WorkflowParser.ConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link WorkflowParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(WorkflowParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link WorkflowParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(WorkflowParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link WorkflowParser#fieldList}.
	 * @param ctx the parse tree
	 */
	void enterFieldList(WorkflowParser.FieldListContext ctx);
	/**
	 * Exit a parse tree produced by {@link WorkflowParser#fieldList}.
	 * @param ctx the parse tree
	 */
	void exitFieldList(WorkflowParser.FieldListContext ctx);
	/**
	 * Enter a parse tree produced by {@link WorkflowParser#fieldAssign}.
	 * @param ctx the parse tree
	 */
	void enterFieldAssign(WorkflowParser.FieldAssignContext ctx);
	/**
	 * Exit a parse tree produced by {@link WorkflowParser#fieldAssign}.
	 * @param ctx the parse tree
	 */
	void exitFieldAssign(WorkflowParser.FieldAssignContext ctx);
	/**
	 * Enter a parse tree produced by {@link WorkflowParser#paramList}.
	 * @param ctx the parse tree
	 */
	void enterParamList(WorkflowParser.ParamListContext ctx);
	/**
	 * Exit a parse tree produced by {@link WorkflowParser#paramList}.
	 * @param ctx the parse tree
	 */
	void exitParamList(WorkflowParser.ParamListContext ctx);
	/**
	 * Enter a parse tree produced by {@link WorkflowParser#paramAssign}.
	 * @param ctx the parse tree
	 */
	void enterParamAssign(WorkflowParser.ParamAssignContext ctx);
	/**
	 * Exit a parse tree produced by {@link WorkflowParser#paramAssign}.
	 * @param ctx the parse tree
	 */
	void exitParamAssign(WorkflowParser.ParamAssignContext ctx);
	/**
	 * Enter a parse tree produced by {@link WorkflowParser#field}.
	 * @param ctx the parse tree
	 */
	void enterField(WorkflowParser.FieldContext ctx);
	/**
	 * Exit a parse tree produced by {@link WorkflowParser#field}.
	 * @param ctx the parse tree
	 */
	void exitField(WorkflowParser.FieldContext ctx);
	/**
	 * Enter a parse tree produced by {@link WorkflowParser#value}.
	 * @param ctx the parse tree
	 */
	void enterValue(WorkflowParser.ValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link WorkflowParser#value}.
	 * @param ctx the parse tree
	 */
	void exitValue(WorkflowParser.ValueContext ctx);
}