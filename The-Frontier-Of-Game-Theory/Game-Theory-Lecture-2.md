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