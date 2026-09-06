function mult(strNum1, strNum2) {
  let s1 = String(strNum1).trim();
  let s2 = String(strNum2).trim();
  let negative = false;

  if (s1[0] === '+') {
    s1 = s1.slice(1);
  } else if (s1[0] === '-') {
    negative = !negative;
    s1 = s1.slice(1);
  }

  if (s2[0] === '+') {
    s2 = s2.slice(1);
  } else if (s2[0] === '-') {
    negative = !negative;
    s2 = s2.slice(1);
  }

  s1 = s1.replace(/^0+/, '') || '0';
  s2 = s2.replace(/^0+/, '') || '0';

  if (s1 === '0' || s2 === '0') {
    return '0';
  }

  const base = 10000;
  const chunkSize = 4;
  const a = [];
  const b = [];

  for (let i = s1.length; i > 0; i -= chunkSize) {
    a.push(parseInt(s1.slice(Math.max(0, i - chunkSize), i), 10));
  }

  for (let i = s2.length; i > 0; i -= chunkSize) {
    b.push(parseInt(s2.slice(Math.max(0, i - chunkSize), i), 10));
  }

  const result = new Array(a.length + b.length).fill(0);

  for (let i = 0; i < a.length; i++) {
    let carry = 0;

    for (let j = 0; j < b.length; j++) {
      const sum = result[i + j] + a[i] * b[j] + carry;
      result[i + j] = sum % base;
      carry = Math.floor(sum / base);
    }

    let pos = i + b.length;
    while (carry > 0) {
      if (pos === result.length) {
        result.push(0);
      }

      const sum = result[pos] + carry;
      result[pos] = sum % base;
      carry = Math.floor(sum / base);
      pos++;
    }
  }

  while (result.length > 1 && result[result.length - 1] === 0) {
    result.pop();
  }

  let output = String(result[result.length - 1]);

  for (let i = result.length - 2; i >= 0; i--) {
    let chunk = String(result[i]);

    while (chunk.length < chunkSize) {
      chunk = '0' + chunk;
    }

    output += chunk;
  }

  return negative ? '-' + output : output;
}
