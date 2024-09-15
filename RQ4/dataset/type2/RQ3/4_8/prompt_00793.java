/**
 * Print method used for debugging.
 */
@SuppressWarnings("unused")
private void print() 
{
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            System.out.print(board[i][j] + " ");
        }
        System.out.println();
    }
    System.out.println();
}   