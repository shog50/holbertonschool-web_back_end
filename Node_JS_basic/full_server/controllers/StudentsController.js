import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(req, res) {
    const dbPath = process.argv[2];
    readDatabase(dbPath)
      .then((students) => {
        let response = 'This is the list of our students\n';
        const fields = Object.keys(students).sort((a, b) =>
          a.toLowerCase().localeCompare(b.toLowerCase())
        );
        fields.forEach((field) => {
          const list = students[field].join(', ');
          response += `Number of students in ${field}: ${students[field].length}. List: ${list}\n`;
        });
        res.status(200).send(response.trim());
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(req, res) {
    const { major } = req.params;
    const dbPath = process.argv[2];
    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }
    readDatabase(dbPath)
      .then((students) => {
        const list = students[major] || [];
        res.status(200).send(`List: ${list.join(', ')}`);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }
}

export default StudentsController;

