/**
 * Retrieve the number of objects in the object, recursive method
 *
 * @return int the total object count for the object.
 */
public int getNumObjects() 
{
    int count = 0;
    for (Object obj : objects)
    {
        if (obj instanceof GameObject)
        {
            count++;
            count += ((GameObject) obj).getNumObjects();
        }
    }
    return count;
}   