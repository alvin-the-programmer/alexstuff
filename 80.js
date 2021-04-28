const foo = (n) => {
  const potato = [1,2,3,4,5]
  console.log(n);
  foo(n + 1);
};

foo(0);