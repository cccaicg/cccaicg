////////////////end of event///////////////////////////
@Override
public synchronized void registerDispatcher(IBinder dispatcherBinder) throws RemoteException 
{
    if (dispatcherBinder == null) {
        throw new NullPointerException("null dispatcher");
    }
    if (mDispatcher != null) {
        throw new IllegalStateException("dispatcher already set");
    }
    mDispatcher = IDispatcher.Stub.asInterface(dispatcherBinder);
    notifyAll();
}   