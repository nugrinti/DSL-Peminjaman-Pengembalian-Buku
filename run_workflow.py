from antlr4 import *
from WorkflowLexer import WorkflowLexer
from WorkflowParser import WorkflowParser
from WorkflowVisitor import WorkflowVisitor
from workflow_error import WorkflowErrorListener 


class WorkflowExecutor(WorkflowVisitor):

    # -------------------------
    # PROGRAM
    # -------------------------
    def visitProgram(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)
        return None

    # -------------------------
    # DEFINE
    # -------------------------
    def visitDefineStatement(self, ctx):
        print("\n[DEFINE]")

        # Case 1: define <ID> <ITEM_ID> { ... }
        if ctx.defineStmt().ITEM_ID():
            obj = ctx.defineStmt().ID().getText()
            item_id = ctx.defineStmt().ITEM_ID().getText()
            print(f"  Object = {obj}, ID = {item_id}")

        # Case 2: define <MEMBER_ID> { ... }
        elif ctx.defineStmt().MEMBER_ID():
            member_id = ctx.defineStmt().MEMBER_ID().getText()
            print(f"  Member = {member_id}")

        # field list
        fld = ctx.defineStmt().fieldList()
        if fld:
            for assign in fld.fieldAssign():
                key = assign.field().getText()
                val = assign.value().getText()
                print(f"    {key} = {val}")
        return None

    # -------------------------
    # TRANSACTIONS
    # -------------------------
    def visitTxnStatement(self, ctx):
        txn = ctx.txnStmt()

        action = txn.action().getText()
        print(f"\n[TXN] action={action}")

        # Target
        target = txn.target()
        if target.MEMBER_ID():
            member = target.MEMBER_ID().getText()
            obj = target.ID(0).getText()
            iid = target.ITEM_ID().getText()
            print(f"  Target: {member} -> {obj} {iid}")
        else:
            obj = target.ID(0).getText()
            iid = target.ITEM_ID().getText()
            print(f"  Target: {obj} {iid}")

        # WITH param
        if txn.WITH():
            print("  Params:")
            for p in txn.paramList().paramAssign():
                print(f"    {p.ID().getText()} = {p.value().getText()}")
        return None

    # -------------------------
    # UPDATE
    # -------------------------
    def visitUpdateStatement(self, ctx):
        u = ctx.updateStmt()

        # target
        target = u.target()
        if target.MEMBER_ID():
            member = target.MEMBER_ID().getText()
            obj = target.ID(0).getText()
            iid = target.ITEM_ID().getText()
            print(f"\n[UPDATE] {member} -> {obj} {iid}")
        else:
            obj = target.ID(0).getText()
            iid = target.ITEM_ID().getText()
            print(f"\n[UPDATE] {obj} {iid}")

        # fields
        for f in u.fieldList().fieldAssign():
            key = f.field().getText()
            val = f.value().getText()
            print(f"    {key} = {val}")
        return None

    # -------------------------
    # QUERY
    # -------------------------
    def visitQueryStatement(self, ctx):
        print("\n[QUERY]")

        q = ctx.queryStmt()

        if q.selectClause():
            print("  SELECT:", q.selectClause().selectFields().getText())

        if q.whereClause():
            print("  WHERE:", q.whereClause().condition().getText())
        return None

    # -------------------------
    # IF
    # -------------------------
    def visitIfStatement(self, ctx):
        i = ctx.ifStmt()
        cond = i.condition().getText()
        print(f"\n[IF] condition: {cond}")

        # THEN block
        print("  THEN:")
        for st in i.statement(0):
            self.visit(st)

        # ELSE block
        if i.ELSE():
            print("  ELSE:")
            for st in i.statement(1):
                self.visit(st)

        return None


# ======================================================
# MAIN RUNNER
# ======================================================
def run_workflow(file_path):
    input_stream = FileStream(file_path)

    lexer = WorkflowLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(WorkflowErrorListener()) 

    tokens = CommonTokenStream(lexer)

    parser = WorkflowParser(tokens)
    parser.removeErrorListeners()
    parser.addErrorListener(WorkflowErrorListener()) #error

    tree = parser.program()

    executor = WorkflowExecutor()
    executor.visit(tree)


# Fix main!
if __name__ == "__main__":
    run_workflow("workflow.kita")
