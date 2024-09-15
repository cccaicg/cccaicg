/**
 * Initializes HashBuilder.  This should be called only once.  Well, it can
 * be called more often, but it won't do anything past the first time.
 */
public static synchronized void initialize(Context c) 
{
    if (mInitialized)
        return;

    mInitialized = true;
    mInstance = new HashBuilder(c);
}   