
def valor_deuda(contrato:str,valor1:float,valor2:float,valor3:float,valor4:float,valor5:float,valor6:float,Tasa_cambio:float)->str:
    ValorTotal1 = ((valor1)+(valor1*0.05))
    ValorTotal2 = ((valor2)+(valor2*0.05))
    ValorTotal3 = ((valor3)+(valor3*0.05))
    ValorTotal4 = ((valor4)+(valor4*0.05))
    ValorTotal5 = ((valor5)+(valor5*0.05))
    ValorTotal6 = ((valor6)+(valor6*0.05))
    ValorTotal =ValorTotal1+ValorTotal2+ValorTotal3+ValorTotal4+ValorTotal5+ValorTotal6
    ValorCambio = ValorTotal/Tasa_cambio
    ValorTotal=round(ValorTotal,2)
    ValorCambio=round(ValorCambio,2)
    return ("El contrato {} adeuda un valor de: ${} COP y un valor ${} USD".format(contrato,ValorTotal,ValorCambio))



