//主动结束和数据库的连接
public void releaseConn(){
    if(resultSet != null){
        try{
            resultSet.close();
        }catch(SQLException e){
            e.printStackTrace();
        }
    }
}