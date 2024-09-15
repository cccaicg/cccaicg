/**
	 * Shuts down the ServiceLocator and releases any used resources.
	 */
public synchronized void shutdown(){
		if (this.beanFactoryReference != null) {
			this.beanFactoryReference.release();
			this.beanFactoryReference = null;
		}
	}