### Game Theory - Lecture 2

---

#### Dynamic Games of Complete Information (Extension-Form Games)

**Two cases: **

**dynamic games with perfect information**

**dynamic games with imperfect information**

##### Toy Example:

<img src="..\Pictures\l1-5.png" style="zoom:50%;" />

When considering static-form game, there exist two NEs: $(\bar{E},F),(E,\bar{F})$. 

However $(\bar{E},F)$ is a threat strategy, thus **Backward-Induction Outcome** is going to be introduced next.

Algorithm steps:

- start with the last players and choose their actions that maximize payoff.
- Turn to the second-to-last players, fix the first step choice and decide second-to-last players' choices that maximize their utilities.
- Repeat this procedure iteratively until the beginning of the game.

**[Example 1]** Centipede game:

<img src="..\Pictures\l1-6.png" style="zoom:50%;" />

When using the backward-induction outcome, we can get the results:
$$
s_6\to s_5\to s_4\to s_3\to s_2\to s_1
$$
<font color=red>Consider a question: Whether there exist a Nash Equilibrium in which P1 chooses c1?</font>

My answer is: there will be no NE that player 1 chooses c1. Notice that there are many NEs in this game but in all of them, player 1 will choose s1. 



**[A new question]**: consider a game where 2 players and 3 rounds,  construct a situation where BIO stops at first step: p1 chooses s1 and there exist a NE where stops at 3 step and both p1 and p2 choose c1,c2,c3. Also consider a reverse version?



**[Example 2]** Stackelberg Duopoly 

Two players: firm1 and firm2

firm1 first chooses a $q_1$ and then firm2 chooses a $q_2$.

payoff function is:
$$
\pi_i(q_i,q_j)=(a-q_1-q_2)q_i -cq_i
$$
Note here this game's game tree looks like this:

<img src="..\Pictures\l2-2.png" style="zoom:60%;" />

Using backwards induction and FOC we can get the final result of NE:
$$
q_1^\ast=\frac{a-c}{2},\quad q_2^\ast=\frac{a-c}{4}
$$

##### Extensive-Form Representation

- players in the game
- each player takes turns to move (note that each player can do at each opportunities and they know these opportunities)
- payoff received by each player for each combination of moves

**Information Set**: a collection of decision nodes (player must have the same set of feasible actions at each decision node in an information set)

Game with perfect information: every information set is a singleton.

Game with imperfect information: at least one non-singleton information set

A static game can be represented in extensive form like this:

The Prisoner's Dilemma

<img src="..\Pictures\l2-3.png" style="zoom:50%;" />

Extensive Form Game Tree:

<img src="..\Pictures\l2-4.png" style="zoom:67%;" />

Note the information set of p2 is non-singleton, she only knows p1 has two choice but does not know which p1 takes first. So at the second step, p2's action is consistent whether p1 confesses or not. 

<font color=red>Vital difference between action and strategy</font>

A strategy for a player can be seen as a complete plan of actions, a function which assigns an action to each information set belonging to the player.

(E.g., if a player has two information set and in each she has $m_1$ and $m_2$ feasible actions respectively, her strategies space is $m_1\times m_2$.)

**[Example 3]** Sequential Bargaining 

(One period) P1 and P2 bargain for a pie, P1 first proposes a share $s_1$， leaving $1-s_1$ for P2. P2 chooses either accept or reject.

**[Solution]**: Using Backward-Induction, we can see P2's best response is accept since once $s_1< 1$, P2 will get a non-negative payoff, and thus P1's best response is $s_1^\ast=1$ (when $s_1=1$, P2's payoff is always zero whether she accept or not). 

Consider NE in this game:

For $s_1^0\in [0,1]$, $(s_1^0,s_2^0=\begin{cases}accept &s_1=s_1^0\\ reject &s_1\neq s_1^0\end{cases})$ is NE.

There are infinite NE in this game, note that the description for agents' strategies must be clear.

Consider SPNE in this game:

$(s_1^\ast=1,s_2^\ast(s_1)=accept, \, s_1\in[0,1])$.

There is only one SPNE in this game.

<font color=red>Relationship between NE and SPNE:</font> Every SPNE is a NE, the reverse not true. A strategy profile that induces a NE in every subgame is a SPNE. 

Back to this bargain with one period, we can find that if $s_1<1$, P2's optimal action is to accept and accept or reject if $s_1=1$. If P2's strategy is to accept all offers and P1's best response is $s_1=1$, if P2's strategy is to reject if $s_1=1$, then P1 has no best choice. 

(Three periods) P1 and P2 bargain for a pie for three steps. 

<img src="..\Pictures\l2-5.png" style="zoom:67%;" />

 Model is like this, consider using BIO, we can find that P2 should choose $s_2$ satisfying $\delta s_2\geq \delta^2 s$. Then P1 should choose $s_1$ satisfying $1-s_1\geq \delta(1-\delta s)$ so that P2 will accept in period 1.

So the BIO is: $(1-\delta(1-\delta s),\delta(1-\delta s))$.

##### Rubinstein's Alternating-Offer Model

This bargain changes to finite periods, payoff functions: $(\delta^{K-1}s_k,\delta^{K-1}(1-s_K))$.

When it comes to infinite-period, assume the BIO is $(s,1-s)$, this game is a 2-period stationary , subgame starting in period 3 is exactly in period 1. In period 3 case P1 will offer $(f(s),1-f(s))$ in the first period. If the BIO is unique, then there must be a unique value $s^\ast$ which satisfy $f(s)=s$ (the fix-point).  $s^\ast=\frac{1}{1+\delta}$.

So in infinite period model, the BIO result is $(s^\ast,1-s^\ast)=(\frac{1}{1+\delta},\frac{\delta}{1+\delta})$.

##### Repeated Games

A repeated game is a dynamic game in which the same static game is played at every stage.

Folk Theorem: the cooperative outcomes of stage game $G$ can be supported by the SPNE outcomes of its repeated game $G^\infty$.

**Proposition**: If the stage game has a unique NE, then the finitely repeated game has a unique SPNE: the NE of the stage game is played in every stage.

When the stage game has more than one NE:

**[Example]** Prisoners' Dilemma:

<img src="..\Pictures\l2-6.png" style="zoom:67%;" />

Two NE in this stage game: (C,C) and (A,A).

There is a subgame-perfect outcome in this repeated game, first stage is (D,D) and then (A,A); if the first stage game result is not (D,D), then (C,C). 

**Infinitely repeated games**: 

Consider infinitely repeated Prisoners' dilemma

- There is a SPNE outcome in which both players play the non-cooperative strategy $C$.
- When the $\delta$ is big enough, there exist another SPNE outcome where two players choose to cooperate, considering the following trigger strategy: Play $D$ in the first stage, in the t-th stage, if the outcome of all $t-1$ stages has been $(D,D)$, then play D, otherwise play $C$. (If both take this trigger strategy, then the cooperative outcome $(D,D)$ happens in every stage)

We can calculate the threshold value of $\delta$:

Someone deviates:
$$
5+\delta\cdot 1+\delta^2\cdot 1+\cdots=5+\frac{\delta}{1-\delta}
$$
Nobody deviates:
$$
4(1+\delta+\delta^2+\cdots)=\frac{4}{1-\delta}
$$
Note the common infinite series equation:  <font color=red>$\sum_{n=0}^\infty x^n=\frac{1}{1-x}$</font>
$$
\frac{4}{1-\delta} \geq 5+\frac{\delta}{1-\delta}\Leftrightarrow\delta \geq \frac{1}{4}
$$

##### Folk Theorem

> $(e_1,\cdots,e_n)$ denote the payoffs from a NE of stage game $G$, $(x_1,\cdots,x_n)$ denote any other feasible payoffs from $G$. If $x_i> e_i$ for every $i$ and if discount rate $\delta$ is sufficiently close to one, then there exists a SPNE of infinitely repeated game $G(\infty,\delta)$ that achieves $(x_1,\cdots,x_n)$ as the average payoff.