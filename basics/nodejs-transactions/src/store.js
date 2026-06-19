let nextId = 1;
const transactions = [];

function add({ amount, type, description }) {
  const txn = { id: nextId++, amount, type, description };
  transactions.push(txn);
  return txn;
}

function listAll() {
  return [...transactions];
}

function balance() {
  return transactions.reduce((total, txn) => {
    return txn.type === 'credit' ? total + txn.amount : total - txn.amount;
  }, 0);
}

function reset() {
  transactions.length = 0;
  nextId = 1;
}

module.exports = { add, listAll, balance, reset };
