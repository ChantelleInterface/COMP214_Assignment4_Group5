
import cx_Oracle

def create_employee_hire_sp():
    
    connection = None
    username = 'COMP214_W24_ers_77'
    password = 'passwords'
    dsn = '199.212.26.208:1521/SQLD'
    encoding = 'UTF-8'
    
    try:
        connection = cx_Oracle.connect(username, password, dsn, encoding=encoding)
        
        cursor = connection.cursor()
        
        sql_procedure = """
        
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
        
        """
        cursor.execute(sql_procedure)

        print("Procedure Employee_hire_sp created successfully!")

    except cx_Oracle.Error as error:
        print(f"Error creating procedure: {error}")
    finally:
        if connection:
            connection.close()
    
    try:
        connection = cx_Oracle.connect(username, password, dsn, encoding=encoding)
        
        cursor = connection.cursor()
        
        sql_statement = """
        
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
        
        """
        cursor.execute(sql_statement)

        print("Employee record created successfully!")

    except cx_Oracle.Error as error:
        print(f"Error creating procedure: {error}")
    finally:
        if connection:
            connection.close()

    try:
        connection = cx_Oracle.connect(username, password, dsn, encoding=encoding)
        
        cursor = connection.cursor()
        
        sql_statement = """

        CREATE OR REPLACE PROCEDURE new_job(
            p_jobid IN HR_JOBS.job_id%TYPE,
            p_title IN HR_JOBS.job_title%TYPE, 
            p_minsal IN HR_JOBS.min_salary%TYPE
        ) IS
            v_maxsal HR_JOBS.max_salary%TYPE := 2 * p_minsal;  
        BEGIN
            INSERT INTO HR_JOBS (job_id, job_title, min_salary, max_salary)
            VALUES (p_jobid, p_title, p_minsal, v_maxsal);

            DBMS_OUTPUT.PUT_LINE('New row added to JOBS table:');
            DBMS_OUTPUT.PUT_LINE(p_jobid || ' | ' || p_title || ' | ' || p_minsal || ' | ' || v_maxsal);
        END new_job;

        """

        cursor.execute(sql_procedure)

        print("Procedure new_job created successfully!")

    except cx_Oracle.Error as error:
        print(f"Error creating procedure: {error}")
    finally:
        if connection:
            connection.close()

if __name__ == "__main__":
    create_employee_hire_sp()
    
