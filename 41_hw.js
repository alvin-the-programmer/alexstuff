const shortestAlternatingPaths = (n, red_edges, blue_edges) =>  {
  const graph = makeGraph(n, red_edges, blue_edges);

  const result = [];

  for (let i = 0; i < n; i += 1) {
    result.push(Infinity);
  }

  const memo = {};
  for (let i = 0; i < n; i += 1) {
    result[i] = Math.min(result[i], calcMinAltPath(graph, 0, i, 'red', new Set(), '', memo));
    result[i] = Math.min(result[i], calcMinAltPath(graph, 0, i, 'blue', new Set(), '', memo));
  }

  return result.map(res => res === Infinity ? -1 : res);
};

const makeGraph = (n, redEdges, blueEdges) => {
const graph = {};

for (let i = 0; i < n; i += 1) {
  graph[i] = { red: [], blue: [] };
}

for (let redEdge of redEdges) {
  const [ src, dst ] = redEdge;
  graph[src].red.push(dst);
}

for (let blueEdge of blueEdges) {
  const [ src, dst ] = blueEdge;
  graph[src].blue.push(dst);
}

return graph;
};


const calcMinAltPath = (graph, node, target, thisColor, visited, visitedOrdered, memo) => {
const memoKey = `${node}#${target}#${thisColor}#${visitedOrdered}`;
if (memoKey in memo) {
  console.log('hit');
  return memo[memoKey];
}

const visKey = node + ',' + thisColor;
if (visited.has(visKey)) {
  return Infinity;
}

if (node === target) {
  return 0;
}

visited.add(visKey);
visitedOrdered += '|' + visKey;

const nextColor = thisColor === 'red' ? 'blue' : 'red';
const neighbors = graph[node][thisColor];
let bestPath = Infinity;
for (let neighbor of neighbors) {
  bestPath = Math.min(calcMinAltPath(graph, neighbor, target, nextColor, new Set(visited), visitedOrdered, memo), bestPath);
}

memo[memoKey] = 1 + bestPath;
return 1 + bestPath;
};