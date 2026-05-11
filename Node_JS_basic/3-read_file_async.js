const fs = require('fs');

module.exports = function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const students = data.split('\n');
      const fieldGroups = {};
      students.forEach((element) => {
        const result = element.split(',');
        if (element !== '' && result[0] !== 'firstname') {
          const domain = result[3];
          if (!fieldGroups[domain]) {
            fieldGroups[domain] = [];
          }
          fieldGroups[domain].push(result[0]);
        }
      });
      let sumResult = 0;
      for (const domain in fieldGroups) {
        if (Object.prototype.hasOwnProperty.call(fieldGroups, domain)) {
          sumResult += fieldGroups[domain].length;
        }
      }
      console.log(`Number of students: ${sumResult}`);

      for (const domain in fieldGroups) {
        if (Object.prototype.hasOwnProperty.call(fieldGroups, domain)) {
          const list = fieldGroups[domain].join(', ');
          console.log(`Number of students in ${domain}: ${fieldGroups[domain].length}. List: ${list}`);
        }
      }

      resolve();
    });
  });
};
