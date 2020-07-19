# Important-Coding-Questions
These are few coding questions asked prviously in companies. I have gathered these questions and solutions from *EDYST Daily Coding Challenge April 2020*.My sincere thanks to edyst for providing these questions to practice.

**Challenge #1 [TCS] - Superman's encounter**

It's the summer and you are thinking about internship opportunities at some organizations - the Justice League being one of them. You have cleared the first round or tests and are now sitting in a face-to-face interview with Superman.


Superman is planning a journey to his home planet. It is very important for him to know which day he arrives there. They don't follow the 7-day week like us. Instead, they follow a 10-day week with the following days:

Day Number	Name of Day
1	sunday
2	monday
3	tuesday
4	wednesday
5	thursday
6	friday
7	saturday
8	kryptonday
9	coluday
10	daxamday
Here are the rules of the calendar:

The calendar starts with sunday always
It has only 296 days. After the 296th day, it goes back to sunday
You begin your journey on a sunday and will reach after n days. You have to tell on which day you will arrive when you reach there.

Input format
The first line contains T, the number of test cases
The following T lines contain a number n ( 0 < n)
Output format
For each input, print the name of the day you are arriving on
Example Input
5
1
7
10
300
550
Example Output
monday
kryptonday
sunday
thursday
thursday
Explanation
We arrive 1 day after sunday, which is day #2 -> monday
We arrive 7 days later, which is day #8 -> kryptonday
We arrive 10 days later, which means a week later. Thus we arrive at day #11 -> sunday
We arrive 300 days later on day # 301. After 295 days of journey we finish the calendar year. We start again from sunday (297th day) -> monday (298th day) -> tuesday (299th day) -> wednesday  (300th day) -> thursday (301st day)
We arrive on day # 551. This means we have completed 1 calendar year. In the new year, this is the 255 th day. The 250th day is daxamday, then we have sunday (251st day) -> monday (252nd day) -> tuesday (253rd day) -> wednesday  (254th day) -> thursday (255th day)


**[Infosys] - Shaktimaan's suggestion**

You are excited about your internship interview with Superman. It took him a few days to reach home, but it seems he reached on the day that you predicted!

He passes you on the HR interviewer. For the India office, the Head of HR is none other than Shaktimaan!

Shaktimaan is a bit busy putting some prisoners in jail and can't take your interview right away. This is your perfect opportunity to make a good impression.  Help him place the prisoners in the respective cells properly.


There are n cells, and Shaktimaan wants to fill p prisoners as follows:

First all the n cells receive 1 prisoner each
Then, each cell from 2 to n receives 1 prisoner each
Then, each cell from 3 to n receives 1 prisoner each
And so on...
This keeps on going till we have run out of prisoners. If there are more prisoners left even after filling n rounds, then fill the remaining ones in the 1st cell
Input Format
The first line contains T, the number of test cases
Each test case contains 2 integers: n (number of cells) and p (number of prisoners)
Note: n <= p

Output Format
Print the number of prisoners in each cell
Example Input
3
2 3
3 10
3 20
Example Output
1 2
5 2 3
15 2 3
Explanation
We have 2 cells. We first fill and get 1 1, we have one more prisoner, so we fill 1 2
We have 3 cells and 10 prisoners. First we get: 1 1 1, then 1 2 2, then 1 2 3, we have 4 more prisoners left, which we place in the first cell, thus making it 5 2 3
Similarly the last one becomes 15 2 3


**[Mindtree] - Scarlet Witch's solution**

You see, while you got the solution to the prisoner dilemma, Shaktimaan didn't suggest your name for the internship. He wasn't wearing his glasses, and instead drafted you to the forensic team.


It seems one of the prisoners have an ancient lock with them. It is your first day in the forensics team and you want to make a great impression - you decide to unlock this ancient lock.

The lock's password is directly related with the time of the day and a secret series, denoted by the following

an = 2an-1 - 1

The hour in current time tells us the value of a0
And the minute tells us the number of terms (numbering starts from 0)
Let's say we have the time as 23:05, then :

a0 = 23
a1 = 2*23 - 1 = 45
a2 = 89
a3 = 177
a4 = 353
a5 = 705
Then, we sum up these numbers, we get: 23 + 45 + 89 + 177 + 353 + 705 = 1392

In terms of password, this corresponds to BDJC. (Because 0 corresponds to A, 1 corresponds to B, 2 to C and so on...)

Given the time, please print the password for this lock.

Input format
The first line contains T, the number of test cases
Each line after that contains the current time
Note a0 > 0
Output format
For each input, print the password
Example Input
3
23:05
10:03
01:10
Example Output
BDJC
BDJ
BB
Explanation
The sum of the first one becomes: 1392 -> BDJC
The sum of second one becomes: 139 -> BDJ
The sum of third one becomes: 11 -> BB


**[TCS CodeVita] - Black Widow's riddle**

Also, did you realize that you applied to the Justice League, yet the last challenge you were working for the Avengers? Black Widow noticed this anomaly and she suspects you aren't from the Avengers - she thinks you're with Thanos!


You want to prove that you're one of the good people. This is the test she has for you. You are given a set of people in a NxN power grid. Some of them are Titans, friends of Thanos.

You can know if they are Titans by knowing if there are any repeated people in a particular row or column of the power grid.

If there are no repeated people in the rows or columns, then the power grid contains no Titans.

Given an NxN grid, you must print:

SAFE if there are no titans
DANGER, followed by number of rows and columns where the repeated people are
Input Format
First line contains T, the number of test cases
This is followed by N N, the size of the grid followed by N x N numbers denoting the grid
Output Format
SAFE if there are no titans
DANGER, followed by number of rows and columns where the repeated people are
Example Input
4
2 2 1 2 3 4
3 3 1 2 3 3 1 2 4 5 6
3 3 1 2 3 1 2 3 1 2 3
4 4 1 2 3 1 2 3 4 5 6 7 8 9 10 2 12 1
Example Output
SAFE
SAFE
DANGER 0 3
DANGER 1 2
Explanation
First and second case are safe because there are no repeated elements
In third case, no row has repeated elements but all 3 columns have repeated elements hence DANGER 0 3


**[HackWithInfy] - Iron Man's new invention**

Marvel HQ is beginning to warm up to you. They first thought you are an intruder, but now it looks like you're starting to find your way.

You meet Tony Stark, a.k.a Iron Man, on your way out from that dangerous grid. He seems pretty chilled out - he's playing with a new invention a stargazing machine. Seeing as you are the new intern, he wants you to help him with some classification work.


He is looking at some planets, and we wants to group planets together by their diameter.

A group's diameter is the maximum sum possible formed by any pair of the planets. For example, if you have the group (2, 4, 3), this group's diameter is 7. This is because the possible diameters are: 2 + 3, 2+ 4, and 4+3, and 4+3 is the maximum from that.

If a certain group contains only 1 planet, then the group's diameter is the same as the diameter of the planet. So a group of (10), has diameter 10.

Given a list of planets, your job is to count minimum number of groups possible, such that their diameter is less than or equal to a certain limit.

If it is not possible, you must print impossible

Input format
The first line contains T, the number of test cases
In each test case, the first line is N, number of planets and M, the limit of group diameter
This is followed by N integers, denoting the diameter for each planet
Note: 0 <= planet_size <= 5000, 1 <= N <= 10000

Example Input

3
5 14
6 14 15 0 8
8 5
2 4 3 0 0 0 4 0
10 15
12 9 9 9 7 7 15 5 3 3
Output

impossible
3
6
Explanation

In the first case, the diameter limit should is 14, but the maximum planet we have is 15. Thus we can't make any groups satisfying the condition
In the second case, one possible division is:
Group 1: 4 0 0 0
Group 2: 3 2 0
Group 3: 4 0
There are other combinations too, but we will never get less than 3 groups
In the 3rd case, one possible division is:
Group 1: 15
Group 2: 7 7 5 (here diameter is 14, because maximum sum pair is 14)
Group 3: 12
Group 4: 9
Group 5: 9 3
Group 6: 9 3
There are other combinations too, but we will never get less than 6 groups


**[Goldman Sachs] - Black Panther's party**
Iron Man is impressed with the way you grouped those planets. It saved him a lot of work. He said something about getting some donuts or pizza - and you're the intern! So you have to go and get it. His favorite snacks place is in Wakanda. You go to Wakanda (don't ask us how!), and find that all the shops are closed for elections. Wakanda has turned into a very modernistic democracy.


The voting machine is having some problems, and you are now in charge of re-writing the program that makes it work (after all, Iron Man has sent you right?)

This is how voting works in Wakanda:

The ballot has a list of parties that are contesting for the election. It is possible for multiple parties to win
The voter can vote for more than one party, so they don't enter the party name. Instead, they mention a pattern that matches all their desired parties
At the end, the parties with the most votes wins, we have to print the name of those parties
If no party gets any votes, then we print stalemate
It is possible that some votes don't map to any party
Input format
The first line contains T, the number of test cases
Each test case contains P followed by names of P parties
Followed by N (number of voters), and then N passwords, 1 for each voter
Note: all votes will be in lowercase alphabets. All parties are unique.

1 <= P <= 1000

1 <= N <= 30

Output format
Print name of the winners in alphabetical order, or print stalemate
Example Input
5
5 aabb abcd abce abcf abbc
4 xxyy xywz lmmn efgh
8 hello bello gekki ditto not winning but sinning
5 litte abxxbxe lmo spite spool
2 abc def
3 xxx yyy zzz
2 aaaa aaab
2 mnop rsav
5 root note boot yoke egg
2 book efgh
Example Output
abcd abce abcf 
bello ditto gekki hello 
stalemate
stalemate
boot note root yoke 
Explanation
In the first case, xywz and efgh both vote for the following: abcd, abce, abcf. How? Because in both xywz and efgh we have all distinct characters. xxyy is a vote for aabb because the first character appears twice and next character also appears twice.

In the 2nd case:


In the third case, we don't have any votes. Each of xxx, yyy and zzz are votes for parties which have 3 characters and all characters repeated. Since we have no such party, it's a stalemate. Similarly the 4th case.

In the fifth case, book votes for boot, and root. efgh votes for yoke and note.



**[Microsoft] - Captain Marvel's victory**
What a confusing election that was! We don't blame you for being exhausted. But hey, you're an intern! There is no respite for the intern.

The winner of the election was Captain Marvel's party! She is super excited and now needs a new Chief of Staff. Look at you - 6 days ago you were worried about internships, and now you are being interviewed to be the Chief of Staff.


Captain Marvel has to choose ministers for her cabinet. She does so by choosing the most compatible ministers in terms of ratings. Politics is a tricky business, so it's not just enough to choose the maximum ratings.

Instead you have to choose them based on their compatibility. 3 ministers with ratings a, b and c are said to be compatible if:

a < b < c
In the candidate's rating list, a occurs before b, and b occurs before c
Their compatibility is calculated by the formula: a - b + c

Given a list of candidates ratings, find the best compatibility possible

Input format
The first line contains T, the number of test cases
Each test contains N, the size of the list followed by N ratings
Note: 0 <= rating <= 106, 3 <= N <= 106

Output format
For each test case, print the maximum compatibility possible
Example Input
3
5 2 13 3 14 9
8 4 3 4 3 4 5 2 1
10 3 8 1 13 7 11 8 6 2 11
Output
13
4
10
Explanation
In the first case, we choose (2,3,14). This gives us compatibility of 13
In the second case, we choose (3,4,5).  This gives us compatibility of 4
In the third case, we choose (1,2,11). This gives us compatibility of 10


**[LinkedIn] - Jean Gray's quandary**

Cabinet Ministries were always going to be tough to choose, but you did it. While you were just about to ask about what your next task is, a danger has come knocking on the doors of Wakanda.


It is Jean Grey - and she is in her Phoenix form. She is out to destroy the entire town. However, there is one way to save everyone. If we are able to give Phoenix an antidote in just the right amount, she can recover and everyone else will be saved.

Captain Marvel is impressed by your analytical abilities, so she has put you in-charge of gathering up exactly L amounts of antidote.

There are N glasses of antidote. The ith glass has 2i-1 amount of antidote in it. 1 <= i < N

Further more, each antidote has a certain amount of energy required to get it. This is given to you as a list e0 e1 e2.... eN-1.

Find the minimum energy we need to spend in order to get exactly L amounts of antidote. Note that we can't take any antidote partially. We need to take the entire glass.

Input format
The first line of input contains T, the number of test cases
The first line of each test cases contains L, the amount of antidote required
The next line contains N followed by the N values that denote energy required for each antidote
Note: 1 <= N <= 20, 1 <= L  <= 20000

Output format
For each test case, print the minimum amount of energy required
Example Input
2
8
4 66 1 2 84
200
10 137 96 118 112 86 91 37 54 178 121
Example Output
4
203
Explanation
First case
We need to get exactly 8 antidote. There are 4 glasses. Remember, the ith glass has 2i-1 amount of antidote in it. So:

Amount	Energy
1	66
2	1
4	2
8	84
We can choose 4 glasses of amount 2. This gives us 8 amount of antidote, and only 4 energy has been spent

Second case
We need to get exactly 200 antidote. There are 10 glasses. Remember, the ith glass has 2i-1 amount of antidote in it. So:

Amount	Energy
1	137
2	96
4	118
8	112
16	86
32	91
64	37
128	54
256	178
512	121
Here we select 1 glass of 128 amount, 1 glass of 64 amount and 1 glass of 8 amount to reach 200 exactly. The number energy from each is: 54 + 37 + 112 = 203


 **[Google] - Wonder Woman's great escape**
 
 Sometimes instructions are straightforward, and other times they are not. For example, if Shaktimaan had just drafted you as a normal intern, you wouldn't be in this mess.

What's the mess? Well, you were able to cure Phoenix by getting the antidotes. The problem was that the antidotes also released so much energy that you got caught in a wormhole. And just your luck - you landed in a maze at the side of Wonder Woman.


Wonder Woman is racing through the 2D maze. She starts at a position A and wants to go to position B. She can move only 1 block at a time - either vertically or horizontally. Also, her vertical moves and horizontal move can only be in 1 direction each.

Let' say she starts at A (1,1) and needs to reach B (3,3). Vertically she is allowed to move only to the South S and horizontally to the E. No matter what moves she makes, it's impossible to reach B, because she can never go North

However, if she is allowed to move NE, which means vertically North and horizontally East, she has many ways of reaching B:


Totally she has 6 ways. of reaching her destination.

Given the coordinates of her starting and and desired ending positions, you need tell either impossible if it's not possible to reach, or print the total ways possible to reach B from A

Input format
The first line of input contains T, the number of test cases
The first line contains the x and y coordinates of A
The second line contains the x and y coordinates of B
This is followed by the direction string. The first character contains S or N, the second one E or W
0 <= x,y <= 15

Output format
For each test case, print impossible or the total way possible to reach B from A
Example Input
4
1 1
3 3
NE
10 10
1 1
NE
3 7
5 3
SW
1 4
0 6
NW
Example Output
Total Ways: 6
impossible
impossible
Total Ways: 3
Explanation
The first case is explained above
The second case requires us to move S and W, but allowed is N and E. Hence it's impossible
The third case requires us to move E for 3 -> 5, and S for 7 -> 3. We need SE, but we have SW. Hence it's impossible
The last case is possible. The possible paths are: 1,4 -> 1,5 -> 1,6 -> 0,6, 1,4 -> 0,4 -> 0,5 -> 0, 6, 1,4 -> 1,5 -> 0,5 -> 0,6


**[Amazon] - Batman's jackpot**


