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

    results = re.findall(r"[A-Z\.'_%+-]*@softwire.com\b", samples, re.I)

    return len(results)


def main():
    print("Part One results: " + str(part_one()))
    print("Part Two results: " + str(part_two()))


if __name__ == "__main__": main()