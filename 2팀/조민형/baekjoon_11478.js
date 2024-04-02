const INPUT = require("fs")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split("\n");
function solution() {
  console.log(INPUT);
}

module.exports = solution;
