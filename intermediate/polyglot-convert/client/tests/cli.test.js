const { describe, it } = require('node:test');
const assert = require('node:assert/strict');
const { convert } = require('../cli');

describe('convert client (mocked via module export)', () => {
  it('module exports convert function', () => {
    assert.equal(typeof convert, 'function');
  });
});
