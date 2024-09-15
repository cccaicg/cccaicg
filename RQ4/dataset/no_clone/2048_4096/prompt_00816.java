/*
 * (non-Javadoc)
 * 
 * @see lbms.plugins.mldht.kad.DHTBase#update()
 */
public void update () 
{
    try
    {
        if (isRunning())
        {
            if (isBootstraped())
            {
                bootstrap();
            }
            else
            {
                refreshBucket();
            }
        }
    }
    catch (Exception e)
    {
        log.error("Error updating DHT", e);
    }
}   