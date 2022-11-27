begin_problem(fisa).

list_of_descriptions.
name({*Pelletier's Problem No. 54*}).
author({*Christoph Weidenbach*}).
status(unsatisfiable).
description({*Problem taken in revised form from the "Pelletier Collection", Journal of Automated
	Reasoning, Vol. 2, No. 2, pages 191-216*}).
end_of_list.

list_of_symbols.
functions[
(message,0),(none,0),(yes,0),(no,0),
(electronic,0),(mechanical,0),(otherSurv,0),
(wire,0),(radio,0),
(sender,0),(receiver,0),(usa,0),
(targetPerson,0)
].
predicates[
(formAcqu,2),
(form,2),
(sentBy,2),(nationality,2),(location,2),(receivedBy,2),
(target,2),(privacy,2),(needWarrant,2),
(formAcquSurv,1),(formSurv,1),(formSendReceive,1),(formTarget,1),
(electronicSurv,1)
].
end_of_list.

list_of_formulae(axioms).
formula(forall([X],implies(or(formAcqu(X,electronic),or(formAcqu(X,mechanical),formAcqu(X,otherSurv))),formAcquSurv(X)))).
formula(forall([X],implies(or(form(X,wire),form(X,radio)),formSurv(X)))).
formula(forall([X],implies(or(and(nationality(sender,usa),location(sender,usa)),and(nationality(receiver,usa),location(receiver,usa))),formSendReceive(X)))).
formula(forall([X],implies(and(needWarrant(targetPerson,yes),and(privacy(targetPerson,yes),and(target(message,targetPerson),nationality(targetPerson,usa)))),formTarget(X)))).


formula(formAcqu(message,otherSurv)).
formula(form(message,wire)).
formula(nationality(sender,usa)).
formula(location(sender,usa)).
formula(nationality(receiver,none)).
formula(location(receiver,none)).
formula(target(message,targetPerson)).
formula(nationality(targetPerson,usa)).
formula(privacy(targetPerson,yes)).
formula(needWarrant(targetPerson,no)).



formula(sentBy(message,sender)).
formula(receivedBy(message,receiver)).
formula(forall([X],implies(and(formTarget(X),and(formSendReceive(X),and(formAcquSurv(X),formSurv(X)))),electronicSurv(X)))).
end_of_list.


list_of_formulae(conjectures).
formula(exists([X],electronicSurv(X))).
end_of_list.


list_of_settings(SPASS).
{*
set_flag(PGiven,1).
set_flag(PProblem,0).
*}
end_of_list.

end_problem.