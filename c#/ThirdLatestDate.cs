/*
 * Print third latest date
 
Examples

In:
6
14-04-2001
29-12-2061
21-10-2019
07-01-1973
19-07-2014
11-03-1992

Out: 19-07-2014
 
---------

In: 
7
14-04-2001
29-12-2061
21-10-2019
07-01-1973
19-07-2014
11-03-1992
21-10-2019

Out: 19-07-2014

 * Complete the function below.
 */
static Date ThirdLatest(Date[] dates) {
    Date date1 = GetInitialDate();
    Date date2 = GetInitialDate();
    Date date3 = GetInitialDate();
    
    foreach(var date in dates)
    {
        if (IsDateGreather(date, date1) || IsDateEquals(date, date1))
        {
            date1 = date;
        }
        else if (IsDateGreather(date, date2) || IsDateEquals(date, date2))
        {
            date2 = date;    
        } 
        else if (IsDateGreather(date, date3) || IsDateEquals(date, date3))
        {
            date3 = date;
        }
    }
    
    return date3;
}

static bool IsDateGreather(Date date1, Date date2)
{
    return (date1.Year > date2.Year)
        || (date1.Year == date2.Year && date1.Month > date2.Month)
        || (date1.Year == date2.Year && date1.Month == date2.Month && date1.Day > date2.Day);    
}

static bool IsDateEquals(Date date1, Date date2)
{
    return date1.Year == date2.Year 
            && date1.Month == date2.Month
            && date1.Day == date2.Day;    
}

static Date GetInitialDate()
{
    return new Date() { Year = 0, Month = 0, Day = 0 };
}