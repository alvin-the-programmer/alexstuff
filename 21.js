const maxAreaOfIsland = (grid) => {
  const visited = new Set();
  
  let maxArea = 0;
  for (let r = 0; r < grid.length; r += 1) {
    for (let c = 0; c < grid[0].length; c += 1) {
      maxArea = Math.max(maxArea, unexploredIslandArea(grid, r, c, visited));
    }
  }

  return maxArea;
};

const unexploredIslandArea = (grid, r, c, visited) => {
  if (r < 0 || r >= grid.length)
    return 0;
    
  if (c < 0 || c >= grid[0].length)
    return 0;
  
  if (grid[r][c] === 0)
    return 0;

  const key = r + ',' + c;
  
  if (visited.has(key))
    return 0;
  
  visited.add(key);

  return unexploredIslandArea(grid, r + 1, c, visited)
    + unexploredIslandArea(grid, r - 1, c, visited)
    + unexploredIslandArea(grid, r, c + 1, visited)
    + unexploredIslandArea(grid, r, c - 1, visited)
    + 1;
};