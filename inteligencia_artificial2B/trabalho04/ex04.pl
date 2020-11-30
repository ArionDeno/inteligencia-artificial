%EX04
% copiar uma lista e ordenar 

list1([3,2,1,4,5,6])
list2([7,9,8,10])

% predicados
organiza_lista(H|L,X).
insere_lista(E,L,S).
ordenada([], Z).



% regras

insere_lista(E,L,S):-
  E < X, !,
    insere_lista(E,L,S).
  insere_lista(E,L,[E]S).
    

organiza_lista(H|L,X):-
  H <L[X] 
  insere_lista(H,L[X],S).
  


ordenada([], Z):-
  organiza_lista(H|L[X],Z).
  insere_lista(L[X],X,Z).

%----------
ordenada(list1,5).
ordenada(list2,9).






