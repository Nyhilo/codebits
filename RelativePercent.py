Percentlist=[93.6,
82.0,
81.7,
78.3,
76.9,
76.1,
74.3,
73.2,
71.8,
68.4,
67.0,
66.7,
66.1,
65.1,
65.0,
63.1,
62.2,
61.3,
59.2,
55.6,
53.9,
51.7,
50.2,
49.9,
49.6,
48.6,
47.8,
45.6,
43.5,
43.3,
43.3,
43.1,
41.7,
40.2,
38.8,
38.4,
35.0,
32.0,
21.8,
17.5
]

def percentCalculation(list):
    out = [list[0]]
    for i in range(1, len(list)):
        out.append((100-sum(out[:i]))*(list[i]/100))
    return out

def main():
    for item in percentCalculation(Percentlist):
        print(str(item) + "%")

if __name__ == '__main__':
    main()