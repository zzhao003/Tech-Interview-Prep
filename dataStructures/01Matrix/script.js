var updateMatrix = function (mat) {
  // make a queue with all the none zeros
  let q = [];
  for (let i = 0; i < mat.length; i++) {
    for (let j = 0; j < mat[0].length; j++) {
      console.log("testing");
      // if(mat[i][j]== 0) {console.log('testing')}
      // else mat[i][j] = '#'
    }
  }
  // console.log(q)
  // let k = 0;
  // while(q){
  //     let row = q[k][0];
  //     let column = q[k][1];
  //     let dir = [[1,0],[-1,0],[0,1],[0,-1]]
  //     for(let l=0; l<dir.length; l++){
  //         let nr = row + dir[l][0];
  //         let nc = column + dir[l][1];
  //         if(0< nr <=mat && 0< nc <=mat[0] && mat[nr][nc] == '#'){
  //            mat[row][column] = mat[nr][nc] + 1;
  //            q.push([nr][nc])
  //         }
  //     }
  //     q.shift()
  //     k++;
  // }
  // return mat
};
let mat = [
  [0, 0, 0],
  [0, 1, 0],
  [0, 0, 0],
];

updateMatrix(mat);
