def parse_input(input_:list[str]) -> tuple[dict[int, list[list[int]]], list[tuple[tuple[int, int], list[int]]]]:
    part = 0
    gifts = {}
    regions = []
    gift = []
    id = 0

    for line in input_:
        if 'x' in line: part = 1

        if part == 0:
            if len(line.split(':')) == 2: id = int(line[0])
            else:
                if not line:
                    gifts[id] = gift
                    gift = []
                else:
                    gift.append([1 if ch == '#' else 0 for ch in line])
        
        else:
            sides, required_gifts = line.split(':')
            sides = tuple(map(int, sides.split('x')))
            required_gifts = list(map(int, required_gifts.split()))
            regions.append((sides, required_gifts))

    return gifts, regions

def main():
    with open('2025/12_in.txt') as f:
        input_ = f.read().splitlines()

    gifts, regions = parse_input(input_)

    gift_areas = {}
    for id, gift in gifts.items():
        gift_areas[id] = sum([sum(row) for row in gift])        

    ok_regions = 0
    for sides, required_gifts in regions:
        area = sides[0] * sides[1]
        area_of_gifts = sum([gift_areas[id] * ngift for id, ngift in enumerate(required_gifts)])
        if area >= area_of_gifts: ok_regions += 1
    
    print('Part 1:', ok_regions)

if __name__ == '__main__': main()