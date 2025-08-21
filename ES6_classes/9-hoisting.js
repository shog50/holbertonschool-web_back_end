// Class representing a Holberton class
export class HolbertonClass {
  constructor(year, location) {
    this._year = year;       // store year with underscore version
    this._location = location; // store location with underscore version
  }

  // Getter for year
  get year() {
    return this._year;
  }

  // Getter for location
  get location() {
    return this._location;
  }
}

// Class representing a Holberton student
export class StudentHolberton {
  constructor(firstName, lastName, holbertonClass) {
    this._firstName = firstName;       // student's first name
    this._lastName = lastName;         // student's last name
    this._holbertonClass = holbertonClass; // student's Holberton class
  }

  // Getter for full name
  get fullName() {
    return `${this._firstName} ${this._lastName}`;
  }

  // Getter for the Holberton class object
  get holbertonClass() {
    return this._holbertonClass;
  }

  // Getter for full student description
  get fullStudentDescription() {
    return `${this._firstName} ${this._lastName} - ${this._holbertonClass.year} - ${this._holbertonClass.location}`;
  }
}

// Define Holberton class instances
const class2019 = new HolbertonClass(2019, 'San Francisco');
const class2020 = new HolbertonClass(2020, 'San Francisco');

// Define students
const student1 = new StudentHolberton('Guillaume', 'Salva', class2020);
const student2 = new StudentHolberton('John', 'Doe', class2020);
const student3 = new StudentHolberton('Albert', 'Clinton', class2019);
const student4 = new StudentHolberton('Donald', 'Bush', class2019);
const student5 = new StudentHolberton('Jason', 'Sandler', class2019);

// Export the list of students as default
export default [student1, student2, student3, student4, student5];

