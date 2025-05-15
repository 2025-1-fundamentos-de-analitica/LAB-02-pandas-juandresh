"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd

def pregunta_11():
    """
    Construya una tabla que contenga `c0` y una lista separada por ',' de
    los valores de la columna `c4` del archivo `tbl1.tsv`.

    Rta/
         c0       c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    df = pd.read_csv('files/input/tbl1.tsv', sep='\t')

    dic = {}

    for reg in range(len(df)):

        let = df.iloc[reg]['c0']
        num = df.iloc[reg]['c4']

        if let in dic:
            dic[int(let)].append(num)
        else:
            dic[int(let)] = [num]

    dic = sorted(list(dic.items()))

    nums = {cla:','.join(map(str, sorted(tup))) for cla, tup in dic}
    
    resp = pd.DataFrame.from_dict(nums, orient='index', columns=['c4'])
    resp.reset_index(inplace=True)
    resp.columns = ['c0', 'c4']

    return resp