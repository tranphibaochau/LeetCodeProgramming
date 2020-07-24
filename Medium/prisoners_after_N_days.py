"""
There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)

"""
def prisonAfterNDays(cells, N) -> List[int]:
        seen = {} #a dictionary to find the patterns
        n = 0
        prev = cells.copy()
        remaining = 0
        if N == 0:
            return cells
        #if N > 0, first and last cells are always empty
        cells[0] = 0
        cells[-1] = 0
        #running the simulation until either the N-th day (if N is sufficiently small) or until we find a pattern
        while True:
            n+=1
            for i in range(1, len(cells)-1):
                if prev[i-1] == prev[i+1]:
                    cells[i] = 1
                else:
                    cells[i] = 0
            cell_key = tuple(cells)
            if cell_key in seen: #once the pattern is seen, we will fast forward it and the the target date's pattern
                break
            elif cell_key not in seen: #if the pattern is not yet repeated, keep storing new patterns
                seen[cell_key] = n
                prev = cells.copy()
            if n == N: #if N is smaller than the number of days it takes until we recognize a cycle, just return the cell
                return cells
        #because we don't store the pattern of day 0, we will convert it into day n-1
        remaining= N%(n-1)
        if remaining == 0:
            remaining = n-1
        for cell in seen:
            if seen[cell] == remaining:
                return list(cell)
            