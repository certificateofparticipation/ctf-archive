**hdb**

---

Inflation has gotten so high every square metre now has a different price and people are auctioning for every single one of them. You are given an _N x N_ square grid. Each square has a price _P_. There are _B_ buyers and _B_ queries for the prices they have to pay to buy a rectangular set of land. Find out what each of them needs to pay.    

## **Input**

Each input file contains one test case. There are 10 input files in total.
For each file:

- The first line contains _3 ≤ N ≤ 256_.

- The second line contains an _N x N_ grid of _P<sub>1</sub>_ ... _P<sub>N<sup>2</sup></sub>_.
1 ≤ _P<sub>x</sub>_ ≤ 65536 and are random. 

- The third line contains _2 < B ≤ 100000_

- The next _B_ lines contains _X<sub>start</sub>_ _Y<sub>start</sub>_ _X<sub>end</sub>_ _Y<sub>end</sub>_ (separated by 1 space) such that

  - 0 ≤ _X<sub>s</sub>_ _Y<sub>s</sub>_ _X<sub>e</sub>_ _Y<sub>e</sub>_ < N 
  - _X<sub>s</sub>_ ≤ _X<sub>e</sub>_ ; _Y<sub>s</sub>_ ≤ _Y<sub>e</sub>_

## **Output**

_B_ lines, each line containing the sum of all squares _i_ such that _X<sub>s</sub>_ ≤ _X<sub>i</sub>_ ≤ _X<sub>e</sub>_ and _Y<sub>s</sub>_ ≤ _Y<sub>i</sub>_ ≤ _Y<sub>e</sub>_

## **Constraints**

Time limit (per input file): 1 second

## **Sample input**

3<br>
1 6 5 <br>
7 3 8 <br>
9 2 4 <br>
3<br>
1 1 1 2<br>
1 2 2 2<br>
1 0 2 1

## **Sample output**

11<br>
12<br>
21

## **Explanation**

3 + 8 = 11<br>
8 + 4 = 12<br>
7 + 3 + 9 + 2 = 21
