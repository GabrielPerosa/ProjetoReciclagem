```
IF #liga = TRUE THEN
    #memoria := 1;
    #led_liga := 1;
END_IF;
IF #memoria = TRUE THEN
    #esteira := 1;
END_IF;

IF #desliga = FALSE THEN
    #esteira := 0;
    #atuador1 := 0;
    #atuador2 := 0;
    #esteira_atuador1 := 0;
    #esteira_atuador2 := 0;
    #led_desliga := 1;
    #memoria := 0;
END_IF;
IF #sensor_capacitivo = TRUE THEN
    #memoria_1 := 1;
END_IF;

IF #memoria_1 = TRUE THEN
    #esteira_atuador1 := 1;
    
END_IF;
"IEC_Timer_0_DB_1".TON(IN:=#memoria_1,
                       PT:=t#2s,
                       Q=>#atuador1);

IF #sensor_indutivo = TRUE THEN
    #atuador2 := 1;
    #esteira_atuador2 := 1;
    #memoria_1 := 0;
END_IF;

IF #optico_esteira_final = TRUE THEN
    #esteira := 0;
    #memoria_1 := 0;
    #esteira_atuador1 := 0;
    #atuador2 := 0;
    #esteira_atuador2 := 0;
END_IF;

IF #optico_rampa1 = TRUE THEN
    #atuador1 := 0;
    #esteira_atuador1 := 0;
    #memoria_1 := 0;
END_IF;

IF #optico_rampa2 = TRUE THEN
    #atuador2 := 0;
    #esteira_atuador2 := 0;
END_IF;

IF #optico_altura = TRUE THEN
    #memoria_1 := 0;
    #esteira_atuador1 := 0;
    #atuador2 := 0;
    #esteira_atuador2 := 0;
END_IF
```