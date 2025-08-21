import HolbertonCourse from './2-hbtn_course.js';

describe('HolbertonCourse constructor type checks', () => {
  test('should throw TypeError if name is not a string', () => {
    expect(() => {
      new HolbertonCourse(10, 20, ["Lucie", "Guillaume"]);
    }).toThrow(TypeError);
  });

  test('should throw TypeError if length is not a number', () => {
    expect(() => {
      new HolbertonCourse('PHP', '20', ["Lucie", "Guillaume"]);
    }).toThrow(TypeError);
  });

  test('should throw TypeError if students is not an array', () => {
    expect(() => {
      new HolbertonCourse('Python', 20, 'Lucie');
    }).toThrow(TypeError);
  });

  test('should create object correctly if types are valid', () => {
    const course = new HolbertonCourse('JavaScript', 6, ['Bob', 'Jane']);
    expect(course.name).toBe('JavaScript');
    expect(course.length).toBe(6);
    expect(course.students).toEqual(['Bob', 'Jane']);
  });
});

