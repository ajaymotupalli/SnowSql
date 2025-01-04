-- Highest Salaries for Departments
--------------------------------------------------------------------------------

select distinct department, salary
from employees
where department = 'Engineering';

---------------------------------------------------------------------------------

-- First Highest Salary at particular department

select max(salary) as first_highest_salary
from employees
where department = 'Engineering';

---------------------------------------------------------------------------------

-- Second Highest Salary at particular department

select max(salary) as second_highest_salary
from employees
where department = 'Engineering'
    and salary < (select max(salary)
    from employees
    where department = 'Engineering');

-- or --

with
    rankedlist
    as
    (
        select salary,
            row_number() over (order by salary desc) as rank
        from employees
        where department = 'Engineering'
        group by salary
    )
select salary, rank
from rankedlist
where rank = 2;

---------------------------------------------------------------------------------

-- Third Highest Salary at particular department

select max(salary) as third_highest_salary
from employees
where department = 'Engineering'
    and salary < (
    select max(salary)
    from employees
    where department = 'Engineering'
<
(
        select max(salary)
from employees
where department = 'Engineering')
);

-- or --

with
    rankedlist
    as
    (
        select salary,
            row_number() over (order by salary desc) as rank
        from employees
        where department = 'Engineering'
        group by salary
    )
select salary, rank
from rankedlist
where rank = 3;

---------------------------------------------------------------------------------

-- Fourth Highest Salary at particular department

select distinct max(salary) as Fourth_highest_salary
from employees
where department = 'Engineering'
    and salary < (
    select max(salary)
    from employees
    where department = 'Engineering'
<
(
        select max(salary)
from employees
where department = 'Engineering'
<
(
            select max(salary)
from employees
where department = 'Engineering'
            )
)
    );

-- or --

with
    rankedlist
    as
    (
        select salary,
            row_number() over (order by salary desc) as rank
        from employees
        where department = 'HR'
        group by salary
    )
select salary, rank
from rankedlist
where rank = 4;

---------------------------------------------------------------------------------

-- First 3 Highest Salary at particular department

with
    rankedlist
    as

    (
        select salary,
            row_number() over (order by salary desc) as rank
        from employees
        where department = 'Engineering'
        group by salary
    )
select salary, rank as rankslist
from rankedlist
where rank <= 3;

---------------------------------------------------------------------------------
---------------------------------------------------------------------------------

-- First Highest Salary at Each department

select department, max(salary) as highest_salary
from employees
group by department;

---------------------------------------------------------------------------------

-- Second Highest Salary at Each department

with
    rankedlist
    as
    (
        select distinct department,
            salary,
            dense_rank() over (partition by department order by salary desc) as rank
        from employees
    )
select department, salary as second_highest_salaries
from rankedlist
where rank = 3;

---------------------------------------------------------------------------------

-- First 2 Highest Salaries at Each department

with
    rankedlist
    as
    (
        select distinct department,
            salary,
            dense_rank() over (partition by department order by salary desc) as rank
        from employees
    )
select department, salary as second_highest_salaries
from rankedlist
where rank <= 2;

---------------------------------------------------------------------------------
-- First 2 Highest Salaries for Engineering Department with Department name
with
    rankedlist
    as
    (
        select department,
            salary,
            dense_rank() over (partition by department order by salary desc) as ranked_sal
        from employees
        where department = 'Engineering'
    )
select distinct department, salary, ranked_sal
from rankedlist
where ranked_sal <= 2;