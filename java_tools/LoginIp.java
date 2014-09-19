public class LoginIp{
	
	/**
	 * »ñÈ¡µÇÂ¼×ÅIP
	 * */
	public static String getIp(HttpServletRequest request){
        if (request == null){
            return null;
        }
        String ipaddress = "";
        if (request.getHeader("x-forwarded-for") == null){
            ipaddress = request.getRemoteAddr();
        }
        else{
            ipaddress = request.getHeader("x-forwarded-for");
        }
        if(ipaddress != null){
            String[] s = ipaddress.split(",");
            if(s.length==1)
            {
                ipaddress = s[0].trim();
            }
            else if(s.length > 1)
            {
                ipaddress = s[s.length - 2].trim();
            }
        }
        return ipaddress;
    }

}