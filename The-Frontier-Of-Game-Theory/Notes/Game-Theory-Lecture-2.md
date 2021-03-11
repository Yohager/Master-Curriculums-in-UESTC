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

(Three periods) P1 and P2 bargin for a pie for three steps. 

trigger strategy

folk 