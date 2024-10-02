from Graph import Graph
from validate_regex import is_simple_regex
from Alphabet_from_regex import Alphabet
from Thompson_Graph import thompson, printgraph
from Transition_table import transition_table
from subset_method import subset_method
from Significant_States_Method import AFD
from test_expression import test
regex = 'a*'
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
    print(test(df,exp1))
    print('-----------Probar el AFD optimo con una cadena -------------------')
    exp2=''
    print(test(df2,exp2))