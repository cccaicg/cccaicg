/**
 * Close read connection
 */

@Override
public StandardSource<C> closeReading() 
{
    if (this.reader != null)
    {
        try
        {
            this.reader.close();
        }
        catch (IOException e)
        {
            throw new RuntimeException(e);
        }
    }
    return this;
}   