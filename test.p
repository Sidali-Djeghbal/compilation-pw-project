programme ComprehensiveTest ;

reel X = 1.24 ; test = 100 ; variablle = 50 ;

variable A, B, C: entier; X: reel; I: entier;

debut
    A := -(B + 5) * C + X / (2.0 - PI) ;
    si A < X alors
        B := B + 1; 
    sinon B := 0;

    tantque A >= 0 faire
        debut 
            A := A - 1 ;
            C := A mod 2 ;
        fin;
    
    repeter X := X * 1.05 ;
    jusqu'a X >= LIMIT;
    
    pour I allant de 1 a LIMIT pas TEXTE faire
    A := A + I;
    A := (B div C) et 1;
fin.