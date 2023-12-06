# CASH TRACKER
  * By Solomon Kaniaru

=====================================================

To help solve an issue I am facing rn:
decided to divert a little from the original idea.(The Subsription helper)

=====================================================

-> Python script to help me know my income and the sources
-> Have my Expenditures
-> calculate net worth
-> save all this in a DB (I only know mysql rn, I can also save in txt file)

======================================================

-> 1st run it on the command line.

======================================================
FEEDING THE SYSTEM WITH DATA
======================================================
-> select ADD DATA.
-> Enter type of data: Income, Expenditure
      * ____INCOME____
          - Enter source of income.
          - Enter Amount
          
      * ____Expenditure_______
          - What was spent on.
          - Amount spent
          
          
======================================================
VIEWING DATA STORED
======================================================
-> Select VIEW DATA
-> System display the data in tables:
           - income and expenduture
           
           


======================================================
DATA STORAGE AND RETRIEVAL
=======================================================
-> Save related data(income source, Amount) in tables
// I am thinking in SQL rn
       - Use the insert statement DML
-> Get the data 
       - Use the select statement DML
       - Have an umplified version that allows one to select data between time stamps.
       
       
       
================================================
 ARITHMETIC LOGIC
===============================================
 
 Populate a Total INCOME.
 	Income =+ NewIncome
 	
Populate a Total Expenditure.
	Expenditure =+ NewExpenditure
	
NetWorth = Income - Expenditure
// I am sure this is not how you get a networth of someone.__RESEARCH
 	
================================================
 IMPLEMENTATION
================================================
 
 Data insertion(Income):
        -> Time when the data was inserted
        -> Source
        -> Amount
        
 Data insertion(Expenditures):
        -> Time
        -> SpentOn
        -> Amount
 
 * DB TABLES:
	-> Incomes:
		Time, Source, Amount
	-> Expenditures:
		Time, SpentOn, Amount
 
 
 -> Have a class Income with attributes: Time, Source and Amount
 -> Have a class Expenditure with attributes: Time, SpentOn and Amount
 