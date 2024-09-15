/**
 * Sets whether this transfer is active, i.e., if the connection is still established.
 *
 * @param active Whether this transfer is active.
 */
public void setActive(boolean active) 
{
    if (active)
    {
        this.active = true;
    }
    else
    {
        this.active = false;
        this.cancel();
    }
}   