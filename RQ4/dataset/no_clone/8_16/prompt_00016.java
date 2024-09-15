/**
 * Move selected Pictures down
 */




public static void movePicturesDown() 
{
    ISelection selection = getSite().getSelectionProvider().getSelection();
    if (selection instanceof IStructuredSelection)
    {
        IStructuredSelection structuredSelection = (IStructuredSelection) selection;
        Iterator<?> iterator = structuredSelection.iterator();
        List<IPicture> pictures = new ArrayList<IPicture>();
        while (iterator.hasNext())
        {
            Object next = iterator.next();
            if (next instanceof IPicture)
            {
                pictures.add((IPicture) next);
            }
        }
        if (!pictures.isEmpty())
        {
            movePicturesDown(pictures);
        }
    }
}   