#!/usr/bin/env node
/**
 * I4 — Node.js CLI client for the currency convert service.
 * Usage: node cli.js <amount> <from> <to>
 */

const http = require('http');

const BASE_URL = process.env.CONVERT_URL || 'http://127.0.0.1:8001';

function convert(amount, fromCurrency, toCurrency) {
  const payload = JSON.stringify({
    amount: Number(amount),
    from_currency: fromCurrency,
    to_currency: toCurrency,
  });

  return new Promise((resolve, reject) => {
    const url = new URL('/convert', BASE_URL);
    const req = http.request(
      {
        hostname: url.hostname,
        port: url.port || 80,
        path: url.pathname,
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Content-Length': Buffer.byteLength(payload),
        },
      },
      (res) => {
        let data = '';
        res.on('data', (chunk) => { data += chunk; });
        res.on('end', () => {
          if (res.statusCode >= 400) {
            return reject(new Error(`API error ${res.statusCode}: ${data}`));
          }
          resolve(JSON.parse(data));
        });
      }
    );
    req.on('error', reject);
    req.write(payload);
    req.end();
  });
}

async function main() {
  const [, , amount, from, to] = process.argv;
  if (!amount || !from || !to) {
    console.error('Usage: node cli.js <amount> <from_currency> <to_currency>');
    process.exit(1);
  }

  try {
    const result = await convert(amount, from, to);
    console.log(
      `${result.amount} ${result.from_currency} = ${result.converted_amount} ${result.to_currency} (rate: ${result.rate})`
    );
  } catch (err) {
    console.error(err.message);
    process.exit(2);
  }
}

if (require.main === module) {
  main();
}

module.exports = { convert };
