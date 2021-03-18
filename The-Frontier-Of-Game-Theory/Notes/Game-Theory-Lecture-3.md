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