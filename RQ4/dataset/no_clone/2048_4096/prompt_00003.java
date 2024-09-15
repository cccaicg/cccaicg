/**
 * isToBeIncluded function works in 2 modes,
 * 1. ID mode : exclude if the ID is present.
 * 2. Index mode: exclude a specific index.
 *
 * @param view  the view to be checked for exclusion.
 * @param index index of the view/
 * @return true of the view is to be included else excluded.
 */
public boolean isToBeIncluded(View view, int index) 
{
    if (mMode == ID_MODE)
    {
        return !mIds.contains(view.getId());
    }
    else
    {
        return index != mIndex;
    }
}   