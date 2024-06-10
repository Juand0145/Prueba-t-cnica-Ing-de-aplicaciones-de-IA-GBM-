def min_jumps_to_reach_x(x):
    sum_jumps = 0
    jumps = 0
    while sum_jumps < x or (sum_jumps - x) % 2 != 0:
        jumps += 1
        sum_jumps += jumps
    return jumps

def process_input(input_data):
    data = input_data.strip().split()
    t = int(data[0])
    results = []
    index = 1
    for _ in range(t):
        x = int(data[index])
        index += 1
        results.append(min_jumps_to_reach_x(x))
    return results

if __name__ == "__main__":
    import sys
    input = sys.stdin.read()
    results = process_input(input)
    for result in results:
        print(result)
