% ex 01 prologo: achar 
%  elementos existente em uma lista
%-----------------------
/*
Lista de diveros elementos alguns repetidos
*/

lista([A,b,c,d,e,f,g,h,i,j,m,n,o,p,k,Z,A,1,B,D,E,F,R,T,1,4,5,8,9,6,3,7,8,9,10,1,212,112,11,a,b,a,c,de,e,zz,Z]).

pertence(X,[C|R]).
 
% predicado
pertence(X,[C|R]):-
  not(X==C),
  pertence(X.R).


% acha elemento
elemt_list(1).
