// $ANTLR start "TYPE_LIST"
public final void mTYPE_LIST() throws RecognitionException 
{
    try
    {
        int _type = TYPE_LIST;
        int _channel = DEFAULT_TOKEN_CHANNEL;
        // C:\\Users\\user\\Desktop\\Univer\\3 course\\2 sem\\КПЗ\\ImageFilter\\src\\ImageFilter\\grammar\\ImageFilter.g4:12:11: ( ( TYPE )+ )
        // C:\\Users\\user\\Desktop\\Univer\\3 course\\2 sem\\КПЗ\\ImageFilter\\src\\ImageFilter\\grammar\\ImageFilter.g4:12:13: ( TYPE )+
        {
        // C:\\Users\\user\\Desktop\\Univer\\3 course\\2 sem\\КПЗ\\ImageFilter\\src\\ImageFilter\\grammar\\ImageFilter.g4:12:13: ( TYPE )+
        int cnt1=0;
        loop1:
        do
        {
            int alt1=2;
            int LA1_0 = input.LA(1);

            if ( (LA1_0==TYPE) )
            {
                alt1=1;
            }


            switch (alt1)
            {
                case 1 :
                    // C:\\Users\\user\\Desktop\\Univer\\3 course\\2 sem\\КПЗ\\ImageFilter\\src\\ImageFilter\\grammar\\ImageFilter.g4:12:13: TYPE
                    {
                    mTYPE(); 

                    }
                    break;

                default :
                    if ( cnt1 >= 1 ) break loop1;
                    EarlyExitException eee =
                        new EarlyExitException(1, input);
                    throw eee;
            }
            cnt1++;
        } while (true);


        }
        state.type = _type;
        state.channel = _channel;
    }
    finally
    {
    }
}   