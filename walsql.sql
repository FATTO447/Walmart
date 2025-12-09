Use walmart;
DROP TABLE if exists  walmart_sales  ;

CREATE TABLE walmart_sales (
	store INT, 
	Date_d DATE, 
    weekly_sales FLOAT, 
    holiday_flag INT, 
    temperature FLOAT, 
    fuel_price FLOAT, 
    CPI FLOAT, 
    Unemployment FLOAT, 
    Year INT, 
    month VARCHAR(10), 
    WeekOfYear INT, 
    DayOfWeek VARCHAR(10),  
    Holiday_name VARCHAR(20) , 
    PRIMARY KEY (store, Date_d) 
);
