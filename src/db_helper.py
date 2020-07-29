import mysql.connector

class DbHelper:

    def get_maximum_salary(self,mycur):
        '''
        Implement the logic to find and return maximum salary from emplo        yee table
        '''        
        mycur.execute("select max(salary) from salaries")
        
        return mycur.fetchone()

    def get_minimum_salary(self,mycur):
        '''
        Implement the logic to find and return minimum salary from emplo        yee table
        '''
        mycur.execute("select min(salary) from salaries")

        return mycur.fetchone()

if __name__ == "__main__":
    mdb =mysql.connector.connect(host="localhost", user="dgdev", passwd     ="Hackuser@7",database = "employees")
    
    mycur=mdb.cursor(buffered=True)
    
    db_helper = DbHelper()
    minsal=db_helper.get_minimum_salary(mycur)
    maxsal=max_sal = db_helper.get_maximum_salary(mycur)

    print(minsal)
    print(maxsal)
    
   
