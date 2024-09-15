/**
 * You can call this function yourself to have the scroll view perform
 * scrolling from a key event, just as if the event had been dispatched to
 * it by the view hierarchy.
 *
 * @param event The key event to execute.
 * @return Return true if the event was handled, else false.
 */
public boolean executeKeyEvent(KeyEvent event) 
{
    keyDown();
    switch (event.getAction()) {
        case KeyEvent.ACTION_DOWN:
            return onKeyDown(event.getKeyCode(), event);
        case KeyEvent.ACTION_UP:
            return onKeyUp(event.getKeyCode(), event);
        default:
            return false;
    }
}   