const fs = require('fs');

const countStudents = (path) => {
  let data;
  try {
    data = fs.readFileSync(path, 'utf8');
  } catch (error) {
    throw new Error('Cannot load the database');
  }

  const lines = data.split('\n');
  const students = [];

  for (let i = 1; i < lines.length; i += 1) {
    const line = lines[i].trim();
    if (line) {
      const fields = line.split(',');
      if (fields.length === 4) {
        students.push(fields);
      }
    }
  }

  console.log(`Number of students: ${students.length}`);

  const fieldGroups = {};
  const fieldOrder = [];

  for (const student of students) {
    const field = student[3];
    if (!fieldGroups[field]) {
      fieldGroups[field] = [];
      fieldOrder.push(field);
    }
    fieldGroups[field].push(student[0]);
  }

  for (const field of fieldOrder) {
    console.log(`Number of students in ${field}: ${fieldGroups[field].length}. List: ${fieldGroups[field].join(', ')}`);
  }
};

module.exports = countStudents;
