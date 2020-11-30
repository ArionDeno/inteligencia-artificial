% ex03 
% inserir elemento e ordenar na lista

% lista
list([1,2,3,4,5,6,7,8])


% predicado

insercao_ord(X,[],[X]).

insercao_ord(E,X|Y],[X,E,Y]) :-

% comparacao
  not( E > X),
  insercao_ord(E,Y,L).
  