/*
 * Restore size and visibility for all listitems
 */
private void unExpandViews(boolean deletion) 
{
    int deleteCount = mListView.getCount();

    for (int i = 0; i < deleteCount; ++i)
    {
        View v = mListView.getChildAt(i);
        if (v != null)
        {
            View w = v.findViewById(R.id.list_item);
            if (deletion)
            {
                w.setVisibility(View.VISIBLE);
            }
            else
            {
                w.setVisibility(View.VISIBLE);
            }
        }
    }
}   