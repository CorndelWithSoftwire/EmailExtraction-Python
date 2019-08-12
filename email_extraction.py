def part_one():
    count = 0

    with open('sample.txt') as f:
        samples = f.read()

    for i in range(len(samples)):
        if (samples[i:i+13] == '@softwire.com'):
            count += 1
    
    print(count)

if __name__ == "__main__": part_one()