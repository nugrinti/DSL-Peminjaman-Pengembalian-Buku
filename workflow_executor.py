# workflow_executor.py
from WorkflowVisitor import WorkflowVisitor

class WorkflowExecutor(WorkflowVisitor):
    def __init__(self):
        self.objects = {}  # database DSL sederhana

    # ------------ DEFINE ---------------
    def visitDefineStatement(self, ctx):
        obj_type = ctx.ID(0).getText()   # book
        obj_id   = ctx.ID(1).getText()   # B-123

        props = {}
        for fa in ctx.objectBody().fieldAssign():
            key = fa.ID().getText()
            val = fa.STRING().getText().strip('"')
            props[key] = val

        self.objects[obj_id] = props
        print(f"[DEFINE] {obj_type} {obj_id} = {props}")
        return None

    # ------------ BORROW ---------------
    def visitBorrowStatement(self, ctx):
        book_id = ctx.ID().getText()
        due = ctx.STRING().getText().strip('"')

        print(f"[BORROW] Book {book_id} borrowed with due={due}")
        return None

    # ------------ UPDATE ----------------
    def visitUpdateStatement(self, ctx):
        book_id = ctx.ID().getText()
        key = ctx.fieldAssign().ID().getText()
        val = ctx.fieldAssign().STRING().getText().strip('"')

        if book_id in self.objects:
            self.objects[book_id][key] = val

        print(f"[UPDATE] {book_id}.{key} = {val}")
        return None

    # ------------ IF STATEMENT ----------
    def visitIfStatement(self, ctx):
        left = ctx.condition().left.getText()      # book.status
        op   = ctx.condition().op.text            # == or !=
        right = ctx.condition().STRING().getText().strip('"')

        obj_name = left.split('.')[0]  # book
        prop = left.split('.')[1]      # status

        val = None
        for obj_id, props in self.objects.items():
            if prop in props:
                val = props[prop]
                break

        if op == "==":
            cond = (val == right)
        else:
            cond = (val != right)

        print(f"[IF] {left} {op} \"{right}\" → {cond}")

        if cond:
            print("[THEN BLOCK]")
            return self.visit(ctx.block(0))
        else:
            print("[ELSE BLOCK]")
            return self.visit(ctx.block(1))

    # ------------ QUERY -----------------
    def visitQueryStatement(self, ctx):
        select_text = ctx.selectClause().getText()
        where_text  = ctx.whereClause().getText()

        print(f"[QUERY] SELECT {select_text} WHERE {where_text}")
        return None
