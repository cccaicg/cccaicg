/**
 * Registers this Controller to handle onActivityResult responses. Calling this method is NOT
 * necessary when calling {@link #startActivityForResult(Intent, int)}
 *
 * @param requestCode The request code being registered for.
 */
public final void registerForActivityResult(final int requestCode) 
{
    if (this.activityResultCallbacks == null)
    {
        this.activityResultCallbacks = new SparseArrayCompat<ActivityResultCallback>();
    }

    this.activityResultCallbacks.put(requestCode, null);
}   