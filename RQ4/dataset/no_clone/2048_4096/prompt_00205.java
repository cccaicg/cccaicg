/**
 * Moves pointer one position right; save current character to lookBack;
 * lookAhead to current one and finally read one more to lookAhead;
 */
private void movePointer() 
{
    lookBack = lookAhead;
    lookAhead = reader.read();
    current = reader.read();
}   