// Convert a String array to a TestParam array:
public static TestParam[] array(String[] values) 
{
    int[] vals = new int[values.length];
    for(int i = 0; i < vals.length; i++)
        vals[i] = Integer.decode(values[i]);
    return array(vals);
}   