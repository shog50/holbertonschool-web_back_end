import fs from 'fs';

function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }
      const lines = data.trim().split('\n');
      const students = {};
      lines.slice(1).forEach((line) => {
        const parts = line.split(',');
        const field = parts[3];
        const firstname = parts[0];
        if (!students[field]) {
          students[field] = [];
        }
        students[field].push(firstname);
      });
      resolve(students);
    });
  });
}

export default readDatabase;

