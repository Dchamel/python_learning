import sys
from itertools import combinations


def parse_line(line):
    # Extract parts between [], (), and {}
    indicator_part = line.split('[')[1].split(']')[0]
    buttons_str = line.split(']')[1].split('{')[0].strip()
    # Parse buttons
    buttons = []
    for part in buttons_str.split(')'):
        if '(' in part:
            btn_str = part.split('(')[1]
            if btn_str.strip():
                indices = tuple(sorted(map(int, btn_str.split(','))))
                buttons.append(indices)
    return indicator_part, buttons


def solve_machine(target, buttons):
    n_lights = len(target)
    # Convert target to binary vector (0=off, 1=on)
    target_vec = [1 if c == '#' else 0 for c in target]

    n_buttons = len(buttons)
    min_presses = float('inf')

    # Try all subsets of buttons (brute-force since number of buttons is small)
    # We only need to consider pressing each button 0 or 1 times (since pressing twice = no effect)
    for r in range(n_buttons + 1):
        for combo in combinations(range(n_buttons), r):
            # Build effect vector
            effect = [0] * n_lights
            for idx in combo:
                for light in buttons[idx]:
                    if light < n_lights:
                        effect[light] ^= 1  # Toggle
            if effect == target_vec:
                min_presses = min(min_presses, r)
                break  # Found minimal for this r
        if min_presses != float('inf'):
            break  # Found global minimal

    return min_presses if min_presses != float('inf') else 0


def main():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    total_presses = 0
    for line in lines:
        indicator, buttons = parse_line(line)
        presses = solve_machine(indicator, buttons)
        total_presses += presses

    print(total_presses)


if __name__ == '__main__':
    main()
