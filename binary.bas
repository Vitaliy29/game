10 PRINT TAB(30);"BINARY"
20 PRINT TAB(15);"CREATIVE COMPUTING  MORRISTOWN NEW JERSEY"
110 B$="01"
120 T0=20
130 PRINT
140 PRINT
150 FOR I=1 TO 10
160 GOSUB 560
170 PRINT "BINARY:";
180 FOR J=1 TO 5
190 PRINT MID$(B$,B(J)+1,1);
200 NEXT J
210 PRINT "     DECIMAL:";
220 INPUT A
230 IF A=D THEN 260
240 PRINT D
250 T0=T0-1
260 PRINT
270 NEXT I
280 PRINT
290 PRINT
300 FOR I=1 TO 10
310 GOSUB 560
320 PRINT "DECIMAL:  ";D;
330 PRINT "     BINARY:   ";
340 I$="00000"
350 INPUT I$
360 IF LEN(I$)> 10 THEN 420
370 I$="00000"+I$
375 I$=RIGHT$(I$,5)
380 FOR J=1 TO 5
390 IF MID$(B$,B(J)+1,1)<>MID$(I$,J,1) THEN 420
400 NEXT J
410 GOTO 480
420 PRINT " ";
430 FOR J=1 TO 5
440 PRINT MID$(B$,B(J)+1,1);
450 NEXT J
460 PRINT
470 T0=T0-1
480 PRINT
490 NEXT I
500 PRINT
510 PRINT
520 PRINT "YOUR SCORE:";INT(T0/.2+.5);"%"
530 PRINT
540 PRINT
550 END
560 D=0
570 FOR J=1 TO 5
580 B(J)=INT(RND(1)+.5)
590 D=D*2+B(J)
600 NEXT J
610 RETURN
620 END