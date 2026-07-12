const fs = require('fs');

let html = fs.readFileSync('public/index.html', 'utf8');

const oldBrix = '<span class="l-y">B</span><span class="l-r">R</span><span class="l-b">I</span><span class="l-g">X</span>';
const newStudz = '<span class="l-y">S</span><span class="l-r">T</span><span class="l-b">U</span><span class="l-g">D</span><span class="l-y">Z</span>';

html = html.replace(oldBrix, newStudz);

fs.writeFileSync('public/index.html', html);
fs.writeFileSync('index.html', html);

console.log('Fixed BRIX text to STUDZ');
