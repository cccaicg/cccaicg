/**
 * Parse of value of result set
 *
 * @param result the result set
 * @param i      the offset in the result set
 * @param type   the JDBC type
 * @param locale the locale to use for parsing
 * @return The parse value
 * @throws SQLException when SQL execution gives an error
 * @throws IOException  when input/output error occurs
 */
@Override
public Object parseType(ResultSet result, Integer i, int type, Locale locale)
        throws SQLException, IOException, ParseException 
{
    Object value = result.getObject(i, type);
    if (value == null)
    {
        return null;
    }
    else
    {
        return value;
    }
}       