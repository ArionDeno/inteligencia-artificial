% EX 02
% juntar duas listas em uma terceira


% listas 
lst1([f,b,c,g,h,j,d,m.n.p,l,]).
lst2([a,e,i,o,u,y]).

intercal([],L,L).
intercal(L,[],L).

intercal([C|H],C2|R2,[C1,C2|R3]):-
  intercal(R1,R2,R3).



