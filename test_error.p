programme P1TEST ;

reel X2 = 10.24 ; t1 = 100 ; v1 = 50 ;

variable A1, B1, C3: entier; X2: reel; I10: entier;

debut
    A1 := -(B1 + 5) * C3 + X2 div (12.0 - 35.14) ;
    si A1 < X2 alors
        B1 := B1 + 1; 
    sinon B1 := 0;

    tantque A1 >= 0 faire
        debut 
            A1 := A1 - 1 ;
            C3 := A1 mod 2 ;
        fin;
    
    repeter X2 := X2 * 10.05 ;
    jusqu'a X >= X2;
    
    pour I10 allant de 1 a X2 pas T3XT faire

        A1 := A1 + I10;
        X := (B1 div C3) et 1;
fin.