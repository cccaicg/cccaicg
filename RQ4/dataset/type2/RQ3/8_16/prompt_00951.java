/**
 * Convert the map to a one-dimensional array of booleans
 * 
 * @return the boolean array representing the bitmap
 */
public boolean[] toBooleanArray() 
{
    boolean[] result = new boolean[map.length];
    for (int i = 0; i < map.length; i++)
    {
        result[i] = map[i];
    }
    return result;
}   