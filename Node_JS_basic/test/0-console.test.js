const assert = require('assert');
const displayMessage = require('../0-console');

describe('displayMessage', () => {
  it('prints the provided string to stdout', () => {
    const logs = [];
    const originalLog = console.log;
    console.log = (msg) => logs.push(msg);

    displayMessage('Hello NodeJS!');

    assert.deepStrictEqual(logs, ['Hello NodeJS!']);

    console.log = originalLog;
  });
});
