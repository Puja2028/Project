const { describe, it, beforeEach } = require('node:test');
const assert = require('node:assert/strict');
const http = require('node:http');

const store = require('../src/store');
const { createServer, validateTransaction } = require('../src/server');

function request(server, method, path, body) {
  return new Promise((resolve, reject) => {
    const port = server.address().port;
    const req = http.request(
      { hostname: '127.0.0.1', port, path, method, headers: { 'Content-Type': 'application/json' } },
      (res) => {
        let data = '';
        res.on('data', (chunk) => { data += chunk; });
        res.on('end', () => {
          resolve({ status: res.statusCode, body: data ? JSON.parse(data) : null });
        });
      }
    );
    req.on('error', reject);
    if (body) req.write(JSON.stringify(body));
    req.end();
  });
}

describe('validateTransaction', () => {
  it('rejects non-positive amount', () => {
    const errors = validateTransaction({ amount: -1, type: 'credit', description: 'x' });
    assert.ok(errors.length > 0);
  });
});

describe('HTTP API', () => {
  let server;

  beforeEach(() => {
    store.reset();
    server = createServer();
    server.listen(0);
  });

  it('creates and lists transactions', async () => {
    const created = await request(server, 'POST', '/transactions', {
      amount: 50,
      type: 'credit',
      description: 'Salary',
    });
    assert.equal(created.status, 201);
    assert.equal(created.body.id, 1);

    const listed = await request(server, 'GET', '/transactions');
    assert.equal(listed.status, 200);
    assert.equal(listed.body.transactions.length, 1);
  });

  it('calculates balance', async () => {
    await request(server, 'POST', '/transactions', {
      amount: 100,
      type: 'credit',
      description: 'Deposit',
    });
    await request(server, 'POST', '/transactions', {
      amount: 30,
      type: 'debit',
      description: 'Groceries',
    });

    const balance = await request(server, 'GET', '/balance');
    assert.equal(balance.status, 200);
    assert.equal(balance.body.balance, 70);
    assert.equal(balance.body.transaction_count, 2);
  });

  it('rejects invalid payload', async () => {
    const response = await request(server, 'POST', '/transactions', {
      amount: 0,
      type: 'credit',
      description: 'Bad',
    });
    assert.equal(response.status, 400);
  });
});
