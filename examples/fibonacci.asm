SETA 1
SETB 0

:LOOP BODY
ADD
JMC :END
OUT
MOVC 64
MOVB 65
LDB 64
LDA 65
JMP :LOOP BODY

:END
HLT