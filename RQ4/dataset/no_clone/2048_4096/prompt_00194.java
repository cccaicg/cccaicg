/**
 * Get JDBC connection for reading
 *
 * @return the connection
 * @throws SQLException when SQL execution gives an error
 */
@Override
public synchronized Connection getConnectionForReading() throws SQLException 
{
    if (connectionForReading == null)
    {
        connectionForReading = createConnectionForReading();
    }
    return connectionForReading;
}   