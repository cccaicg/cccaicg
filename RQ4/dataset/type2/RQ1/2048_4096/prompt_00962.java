//主动结束和数据库的连接
public void releaseConn() 
{
    if (conn != null)
    {
        try
        {
            conn.close();
        }
        catch (SQLException e)
        {
            e.printStackTrace();
        }
    }
}   