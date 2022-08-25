-- 181. Employees Earning More Than Their Managers
-- SQL Schema
-- Table: Employee
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | name        | varchar |
-- | salary      | int     |
-- | managerId   | int     |
-- +-------------+---------+
-- id is the primary key column for this table.
-- Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.
-- Write an SQL query to find the employees who earn more than their managers.
-- Return the result table in any order.
-- The query result format is in the following example.


SELECT emp.name as Employee
FROM Employee as emp
    JOIN 
    Employee as man
ON emp.managerId = man.id
WHERE emp.salary > man.salary;



