

// const board = [
//   "abcde",
//   "fghij",
//   "klmno",
//   "pqrst",
//   "uvwxy",
//   "z"
// ];
// const alphabetBoardPath = (target) => {
//     const position = {};
//     for (let r = 0; r < board.length; r += 1) {
//       for (let c = 0; c < board[r].length; c += 1) {
//           position[board[r][c]] = [ r, c ];
//       }
//     }
//     let curr = [0, 0]
//     let output = '';
    
//     for(let i = 0; i < target.length; i++){
//         if (target[i] === 'z' && board[curr[0]][curr[1]] !== 'z') {
//           output += calculateDelta(curr, position['u'])
//           output += 'D'
//         } else {
//           output += calculateDelta(curr, position[target[i]])
//         }
//         output += '!'
//         curr = position[target[i]]
//     }

//     return output
//   };
const shortestPath = (board, target) => {
  const position = {};
  for(let r = 0; r < board.length; r++) {
    for(let c = 0; c < board[r].length; c++) {
      if (!(board[r][c] in position)) {
        position[board[r][c]] = []
      }
      position[board[r][c]].push([r, c])
    }
  }

  return shortestPathHelper(board, position, target, [0, 0]);
}

const shortestPathHelper = (board, position, target, src) => {
  if(target === '') {
    return '';
  }

  const firstLetter = target[0];
  const poss = position[firstLetter];

  let shortest_output = null;
  for(let i = 0; i < poss.length; i++) {
    const curr_str = calculateDelta(src, poss[i]);
    let output = curr_str + '!' + shortestPathHelper(board, position, target.slice(1), poss[i]); 
    if(shortest_output === null || output.length < shortest_output.length) {
      shortest_output = output
    }
  }

  return shortest_output;
  
}



const calculateDelta = (posA, posB) => {
  const [ rowA, colA ] = posA;
  const [ rowB, colB ] = posB;
  const deltaRow = rowA - rowB;
  const deltaCol = colA - colB;
  let moves = '';
  for (let i = 0; i < Math.abs(deltaRow); i += 1) {
    if (deltaRow < 0) {
      moves += 'D';
    } else {
      moves += 'U';
    }
  }
  for (let i = 0; i < Math.abs(deltaCol); i += 1) {
    if (deltaCol < 0) {
      moves += 'R';
    } else {
      moves += 'L';
    }
  }
  return moves;
}
const target = "fze";
const board = [
  "oabcqe",
  "ofghij",
  "zklmno",
  "oqrstu",
  "dvwxtz",
];

console.log(shortestPath(board, target)); // dr!urrr!r!




