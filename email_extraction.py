import re

def part_one():
    count = 0

    with open('sample.txt') as f:
        samples = f.read()

    for i in range(len(samples)):
        if (samples[i:i+13] == '@softwire.com'):
            count += 1
    
    return count

def part_two():
    with open('sample.txt') as f:
        samples = f.read()

    results = re.findall(r"\b[A-Z\.'_%+-]*@softwire.com\b", samples, re.I)

    return len(results)

def part_three():
    with open('sample.txt') as f:
        samples = f.read()

    results = {}
    groups = re.findall(r"\b[A-Z\.'_%+-]*@([A-Z\.'_%+-]+\.[A-Z'_%+-]*)\b", samples, re.I)

    for g in groups:
        results[g] = results.get(g, 0) + 1
    
    sorted_results = sorted(results.items(), key=lambda kv: -kv[1])
    report = ''.join([f"  {r[1]}: {r[0]}\n" for r in sorted_results])
    return report

def main():
    print("Part One results: " + str(part_one()))
    print("Part Two results: " + str(part_two()))
    print("Part Three results: \n" + part_three())


if __name__ == "__main__": main()