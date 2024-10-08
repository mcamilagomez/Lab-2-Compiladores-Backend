import json
import os
from Graph import Graph
from export_data_to_file import export_to_file
from transitions_to_json import transitions_to_json
from validate_regex import is_simple_regex
from Alphabet_from_regex import Alphabet
from Thompson_Graph import thompson, printgraph
from Transition_table import transition_table
from subset_method import subset_method
from Significant_States_Method import AFD
from test_expression import test
from obj_to_json import generate_emptyjson2, generate_json

def procesar_regex(regex):
    valido = is_simple_regex(regex)
    if valido:
        alfabeto = Alphabet(regex)
        Grafo = thompson(regex)
        TTable= transition_table(Grafo, alfabeto)
        df , T = subset_method(Grafo, alfabeto)
        df2, T2, N = AFD(list(T), Grafo, df)
        exp1='aaa'
        flag, test1 =test(df,exp1)
        jsonR= generate_json(valido,alfabeto, Grafo, TTable, df, T, df2,T2,N)
        jsontest = transitions_to_json(flag, test1)
        export_to_file(jsonR, 'appi1.json')
        export_to_file(jsontest, 'appi2.json')
    else:
        export_to_file(generate_emptyjson2(valido), 'appi1.json')
        
        
def procesar_regex2(regex,cadena):
    valido = is_simple_regex(regex)
    if valido:
        alfabeto = Alphabet(regex)
        Grafo = thompson(regex)
        TTable= transition_table(Grafo, alfabeto)
        df , T = subset_method(Grafo, alfabeto)
        df2, T2, N = AFD(list(T), Grafo, df)
        exp1=cadena
        flag, test1 =test(df,exp1)
        jsonR= generate_json(valido,alfabeto, Grafo, TTable, df, T, df2,T2,N)
        jsontest = transitions_to_json(flag, test1)
        export_to_file(jsonR, 'appi1.json')
        export_to_file(jsontest, 'appi2.json')

def procesar_regex3(regex,cadena):
    valido = is_simple_regex(regex)
    if valido:
        alfabeto = Alphabet(regex)
        Grafo = thompson(regex)
        TTable= transition_table(Grafo, alfabeto)
        df , T = subset_method(Grafo, alfabeto)
        df2, T2, N = AFD(list(T), Grafo, df)
        exp2=cadena
        flag, test1 =test(df2,exp2)
        jsonR= generate_json(valido,alfabeto, Grafo, TTable, df, T, df2,T2,N)
        jsontest = transitions_to_json(flag, test1)
        export_to_file(jsonR, 'appi1.json')
        export_to_file(jsontest, 'appi2.json')