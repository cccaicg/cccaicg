/**
 * Notify te view is closed to the left to the DraggableListener
 */
private void notifyCloseToLeftListener() 
{
    if (mCloseToLeftListener != null)
    {
        mCloseToLeftListener.onCloseToLeft();
    }
}   