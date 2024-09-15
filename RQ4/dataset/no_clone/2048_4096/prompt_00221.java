/**
 * 得到种子日期所在周的周日
 *
 * @param seedDate 种子日期
 * @return CalendarDate 所在周周日
 */
public static CalendarDate getSunday(CalendarDate seedDate) 
{
    CalendarDate sunday = new CalendarDate(seedDate);
    sunday.add(Calendar.DAY_OF_MONTH, 7 - sunday.getDayOfWeek().getValue());
    return sunday;
}   