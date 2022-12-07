function replacer(key, value) {
  if (key === "parent") {
    return "";
  }
  if (value instanceof Map) {
    return {
      value: Array.from(value.entries()), // or with spread: value: [...value]
    };
  } else {
    return value;
  }
}

const mkdir = (parent) => {
  return {
    parent,
    dirs: new Map(),
    files: new Map(),
    size: null,
  };
};
const fs = require("fs");
const content = fs.readFileSync("07.in").toString();

const root = mkdir("/");

let pwd = root;
content.split("\n").forEach((line) => {
  // console.log(JSON.stringify(root, replacer));
  if (line) {
    if (line.startsWith("$")) {
      if (line[2] == "c") {
        if (line[5] == "/") {
          pwd = root;
        } else if (line.substring(5) == "..") {
          pwd = pwd.parent;
        } else {
          if (!pwd.dirs.has(line.substring(5))) {
            pwd.dirs.set(line.substring(5), mkdir(pwd));
          }
          pwd = pwd.dirs.get(line.substring(5));
        }
      }
    } else {
      if (line.startsWith("dir")) {
        if (!pwd.dirs.has(line.substring(4))) {
          pwd.dirs.set(line.substring(4), mkdir(pwd));
        }
      } else {
        [size, name] = line.split(" ");
        pwd.files.set(name, parseInt(size));
      }
    }
  }
});
const du = (dir) => {
  if (!dir.size) {
    dir.size = 0;
    for (const val of dir.dirs.values()) {
      dir.size += du(val);
    }
    for (const val of dir.files.values()) {
      dir.size += val;
    }
  }
  return dir.size;
};
du(root);
// console.log(JSON.stringify(root, replacer, 2));

let sumSmall = 0;
const sumSmallFn = (dir) => {
  if (dir.size <= 100000) {
    sumSmall += dir.size;
  }
  for (const child of dir.dirs.values()) {
    sumSmallFn(child);
  }
};
sumSmallFn(root);
console.log(sumSmall);
const totalSize = 70000000;
const unusedSpace = 30000000;
const occupiedSize = du(root);
const freeSize = totalSize - occupiedSize;
const toFree = unusedSpace - freeSize;
let minFree = unusedSpace;
const getMinFree = (dir) => {
  if (dir.size > toFree && dir.size < minFree) {
    minFree = dir.size;
  }
  for (const child of dir.dirs.values()) {
    getMinFree(child);
  }
};
getMinFree(root);
console.log(minFree);
