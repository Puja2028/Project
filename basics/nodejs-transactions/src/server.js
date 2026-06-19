const store = require('./store');

function validateTransaction(body) {
  const errors = [];
  if (typeof body.amount !== 'number' || body.amount <= 0) {
    errors.push('amount must be a positive number');
  }
  if (!['credit', 'debit'].includes(body.type)) {
    errors.push('type must be credit or debit');
  }
  if (!body.description || typeof body.description !== 'string' || body.description.trim() === '') {
    errors.push('description is required');
  }
  return errors;
}

function parseJson(req) {
  return new Promise((resolve, reject) => {
    let data = '';
    req.on('data', (chunk) => { data += chunk; });
    req.on('end', () => {
      try {
        resolve(data ? JSON.parse(data) : {});
      } catch {
        reject(new Error('Invalid JSON'));
      }
    });
  });
}

function sendJson(res, status, payload) {
  res.writeHead(status, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify(payload));
}

function createServer() {
  const http = require('http');

  return http.createServer(async (req, res) => {
    const url = new URL(req.url, 'http://localhost');

    if (req.method === 'GET' && url.pathname === '/health') {
      return sendJson(res, 200, { status: 'ok' });
    }

    if (req.method === 'POST' && url.pathname === '/transactions') {
      try {
        const body = await parseJson(req);
        const errors = validateTransaction(body);
        if (errors.length) {
          return sendJson(res, 400, { errors });
        }
        const txn = store.add(body);
        return sendJson(res, 201, txn);
      } catch {
        return sendJson(res, 400, { error: 'Invalid request body' });
      }
    }

    if (req.method === 'GET' && url.pathname === '/transactions') {
      return sendJson(res, 200, { transactions: store.listAll() });
    }

    if (req.method === 'GET' && url.pathname === '/balance') {
      const transactions = store.listAll();
      return sendJson(res, 200, {
        balance: store.balance(),
        transaction_count: transactions.length,
      });
    }

    sendJson(res, 404, { error: 'Not found' });
  });
}

module.exports = { createServer, validateTransaction };
