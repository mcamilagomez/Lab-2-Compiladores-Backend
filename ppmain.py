from Graph import Graph
from validate_regex import is_simple_regex
from Alphabet_from_regex import Alphabet
from Thompson_Graph import thompson, printgraph
from Transition_table import transition_table
from subset_method import subset_method
from Significant_States_Method import AFD
from test_expression import test
from obj_to_json import generate_json
from export_data_to_file import export_to_file
from transitions_to_json import transitions_to_json

regex = '(a|b)*ab*b(b|a*)*b*a*'
print(regex)
print('-----------La expresion es valida?-------------------')
valido = is_simple_regex(regex)
print(valido)

if valido:
    print('-----------Alfabeto-------------------')
    alfabeto = Alphabet(regex)
    print(alfabeto)
    print('-----------Grafo de thompson-------------------')
    Grafo = thompson(regex)
    printgraph(Grafo)
    print('-----------Tabla de trasiciones de thompson-------------------')
    TTable= transition_table(Grafo, alfabeto)
    print(transition_table(Grafo, alfabeto))
    print('-----------Tabla del AFD no optimo -------------------')
    df , T = subset_method(Grafo, alfabeto)
    print(df)
    print('-----------Relaci0n de cada Estado del AFD con cada estado del AFN -------------------')
    print(T)
    print('-----------Tabla del AFD optimo -------------------')
    df2, T2, N = AFD(T, Grafo, df)
    print(df2)
    print('-----------Estados significativos de cada estado del AFD optimo-------------------')
    print(T2)
    print('-----------Estados identicos a otros en el AFD optimo-------------------')
    print(N)
    print('-----------Probar el AFD no optimo con una cadena -------------------')
    exp1='aaa'
    flag, test1 =test(df,exp1)
    print(flag, test1)
    print('-----------Probar el AFD optimo con una cadena -------------------')
    exp2=''
    print(test(df2,exp2))
    print('-----------Json -------------------')
    jsonR= generate_json(valido,alfabeto, Grafo, TTable, df, T, df2,T2,N)
    print(jsonR)
    jsontest = transitions_to_json(flag, test1)
    print(jsontest)

export_to_file(jsonR, 'appi1.json')
export_to_file(jsontest, 'appi2.json')
