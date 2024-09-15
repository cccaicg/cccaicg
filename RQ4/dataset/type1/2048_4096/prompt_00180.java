/**
 * Close statement
 *
 * @param statement the statement to be closed or null
 * @throws SQLException when SQL execution gives an error
 */
@Override
public StandardSource<C> close(Statement statement) throws SQLException 
{
    if (statement != null)
    {
        statement.close();
    }
    return this;
}   