// $ANTLR start exit
// /Users/michaelarace/CodaClient/CodaClient.g:220:1: exit returns [boolean response] : 'EXIT' ;
public final exit_return exit() throws RecognitionException 
{
    boolean response = false;
    try
    {
        // /Users/michaelarace/CodaClient/CodaClient.g:221:2: ( 'EXIT' )
        // /Users/michaelarace/CodaClient/CodaClient.g:221:4: 'EXIT'
        {
        match("EXIT"); 

        response = true;
        }

    }
    catch (RecognitionException re)
    {
        reportError(re);
        recover(input, re);
    }
    finally
    {
    }
    return response;
}   