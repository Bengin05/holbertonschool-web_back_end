import createEmployeesObject from './11-createEmployeesObject.js';

export default function createReportObject(employeesList) {
  // eslint-disable-next-line no-unused-vars
  const unused = createEmployeesObject;
  return {
    allEmployees: employeesList,
    getNumberOfDepartments(employees) {
      return Object.keys(employees).length;
    },
  };
}
