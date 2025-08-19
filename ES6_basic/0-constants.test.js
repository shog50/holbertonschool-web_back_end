import { taskFirst, taskNext, getLast } from './0-constants.js';

test('taskFirst returns correct string', () => {
  expect(taskFirst()).toBe('I prefer const when I can.');
});

test('getLast returns correct string', () => {
  expect(getLast()).toBe(' is okay');
});

test('taskNext returns correct combination string', () => {
  expect(taskNext()).toBe('But sometimes let is okay');
});

