/* 
task1_1.sql 
Procedure Employee_hire_sp 
*/

CREATE OR REPLACE PROCEDURE Employee_hire_sp (
    p_first_name    IN HR_EMPLOYEES.FIRST_NAME%TYPE,
    p_last_name     IN HR_EMPLOYEES.LAST_NAME%TYPE,
    p_email         IN HR_EMPLOYEES.EMAIL%TYPE,
    p_salary        IN HR_EMPLOYEES.SALARY%TYPE,
    p_hire_date     IN HR_EMPLOYEES.HIRE_DATE%TYPE,
    p_phone         IN HR_EMPLOYEES.PHONE_NUMBER%TYPE,
    p_job_id        IN HR_EMPLOYEES.JOB_ID%TYPE,
    p_manager_id    IN HR_EMPLOYEES.MANAGER_ID%TYPE,
    p_department_id IN HR_EMPLOYEES.DEPARTMENT_ID%TYPE
) AS
BEGIN
    INSERT INTO HR_EMPLOYEES (
        EMPLOYEE_ID,
        FIRST_NAME,
        LAST_NAME,
        EMAIL,
        PHONE_NUMBER,
        HIRE_DATE,
        JOB_ID,
        SALARY,
        MANAGER_ID,
        DEPARTMENT_ID
    ) VALUES (
        HR_EMPLOYEES_SEQ.NEXTVAL,
        p_first_name,
        p_last_name,
        p_email,
        p_phone,
        p_hire_date,
        p_job_id,
        p_salary,
        p_manager_id,
        p_department_id
    );
    
    COMMIT;
END Employee_hire_sp;

/*
Test for the Procedure
*/
BEGIN
    Employee_hire_sp(
        p_first_name    => 'Julian',
        p_last_name     => 'Aristizabal',
        p_email         => 'juliandres1227@gmail.com',
        p_salary        => 6000,
        p_hire_date     => TO_DATE('2024-04-01', 'YYYY-MM-DD'),
        p_phone         => '4379918059',
        p_job_id        => 'IT_PROG',
        p_manager_id    => 103,
        p_department_id => 60
    );
END;
