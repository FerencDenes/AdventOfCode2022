const fs = require("fs");

const content = fs.readFileSync("06.in").toString();
var [a, b, c, d] = ["x", "x", "x", "x"];
content.split("").every((element, index) => {
  [a, b, c, d] = [b, c, d, element];
  if (index > 3 && a != b && a != c && a != d && b != c && b != d && c != d) {
    console.log(index + 1);
    return false;
  }
  return true;
});

const set = new Set();
const arr = new Array(14);
content.split("").every((element, index) => {
  arr.shift();
  arr.push(element);
  set.clear();
  arr.forEach((element) => {
    set.add(element);
  });
  if (set.size == 14) {
    console.log(index + 1);
    return false;
  }
  return true;
});
