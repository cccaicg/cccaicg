/**
 * Gets the coordinates of the main action view
 * This method should only be called after the main layout of the Activity is drawn,
 * such as when a user clicks the action button.
 * @return a Point containing x and y coordinates of the top left corner of action view
 */
private Point getActionViewCoordinates() 
{
    int[] location = new int[2];
    actionView.getLocationOnScreen(location);
    return new Point(location[0], location[1]);
}   