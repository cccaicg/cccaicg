// Returns the highest key in the symbol table smaller than or equal to key.
public Key floor(Key key) 
{
    if (isEmpty()) return null;
    int i = rank(key);
    if (i < N && key.compareTo(keys[i]) == 0) return keys[i];
    return (i == 0) ? null : keys[i-1];
}   