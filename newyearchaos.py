
def minimumBribes(q):
    # Write your code here
    total_bribes = 0
    swaps = 1
    # If any person is more than 3 places ahead of where they should be,
    # too many bribes have taken place.
    for index, item in enumerate(q):
        if item > index + 3:
            print("Too chaotic")
            return 

    # Finally! A use for bubblesort!
    while (swaps != 0):
        swaps = 0
        for i in range(len(q) - 1):
            if q[i] > q[i + 1]:
                swaps += 1
                q[i], q[i + 1] = q[i + 1], q[i]
                total_bribes += 1
    print(total_bribes)

# q=[1,2,3,5,4,6,7,8]
# q=[4,1,2,3]
q=[2,1,5,3,4]      # 5 before 4 then 5 before 3 then 2 before 1 , to look like result.
minimumBribes(q)