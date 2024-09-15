/**
 * Call this method after you handle a keypress so that the meta state will be reset to
 * unshifted (if it is not still down) or primed to be reset to unshifted (once it is released).
 * Takes the current state, returns the new state.
 */
public static long adjustMetaAfterKeypress(long state) 
{
    if ((state & SHIFT_DOWN_MASK) != 0)
    {
        state |= SHIFT_PRIMED_MASK;
    }
    else
    {
        state &= ~SHIFT_PRIMED_MASK;
    }
    return state & ~SHIFT_DOWN_MASK;
}   