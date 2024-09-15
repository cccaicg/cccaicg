/**
 * Close result set
 *
 * @param result the result set to be closed or null
 * @throws SQLException when SQL execution gives an error
 */
@Override
public StandardSource<C> close(ResultSet result) throws SQLException 
{
    if (result != null)
    {
        result.close();
    }
    return this;
}   