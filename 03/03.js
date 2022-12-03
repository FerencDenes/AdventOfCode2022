const fs = require("fs");

const content = fs.readFileSync("03.in").toString();
const letters = new Array(52);
const letters2 = new Array(52);
letters2.fill(0);
let sum = 0;
let sum2 = 0;
function getCode(line, i) {
  let code = line.charCodeAt(i);
  code = code <= 90 ? code - 65 + 27 : code - 97 + 1;
  return code;
}
let lineNo = 1;
content
  .split(/\n/)
  .filter((line) => line.length)
  .forEach((line) => {
    letters.fill(0);
    let i = 0;
    for (; i < line.length / 2; ++i) {
      letters[getCode(line, i)] = 1;
    }
    while (!letters[getCode(line, i)]) {
      ++i;
    }
    sum += getCode(line, i);

    if (lineNo == 3) {
      lineNo = 1;
      let i = 0;
      while (letters2[getCode(line, i)] != 3) {
        ++i;
      }

      sum2 += getCode(line, i);
      letters2.fill(0);
    } else {
      for (const ch of line) {
        letters2[getCode(ch, 0)] |= lineNo;
      }
      lineNo++;
    }
  });

console.log(sum);
console.log(sum2);
