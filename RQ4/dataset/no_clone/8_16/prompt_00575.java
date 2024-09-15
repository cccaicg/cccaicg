/*
 * (non-Javadoc)
 * @see java.awt.event.MouseListener#mouseClicked(java.awt.event.MouseEvent)
 */
@Override
public final void mouseClicked(final MouseEvent e) 
{
    if (e.getButton() == MouseEvent.BUTTON1)
    {
        if (e.getClickCount() == 2)
        {
            // double click
            this.doubleClick(e);
        }
        else
        {
            // single click
            this.singleClick(e);
        }
    }
}   