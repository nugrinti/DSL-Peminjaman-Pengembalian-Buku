grammar Workflow;

// ------------------------------------
// PROGRAM
// ------------------------------------
program
    : statement* EOF
    ;

statement
    : defineStmt SEMICOLON
    | txnStmt SEMICOLON
    | updateStmt SEMICOLON
    | queryStmt SEMICOLON
    | ifStmt
    ;

// ------------------------------------
// DEFINITIONS
// ------------------------------------
defineStmt
    : DEFINE ID ITEM_ID LBRACE fieldList? RBRACE        // define book B-123 { ... }
    | DEFINE MEMBER_ID LBRACE fieldList? RBRACE         // define A001 { ... }
    ;

// ------------------------------------
// TRANSACTIONS
// ------------------------------------
txnStmt
    : action target (WITH paramList)?
    ;

action
    : BORROW
    | RETURN
    | RESERVE
    | EXTEND
    | MARK_LOST
    ;

target
    : ID ITEM_ID                     // book B-123
    | MEMBER_ID ARROW ID ITEM_ID     // A001 -> book B-123
    ;

// ------------------------------------
// UPDATE
// ------------------------------------
updateStmt
    : UPDATE target SET fieldList
    ;

// ------------------------------------
// QUERY
// ------------------------------------
queryStmt
    : QUERY (selectClause)? whereClause?
    ;

selectClause
    : SELECT selectFields
    ;

selectFields
    : STAR
    | field (COMMA field)*
    ;

whereClause
    : WHERE condition
    ;

// ------------------------------------
// IF
// ------------------------------------
ifStmt
    : IF condition THEN LBRACE statement* RBRACE
      (ELSE LBRACE statement* RBRACE)?
    ;

// ------------------------------------
// CONDITIONS
// ------------------------------------
condition
    : expression (LOGICAL_OP expression)*
    ;

expression
    : field COMPARISON value
    | LPAREN condition RPAREN
    ;

// ------------------------------------
// FIELD ASSIGNMENT
// ------------------------------------
fieldList
    : fieldAssign (COMMA fieldAssign)*
    ;

fieldAssign
    : field EQ value
    ;

paramList
    : paramAssign (COMMA paramAssign)*
    ;

paramAssign
    : ID EQ value
    ;

// ====================================
// LEXER RULES
// ====================================

// Keywords (must be above ID)
BORROW      : 'borrow';
RETURN      : 'return';
RESERVE     : 'reserve';
EXTEND      : 'extend';
MARK_LOST   : 'mark_lost' | 'lost';
DEFINE      : 'define';
UPDATE      : 'update';
QUERY       : 'query';
SELECT      : 'select';
WHERE       : 'where';
IF          : 'if';
THEN        : 'then';
ELSE        : 'else';
WITH        : 'with';
SET         : 'set';

TRUE        : 'true';
FALSE       : 'false';

// Identifiers MUST NOT conflict with keywords
ITEM_ID     : [A-Z][A-Z0-9\-]*;      // B-123
MEMBER_ID   : [A-Z][A-Z0-9_]*;       // A001

COMPARISON  : '==' | '!=' | '<=' | '>=' | '<' | '>';
LOGICAL_OP  : 'and' | 'or';

// Literals
STRING      : '"' (~["\\] | '\\' .)* '"' ;
DATE        : '"' [0-9]{4} '-' [0-9]{2} '-' [0-9]{2} '"' ;
NUMBER      : [0-9]+ ('.' [0-9]+)? ;

// Generic IDs (placed after keywords)
ID          : [a-zA-Z_][a-zA-Z0-9_]* ;

// Fields
field
    : ID ('.' ID)*
    ;

// Value union
value
    : STRING
    | NUMBER
    | DATE
    | TRUE
    | FALSE
    ;

// Comments & whitespace
COMMENT
    : '/*' .*? '*/' -> channel(HIDDEN)
    ;

COMMENT_LINE
    : '//' ~[\r\n]* -> channel(HIDDEN)
    ;

WS
    : [ \t\r\n]+ -> skip
    ;

// Symbols
SEMICOLON   : ';';
COMMA       : ',';
LPAREN      : '(';
RPAREN      : ')';
LBRACE      : '{';
RBRACE      : '}';
ARROW       : '->';
EQ          : '=';
STAR        : '*';
