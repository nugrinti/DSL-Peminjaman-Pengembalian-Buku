# workflow_error.py
from antlr4.error.ErrorListener import ErrorListener

class WorkflowErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, col, msg, e):
        raise Exception(f"[Syntax Error] line {line}:{col} → {msg}")

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        print(f"[Ambiguity Warning] tokens {startIndex}-{stopIndex}")

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        print("[Warning] Attempting full context analysis")

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        print("[Warning] Context sensitivity detected")
