SETA 2
SETB 15
MOVA 129
MOVB 130
:FOR LOOP
:SAVE VALUES

MOVA 131
MOVB 132
MOVC 133

:INIT
SETA 0
MOVA 134
LDA 129
MOVA 135

:LOOP BODY
LDA 134
LDB 130
ADD
MOVC 134
SETB 1
LDA 135
SUB
JMZ :END
MOVC 135

JMP :LOOP BODY

:END
LDC 134
OUT

LDA 131
LDB 132
LDC 133
HLT