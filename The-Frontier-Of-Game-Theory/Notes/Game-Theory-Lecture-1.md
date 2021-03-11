### Game Theory - Lecture 1

---

#### Topics

|         | Complete Information          | Incomplete Information         |
| ------- | ----------------------------- | ------------------------------ |
| Static  | Normal-form games (NE)        | Bayesian games (BNE)           |
| Dynamic | PI games (Subgame perfect NE) | II games (Perfect Bayesian NE) |

##### Prisoners' Dilemma

both of two suspects not confessing will get -1 reward but one confess while one not, former gets 0 and later gets -9. both of them confessing will get -6 reward. Without communication, they will betray each other and confess, that is (-6,-6). From a spectator's perspective, they could get higher profit by not confessing. 

#### Normal-Form Games (NE)

##### some concepts: 

**strictly dominated strategies**: 
$$
u_i(s_i',s_{-i})<u_i(s_i'',s_{-i}),\forall s_{-i}\in S_{-i}
$$
**iterated elimination of strictly dominated strategies**

Consider the game:

<img src="F:\UESTC\MasterⅠ(spring)\Curriculums\The-Frontier-of-Game-Theory\Pictures\l1-1.png" alt="example1" style="zoom:50%;" />

For player 2, right is strictly dominated by middle (if P1 plays up, playing middle or right, P2's reward changes from 1 to 0, P1 plays down, that changes from 1 to 0). After eliminating right, game is reduced:

<img src="F:\UESTC\MasterⅠ(spring)\Curriculums\The-Frontier-of-Game-Theory\Pictures\l1-2.png" style="zoom: 50%;" />

For player 1, down is strictly dominated by up:

<img src="F:\UESTC\MasterⅠ(spring)\Curriculums\The-Frontier-of-Game-Theory\Pictures\l1-3.png" alt="example1" style="zoom:70%;" />

After this elimination, player 2 will always play middle rather than left.

<font color=red>It is useful to perform IESDS at first place when analyzing complex games.</font>

##### Relationship between IESDS and Nash Equilibrium

1. A Nash equilibrium survives IESDS.
2. A unique outcome resulting from IESDS is a Nash Equilibrium.

*Proof.* 

1. From the definition, we can see that $s^\ast$ is a Nash Equilibrium and it will not be eliminated in IESDS since it is not strictly dominated by any other strategy.

2. Proof by  contradiction, assuming the unique outcome $s^\ast$ resulting from IESDS is not a Nash Equilibrium, since the game is finite, for some player $i$, there exist one strategy $\hat{s}_i\in S_i$:
   $$
   u_i(\hat{s}_i,s^\ast_{-i})=\max_{s_i\in S_i} u_i(s_i,s^\ast_{-i})>u_i(s^\ast_i,s^\ast_{-i})
   $$
   However, $\hat{s}_{i}$ must be eliminated at some stage $\hat{k}$, which satisfies:
   $$
   u_i(s_i',s_{-i})> u_i(\hat{s}_i,s_{-i})
   $$
   Note that each $s_{-i}$ remaining at stage $\hat{k}$ meets this. $s^\ast_{-i}$ survives IESDS implies $u_i(s_i',s^\ast_{-i})>u_{i}(\hat{s}_i,s^\ast_{-i})$, which contradicts.

##### Finding Nash Equilibrium in some examples

**[Example 1]** Two players share a pie, they propose their demand respectively as $s_1,s_2\in [0,1]$. if $s_1+s_2\leq 1$, each gets their part, otherwise, both receive zero. Considering the NE?

**[Solutions]** Firstly considering best responses of each player:

For P1: $\forall s_2\in [0,1]$:
$$
R_1(s_2)=\begin{cases}1-s_2 & s_2\in [0,1)\\ [0,1] & s_2 = 1\end{cases}
$$
This is symmetric for P2, such that the set of NE is the intersections of $R_1(\cdot)$ and $R_2(\cdot)$.

The set of NE can be illustrated as one line segment $y=-x+1(x\in [0,1])$ and one dot $(1,1)$.

----

**[Example 2]** (Cournot Duopoly) Two firms choose their quantities $q_1,q_2$ (a homogeneous product). The market-clearing price:
$$
P(Q)=\begin{cases}a-Q & Q<a \\ 0 & Q\geq a\end{cases}
$$
where $Q=q_1+q_2$. The marginal cost is constant at $c$, where $0<c<a$.

For $i$, utility function is:
$$
u_i(q_1,q_2)=q_i[a-(q_1+q_2)-c]
$$
By the partial derivative, their best responses:
$$
\begin{split}
q_1&=\frac{1}{2}(a-q_2-c)\\
q_2&=\frac{1}{2}(a-q_1-c)
\end{split}
$$
Their intersection is NE: $(\frac{a-c}{3},\frac{a-c}{3})$.

This problem can be solved by IESDS as well:

Initially, their strategy space are $[0,+\infty)$. However, both of them would not choose any $q_i$ larger than $\frac{a-c}{2}$. Note the best response is $\frac{a-q_{-i}-c}{2}$, even the other player reports zero, the upper bound of $i$'s report should not larger than $\frac{a-c}{2}$. This process can be done iteratively, since both of them choose at most $\frac{a-c}{2}$, $\frac{a-c}{4}$ will dominant this strategy and at last the finally choice in their strategy space is $\frac{a-c}{3}$.

**[Example 3]** (Bertrand Duopoly) Two firms choose their prices $p_1$ and $p_2$. The demand of market from firm $i$ is:
$$
q_i(p_i,p_j)=a-p_i+bp_j
$$
$b$ reflects the extent to which firm $i$'s product is a substitute for firm $j$'s product. Marginal cost $c$.

utility function is:
$$
u_i(p_1,p_2)=(a-p_i+bp_j)(p_i-c)
$$
best responses:
$$
\begin{split}
p_1 &= \frac{1}{2}(a+c+bp_2)\\
p_2 &=\frac{1}{2}(a+c+bp_1)
\end{split}
$$
Intersection:
$$
p_1^\ast=p_2^\ast=\frac{a+c}{2-b}
$$
Finding a Nash Equilibrium Procedures:

(1) Simplify by IESDS; (2) Calculate the best-response; (3) Take the intersection of best responses.

Sometimes there is no PNE in a game and we extend it into mixed Nash Equilibrium.

**Nash's Theorem (1950)**: Every finite normal-form game has at least one Nash Equilibrium.

(Proof follows directly from Kakutani's fixed point theorem.)

**[Example 4]** Consider a 3-person game, P1,P2,P3 pick the row column and matrix respectively.

<img src="..\Pictures\l1-4.png" style="zoom:67%;" />

First step is to IESDS: for P2, c is always dominated by a (1>0, 3>1, 3>1); after this for P3, x is always dominated by y; after this for P1, it is not hard to see P1 will never choose c because any mixed strategy with a and b achieves higher profit. 

Second step is to calculate best responses for P1 and P2:
$$
\begin{split}
u_1&=3x+2y-5xy\\
u_2&=4xy-2x-2y+3
\end{split}
$$
By the partial derivative, best responses:
$$
\begin{split}
x=\frac{1}{2}\\
y=\frac{3}{5}
\end{split}
$$
Last step, the unique NE is: $(\frac{1}{2}a+\frac{1}{2}b,\frac{3}{5}a+\frac{2}{5}b,y)$.



