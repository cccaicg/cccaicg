/**
	 * Shuts down the ServiceLocator and releases any used resources.
	 */
public synchronized void shutdown() 
{
	if (this.locator != null)
	{
		this.locator.shutdown();
		this.locator = null;
	}
}	