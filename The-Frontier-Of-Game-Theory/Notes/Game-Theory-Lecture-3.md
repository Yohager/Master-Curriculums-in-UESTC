### Game Theory - Lecture 3

---

#### Static Bayesian Games

games of incomplete information (i.e. at least one player does not know another player's identity)

**[Example]** Cournot Competition under asymmetric information

Consider two firms choose their quantities $q_1$ and $q_2$. Market-clearing price is decided by the demand function: $P(Q)=a-Q,Q=q_1+q_2$. Firm 1's cost function is: $C_1(q_1)=cq_1$ and for Firm 2:
$$
C_2(q_2)=\begin{cases}
c_H q_2 & \text{with prob }\theta\\
c_L q_2 & \text{with prob } 1-\theta
\end{cases}
$$
We can transfer it into a dynamic game:

<img src="..\Pictures\l3-1.png" style="zoom:40%;" />

It is not hard to calculate the NE in this game:

First we can get best responses of two players:
$$
\begin{split}
&r_1 = \theta[a-q_1-q_2(c_H)-c]q_1+(1-\theta)[a-q_1-q_2(c_L)-c]q_1\\
&r_2(c_H) = (a-q_1-q_2(c_H))q_2(c_H)\\
&r_2(c_L) = (a-q_1-q_2(c_L))q_2(c_L)
\end{split}
$$
By FOC we can get the NE:
$$
\begin{split}
q_1^\ast &= \frac{a-2c-\theta c_H +(1-\theta)c_L}{3}\\
q_2^\ast(c_H) &= \frac{a-2c_H+c}{3} + \frac{1-\theta}{6} (c_H-c_L)\\
q_2^\ast(c_L) &= \frac{a-2c_L+c}{3} - \frac{\theta}{6}(c_H-c_L)
\end{split}
$$

#### Norm-Form Representation of Static Bayesian Games

$$
G=(\mathcal{A},\mathcal{T},\mathcal{P},\mathcal{U})
$$

players $i\in\{1,2,\cdots,n\}$; 

action spaces: $\mathcal{A}=\{A_1,A_2,\cdots,A_n\}$; 

type spaces: $\mathcal{T}=\{T_1,T_2,\cdots,T_n\}$

prior distribution: $\mathcal{P}=\{p_1,p_2,\cdots,p_n\}$; 

utilities: $\mathcal{U}=\{U_1,U_2,\cdots,U_n\}$.

player $i$'s belief: $p_i(T_{-i}|T_i)$, which means $i$'s uncertainty about the other players' possible types.

player $i$'s payoff functions: $U_i(A_1,\cdots,A_n,T_1,\cdots,T_n)$.

#### Harsanyi's Theorem

- Nature selects a type profile $T=(T_1,\cdots,T_n)$.
- Nature informs each player $i$ about his type.
- The players simultaneously choose their actions.
- Payoffs $U_i(A_1,\cdots,A_n;T)$ are received.

**Games of incomplete information $\Rightarrow $ Game of imperfect information** 

Strategy for player $i$ is a function $s_i(t_i)$, i.e. $s_i:T_i\to A_i$.  For a given type $t_i$ in $T_i$, $s_i(t_i)$ is a specific action for player $i$.

We can consider a two-players Bayesian game $G$, where $A_1=\{a,b\},A=\{x,y\}$; $T_1=\{t_{11},t_{12}\},T_2=\{t_{21},t_{22}\}$. A prior joint probability distribution $p=(p_{11},p_{12},p_{21},p_{22})$.

#### Bayesian Nash Equilibrium

The notion of BNE in a static Bayesian game can be defined by the following two ideas:

1. Nash Equilibrium in the agent-norm-form game;
2. Nash Equilibrium in the associated normal-form game

##### First form definition of BNE

The strategy profile $s^\ast=(s^\ast_1,\cdots,s^\ast_n)$ is a pure-strategy Bayesian Nash Equilibrium if for each player $i$ and for each of $i$'s type $t_i$, $s^\ast_i(t_i)$ solves:
$$
\max_{a_i\in A_i}E_{t_{-i}}[u_i(s^\ast_{-i}(t_{-i}),a_i;t_i)]
$$
where $E_{t_{-i}}[s^\ast_{-i}(t_{-i}),a_i;t_i]=\sum_{t_{-i}\in T_{-i}}p_i(t_{-i}|t_i)u_i(s^\ast_{-i}(t_{-i}),a_i;t)$.

##### Second form definition of BNE

The strategy profile $s^\ast=(s^\ast_1,\cdots,s^\ast_n)$ is a pure-strategy Bayesian Nash Equilibrium if for each player $i$, $s_i^\ast$ solves:
$$
\max_{s_i\in S_i}E_t[u_i(s_i,s^\ast_{-i};t)]
$$
where $E_t[u_i(s_i,s^\ast_{-i};t)]=\sum_{t\in T}p(t)u_i(s_i(t_i),s^\ast_{-i}(t_{-i});t)$.

#### BNE vs NE

Consider a static Bayesian game:
$$
G=\{A_1,\cdots,A_n;T_1,\cdots,T_n;p_1,\cdots,p_n;u_1,\cdots,u_n\}
$$
Define the agent-normal-form game of $\bar{G}$ as follows:
$$
\bar{G}=(\bar{N},\{\bar{S}_j\},\{\bar{u}_j\})
$$
where $\bar{N}=\{t_i|i\in N\text{ and } t_i\in T_i\},\bar{S}_{t_i}=A_i$, and for $\bar{s}\in \times_{t_i\in \bar{N}}\bar{S}_{t_i}$, $\bar{u}_{t_i}(\bar{s})=E_{t_{-i}}[u_i(\bar{s}_{-i}(t_{-i}),\bar{s}_i(t_i);t_i)]$

In this form, we extend the player space and all the types are redefined as agents in this game. That is called agent-norm-form game and we can maximize all agents' payoff via the new payoff matrix. 

Another form definition of the Bayesian game:
$$
G=\{A_1,\cdots,A_n;T_1,\cdots,T_n;p_1,\cdots,p_n;u_1,\cdots,u_n\}
$$
Define the associated normal-form game of $G$ as follows:
$$
\tilde{G}=\{N,S_1,\cdots,S_n;\tilde{u}_1,\cdots,\tilde{u}_n\}
$$
where $N=\{1,\cdots,n\}$, $S_i=\{s_i:T_i\to A_i\}$
$$
\tilde{u}_i(s_1,\cdots,s_n)=\sum_{t=(t_1,\cdots,t_n)\in T}p(t)u_i(s_1(t_1),\cdots,s_n(t_n);t)
$$
In this form we transfer the Bayesian game into a static norm-form game and we calculate the strategies of all players via their actions and types. 

#### E-mail Game "Almost Common Knowledge"

Consider there exists two games: $G_a$ and $G_b$.

<img src="..\Pictures\l3-2.png" style="zoom:80%;" />

where the parameters satisfy $L > M > 1$ and $p<\frac{1}{2}$.

It is not hard to see that $(A,A)$ is the unique NE in $G_a$ while $(A,A) \&(B,B)$ are two NEs in $G_b$. 

The game is only known to player 1 initially. Player 1 can communicate with player 2 via computer if the game is $G_b$. However, there is  a small probability $\epsilon >0$ that any given message does not arrive at its intended destination. 

Consider this game from the perspective of Bayesian Nash Equilibrium. 

<img src="..\Pictures\l3-3.png" style="zoom:67%;" />

$N=\{1,2\}$.

$Q_i=\{0,1,2,\cdots\}$. (Here this is the type space for player $i$)

$A_i=\{A,B\}$.

Strategies of player $i$ is infinity but countable. Player $i$ can choose to send any number emails.

If $(q_1,q_2)=(0,0)$, then game $G_a$ happens, the payoffs are given by $G_a$.

If $(q_1,q_2)\neq(0,0)$, then the payoffs are give by $G_b$. 

For player 1: if $q_1=0$, then $p(q_2|0)=\begin{cases}1,&q_2=0\\0,&\text{otherwise}\end{cases}$

if $q_1=q\neq 0$, then $p_1(q_2|q)=\begin{cases}\frac{1}{2-\epsilon} & q_2=q-1\\\frac{1-\epsilon}{2-\epsilon} & q_2=q\\ 0&\text{otherwise}\end{cases}$

For player 2: if $q_2=0$, then $p_2(q_1|0)=\begin{cases}\frac{1-p}{1-p+p\epsilon} & q_1=0\\ \frac{p\epsilon}{1-p+p\epsilon} & q_1=1\\ 0&\text{otherwise}\end{cases}$

if $q_2=q\neq 0$, then $p_2(q_1|q)=\begin{cases}\frac{1}{2-\epsilon} & q_1=q\\\frac{1-\epsilon}{2-\epsilon} & q_1=q+1\\0&\text{otherswise}\end{cases}$

How to find the BNE in email game?

We use the mathematic induction method. First we give the result that the electronic mail game has a unique BNE, in which two players both play action $A$.

***Proof***: First consider the special case that $(0,0)$. Player 1 will always choose $A$. For player 2, if she choose $A$, she will get $(1-p)M/[(1-p)+p\epsilon]$, however if she chooses $B$, she will get at most $[-L(1-p)+p\epsilon M]/[(1-p)+p\epsilon]$. The former is always bigger than the later. So player 2 will always choose $A$ as well.

Then we assume that player 1 and player 2 will always choose $A$ when then receive signal is less than $q$. Now considering the signal $q$ comes, player 1 guess there is a prob $1/(2-\epsilon)$ that player 2 chooses $q-1$ while $(1-\epsilon)/(2-\epsilon)$ chooses $q$. To simplify it, we use $z$ denoting prob $1/(2-\epsilon)$. Consider player 1 chooses action $B$, her expected payoff is $z(-L)+(1-z)M$ at most while choosing $A$ that is at least $0$. Similar process for player 2.  

Up to now we finished the proof. This proof tells us the common knowledge is totally different from almost common knowledge. Consider the $\epsilon=0$, the BNE of this game will be $((A,A),(A,A))$ and $((A,B),(A,B))$, which is different from that when $\epsilon$ is positive.

#### Revelation Principle

**[Theorem by Myerson]** Any BNE of any Bayesian game can be represented by an incentive-compatible mechanism. Here we omit the proof.

#### Sealed-bid Auctions

##### First Price Auction under Complete Information

Two bidders $i=1,2$ submit bids for one object. Bidders valuation for this good $v_1>v_2$.
$$
u_i(b_i,b_{-i})=\begin{cases}
v_i-b_i & b_i>b_j\\
(v_i-b_i)/2 & b_i = b_j\\
0 & b_i<b_j
\end{cases}
$$
Question is about whether exist PNE in this game. 

The idea is treating this game as one static norm form game and analyze it by comparing $b_1$ and $b_2$ with their value ranges. 

The answer is there exist no PNE in this game.

##### Second Price Auction under Complete Information

Two bidders $i=1,2$ submit bids for one object. Bidders valuation for this good $v_1>v_2$.
$$
u_i(b_i,b_{-i})=\begin{cases}
v_i-b_j & b_i>b_j\\
(v_i-b_j)/2 & b_i = b_j\\
0 & b_i<b_j
\end{cases}
$$
Question is about whether exist PNE in this game.

Idea is similar with first price auction under complete information. Result is: when $b_1>v_2\geq b_2$,  there exist NEs, another situation is $b_2\geq v_1$ and $b_1\leq v_2$. In this way, p1 will never bid more than $v_1$ to win in which her payoff changes from 0 to negative; p2 will never underbid since her payoff is $v_2-b_1\geq 0$. When $b_1=b_2$, there exists no NE.

##### First Price Auction under Incomplete Information

Two bidders $(i=1,2)$ submit bids for one object.

Bidders have valuations $v_1,v_2$, which are their private information. It is common knowledge that $v_1,v_2$ are independently and uniformly distributed on $[0,1]$.

We can formulate the auction as a static Bayesian game:
$$
G=\{A_1,A_2;T_1,T_2;p_1,p_2;u_1,u_2\}
$$
$A_1=A_2=[0,\infty)$.

$T_1=T_2=[0,1]$.

$i$'s belief $p_i(v_j)$ is the uniform distribution on $[0,1]$,

$i$'s payoff is: 
$$
u_i(b_i,b_{-i})=\begin{cases}
v_i-b_j & b_i>b_j\\
(v_i-b_j)/2 & b_i = b_j\\
0 & b_i<b_j
\end{cases}
$$
Player $i$'s strategy is a function $b_i(v_i)$ from $[0,1]$ into $[0,\infty)$.

