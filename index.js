const lowercase = document.getElementById("lowercase");
const uppercase = document.getElementById("uppercase");
const number = document.getElementById("number");
const specialchar = document.getElementById("specialchar");
const mybutton = document.getElementById("mybutton");
const result = document.getElementById("result");

mybutton.onclick = function () {
  const len = document.getElementById("len").value;
  const l = "abcdefghijklmnopqrstuvwxyz";
  const u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  const n = "0123456789";
  const chars = "$_@#!%&*()/";

  let res = "";
  let password = "";

  res += lowercase.checked ? l : "";
  res += uppercase.checked ? u : "";
  res += specialchar.checked ? chars : "";
  res += number.checked ? n : "";

  if (len <= 0) {
    result.textContent = `atleast the length must be 1`;
    return;
  }

  if (res.length === 0) {
    result.textContent = `atleast one checked must be selected `;
    return;
  }

  for (let i = 0; i < len; i++) {
    let randomIndex = Math.floor(Math.random() * res.length);
    password += res[randomIndex];
  }
  result.textContent = `password:${password}`;
};
