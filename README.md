# GATE 2023 Score Generator

## Steps to calculate your gate score
1. Fork this respository
2. Copy your responses from your login as it is. Note: start copying from 1 upto last NAT excluding the headers such as question no etc.

Example: 
```text
1	B	MCQ	2	B	MCQ	3	A	MCQ
4	A	MCQ	5	C	MCQ	6	D	MCQ
7	C	MCQ	8	D	MCQ	9	B	MCQ
10	C	MCQ	11	--	MCQ	12	--	MCQ
13	--	MCQ	14	A	MCQ	15	A	MCQ
16	A	MCQ	17	--	MCQ	18	--	MCQ
19	C	MCQ	20	--	MCQ	21	--	MCQ
22	A;C	MSQ	23	A;B;D	MSQ	24	A;B;C	MSQ
25	B;D	MSQ	26	--	MSQ	27	C;D	MSQ
28	A;D	MSQ	29	A;B;D	MSQ	30	--	NAT
31	2.4	NAT	32	25152	NAT	33	4400	NAT
34	1.2	NAT	35	6	NAT	36	A	MCQ
37	--	MCQ	38	--	MCQ	39	--	MCQ
40	--	MCQ	41	--	MCQ	42	--	MCQ
43	--	MCQ	44	--	MCQ	45	--	MCQ
46	--	MCQ	47	A	MCQ	48	--	MCQ
49	B;C	MSQ	50	B	MSQ	51	A;D	MSQ
52	B;C	MSQ	53	A;D	MSQ	54	A;B;C	MSQ
55	--	MSQ	56	8	NAT	57	--	NAT
58	1256	NAT	59	8	NAT	60	--	NAT
61	2	NAT	62	5	NAT	63	3	NAT
64	28	NAT	65	5	NAT
```
3. Create a text file in the current directory with your name.txt
4. Open main.py file and edit your filename in the filename variable (5th line)
5. Install necessary packages by running the following command
```python
    pip install -r requirements.txt
```
6. Now run the main.py file and your response summary will be displayed and an estimated final score will be displayed

### Note:
- Response key is taken from [Unacademy](https://unacademy.com/content/gate/gate-2023-question-paper-solution/)
- This is just for assesing personal performance and not an official score predictor
- Answer key may change in future 
- Code will be updated once the official answer key is released.
- Any code optimization and bug fixes are welcomed.