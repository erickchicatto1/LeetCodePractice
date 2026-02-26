def twoPluses(grid):
    n = len(grid)
    m = len(grid[0])
    pluses = []
    
    # Convert grid to list of lists
    grid = [list(row) for row in grid]
    
    # Find all possible pluses
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 'G':
                k = 0
                cells = {(r, c)}
                pluses.append((1, cells.copy()))
                
                # Expand plus
                while True:
                    k += 1
                    new_cells = [
                        (r + k, c),
                        (r - k, c),
                        (r, c + k),
                        (r, c - k)
                    ]
                    
                    if all(0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 'G'
                           for nr, nc in new_cells):
                        for cell in new_cells:
                            cells.add(cell)
                        pluses.append((1 + 4 * k, cells.copy()))
                    else:
                        break
    
    max_product = 0
    
    # Compare all pairs
    for i in range(len(pluses)):
        for j in range(i + 1, len(pluses)):
            area1, cells1 = pluses[i]
            area2, cells2 = pluses[j]
            
            # Check no overlap
            if cells1.isdisjoint(cells2):
                max_product = max(max_product, area1 * area2)
    
    return max_product
