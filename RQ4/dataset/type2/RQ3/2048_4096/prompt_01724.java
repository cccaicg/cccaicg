/**
 * Processes requests for HTTP <code>GET</code>
 *
 * @param request servlet request
 * @param response servlet response
 * @throws ServletException if a servlet-specific error occurs
 * @throws IOException if an I/O error occurs
 */
protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException 
{
    try
    {
        processRequest(request, response);
    }
    catch (Exception ex)
    {
        Logger.getLogger(UploadServlet.class.getName()).log(Level.SEVERE, null, ex);
    }
}   