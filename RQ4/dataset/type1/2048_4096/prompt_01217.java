/**
 * Add a listener that will be invoked whenever the page changes or is incrementally
 * scrolled. See {@link OnPageChangeListener}.
 *
 * <p>Components that add a listener should take care to remove it when finished.
 * Other components that take ownership of a view may call {@link #clearOnPageChangeListeners()}
 * to remove all attached listeners.</p>
 *
 * @param listener listener to add
 */
import java.util.ArrayList;
public void addOnPageChangeListener(OnPageChangeListener listener) 
{
    if (mOnPageChangeListeners == null)
    {
        mOnPageChangeListeners = new ArrayList<>();
    }
    mOnPageChangeListeners.add(listener);
}   