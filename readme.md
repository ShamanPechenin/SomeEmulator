
```
Name    opcode  argument
LDA	000011  xxxxxxxx	load from memory to A
LDB     000101  xxxxxxxx	load from memory to B
LDC     000111  xxxxxxxx        load from memory to C

MOVA	001001	xxxxxxxx	move from A to memory
MOVB	001011	xxxxxxxx	move from B to memory
MOVC	001101	xxxxxxxx	move from C to memory

SETA	001111	xxxxxxxx	set value to A
SETB	010001	xxxxxxxx	set value to B
SETC	010011	xxxxxxxx 	set value to C

ADD     010100                  add A and B save to C
SUB 	010110                  subtract B from A save to C

AND     011000                  A logical AND B save to C
OR      011010                  A logical OR B save to C
XOR     011100                  A logical XOR B save to C
NOT     011110                  A logical NOT save to C

HLT     100000                  halt
OUT     100010                  display C
OUTC    110010                  display C as a ASCII

JMP     100101	xxxxxxxx        unconditional jump to address
JMC     100111	xxxxxxxx        jump to address if carry flag
JMZ     101001	xxxxxxxx        jump to address if zero flag

FLC     101011	0000000x        set value to flag C
FLZ     101101	0000000x        set value to flag Z

GEC     101110                  save value of flag C to A
GEZ     110000                  save value of flag Z to A

```