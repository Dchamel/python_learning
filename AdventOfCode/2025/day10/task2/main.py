import sys
import re
import pulp


def solve() -> None:
    total_presses_all = 0

    with open('input.txt', 'r') as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line:
                continue

            # Extract button definitions: content inside parentheses
            button_strings = re.findall(r'\(([0-9, ]+)\)', line)
            # Extract target counters: content inside curly braces
            target_match = re.search(r'\{([0-9, ]+)\}', line)
            if not target_match:
                continue  # skip malformed lines

            # Parse button sets
            button_sets = []
            for s in button_strings:
                s = s.replace(' ', '')  # remove spaces, e.g., "0, 2, 3" -> "0,2,3"
                if s:
                    indices = list(map(int, s.split(',')))
                    button_sets.append(indices)

            # Parse target vector
            target_str = target_match.group(1).replace(' ', '')
            target = list(map(int, target_str.split(',')))

            n_counters = len(target)
            n_buttons = len(button_sets)

            # Build ILP model
            prob = pulp.LpProblem('min_presses', pulp.LpMinimize)

            # Decision variables: how many times each button is pressed
            x_vars = [
                pulp.LpVariable(f"x{i}", lowBound=0, cat='Integer')
                for i in range(n_buttons)
            ]

            # Objective: minimize total number of presses
            prob += pulp.lpSum(x_vars)

            # Constraints: each counter must reach its required value
            for counter_idx in range(n_counters):
                prob += (
                        pulp.lpSum(
                            x_vars[btn_idx]
                            for btn_idx, btn in enumerate(button_sets)
                            if counter_idx in btn
                        )
                        == target[counter_idx]
                )

            # Solve using CBC (default solver)
            prob.solve(pulp.PULP_CBC_CMD(msg=False))

            # Ensure we found an optimal solution
            if pulp.LpStatus[prob.status] != 'Optimal':
                raise RuntimeError(
                    f"No optimal solution for line: {line}\nStatus: {pulp.LpStatus[prob.status]}"
                )

            # Sum the presses for this machine
            machine_presses = sum(int(pulp.value(var)) for var in x_vars)
            total_presses_all += machine_presses

    print(total_presses_all)


if __name__ == "__main__":
    solve()
