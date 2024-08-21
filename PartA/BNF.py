expr	    : KEYWORD:VAR IDENTIFIER EQ expr
		    : comp-expr ((KEYWORD:AND|KEYWORD:OR) comp-expr)*

comp-expr	: NOT comp-expr
			: arith-expr ((EE|LT|GT|LTE|GTE) arith-expr)*

arith-expr	: term ((PLUS|MINUS) term)*

term		: factor ((MUL|DIV) factor)*

factor	    : (PLUS|MINUS) factor
			: call

call		: atom (LPAREN (expr (COMMA expr)*)? RPAREN)?

atom 		: INT|IDENTIFIER
			: LPAREN expr RPAREN
			: Defun
            : lambd

Defun		: KEYWORD:Defun IDENTIFIER? LPAREN (IDENTIFIER (COMMA IDENTIFIER)*)? RPAREN ARROW expr

lambd       : KEYWORD:Lambd IDENTIFIER ((COMMA IDENTIFIER)*)? DOT LPREAN expr RPAREN LPREAN NUMBER ((COMMA NUMBER)*)? RPAREN