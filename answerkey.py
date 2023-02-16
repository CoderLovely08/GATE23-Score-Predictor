l1 = """
1 C MCQ
2 B MCQ
3 A MCQ
4 A MCQ
5 C MCQ
6 D MCQ
7 C MCQ
8 D MCQ
9 B MCQ
10 A MCQ
11 B MCQ
12 B MCQ
13 D MCQ
14 C MCQ
15 A MCQ
16 A MCQ
17 A MCQ
18 B MCQ
19 C MCQ
20 C MCQ
21 B MCQ
22 B;C;D MSQ
"""

l2= """
23 C;D MSQ
24 A;C;D MSQ
25 A;C MSQ
26 B;C MSQ
27 C;D MSQ
28 B;D MSQ
29 A;C MSQ
30 2 NAT
31 0 NAT
32 110 NAT
33 2040 NAT
34 10.2 NAT
35 7 NAT
36 A MCQ
37 D MCQ
38 C MCQ
39 B MCQ
40 A MCQ
41 B MCQ
42 C MCQ
43 A MCQ
44 C MCQ
"""

l3 = """
45 C MCQ
46 B MCQ
47 C MCQ
48 C MCQ
49 B;C;D MSQ
50 B;C;D MSQ
51 A;D MSQ
52 A;B MSQ
53 C;D MSQ
54 A;D MSQ
55 A;B MSQ
56 5040 NAT
57 4096 NAT
58 5 NAT
59 8 NAT
60 2.375 NAT
61 2 NAT
62 7 NAT
63 4 NAT
64 19 NAT
65 3 NAT
"""
answerkey = l1.strip().replace("\n"," ").split(" ") + l2.strip().replace("\n"," ").split(" ") + l3.strip().replace("\n"," ").split(" ")
answerkey = [answerkey[x:x+3] for x in range(0, len(answerkey),3)]