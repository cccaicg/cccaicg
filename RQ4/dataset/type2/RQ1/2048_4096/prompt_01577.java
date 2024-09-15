/**
 * Notify te view is minimized to the DraggableListener
 */
private void notifyMinimizeToListener() 
{
    if (mDraggableListener != null)
    {
        mDraggableListener.onMinimize();
    }
}   